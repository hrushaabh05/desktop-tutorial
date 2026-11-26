"""The seven movements of THE ASH-SMEARED HEART."""
import functools
import math

import numpy as np
from PIL import Image

from engine import (C, F32, FONT_DEVA, FONT_TEXT, FONT_TITLE, H, W, XX, YY, Mask, blur,
                    comp, fade, glow, mix, noise, put_text, radial, sample, shade, solid,
                    sstep, vgrad, zoom)
from figures import (HAIR, SKIN, render_profile, bilva, diya, flame, lingam_masks, lying_mask,
                     mask_features, nataraja_mask, render_face, render_seated,
                     seated_masks, standing_masks, tiger_skin, villager)
import timeline as TL

GOLD = C(1.25, 0.82, 0.36)
INDIGO = C(0.025, 0.025, 0.07)


# ================================================================ particles
def drift_mask(t, n, seed, box, v, sway=10.0, r=(1, 3), twinkle=0.5, wrap=True, life=None):
    x0, y0, x1, y1 = box
    rng = np.random.default_rng(seed)
    X = rng.uniform(x0, x1, n)
    Y = rng.uniform(y0, y1, n)
    R = rng.uniform(r[0], r[1], n)
    ph = rng.uniform(0, 6.283, n)
    sp = rng.uniform(.6, 1.4, n)
    x = X + v[0] * sp * t + sway * np.sin(t * .8 + ph)
    y = Y + v[1] * sp * t + sway * .5 * np.cos(t * .6 + ph * 1.3)
    if wrap:
        x = x0 + (x - x0) % (x1 - x0)
        y = y0 + (y - y0) % (y1 - y0)
    b = (1 - twinkle) + twinkle * (0.5 + 0.5 * np.sin(t * 3 + ph * 5))
    m = Mask()
    for i in range(n):
        m.circ(x[i], y[i], R[i], int(255 * b[i]))
    return m.arr(0.7)


def add_light(img, mask, col, g=6, gk=1.0):
    img = img + np.asarray(col, F32) * mask[..., None]
    if g:
        img = img + np.asarray(col, F32) * (blur(mask, g) * gk)[..., None]
    return img


@functools.lru_cache(None)
def starfield(seed=5, n=420):
    rng = np.random.default_rng(seed)
    m = Mask()
    for _ in range(n):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        r = rng.choice([0.6, 0.8, 1.0, 1.4, 2.0], p=[.4, .3, .15, .1, .05])
        m.circ(x, y, r, int(rng.uniform(80, 255)))
    a = m.arr(0.5)
    a.flags.writeable = False
    return a


def wrap_sample(a, sx, sy):
    w = a.shape[1]
    return sample(a, np.mod(sx, w - 2), sy)


# =================================================================== TITLE
def sc_title(t, d):
    img = solid((0.006, 0.005, 0.012))
    emb = drift_mask(t, 70, 1, (0, -40, W, H + 40), (4, -26), sway=20, r=(0.8, 2.2))
    img = add_light(img, emb * fade(t, 0, 2, 10, 12), (1.6, .65, .2), g=4, gk=1.5)
    smoke = noise(2, base=2, sx=1.5)
    sm = np.roll(smoke, int(-t * 8), axis=0)
    img = img + C(0.05, 0.03, 0.02) * (sm ** 3 * fade(t, 0, 4, 9, 12))[..., None]
    a = fade(t, 1.8, 4.5, 9.5, 11.5)
    img = put_text(img, "THE ASH-SMEARED HEART", 76, a, H * 0.46, color=(1.25, .82, .38),
                   font=FONT_TITLE, tracking=7, glow_s=10, glow_k=.45)
    img = put_text(img, "an animated short in seven movements", 26,
                   fade(t, 4.0, 6.0, 9.5, 11.5), H * 0.58, color=(.7, .64, .58),
                   font=FONT_TEXT, glow_s=0)
    return img


# ==================================================================== ACT I
@functools.lru_cache(None)
def ghat_layers():
    hz = 0.42 * H
    sky = vgrad([(0, (0.012, 0.012, 0.04)), (0.25, (0.03, 0.03, 0.08)),
                 (0.42, (0.16, 0.09, 0.13))])
    cl = noise(61, base=2, sx=3, sy=.7)
    sky = sky * (0.8 + 0.5 * cl[..., None])
    # far bank: temple skyline
    far = Mask()
    rng = np.random.default_rng(3)
    x = -20
    while x < W + 40:
        w = rng.uniform(40, 120)
        h = rng.uniform(25, 70)
        far.d.rectangle([x, hz - h, x + w, hz + 5], fill=255)
        if rng.random() < .45:  # shikhara spire
            cx = x + w / 2
            sh = rng.uniform(60, 140)
            pts = []
            for u in np.linspace(0, 1, 14):
                pts.append((cx + (w * .45) * (1 - u) ** .7, hz - h - sh * u))
            pts += [(2 * cx - px, py) for px, py in pts[::-1]]
            far.d.polygon(pts, fill=255)
            far.d.ellipse([cx - 5, hz - h - sh - 8, cx + 5, hz - h - sh + 2], fill=255)
        x += w * rng.uniform(.7, 1.05)
    far_a = far.arr(1.0)
    lamps = Mask()
    for _ in range(26):
        lx, ly = rng.uniform(0, W), hz - rng.uniform(4, 40)
        lamps.circ(lx, ly, 1.6)
    river = vgrad([(0.42, (0.05, 0.04, 0.08)), (0.62, (0.015, 0.02, 0.04))])
    # steps (perspective bands)
    steps = np.zeros((H, W, 3), F32)
    st_a = (YY >= 0.62 * H).astype(F32)
    N = 9
    ys = [0.62 * H + (0.38 * H) * (k / N) ** 1.5 for k in range(N + 1)]
    stone = noise(62, base=6, octaves=5)
    base = C(0.20, 0.16, 0.13)
    for k in range(N):
        a, b = ys[k], ys[k + 1]
        tread = (YY >= a) & (YY < a + (b - a) * .62)
        riser = (YY >= a + (b - a) * .62) & (YY < b)
        steps[tread] = base * 1.0
        steps[riser] = base * 0.7
    steps = steps * (0.6 + 0.8 * stone[..., None])
    st_a = blur(st_a, 1)
    out = dict(sky=sky, far_a=far_a, lamps=lamps.arr(1.2), river=river, steps=steps, st_a=st_a)
    return out


def sc_ghats(t, d):
    if t >= TL.GHAT_CLOSEUP:
        return ghats_closeup(t - TL.GHAT_CLOSEUP, d - TL.GHAT_CLOSEUP)
    L = ghat_layers()
    flick = 0.5 + 0.3 * math.sin(t * 11.7) + 0.2 * math.sin(t * 23.3 + 1)
    lamp = (0.395 * W, 0.885 * H)
    light = (lamp[0], lamp[1] - 40)
    reveal = sstep(2.5, 8.0, t)
    lampon = sstep(0.8, 2.2, t)
    glowfield = radial(light[0], light[1], 700, 1.6) * (0.85 + 0.15 * flick)
    # background composite (sky, far, river)
    bg = L["sky"].copy()
    bg = comp(bg, C(0.02, 0.018, 0.035), L["far_a"])
    bg = bg + C(1.5, .8, .3) * L["lamps"][..., None] * (0.6 + 0.4 * math.sin(t * 2))
    riv = (YY >= 0.42 * H) & (YY < 0.63 * H)
    wave = np.roll(noise(63, base=3, sx=8, sy=.5), int(t * 12), axis=1)
    rv = L["river"] * (0.7 + 0.6 * wave[..., None])
    # lamp reflections shimmer on water
    refl = np.roll(L["lamps"], 0, axis=0)
    shimmer = blur(L["lamps"], 0.5, sx=1, sy=18) * (0.5 + wave) * 2.5
    rv = rv + C(1.2, .6, .25) * shimmer[..., None]
    bg[riv] = rv[riv]
    bg = bg * (0.25 + 0.75 * reveal)
    # foreground: steps + figure
    fg = L["steps"] * (0.05 + 1.6 * glowfield[..., None] * C(1.0, .62, .32)) * reveal
    fa = L["st_a"].copy()
    fx, fy, s = 0.56 * W, 0.865 * H, 125
    fg = tiger_skin(fg, fx, fy + 10, s * .75, light, C(1.6, 1.0, .5) * reveal)
    fg, fu = render_seated(fg, fx, fy, s, (light[0] - 60, light[1] - 160),
                           C(1.5, .95, .45) * (0.85 + .15 * flick) * reveal,
                           amb=(0.01, 0.01, 0.025), rim=C(.08, .07, .14) * reveal)
    fa = np.maximum(fa, fu)
    fg = diya(fg, lamp[0], lamp[1], 13, t, flick) if lampon > 0 else fg
    if lampon < 1:
        fg = fg * lampon
    fa = np.maximum(fa, radial(lamp[0], lamp[1] - 25, 60, 1) * lampon)
    # camera push with parallax
    z = 1 + 0.33 * sstep(2.0, 17.5, t)
    tx, ty = mix(W / 2, fx - 30, sstep(2, 17.5, t)), mix(H / 2, 0.68 * H, sstep(2, 17.5, t))
    bgz = zoom(bg, 1 + 0.3 * (z - 1), mix(W / 2, tx, .3), mix(H / 2, ty, .3))
    fga = zoom(np.dstack([fg, fa]), z, tx, ty)
    img = comp(bgz, fga[..., :3], np.clip(fga[..., 3], 0, 1))
    # mist layers between
    for i, (sp, dens, yc) in enumerate(((10, .5, .55), (22, .4, .72))):
        n = noise(64 + i, base=2, sx=2.5, sy=.6)
        n = np.roll(n, int(t * sp), axis=1)
        band = np.exp(-((YY / H - yc) / .12) ** 2)
        m = np.clip(n - .35, 0, 1) * band * dens
        mc = C(0.12, 0.11, 0.16) * reveal + C(.9, .5, .2) * glowfield[..., None] * .5 * reveal
        img = img + mc * m[..., None]
    img = add_light(img, glowfield * 0.0, (0, 0, 0), g=0)
    img = glow(img, 18, 0.5, 0.9)
    return img


