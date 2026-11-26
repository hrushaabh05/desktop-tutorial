"""Core painterly 2D rendering helpers (numpy + PIL).

Everything works on float32 RGB arrays of shape (H, W, 3) in linear-ish 0..1
(values above 1 are allowed for emissive light and are tone-mapped at the end).
"""
import functools
import math

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FPS = 24
F32 = np.float32
YY, XX = np.mgrid[0:H, 0:W].astype(F32)

FONT_TITLE = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
FONT_TEXT = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
FONT_DEVA = "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf"


# ----------------------------------------------------------------- math utils
def sstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def fade(t, a, b, c, d):
    """1 between b and c, ramps in a->b and out c->d."""
    return float(sstep(a, b, t) * (1 - sstep(c, d, t)))


def mix(a, b, t):
    return a + (b - a) * t


def C(*c):
    return np.array(c, F32)


def hexc(h):
    return np.array([int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)], F32)


def solid(c):
    return np.broadcast_to(np.asarray(c, F32), (H, W, 3)).copy()


def vgrad(stops):
    """Vertical gradient from list of (pos 0..1, color)."""
    v = YY[:, 0] / H
    out = np.zeros((H, 3), F32)
    done = np.zeros(H, bool)
    for (p0, c0), (p1, c1) in zip(stops[:-1], stops[1:]):
        m = (v >= p0) & (v <= p1) & ~done
        tt = np.clip((v - p0) / max(p1 - p0, 1e-6), 0, 1)[:, None]
        val = np.asarray(c0, F32) + (np.asarray(c1, F32) - np.asarray(c0, F32)) * tt
        out[m] = val[m]
        done |= m
    out[v < stops[0][0]] = stops[0][1]
    out[v > stops[-1][0]] = stops[-1][1]
    return np.broadcast_to(out[:, None, :], (H, W, 3)).copy()


def radial(cx, cy, r, power=2.0):
    d = np.sqrt((XX - cx) ** 2 + (YY - cy) ** 2) / r
    return np.clip(1 - d, 0, 1) ** power


# -------------------------------------------------------------------- noise
@functools.lru_cache(None)
def noise(seed, w=W, h=H, base=3, octaves=6, sx=1.0, sy=1.0, persistence=0.55):
    rng = np.random.default_rng(seed)
    out = np.zeros((h, w), F32)
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        nx = max(2, int(base * 2 ** o * sx))
        ny = max(2, int(base * 2 ** o * sy * h / w))
        small = rng.random((ny, nx)).astype(F32)
        out += np.asarray(Image.fromarray(small).resize((w, h), Image.BICUBIC)) * amp
        tot += amp
        amp *= persistence
    out /= tot
    out = (out - out.min()) / (out.max() - out.min() + 1e-6)
    out.flags.writeable = False
    return out


@functools.lru_cache(None)
def paint_tex():
    """Brush-stroke + canvas texture, centred on 1.0."""
    a = noise(11, base=3)
    strokes = noise(12, base=2, sx=6, sy=0.6, octaves=5)
    strokes2 = noise(13, base=2, sx=0.8, sy=5, octaves=5)
    canvas = noise(14, base=60, octaves=2)
    t = 0.45 * a + 0.3 * strokes + 0.15 * strokes2 + 0.1 * canvas
    t = (t - t.mean())
    t = 1 + t * 0.9
    t.flags.writeable = False
    return t