def ghats_closeup(t, d):
    img = solid((0.004, 0.003, 0.006))
    beats = [b - (TL.SCENES[1][1] + TL.GHAT_CLOSEUP) for b in TL.heartbeats()]
    env = TL.beat_env(t, beats, 6) + 0.6 * TL.beat_env(t, [b + .22 for b in beats], 8)
    s = 520 * (1 + 0.012 * env + 0.012 * t / d)
    syl = max(0.0, math.sin(t * 2 * math.pi * 2.6)) ** .7
    phrase = sstep(-.2, .2, math.sin(t * 1.3 + .5))
    mouth = syl * phrase * 0.8
    flick = 0.5 + 0.3 * math.sin(t * 11.7) + 0.2 * math.sin(t * 23.3 + 1)
    lamp = (W * .08, H * .78)
    img = img + C(.10, .05, .02) * radial(lamp[0], lamp[1], 900, 2)[..., None] * (1 + .3 * env)
    img = render_profile(img, W * .6, H * .38, s * .62, mouth, lamp,
                         C(3.2, 1.9, .8) * (0.85 + .15 * flick + .3 * env))
    img = img * (fade(t, 0, 0.5, d, d + 1))
    return img


@functools.lru_cache(None)
def bead_sprites(n_phase=24, size=160):
    tex_w, tex_h = 512, 256
    n1 = noise(71, tex_w, tex_h, base=6, octaves=6)
    ridge = 1 - np.abs(2 * n1 - 1)
    n2 = noise(72, tex_w, tex_h, base=14, octaves=4)
    yy, xx = np.mgrid[0:size, 0:size].astype(F32)
    u = (xx - size / 2 + .5) / (size / 2)
    v = (yy - size / 2 + .5) / (size / 2)
    rr = u * u + v * v
    inside = rr < 1
    z = np.sqrt(np.clip(1 - rr, 0, 1))
    lat = np.arcsin(np.clip(v, -1, 1))
    lv = np.array([-.45, -.55, .7], F32)
    lv /= np.linalg.norm(lv)
    lam = np.clip(u * lv[0] + v * lv[1] + z * lv[2], 0, 1)
    rim = np.clip(1 - z, 0, 1) ** 3
    sprites = []
    for p in range(n_phase):
        lon = np.arctan2(u, z + 1e-6) + p * 2 * math.pi / n_phase
        tx = ((lon / (2 * math.pi)) % 1 * (tex_w - 1)).astype(np.int32)
        ty = ((lat / math.pi + .5) * (tex_h - 1)).astype(np.int32)
        rd = ridge[ty, tx] * .7 + n2[ty, tx] * .3
        groove = np.exp(-(((lon * 5 / (2 * math.pi)) % 1 - .5) / .05) ** 2)
        alb = C(.34, .16, .07)[None, None] * (0.35 + 0.95 * rd[..., None]) * (1 - .6 * groove[..., None])
        col = alb * (0.08 + 1.5 * lam[..., None]) + C(1.0, .65, .25) * rim[..., None] * .8
        a = np.clip((1 - rr) * size * .25, 0, 1) * inside
        sprites.append(np.dstack([col, a]).astype(F32))
    return sprites


def paste_sprite(img, spr, x, y, size, alpha=1.0, add=False):
    size = int(max(2, size))
    rs = np.stack([np.asarray(Image.fromarray(np.ascontiguousarray(spr[..., i])).resize(
        (size, size), Image.BILINEAR)) for i in range(4)], -1)
    x0, y0 = int(x - size / 2), int(y - size / 2)
    xa, ya = max(0, x0), max(0, y0)
    xb, yb = min(W, x0 + size), min(H, y0 + size)
    if xb <= xa or yb <= ya:
        return img
    sub = rs[ya - y0:yb - y0, xa - x0:xb - x0]
    a = sub[..., 3:4] * alpha
    if add:
        img[ya:yb, xa:xb] += sub[..., :3] * a
    else:
        img[ya:yb, xa:xb] = img[ya:yb, xa:xb] * (1 - a) + sub[..., :3] * a
    return img


def sc_cosmos(t, d):
    neb = noise(81, base=2, octaves=6)
    neb2 = noise(82, base=3, octaves=5)
    img = INDIGO * 0.4 + C(0.08, 0.03, 0.16) * (neb ** 3)[..., None] + C(.12, .05, .02) * (neb2 ** 4)[..., None]
    img = img + C(.9, .85, 1.0) * starfield()[..., None] * 0.6
    fcx, fcy, fs = W / 2, H * 0.55, 175
    eye = (fcx, fcy - 0.85 * fs)
    spiral = sstep(13.5, 20.3, t)
    # translucent giant face
    face = np.zeros((H, W, 3), F32)
    face, fu = render_face(face, fcx, fcy, fs, (fcx, fcy - 300), C(1.8, 1.25, .6),
                           amb=(0.02, 0.015, 0.03))
    edge = np.clip(fu - blur(fu, 3), 0, 1)
    breath = 0.5 + 0.08 * math.sin(t * 1.2)
    vis = fade(t, 0.0, 2.5, 30, 31) * breath
    img = img + face * vis * 0.55 + C(1.2, .8, .35) * (blur(edge, 2) * vis)[..., None]
    # orbiting beads that become worlds
    sprites = bead_sprites()
    N = 21
    grow = mix(0.45, 1.9, sstep(1.5, 11, t)) * (1 - 0.8 * spiral)
    order = []
    for i in range(N):
        th = 2 * math.pi * i / N + t * (0.28 + 2.0 * spiral ** 2) + spiral * 4
        rf = (1 - spiral) ** 1.4
        ox = math.cos(th) * 540 * rf
        oy = math.sin(th) * 150 * rf
        tilt = 0.18
        x = fcx + ox * math.cos(tilt) - oy * math.sin(tilt)
        y = (fcy - 0.25 * fs) + ox * math.sin(tilt) + oy * math.cos(tilt)
        x = mix(x, eye[0], spiral ** 2)
        y = mix(y, eye[1], spiral ** 2)
        depth = math.sin(th)
        size = 46 * grow * (1 + 0.38 * depth) * (0.8 + 0.4 * ((i * 7) % 5) / 4)
        order.append((depth, x, y, size, i))
    for depth, x, y, size, i in sorted(order):
        ph = int((t * 3 + i * 5) % 24)
        a = (0.55 if depth < 0 else 1.0) * fade(t, .3, 1.5, 30, 31)
        img = paste_sprite(img, sprites[ph], x, y, size, a)
    # third eye ignites
    e = sstep(12, 20.5, t)
    flash = sstep(19.8, 21.6, t)
    img = img + C(1.6, 1.3, .9) * (radial(eye[0], eye[1], 30 + 400 * e ** 3, 2) * (0.3 + 3 * e))[..., None]
    img = put_text(img, "He doesn't count the beads.  They count him.", 40,
                   fade(t, 4.5, 6.5, 12.0, 13.5), H * 0.88, color=(1.1, .85, .5))
    img = glow(img, 10, .6, 1.0)
    img = mix(img, C(3, 2.8, 2.5), flash)
    return img


# =================================================================== ACT II
def graphic(img, contrast=1.6, edge_k=2.2):
    lum = img.mean(-1)
    e = np.abs(np.gradient(blur(lum, 1.2))[0]) + np.abs(np.gradient(blur(lum, 1.2))[1])
    ink = np.clip(e * 18 * edge_k - .25, 0, 1)
    out = np.clip((img - .18) * contrast + .18, 0, None)
    return out * (1 - .85 * ink[..., None])


def panel_hands(t):
    img = vgrad([(0, (.06, .035, .02)), (1, (.015, .01, .008))])
    light = (W * .3, -H * .2)
    m = Mask(W / 2, H * 1.0, 190)
    for sg in (-1, 1):
        m.ell(sg * .02, -.75, sg * 1.0, .25)
        m.poly([(sg * .1, -.1), (sg * .98, -.2), (sg * 1.15, 1.3), (sg * .25, 1.3)])
        for i in range(4):
            bx = sg * (.14 + i * .22)
            tx = sg * (.1 + i * .2)
            ty = -1.45 + abs(i - 1.2) * .1
            m.line([(bx, -.6), (mix(bx, tx, .55) + sg * .03, mix(-.6, ty, .55))], .17)
            m.line([(mix(bx, tx, .55) + sg * .03, mix(-.6, ty, .55)), (tx, ty)], .145)
        m.line([(sg * .95, -.3), (sg * 1.2, -.75), (sg * 1.12, -1.05)], .19)
    hand = m.arr(1)
    sep = Mask(W / 2, H * 1.0, 190)
    for sg in (-1, 1):
        for i in range(3):
            bx = sg * (.25 + i * .22)
            tx = sg * (.19 + i * .3)
            sep.line([(bx, -.75), (tx, -1.45 + abs(i - 1) * .1)], .012)
    alb_lines = sep.arr(1.5)
    alb = np.zeros((H, W, 3), F32) + SKIN * 1.1
    crease = noise(91, base=10, sx=3, octaves=3)
    alb = alb * (0.75 + 0.4 * crease[..., None]) * (1 - .8 * alb_lines[..., None])
    lit = shade(blur(hand, 14) + blur(hand, 4) * .3 - alb_lines * .02, alb, light, C(2.6, 1.7, .9),
                (.03, .02, .02), k=60, lz=300, falloff=1400)
    img = comp(img, lit, hand)
    lf = Mask()
    veins = bilva(lf, W / 2, H * .8 + 4 * math.sin(t * 1.5), 190, 0.03 * math.sin(t))
    leaf = lf.arr(1)
    lalb = np.zeros((H, W, 3), F32) + C(.05, .2, .05)
    llit = shade(blur(leaf, 10), lalb, light, C(2.2, 2.0, 1.0), (.02, .04, .02), k=40, lz=300,
                 falloff=1400, spec=.6)
    img = comp(img, llit, leaf)
    vm = Mask()
    for v in veins:
        vm.line(v, 2.2, joints=False)
    vg = vm.arr(.6) * leaf
    pulse = 0.7 + 0.3 * math.sin(t * 3)
    img = add_light(img, vg * pulse, (.45, 1.7, .35), g=5, gk=1.6)
    return img


def banyan(t):
    img = vgrad([(0, (1.1, .8, .42)), (.55, (.85, .55, .25)), (.75, (.25, .15, .08)),
                 (1, (.06, .04, .03))])
    m = Mask()
    m.poly([(W * .30, H), (W * .34, H * .5), (W * .31, H * .3), (W * .43, H * .3),
            (W * .40, H * .5), (W * .45, H)])
    rng = np.random.default_rng(9)
    for _ in range(70):
        x, y = rng.uniform(-100, W + 100), rng.uniform(-80, H * .32)
        r = rng.uniform(60, 160)
        m.ell(x - r * 1.3, y - r * .6, x + r * 1.3, y + r * .6)
    for _ in range(40):
        x = W * .37 + rng.normal(0, W * .2)
        y1 = rng.uniform(H * .45, H * .9)
        m.d.line([(x, H * .25), (x + rng.uniform(-10, 10), y1)], fill=255, width=int(rng.uniform(1, 3)))
    tree = m.arr(1)
    holes = (noise(92, base=8, octaves=3) > .72).astype(F32) * (YY < H * .35)
    tree = tree * (1 - holes * .9)
    img = comp(img, C(.03, .025, .02), tree)
    ground = (YY > H * .86).astype(F32)
    img = comp(img, C(.08, .05, .03) * (0.6 + noise(93, base=5)[..., None] * .7), blur(ground, 2))
    ln, yo = lingam_masks(W * .62, H * .9, 85)
    st = ln + yo
    alb = np.zeros((H, W, 3), F32) + C(.18, .17, .15)
    moss = (noise(94, base=25, octaves=3) > .58).astype(F32)
    alb = comp(alb, C(.1, .25, .06), moss * st)
    lit = shade(blur(st, 7), alb, (W * .2, -H * .3), C(3, 2.3, 1.4), (.02, .02, .02), k=25, lz=200,
                falloff=1500)
    img = comp(img, lit, np.clip(st, 0, 1))
    beam = np.clip(1 - np.abs((XX - W * .62) + (YY - H * .85) * .55) / 160, 0, 1) ** 2 * (YY < H * .9) * .6
    motes = drift_mask(t, 40, 12, (W * .3, 0, W * .9, H), (3, 8), r=(.8, 1.8))
    img = img + C(1.0, .75, .35) * (beam * (.35 + motes * 2))[..., None]
    return img


def panel_overhead(t):
    img = solid((.03, .025, .02))
    cx, cy = W / 2, H / 2
    m = Mask(cx, cy, 1)
    stone = noise(95, base=12, octaves=4)
    rings = [(330, .16), (290, .10), (250, .14), (130, .22)]
    out = img
    for r, b in rings:
        mm = Mask()
        mm.ell(cx - r, cy - r * .92, cx + r, cy + r * .92)
        if r == 330:
            mm.poly([(cx + 250, cy - 70), (cx + 520, cy - 40), (cx + 520, cy + 40), (cx + 250, cy + 70)])
        a = mm.arr(1)
        alb = np.zeros((H, W, 3), F32) + C(b, b * .95, b * .85)
        alb = alb * (0.7 + 0.6 * stone[..., None])
        out = comp(out, shade(blur(a, 10), alb, (W * .1, -H * .4), C(2.2, 1.7, 1.1), (.05, .05, .05),
                              k=30, lz=300, falloff=1500), a)
    img = out
    # milk residue
    img = img + C(.08, .07, .05) * radial(cx, cy, 140, 1)[..., None]
    lt = sstep(1.0, 3.0, t)        # hand descends
    wd = sstep(3.2, 4.8, t)        # hand withdraws
    hy = mix(-260, cy - 40, lt) - 700 * wd
    lf = Mask()
    leaf_y = hy + 40 if t < 3.1 else cy - 10
    veins = bilva(lf, cx, leaf_y, 105, 0.15)
    leaf = lf.arr(1)
    img = comp(img, shade(blur(leaf, 6), np.zeros((H, W, 3), F32) + C(.06, .24, .06),
                          (W * .1, -H * .4), C(2.4, 2.2, 1.2), (.02, .04, .02), k=25, lz=300,
                          falloff=1500, spec=.5), leaf)
    vm = Mask()
    for v in veins:
        vm.line(v, 1.6, joints=False)
    img = add_light(img, vm.arr(.5) * leaf * .7, (.4, 1.6, .3), g=4, gk=1.2)
    if wd < 1:
        hm = Mask(cx + 40, hy, 120)
        hm.ell(-.6, -1.6, .7, -.2)
        hm.poly([(-.5, -1.2), (.6, -1.2), (.5, -3.5), (-.4, -3.5)])
        for i in range(4):
            hm.line([(-.45 + i * .3, -.4), (-.4 + i * .3, .45 - abs(i - 1.5) * .12)], .2)
        hm.line([(.6, -.7), (.95, -.05)], .2)
        ha = hm.arr(1)
        img = comp(img, shade(blur(ha, 12), np.zeros((H, W, 3), F32) + SKIN * 1.1, (W * .1, -H * .4),
                              C(2.6, 1.8, 1.0), (.02, .02, .02), k=40, lz=300, falloff=1500), ha)
    return img