@functools.lru_cache(None)
def grain_frames():
    rng = np.random.default_rng(99)
    return [rng.normal(0, 1, (H // 2, W // 2)).astype(F32) for _ in range(6)]


# --------------------------------------------------------------------- blur
def _box(a, r, axis):
    r = int(r)
    if r < 1:
        return a
    n = a.shape[axis]
    pad = [(0, 0)] * a.ndim
    pad[axis] = (r + 1, r)
    p = np.pad(a, pad, mode="edge")
    c = np.cumsum(p, axis=axis, dtype=F32)
    s1 = [slice(None)] * a.ndim
    s2 = [slice(None)] * a.ndim
    s1[axis] = slice(2 * r + 1, 2 * r + 1 + n)
    s2[axis] = slice(0, n)
    return (c[tuple(s1)] - c[tuple(s2)]) / (2 * r + 1)


def _up(sm, h, w):
    if sm.ndim == 2:
        return np.asarray(Image.fromarray(sm.astype(F32)).resize((w, h), Image.BILINEAR))
    return np.stack([_up(sm[..., i], h, w) for i in range(sm.shape[2])], axis=-1)


def blur(a, s, sx=None, sy=None):
    """Approximate gaussian blur with sigma s (or separate sx/sy)."""
    sx = s if sx is None else sx
    sy = s if sy is None else sy
    if max(sx, sy) < 0.5:
        return a
    h, w = a.shape[:2]
    f = 1
    for c in (16, 8, 4, 2):
        if min(sx, sy) / c >= 6.0 and h % c == 0 and w % c == 0:
            f = c
            break
    sm = a.reshape(h // f, f, w // f, f, *a.shape[2:]).mean(axis=(1, 3)) if f > 1 else a
    rx, ry = max(sx / f, 0), max(sy / f, 0)
    for _ in range(3):
        if rx >= 0.5:
            sm = _box(sm, max(1, round(rx)), 1)
        if ry >= 0.5:
            sm = _box(sm, max(1, round(ry)), 0)
    return _up(sm, h, w) if f > 1 else sm


def glow(img, s, k=1.0, thresh=0.6):
    bright = np.clip(img - thresh, 0, None)
    return img + blur(bright, s) * k


# ----------------------------------------------------------------- sampling
def sample(a, sx, sy):
    h, w = a.shape[:2]
    sx = np.clip(sx, 0, w - 1.001)
    sy = np.clip(sy, 0, h - 1.001)
    x0 = sx.astype(np.int32)
    y0 = sy.astype(np.int32)
    fx = sx - x0
    fy = sy - y0
    if a.ndim == 3:
        fx = fx[..., None]
        fy = fy[..., None]
    top = a[y0, x0] * (1 - fx) + a[y0, x0 + 1] * fx
    bot = a[y0 + 1, x0] * (1 - fx) + a[y0 + 1, x0 + 1] * fx
    return top * (1 - fy) + bot * fy


def zoom(a, z, cx=W / 2, cy=H / 2, rot=0.0, ox=0.0, oy=0.0):
    """Camera: output centre looks at (cx,cy) in source with magnification z."""
    h, w = a.shape[:2]
    dx = (XX - W / 2) / z
    dy = (YY - H / 2) / z
    if rot:
        c, s = math.cos(rot), math.sin(rot)
        dx, dy = dx * c - dy * s, dx * s + dy * c
    return sample(a, dx + cx + ox, dy + cy + oy)


# -------------------------------------------------------------- mask drawing
class Mask:
    """PIL 'L' canvas with helpers in a local (cx, cy, scale) frame."""

    def __init__(self, cx=0.0, cy=0.0, s=1.0, w=W, h=H):
        self.img = Image.new("L", (w, h), 0)
        self.d = ImageDraw.Draw(self.img)
        self.cx, self.cy, self.s = cx, cy, s

    def P(self, x, y):
        return (self.cx + x * self.s, self.cy + y * self.s)

    def ell(self, x0, y0, x1, y1, v=255):
        a, b = self.P(x0, y0), self.P(x1, y1)
        self.d.ellipse([min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])], fill=v)

    def circ(self, x, y, r, v=255):
        self.ell(x - r, y - r, x + r, y + r, v)

    def poly(self, pts, v=255):
        self.d.polygon([self.P(*p) for p in pts], fill=v)

    def line(self, pts, width, v=255, joints=True):
        P = [self.P(*p) for p in pts]
        wpx = max(1, int(width * self.s))
        self.d.line(P, fill=v, width=wpx)
        if joints:
            r = wpx / 2
            for x, y in P:
                self.d.ellipse([x - r, y - r, x + r, y + r], fill=v)

    def arc_pts(self, cx, cy, rx, ry, a0, a1, n=24):
        return [(cx + rx * math.cos(a), cy + ry * math.sin(a)) for a in np.linspace(a0, a1, n)]

    def arr(self, soft=0.8):
        a = np.asarray(self.img, F32) / 255.0
        return blur(a, soft) if soft else a


def comp(base, color, alpha):
    """Alpha composite colour (H,W,3 or 3,) with alpha mask (H,W)."""
    a = alpha[..., None]
    return base * (1 - a) + color * a


def shade(height, albedo, light, lcol, amb, k=30.0, lz=220.0, falloff=900.0, spec=0.0):
    """Light a pseudo-3D surface defined by a height field (blurred masks).

    light: (x, y) screen position of light source.
    Returns lit colour (H,W,3).
    """
    gy, gx = np.gradient(height)
    nx, ny, nz = -gx * k, -gy * k, np.ones_like(height)
    nl = np.sqrt(nx * nx + ny * ny + 1)
    lx, ly = light[0] - XX, light[1] - YY
    ll = np.sqrt(lx * lx + ly * ly + lz * lz)
    dot = (nx * lx + ny * ly + nz * lz) / (nl * ll)
    dot = np.clip(dot, 0, 1)
    d = np.sqrt(lx * lx + ly * ly)
    att = 1.0 / (1.0 + (d / falloff) ** 2)
    diff = dot * att
    out = albedo * (np.asarray(amb, F32) + np.asarray(lcol, F32) * diff[..., None])
    if spec:
        out += np.asarray(lcol, F32) * (dot ** 24 * att * spec)[..., None]
    return out


# --------------------------------------------------------------------- text
@functools.lru_cache(maxsize=64)
def text_mask(text, size, font=FONT_TITLE, tracking=0, weather=True, x=None, y=None,
              lang=None):
    f = ImageFont.truetype(font, size)
    img = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(img)
    kw = {"language": lang} if lang else {}
    if tracking:
        widths = [d.textlength(ch, font=f) + tracking for ch in text]
        tw = sum(widths) - tracking
    else:
        tw = d.textlength(text, font=f, **kw)
    x0 = (W - tw) / 2 if x is None else x
    y0 = H / 2 if y is None else y
    if tracking:
        cx = x0
        for ch, wch in zip(text, widths):
            d.text((cx, y0), ch, font=f, fill=255, anchor="lm")
            cx += wch
    else:
        d.text((x0, y0), text, font=f, fill=255, anchor="lm", **kw)
    m = np.asarray(img, F32) / 255.0
    if weather:
        n = noise(21, base=40, octaves=3)
        n2 = noise(22, base=8, octaves=4)
        m = m * np.clip((n * 0.6 + n2 * 0.4 - 0.18) * 3.0, 0.25, 1.0)
    m.flags.writeable = False
    return m


def put_text(img, text, size, alpha, y, color=(1.0, 0.8, 0.45), font=FONT_TEXT,
             tracking=0, glow_s=6, glow_k=0.6, lang=None, shadow=True):
    if alpha <= 0.001:
        return img
    m = text_mask(text, size, font, tracking, True, None, y, lang)
    if shadow:
        img = img * (1 - 0.6 * alpha * blur(m, 6)[..., None])
    col = np.asarray(color, F32)
    img = comp(img, col, m * alpha)
    if glow_s:
        img = img + blur(m, glow_s)[..., None] * col * glow_k * alpha
    return img


# ------------------------------------------------------------------ finishing
def finish(img, t, vignette=0.55, grain=0.035, texture=0.12, exposure=1.0):
    img = img * exposure
    if texture:
        img = img * (1 + (paint_tex() - 1) * texture)[..., None]
    if vignette:
        d = ((XX - W / 2) / (W * 0.62)) ** 2 + ((YY - H / 2) / (H * 0.62)) ** 2
        img = img * (1 - vignette * np.clip(d, 0, 1.4) ** 1.3 / 1.4 ** 1.3)[..., None]
    # filmic tone map (soft shoulder for emissive values)
    img = np.clip(img, 0, None)
    img = img * (1 + img / 6.0) / (1 + img)
    img = img * 1.35
    if grain:
        g = grain_frames()[int(t * FPS) % 6]
        g = np.repeat(np.repeat(g, 2, 0), 2, 1)
        img = img + g[..., None] * grain
    img = np.clip(img, 0, 1) ** (1 / 1.15)
    return (img * 255 + 0.5).astype(np.uint8)