def milk_pour(t, d):
    img = vgrad([(0, (.05, .035, .025)), (1, (.01, .008, .006))])
    # god rays from top-left
    src = (-W * .1, -H * .3)
    ang = np.arctan2(YY - src[1], XX - src[0])
    rays = noise(101, 512, 4, base=40, octaves=3)[0]
    ai = ((ang - .1) / 1.3 * 511).clip(0, 511).astype(np.int32)
    ray = rays[ai] ** 3 * 1.6
    img = img + C(.9, .6, .28) * (ray * .35 * (1 - YY / H * .5))[..., None]
    gx = W / 2
    ln, yo = lingam_masks(gx, H * .9, 150)
    st = np.clip(ln + yo, 0, 1)
    stone = noise(102, base=10, octaves=5)
    alb = np.zeros((H, W, 3), F32) + C(.07, .065, .06) * (0.6 + 0.7 * stone[..., None])
    top = H * .9 - 2.3 * 150
    # milk sheet flowing down the lingam
    flow = top + (H * .9 - top) * sstep(0.5, 9, t)
    streak = np.roll(noise(103, base=3, sx=8, sy=.3), int(t * 12), axis=0)
    milk = ln * (YY < flow) * np.clip((streak - .42) * 3.5, 0, 1)
    milk = milk + yo * sstep(7, 13, t) * 0.6 * (0.5 + streak * .5) * radial(gx, H * .78, 260, .5)
    alb = comp(alb, C(.95, .88, .72), np.clip(milk, 0, 1) * .75)
    lit = shade(blur(st, 18) + blur(ln, 6) * .2, alb, (W * .15, -H * .2), C(2.8, 2.1, 1.3),
                (.03, .025, .02), k=60, lz=380, falloff=1600, spec=.9)
    img = comp(img, lit, st)
    # brass lota
    lm = Mask(gx + 70, 70, 70)
    lm.ell(-1, -.8, 1, .9)
    lm.poly([(-.5, -.75), (.5, -.75), (.4, -1.2), (-.4, -1.2)])
    lm.poly([(-.9, .2), (-.4, .5), (-1.15, 1.0), (-1.3, .85)])
    la = lm.arr(1)
    lit = shade(blur(la, 10), np.zeros((H, W, 3), F32) + C(.6, .38, .12), (W * .15, -H * .2),
                C(3, 2.2, 1.2), (.04, .03, .02), k=40, lz=250, falloff=1400, spec=1.5)
    img = comp(img, lit, la)
    # the stream (slow motion)
    sx0, sy0 = gx + 70 - 1.25 * 70, 70 + .95 * 70
    sm = Mask()
    pts = []
    for u in np.linspace(0, 1, 30):
        y = mix(sy0, top + 10, u)
        x = mix(sx0, gx, u ** .6) + 3 * math.sin(u * 9 - t * 2)
        pts.append((x, y))
    sm.line(pts, 13, joints=True)
    s_a = sm.arr(1.5)
    tex = np.roll(noise(104, base=4, sx=.5, sy=6), int(t * 45), axis=0)
    img = comp(img, C(1.25, 1.12, .9) * (0.75 + 0.5 * tex[..., None]), s_a)
    img = img + C(1.6, 1.2, .6) * (blur(s_a, 8) * .35)[..., None]
    # splash: golden droplets in slow motion
    rng = np.random.default_rng(7)
    nd = 160
    tb = rng.uniform(0, d, nd)
    ang = rng.uniform(-math.pi * .95, -math.pi * .05, nd)
    sp = rng.uniform(60, 230, nd)
    dm = Mask()
    for i in range(nd):
        tau = (t - tb[i]) * 0.35
        if tau < 0 or tau > 2.5:
            continue
        x = gx + math.cos(ang[i]) * sp[i] * tau
        y = top + math.sin(ang[i]) * sp[i] * tau + 0.5 * 260 * tau * tau
        if y > H * .9:
            continue
        r = 2.0 + 2.5 * (i % 3)
        vy = math.sin(ang[i]) * sp[i] + 260 * tau
        vx = math.cos(ang[i]) * sp[i]
        n = math.hypot(vx, vy) + 1e-3
        dm.line([(x, y), (x - vx / n * r * 1.5, y - vy / n * r * 1.5)], r, v=230)
    dmk = dm.arr(.7)
    img = add_light(img, dmk * sstep(.4, 1, t), (1.5, 1.15, .6), g=5, gk=1.4)
    img = glow(img, 14, .5, .95)
    return img


PANELS = [  # x0,y0,x1,y1 , appear time, renderer
    ((36, 36, 516, 684), 0.6, panel_hands),
    ((546, 36, 1244, 350), 4.4, banyan),
    ((546, 370, 1244, 684), 8.2, panel_overhead),
]


def sc_offering(t, d):
    pour_start = 14.0
    if t >= pour_start + 1.0:
        return milk_pour(t - pour_start, d - pour_start)
    paper = noise(111, base=30, octaves=3)
    img = C(.05, .045, .04) * (0.7 + 0.5 * paper[..., None])
    for (x0, y0, x1, y1), ta, fn in PANELS:
        a = sstep(ta, ta + .7, t)
        if a <= 0:
            continue
        pw, ph = x1 - x0, y1 - y0
        content = graphic(fn(t - ta))
        # crop full frame to panel aspect, then resize
        asp = pw / ph
        if asp < W / H:
            cw, ch = int(H * asp), H
        else:
            cw, ch = W, int(W / asp)
        cx0, cy0 = (W - cw) // 2, (H - ch) // 2
        crop = np.clip(content[cy0:cy0 + ch, cx0:cx0 + cw], 0, 4)
        rs = np.stack([np.asarray(Image.fromarray(np.ascontiguousarray(crop[..., i])).resize(
            (pw, ph), Image.BILINEAR)) for i in range(3)], -1)
        off = int((1 - a) * 40)
        ya, yb = y0 + off, min(H, y1 + off)
        sub = rs[:yb - ya]
        img[ya:yb, x0:x1] = img[ya:yb, x0:x1] * (1 - a) + sub * a
        # inked border
        bw = 7
        img[ya:ya + bw, x0:x1] *= 1 - a
        img[max(ya, yb - bw):yb, x0:x1] *= 1 - a
        img[ya:yb, x0:x0 + bw] *= 1 - a
        img[ya:yb, x1 - bw:x1] *= 1 - a
    if t > pour_start:
        k = sstep(pour_start, pour_start + 1.0, t)
        img = mix(img, milk_pour(0.0, d - pour_start), k)
    return img


# ================================================================== ACT III
@functools.lru_cache(None)
def village_bg():
    sky = vgrad([(0, (.30, .36, .48)), (.5, (.42, .47, .56)), (.52, (.16, .19, .26)),
                 (1, (.10, .12, .17))])
    sky = sky * (0.85 + 0.3 * noise(121, base=3, sx=3, sy=.5)[..., None])
    m = Mask()
    rng = np.random.default_rng(4)
    x = -50
    while x < W + 50:
        w = rng.uniform(90, 170)
        h = rng.uniform(50, 90)
        base = H * .52
        m.d.rectangle([x, base - h, x + w, base + 4], fill=255)
        m.d.polygon([(x - 15, base - h), (x + w / 2, base - h - rng.uniform(40, 80)), (x + w + 15, base - h)], fill=255)
        x += w + rng.uniform(10, 60)
    huts = m.arr(1)
    sky = comp(sky, C(.08, .10, .15), huts)
    return sky


def village_wide(t):
    img = village_bg().copy()
    cx = W / 2
    target = (cx, H * .5)
    rng = np.random.default_rng(17)
    people = []
    for i in range(14):
        side = -1 if i % 2 == 0 else 1
        yb = rng.uniform(H * .6, H * 1.02)
        dist = rng.uniform(170, 600)
        x = cx + side * dist * (0.6 + (yb - H * .6) / (H * .42) * .7)
        s = 40 + (yb - H * .55) * .42
        people.append((yb, x, s, i))
    people.sort()
    # pillar of light
    beam = np.exp(-((XX - cx) / 75) ** 2) * (0.75 + 0.25 * noise(122, base=4, sx=.3, sy=4))
    img = img + C(1.1, .75, .3) * (beam * .9)[..., None]
    # long caricatured shadows
    shm = Mask()
    for yb, x, s, i in people:
        dx = (x - cx) * 1.4
        shm.d.polygon([(x - s * .35, yb), (x + s * .35, yb), (x + dx + s * .6, yb + s * .7),
                       (x + dx - s * .2, yb + s * .9)], fill=200)
    img = img * (1 - .65 * shm.arr(4)[..., None])
    # Kashinath standing in the light
    sk, cl, hr = standing_masks(cx, H * .86, 95)
    union = np.clip(sk + cl + hr, 0, 1)
    alb = np.zeros((H, W, 3), F32) + SKIN
    alb = comp(alb, C(.95, .46, .08), cl)
    alb = comp(alb, HAIR, hr)
    lit = shade(blur(union, 9), alb, (cx, H * .1), C(2.6, 1.8, .9), (.05, .05, .08), k=25, lz=200,
                falloff=900)
    img = comp(img, lit, union)
    for yb, x, s, i in people:
        laugh = abs(math.sin(t * 8.5 + i * 1.7))
        bob = -laugh * s * .06
        hunch = 0.05 * math.sin(t * 4 + i)
        sk_, mk_, ft_ = Mask(), Mask(), Mask()
        villager(sk_, mk_, x, yb, s, target, bob, hunch)
        mask_features(ft_, x, yb, s, bob, hunch, laugh)
        body = sk_.arr(1)
        face = mk_.arr(1)
        rimw = np.clip(body - blur(body, 2), 0, 1) * 2.5 * np.exp(-((XX - cx) / 400) ** 2)
        bc = C(.16, .2, .3) * (0.8 + 0.4 * noise(123 + i % 3, base=8)[..., None])
        img = comp(img, bc, body)
        img = img + C(1.0, .7, .3) * rimw[..., None] * .5
        img = comp(img, C(.5, .56, .66), face)
        img = comp(img, C(.02, .02, .04), ft_.arr(.6) * face)
    return img


@functools.lru_cache(None)
def crowd_strip():
    sw = W * 3
    rng = np.random.default_rng(31)
    base = np.zeros((H, sw, 3), F32) + C(.16, .2, .3)
    base = base * (0.7 + 0.6 * noise(131, sw, H, base=8, octaves=4)[..., None])
    m = Mask(w=sw)
    mk = Mask(w=sw)
    for i in range(40):
        x = rng.uniform(0, sw)
        y = rng.uniform(H * .25, H * .55)
        s = rng.uniform(90, 160)
        m.d.ellipse([x - s * .5, y - s * .6, x + s * .5, y + s * .6], fill=255)
        m.d.rectangle([x - s * .8, y + s * .4, x + s * .8, H], fill=255)
        mk.d.ellipse([x - s * .38, y - s * .45, x + s * .38, y + s * .45], fill=255)
        for sg in (-1, 1):
            mk.d.polygon([(x + sg * s * .06, y - s * .12), (x + sg * s * .28, y - s * .22), (x + sg * s * .22, y - s * .02)], fill=0)
            mk.d.line([(x + sg * s * .04, y - s * .2), (x + sg * s * .3, y - s * .34)], fill=0, width=int(s * .05))
        mk.d.ellipse([x - s * .17, y + s * .08, x + s * .17, y + s * .36], fill=0)
    body = np.asarray(m.img, F32) / 255
    face = np.asarray(mk.img, F32) / 255
    base = comp(base, C(.08, .1, .16), body)
    base = comp(base, C(.48, .54, .64), face)
    base.flags.writeable = False
    return base


def spin_pos(t):
    """Integrated position of the 360 degree spin (pixels along crowd strip)."""
    ts = np.linspace(0, t, 200)
    v = 2600 * sstep(11.0, 14.0, ts) * (1 - sstep(20.5, 24.0, ts))
    vel = 2600 * sstep(11.0, 14.0, t) * (1 - sstep(20.5, 24.0, t))
    return float(np.trapezoid(v, ts)), vel


def village_close(t):
    pos, vel = spin_pos(t)
    strip = crowd_strip()
    bx = (XX + pos + 400)
    bg = wrap_sample(strip, bx, YY)
    if vel > 5:
        bg = blur(bg, 1, sx=min(vel * .03, 120), sy=1)
    else:
        bg = blur(bg, 3)
    bg = bg * 0.75
    ang = pos / strip.shape[1] * 2 * math.pi
    lx = W / 2 + 520 * math.sin(ang)
    beam = np.exp(-((XX - W / 2) / 260) ** 2)
    img = bg + C(.7, .45, .18) * beam[..., None] * .5
    fcx, fcy, fs = W / 2, H * .42, 150
    p = sstep(11.0, 14.5, t)
    emit = (sstep(10.8, 11.2, t) * (1 - sstep(15, 17.5, t)) * 1.0 + 0.25 * sstep(15, 17.5, t)
            * (1 - sstep(19.5, 20.5, t)) + 1.8 * fade(t, 19.8, 20.6, 22.4, 24.5))
    img, fu = render_face(img, fcx, fcy, fs, (lx, -H * .2), C(2.7, 1.9, .95),
                          amb=(.03, .035, .06), ash=p, ash_emit=emit)
    # the hand drawing the tripundra
    up = sstep(8.8, 11.0, t)
    down = sstep(14.6, 16.2, t)
    if up > 0 and down < 1:
        hx = fcx + mix(.85, -.75, p) * fs
        hy = mix(H + 200, fcy - .85 * fs, up) + down * 520
        hm = Mask(hx, hy, fs)
        for i in range(3):
            hm.line([(0.03, -.15 + i * .15), (.6, -.12 + i * .12)], .12)
        hm.ell(.45, -.28, 1.05, .4)
        hm.line([(.75, .3), (1.3, .5)], .14)
        am = Mask(hx, hy, fs)
        am.poly([(.8, .05), (1.08, .25), (2.1, 3.2), (1.5, 3.4)])
        arm = am.arr(1)
        img = comp(img, SKIN * .25 * C(.8, .85, 1.2), arm)
        ha = hm.arr(1)
        hl = shade(blur(ha, 9), np.zeros((H, W, 3), F32) + SKIN, (lx, -H * .2), C(2.7, 1.9, .95),
                   (.03, .035, .06), k=25, lz=300, falloff=1350)
        img = comp(img, hl, ha)
        tip = Mask()
        tip.circ(hx, hy, 18)
        img = add_light(img, tip.arr(4) * (p > 0) * (p < 1) * 1.0, (1.4, 1.2, .9), g=8)
    # spiritual fire leaping from the ash
    fire = fade(t, 19.8, 20.6, 22.6, 24.2)
    if fire > 0:
        rng = np.random.default_rng(44)
        fm = Mask()
        for i in range(90):
            line = i % 3
            u = rng.uniform(-.65, .65)
            y0 = fcy + (-.98 + line * .15) * fs + (u * u) * .9 * fs * .25
            ph = rng.uniform(0, 1)
            life = ((t * 1.6 + ph) % 1)
            x = fcx + u * fs + math.sin(t * 9 + i) * 3
            y = y0 - life * 70
            r = 6 * (1 - life)
            fm.circ(x, y, r, int(255 * (1 - life)))
        img = add_light(img, fm.arr(2) * fire, (2.0, 1.0, .35), g=10, gk=1.2)
    img = put_text(img, "Pride, and fear, and 'mine,' and 'how.'", 42, fade(t, 15.4, 16.8, 21.6, 23.0),
                   H * .9, color=(1.15, .85, .5))
    img = glow(img, 12, .5, 1.0)
    return img


def sc_village(t, d):
    if t < 8.5:
        img = village_wide(t)
        img = zoom(img, 1.06 + .01 * t, rot=-0.07)
        return img
    return village_close(t)


# =================================================================== ACT IV
@functools.lru_cache(None)
def tandava_bg():
    top = 0.04 * H + 0.42 * H * np.abs((XX[0] - W / 2) / (W / 2)) ** 1.6
    wall = (YY >= top[None, :]).astype(F32)
    wall = blur(wall, 1)
    stone = noise(141, base=6, octaves=6)
    blocks = np.zeros((H, W), F32)
    bh = 46
    row = (YY // bh).astype(np.int32)
    off = (row % 2) * 60
    bx = ((XX + off) % 120)
    by = YY % bh
    blocks = ((bx < 3) | (by < 3)).astype(F32)
    alb = C(.30, .23, .17)[None, None] * (0.55 + 0.75 * stone[..., None])
    alb = alb * (1 - .55 * blur(blocks, 1)[..., None])
    floor = (YY > H * .86).astype(F32)
    alb = comp(alb, C(.22, .17, .13) * (0.6 + 0.6 * noise(142, base=10)[..., None]), floor)
    return wall, alb, floor


def sc_tandava(t, d):
    T = t + TL.SCENES[5][1]
    beats = TL.tandava_beats()
    env = TL.beat_env(T, beats, 6)
    k = sum(1 for b in beats if b <= T)
    if 0 < k < len(beats):
        frac = (T - beats[k - 1]) / (beats[k] - beats[k - 1])
    else:
        frac = 0.0
    ph = math.pi * (k + sstep(0, 1, frac))
    wall, alb, floor = tandava_bg()
    flick = 0.85 + 0.1 * math.sin(t * 13) + 0.05 * math.sin(t * 29)
    lamp = (W / 2, H * 1.02)
    lightfield = radial(lamp[0], lamp[1], 1000, 1.4) * flick
    # night sky
    sky = INDIGO * .6 + C(.05, .04, .12) * noise(143, base=2)[..., None]
    pole = (W / 2, -260)
    rng = np.random.default_rng(8)
    ns = 260
    sr = rng.uniform(320, 1500, ns)
    sa = rng.uniform(0, 2 * math.pi, ns)
    sb = rng.uniform(.3, 1, ns)
    rot = lambda tt: 0.01 * tt + 0.55 * sstep(5, 27, tt) ** 2.2 * 6
    smk = Mask()
    for i in range(ns):
        for j in range(8):
            tt = t - j * 0.06
            a = sa[i] + rot(tt)
            x, y = pole[0] + sr[i] * math.cos(a), pole[1] + sr[i] * math.sin(a)
            if -5 < x < W + 5 and -5 < y < H + 5:
                smk.circ(x, y, 1.4, int(255 * sb[i] * (1 - j / 8)))
    stars = smk.arr(.6)
    img = sky + C(1.0, .95, .85) * stars[..., None]
    # lit wall with shadow
    seated_sh = np.clip(sum(seated_masks(W / 2, H * .86, 210)), 0, 1)
    morph = sstep(1.8, 4.2, t)
    nm = nataraja_mask(W / 2, H * .86, 150 * (1 + .015 * env), ph, env).arr(0)
    shadow = blur(seated_sh * (1 - morph) + nm * morph, 3.5)
    lw = alb * (0.05 + 3.2 * lightfield[..., None] * C(1.0, .62, .3))
    lw = lw * (1 - .95 * np.clip(shadow * 1.4, 0, 1)[..., None] * (1 - floor[..., None]))
    img = comp(img, lw, wall)
    # Kashinath, motionless, lit from the front
    img, _ = render_seated(img, W / 2, H * .935, 70, (W / 2, H * .75), C(1.3, .8, .35) * flick,
                           amb=(.02, .02, .04), rim=C(.2, .25, .5))
    # stars fall as golden sparks into the crown
    crown = (W / 2, H * .935 - 70 * 2.0)
    sp = Mask()
    absorbed = 0
    for i in range(0, ns, 3):
        td = 9 + (i / ns) * 13
        if t < td:
            continue
        a0 = sa[i] + rot(td)
        p0 = (pole[0] + sr[i] * math.cos(a0), pole[1] + sr[i] * math.sin(a0))
        for j in range(6):
            tau = max(0.0, t - td - j * .04)
            f = math.exp(-tau * .75)
            if f < .02:
                break
            spin = tau * 2.2
            dx, dy = p0[0] - crown[0], p0[1] - crown[1]
            x = crown[0] + f * (dx * math.cos(spin) - dy * math.sin(spin))
            y = crown[1] + f * (dx * math.sin(spin) + dy * math.cos(spin))
            sp.circ(x, y, 2.2 - j * .3, int(255 * (1 - j / 6)))
        if math.exp(-(t - td) * .75) < .05:
            absorbed += 1
    img = add_light(img, sp.arr(.8), (1.8, 1.15, .4), g=5, gk=1.5)
    cg = min(1.0, absorbed / 40)
    img = img + C(1.6, 1.1, .5) * (radial(crown[0], crown[1], 40 + 120 * cg, 2) * (cg * 1.5 + env * .3))[..., None]
    # heartbeat colour pulse: blue-black <-> explosive amber
    grade = mix(C(.42, .55, 1.05), C(1.45, 1.0, .55), env * sstep(2.5, 4, t))
    img = img * grade
    th = TL.thunder_time() - TL.SCENES[5][1]
    if t > th:
        fl = math.exp(-(t - th) * 5) * (0.6 + 0.4 * math.sin((t - th) * 60))
        img = img + C(.8, .85, 1.2) * fl
        img = img * (1 - sstep(th + .4, d, t) * .7)
    img = glow(img, 12, .55, .95)
    return img


# ==================================================================== ACT V
def shiva_reflection(t, amt):
    refl = np.zeros((H, W, 3), F32)
    fcx, fcy, fs = W / 2, H * .63, 82
    if amt < 1:
        a, _ = render_face(refl.copy(), fcx, fcy + 30, fs * 1.15, (W * .3, H * .25), C(2.0, 1.5, 1.0),
                           amb=(.05, .06, .09))
        refl = a * (1 - amt)
    if amt > 0:
        th = fade(t, 9.0, 10.5, 99, 100) * (0.75 + 0.25 * math.sin(t * 4))
        b, _ = render_face(np.zeros((H, W, 3), F32), fcx, fcy, fs, (W * .5, H * .1),
                           C(2.3, 2.0, 1.7), amb=(.08, .1, .16), skin=C(.24, .3, .44),
                           shiva=True, throat=th)
        # third eye
        em = Mask(fcx, fcy, fs)
        em.ell(-.07, -1.05, .07, -.72)
        b = add_light(b, em.arr(1) * fade(t, 11, 12, 99, 100), (1.6, .6, .3), g=6)
        # crescent moon in the locks
        mm = Mask(fcx, fcy, fs)
        mm.circ(-.75, -2.45, .42)
        mm.circ(-.6, -2.58, .38, 0)
        b = add_light(b, mm.arr(1) * fade(t, 8.0, 9.2, 99, 100), (1.3, 1.35, 1.6), g=10, gk=1.2)
        # Ganga: liquid light pouring from the hair
        gm = Mask(fcx, fcy, fs)
        ctrl = [(.2, -3.7), (1.3, -4.3), (2.3, -3.4), (2.7, -1.2), (2.9, 1.5), (3.3, 4.5)]
        pts = []
        for u in np.linspace(0, 1, 60):
            k = u * (len(ctrl) - 1)
            i = min(int(k), len(ctrl) - 2)
            f = k - i
            f = f * f * (3 - 2 * f)
            pts.append((mix(ctrl[i][0], ctrl[i + 1][0], f), mix(ctrl[i][1], ctrl[i + 1][1], f)))
        gm.line(pts, .42, joints=True)
        g = gm.arr(6)
        flow = np.roll(noise(151, base=3, sx=2, sy=8), int(t * 140), axis=0)
        gv = g * (0.4 + 1.2 * flow) * fade(t, 9.5, 11.5, 99, 100)
        b = add_light(b, gv, (1.6, 1.3, .7), g=8, gk=1.0)
        refl = refl + b * amt
    return refl


def sc_throat(t, d):
    if t >= 15.5:
        return throat_close(t - 15.5, d - 15.5)
    water_top = H * .21
    img = vgrad([(0, (.01, .012, .03)), (.21, (.03, .035, .07)), (.22, (.02, .035, .07)),
                 (1, (.005, .012, .03))])
    img = img + C(.9, .9, 1) * (starfield(6, 200) * (YY < water_top))[..., None]
    moon = Mask()
    moon.circ(W * .82, H * .09, 22)
    img = add_light(img, moon.arr(1), (1.2, 1.2, 1.3), g=20, gk=.8)
    # bank and kneeling seeker in silhouette
    bank = (YY < water_top + 6 * np.sin(XX / 90)) & (YY > water_top - 22 - 20 * noise(152, base=3))
    img = comp(img, C(.015, .015, .025), bank.astype(F32))
    img, _ = render_seated(img, W * .5, water_top + 4, 40, (W * .82, H * .09), C(.4, .45, .6),
                           amb=(.005, .005, .01), ribs=False, rim=C(.3, .35, .55))
    # water + reflection with ripples
    amt = sstep(4.5, 8.5, t)
    refl = shiva_reflection(t, amt)
    wob = 1 + 1.5 * fade(t, 4, 6, 7.5, 9.5)
    sx = XX + (3.5 * np.sin(YY / 24 + t * 2.3) + 1.2 * np.sin(YY / 7 - t * 3.9 + XX / 70)) * wob
    sy = YY + 2 * np.sin(XX / 37 + t * 1.7)
    rr = sample(refl, sx, sy)
    if 0 < amt < 1 or wob > 1:
        dd = np.sqrt((XX - W / 2) ** 2 + (YY - H * .64) ** 2)
        ring = 0.5 + 0.5 * np.sin(dd / 18 - t * 7)
        psy = fade(t, 4, 6, 7.5, 9.5)
        rr = rr * (1 + psy * (ring[..., None] * C(-.3, .4, 1.2) + (1 - ring[..., None]) * C(1.2, .6, -.2)))
    wm = (YY > water_top).astype(F32)
    stars_r = np.roll(starfield(6, 200), int(water_top * .3), axis=0) * .25
    rr = rr + C(.6, .65, .8) * stars_r[..., None]
    hl = (noise(153, base=4, sx=6, sy=.4) > .78).astype(F32) * .08
    rr = rr + C(.5, .6, .8) * np.roll(hl, int(t * 15), axis=1)[..., None]
    img = comp(img, img * .3 + rr * C(.8, .9, 1.1), wm * fade(t, 0.5, 2.5, 99, 100) + wm * 0)
    img = img * (1 - wm[..., None] * (1 - fade(t, 0.5, 2.5, 99, 100)) * .0)
    img = glow(img, 12, .6, .9)
    return img


def throat_close(t, d):
    img = solid((.008, .01, .02))
    fcx, fcy, fs = W / 2, H * .1, 205
    th = sstep(1.0, 4.0, t)
    img, fu = render_face(img, fcx, fcy, fs, (W * .2, -H * .1), C(1.9, 1.5, 1.1),
                          amb=(.02, .025, .05))
    nk = Mask(fcx, fcy, fs)
    nk.ell(-.52, 1.0, .52, 2.55)
    neck = nk.arr(fs * .06)
    swirl = zoom(np.dstack([noise(161, base=3), noise(162, base=4), noise(163, base=2)]),
                 1.0, fcx, fcy + 1.8 * fs, rot=t * .9)
    sw = np.sin(swirl[..., :1] * 14 + t * 1.5) * .5 + .5
    pois = C(.03, .2, 1.1) * (0.3 + 1.3 * sw ** 3) + C(.5, .15, 1.2) * swirl[..., 1:2] ** 4
    pulse = 0.8 + 0.2 * math.sin(t * 3.2)
    img = comp(img, img * .35 + pois * pulse, neck * th * .9)
    img = img + C(.1, .3, 1.0) * (blur(neck, 25) * th * .5 * pulse)[..., None]
    # hand at the throat
    hx, hy = fcx + .45 * fs, fcy + 1.7 * fs
    ent = sstep(0.0, 1.2, t)
    hm = Mask(hx + (1 - ent) * 300, hy + (1 - ent) * 300, fs)
    for i in range(4):
        hm.line([(.5, -.3 + i * .16), (.12 - .06 * abs(i - 1.5), -.22 + i * .15),
                 (.02 - .05 * abs(i - 1.5), -.12 + i * .14)], .12)
    hm.ell(.35, -.45, 1.05, .45)
    hm.line([(.6, .3), (.25, .45)], .13)
    hm.poly([(.7, -.1), (1.05, .15), (1.9, 2.6), (1.2, 2.8)])
    ha = hm.arr(1)
    hl = shade(blur(ha, 10), np.zeros((H, W, 3), F32) + SKIN, (W * .2, -H * .1), C(1.9, 1.5, 1.1),
               (.02, .025, .05), k=25, lz=300, falloff=1800)
    img = comp(img, hl, ha)
    img = put_text(img, "Keep what burns, and still you'll stay.", 42, fade(t, 0.8, 2.3, 6.6, 8.0),
                   H * .9, color=(.75, .85, 1.2))
    img = glow(img, 12, .5, .95)
    return img


# =================================================================== ACT VI
@functools.lru_cache(None)
def frost_mask():
    rng = np.random.default_rng(55)
    m = Mask()

    def branch(x, y, a, ln, depth, wd):
        if depth == 0 or ln < 3:
            return
        x2, y2 = x + ln * math.cos(a), y + ln * math.sin(a)
        m.d.line([(x, y), (x2, y2)], fill=int(120 + 30 * depth), width=max(1, int(wd)))
        for f in (0.35, 0.6, 0.85):
            bx, by = x + (x2 - x) * f, y + (y2 - y) * f
            for sg in (-1, 1):
                if rng.random() < .8:
                    branch(bx, by, a + sg * math.pi / 3, ln * .38, depth - 1, wd * .6)
    # crystal mountain peaks (Kailash) across the floor
    for k in range(7):
        px = W * (.52 + k * .085) + rng.uniform(-20, 20)
        py = H * rng.uniform(.62, .9)
        hgt = rng.uniform(110, 210)
        apex = (px, py - hgt)
        for sg in (-1, 1):
            base = (px + sg * hgt * .8, py)
            n = 9
            for j in range(n):
                f = j / n
                x = apex[0] + (base[0] - apex[0]) * f
                y = apex[1] + (base[1] - apex[1]) * f
                branch(x, y, math.atan2(base[1] - apex[1], base[0] - apex[0]) + sg * .3, 22, 3, 2)
            m.d.line([apex, base], fill=255, width=2)
        branch(apex[0], apex[1], math.pi / 2, hgt * .6, 4, 2)
    for _ in range(120):
        branch(rng.uniform(W * .45, W), rng.uniform(H * .6, H), rng.uniform(0, 2 * math.pi),
               rng.uniform(10, 35), 3, 1)
    a = m.arr(.5)
    a.flags.writeable = False
    return a


def sc_snow(t, d):
    img = solid((.006, .008, .016))
    win = np.clip(1 - np.abs((XX - W * .7) + (YY - H * .5) * .4) / 220, 0, 1) * (YY > H * .45)
    img = img + C(.05, .07, .12) * (win * fade(t, 0, 3, 99, 100))[..., None]
    floor = (YY > H * .5).astype(F32)
    img = img + C(.01, .015, .03) * floor[..., None]
    mat = Mask()
    mat.poly([(W * .2, H * .6), (W * .8, H * .6), (W * .84, H * .7), (W * .16, H * .7)])
    img = comp(img, C(.04, .045, .06), mat.arr(2))
    fig = lying_mask(W * .5, H * .62, 140)
    dissolve = sstep(13.0, 19.0, t)
    fv = fade(t, 0.5, 3.0, 99, 100) * (1 - dissolve)
    img = comp(img, C(.85, .9, 1.0), fig * fv)
    img = img + C(.4, .5, .8) * (blur(fig, 14) * fv * .6)[..., None]
    # frost creeping toward his feet
    fr = frost_mask()
    D = (W - XX) / W + noise(171, base=4) * .12
    reach = .02 + .34 * sstep(1.0, 11.5, t)
    rev = np.clip((reach - D) * 25, 0, 1)
    glint = 0.6 + 0.4 * np.sin(XX * .05 + YY * .07 + t * 3)
    img = img + C(.55, .75, 1.1) * (fr * rev * glint * .8)[..., None]
    img = img + C(.2, .3, .55) * (blur(fr * rev, 6) * .5)[..., None]
    # snow that rises instead of falling
    rise = sstep(10.5, 13.0, t)
    if rise > 0:
        rng = np.random.default_rng(66)
        n = 260
        bx = rng.uniform(W * .2, W * .95, n)
        by = rng.uniform(H * .5, H * .75, n)
        tb = rng.uniform(10.5, 19.5, n)
        vs = rng.uniform(25, 70, n)
        ph = rng.uniform(0, 6.28, n)
        rs = rng.uniform(1.0, 3.2, n)
        sm = Mask()
        for i in range(n):
            tau = t - tb[i]
            if tau < 0:
                continue
            x = bx[i] + 14 * math.sin(tau * 1.3 + ph[i])
            y = by[i] - vs[i] * tau
            if y < -10:
                continue
            a = min(1, tau * 2)
            r = rs[i]
            sm.circ(x, y, r, int(255 * a))
            if r > 2.4:
                for kk in range(3):
                    aa = kk * math.pi / 3 + tau
                    sm.d.line([(x - 2.4 * r * math.cos(aa), y - 2.4 * r * math.sin(aa)),
                               (x + 2.4 * r * math.cos(aa), y + 2.4 * r * math.sin(aa))],
                              fill=int(180 * a), width=1)
        img = add_light(img, sm.arr(.6), (.95, 1.0, 1.15), g=4, gk=1.2)
    # the Om: a single expanding ring of light
    om = fade(t, 12.8, 13.8, 17.5, 19.5)
    if om > 0:
        rr = 40 + (t - 12.8) * 160
        dd = np.sqrt((XX - W * .5) ** 2 + ((YY - H * .62) * 1.6) ** 2)
        ring = np.exp(-((dd - rr) / 18) ** 2)
        img = img + C(.35, .45, .7) * (ring * om * .5)[..., None]
    img = img * (1 - sstep(18.5, 20, t) * .6)
    return img


# ================================================================== ACT VII
def door_scene(t):
    img = vgrad([(0, (.55, .5, .45)), (1, (.25, .2, .16))])
    wall = Mask()
    wall.d.rectangle([W * .12, H * .28, W * .88, H * .9], fill=255)
    wa = wall.arr(1)
    mud = C(.42, .32, .22) * (0.7 + 0.5 * noise(181, base=6)[..., None])
    img = comp(img, mud, wa)
    roof = Mask()
    roof.poly([(W * .05, H * .32), (W * .5, H * .02), (W * .95, H * .32)])
    img = comp(img, C(.16, .12, .07) * (0.6 + 0.6 * noise(182, base=3, sx=.3, sy=6)[..., None]), roof.arr(1))
    dx0, dx1, dy0, dy1 = W * .43, W * .57, H * .42, H * .9
    op = sstep(1.8, 4.2, t)
    door = Mask()
    door.d.rectangle([dx0, dy0, dx1, dy1], fill=255)
    da = door.arr(.8)
    img = comp(img, C(2.6, 2.5, 2.3) * (0.2 + op * 1.0), da)
    pan = Mask()
    pan.d.polygon([(dx0, dy0), (dx0 + (dx1 - dx0) * (1 - op * .85), dy0 - 6 * op),
                   (dx0 + (dx1 - dx0) * (1 - op * .85), dy1 + 6 * op), (dx0, dy1)], fill=255)
    img = comp(img, C(.2, .12, .06) * (0.7 + 0.5 * noise(183, base=3, sx=.2, sy=5)[..., None]), pan.arr(.8))
    # light spill + rays
    ang = np.arctan2(YY - H * .62, XX - W / 2)
    rays = noise(184, 360, 4, base=30, octaves=2)[0]
    ri = ((ang + math.pi) / (2 * math.pi) * 359).astype(np.int32)
    spill = radial(W / 2, H * .66, 900, 1.5) * (0.6 + rays[ri] * .8)
    img = img + C(1.6, 1.4, 1.1) * (spill * op * 1.2)[..., None]
    img = img + C(1.5, 1.4, 1.2) * (blur(da, 40) * op * 1.5)[..., None]
    # villagers, backlit
    for i, (x, sc) in enumerate(((.3, 120), (.4, 140), (.62, 135), (.72, 118))):
        sk, cl, hr = standing_masks(W * x, H * 1.12, sc)
        m = np.clip(sk + cl + hr, 0, 1)
        img = comp(img, C(.05, .04, .04), m)
        rim = np.clip(m - blur(m, 3), 0, 1) * 3
        img = img + C(1.5, 1.3, 1.0) * (rim * (0.2 + op))[..., None]
    return img


def white_room(t):
    img = solid((1.5, 1.45, 1.35))
    fog = noise(191, base=3)
    img = img * (0.92 + 0.1 * fog[..., None])
    mat = Mask()
    mat.poly([(W * .15, H * .58), (W * .85, H * .58), (W * .92, H * .78), (W * .08, H * .78)])
    img = comp(img, C(1.15, 1.0, .78), mat.arr(3) * .6)
    fig = blur(lying_mask(W * .5, H * .67, 150), 5)
    pulse = 0.75 + 0.25 * math.sin(t * 2.5)
    img = comp(img, C(.75, .68, .55), fig * .55)
    img = img + C(.9, .6, .2) * (blur(fig, 12) * pulse * .5)[..., None]
    ashp = drift_mask(t, 70, 19, (W * .2, H * .2, W * .8, H * .75), (2, -18), r=(.7, 1.8), wrap=True)
    img = img - C(.6, .62, .65) * ashp[..., None] * .7
    return img


@functools.lru_cache(None)
def landscape():
    W2, H2 = W * 2, H * 2
    yy, xx = np.mgrid[0:H2, 0:W2].astype(F32)
    base = .47 * H2
    sky_t = yy / base
    sky = np.zeros((H2, W2, 3), F32)
    sky[:] = (C(.9, .62, .35)[None, None] * (1 - sky_t[..., None]) + C(1.45, 1.15, .7) * sky_t[..., None])
    sun = np.exp(-(((xx - W2 * .56) ** 2 + (yy - base * .7) ** 2) / (2 * 260 ** 2)))
    sky = sky + C(1.6, 1.3, .8) * sun[..., None]
    cl = noise(201, W2, H2, base=2, sx=3, sy=.6)
    sky = sky * (0.85 + 0.3 * cl[..., None])
    # reclining Shiva ridge
    prof = [(0, .01), (.08, .02), (.12, .05), (.15, .04), (.18, .08), (.21, .065), (.24, .1),
            (.27, .13), (.29, .15), (.305, .155), (.315, .15), (.325, .2), (.335, .165),
            (.345, .16), (.352, .17), (.36, .158), (.37, .162), (.385, .155), (.40, .14),
            (.43, .1), (.47, .13), (.53, .18), (.60, .19), (.66, .15), (.72, .13), (.78, .145),
            (.84, .2), (.89, .13), (.93, .11), (.955, .17), (.975, .08), (1.0, .02)]
    px = np.array([p[0] for p in prof]) * W2
    ph = np.array([p[1] for p in prof]) * H2 * 1.25
    ridge = base - np.interp(np.arange(W2), px, ph)
    rn = noise(202, W2, 8, base=20, octaves=3)[4] * 12
    ridge = ridge - rn
    mtn = (yy >= ridge[None, :]) & (yy < base + 5)
    mcol = C(.42, .36, .45)[None, None] * (0.8 + 0.4 * noise(203, W2, H2, base=6)[..., None])
    depth = np.clip((yy - ridge[None, :]) / 200, 0, 1)
    mcol = mix(C(1.0, .78, .55)[None, None], mcol, depth[..., None] * .8 + .2)
    img = np.where(mtn[..., None], mcol, sky)
    # plains
    plain_t = np.clip((yy - base) / (H2 - base), 0, 1)
    pl = mix(C(.75, .58, .38)[None, None], C(.18, .2, .1)[None, None], plain_t[..., None] ** .7)
    pl = pl * (0.75 + 0.5 * noise(204, W2, H2, base=5, sx=2, sy=.5)[..., None])
    img = np.where((yy >= base)[..., None], pl, img)
    # river: silver ribbon
    rm = Mask(w=W2, h=H2)
    path = []
    for u in np.linspace(0, 1, 160):
        y = H2 - (H2 - base) * u ** .8
        x = W2 * (.5 + .22 * math.sin(u * 7.5) * (1 - u) ** .6 + .05 * u)
        path.append((x, y, 46 * (1 - u) ** 1.4 + 4))
    for (x0, y0, w0), (x1, y1, _) in zip(path[:-1], path[1:]):
        rm.d.line([(x0, y0), (x1, y1)], fill=255, width=int(w0))
        rm.d.ellipse([x0 - w0 / 2, y0 - w0 / 2, x0 + w0 / 2, y0 + w0 / 2], fill=255)
    river = blur(np.asarray(rm.img, F32) / 255, 1.5)
    img = comp(img, C(1.35, 1.38, 1.45), river)
    haze = np.exp(-((yy - base) / 160) ** 2)
    img = img + C(.5, .4, .25) * haze[..., None] * .6
    ridge_line = np.exp(-((yy - ridge[None, :]) / 6) ** 2)
    img.flags.writeable = False
    river.flags.writeable = False
    ridge_line = ridge_line.astype(F32)
    ridge_line.flags.writeable = False
    return img, river, ridge_line


def aerial(t, d):
    L, river, ridge = landscape()
    u = sstep(0, 11, t)
    sc = mix(0.55, 2.0, u ** 1.3)
    cx = mix(W * 1.05, W, u)
    cy = mix(H * 1.75, H, u)
    sx = cx + (XX - W / 2) * sc
    sy = cy + (YY - H / 2) * sc
    img = sample(L, sx, sy)
    rv = sample(river, sx, sy)
    rg = sample(ridge, sx, sy)
    merge = sstep(6, 10, t)
    pulse = 0.65 + 0.35 * math.sin(t * 2.6)
    img = img + C(1.4, 1.1, .6) * ((rv * 1.2 + rg * 1.5) * merge * pulse)[..., None]
    img = img + C(1.0, .8, .45) * (blur(rv + rg, 14) * merge * pulse * 1.3)[..., None]
    img = mix(img, C(2.0, 1.7, 1.2), sstep(9, 12, t) * .35)
    return img


def sc_return(t, d):
    if t < 6.5:
        img = door_scene(t)
        if t > 5.5:
            img = mix(img, C(1.8, 1.7, 1.55), sstep(5.5, 6.5, t))
        return img
    if t < 11.5:
        img = white_room(t - 6.5)
        img = zoom(img, 1.08 - (t - 6.5) * .015, W / 2, H * .62 - (t - 6.5) * 6)
        if t < 7.2:
            img = mix(C(1.8, 1.7, 1.55), img, sstep(6.5, 7.2, t))
        if t > 10.8:
            img = mix(img, C(2.2, 2.0, 1.7), sstep(10.8, 11.5, t))
        return img
    tt = t - 11.5
    img = aerial(tt, d - 11.5)
    if tt < 1.6:
        img = mix(C(2.2, 2.0, 1.7), img, sstep(0, 1.6, tt))
    tb = fade(tt, 7.0, 9.0, 12.4, 13.6)
    img = img * (1 - .45 * tb * sstep(H * .6, H * .95, YY)[..., None])
    img = put_text(img, "हर हर महादेव", 46, fade(tt, 7.5, 9.0, 12.4, 13.6), H * .78,
                   color=(1.4, 1.0, .5), font=FONT_DEVA, lang="hi", glow_s=8)
    img = put_text(img, "Har Har Mahadev.", 44, fade(tt, 8.0, 9.5, 12.4, 13.6), H * .88,
                   color=(1.45, 1.1, .6), font=FONT_TEXT, glow_s=8)
    img = glow(img, 16, .5, 1.1)
    img = img * (1 - sstep(12.6, 14.5, tt))
    return img


def sc_credits(t, d):
    img = solid((.004, .004, .008))
    emb = drift_mask(t, 40, 3, (0, -40, W, H + 40), (3, -20), sway=15, r=(.6, 1.6))
    img = add_light(img, emb * fade(t, 0, 1.5, d - 1.5, d), (1.4, .6, .2), g=3, gk=1.2)
    a = fade(t, .5, 1.8, d - 1.8, d - .3)
    img = put_text(img, "THE ASH-SMEARED HEART", 44, a, H * .42, color=(1.2, .8, .38),
                   font=FONT_TITLE, tracking=5, glow_s=6, glow_k=.4)
    img = put_text(img, "imagery & score rendered procedurally", 22, a * .8, H * .54,
                   color=(.65, .6, .55), glow_s=0)
    img = put_text(img, "ॐ", 40, a, H * .66, color=(1.1, .75, .35), font=FONT_DEVA, glow_s=6)
    return img


RENDER = {
    "title": sc_title, "ghats": sc_ghats, "cosmos": sc_cosmos, "offering": sc_offering,
    "village": sc_village, "tandava": sc_tandava, "throat": sc_throat, "snow": sc_snow,
    "return": sc_return, "credits": sc_credits,
}


def chapter_overlay(img, name, lt):
    if name not in TL.CHAPTERS:
        return img
    a = fade(lt, 0.1, 1.0, 3.0, 4.2)
    if a <= 0:
        return img
    num, title = TL.CHAPTERS[name]
    img = img * (1 - .6 * a)
    img = put_text(img, num, 30, a, H * .40, color=(1.0, .7, .35), font=FONT_TITLE, glow_s=4)
    img = put_text(img, title, 50, a, H * .50, color=(1.2, .85, .45), font=FONT_TITLE,
                   tracking=5, glow_s=8, glow_k=.5)
    return img


def frame(T):
    name, lt, d = TL.scene_at(T)
    img = RENDER[name](lt, d)
    img = chapter_overlay(img, name, lt)
    return img
