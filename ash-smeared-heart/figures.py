"""Characters and props, built from masks and lit with `shade`."""
import math

import numpy as np

from engine import (C, F32, H, W, XX, YY, Mask, blur, comp, noise, shade)

SKIN = C(0.30, 0.18, 0.11)
SAFFRON = C(0.95, 0.46, 0.08)
HAIR = C(0.06, 0.045, 0.04)
ASH = C(0.78, 0.76, 0.72)


# ------------------------------------------------------------ seated ascetic
def seated_masks(cx, cy, s, hands="knees"):
    sk, cl, hr = Mask(cx, cy, s), Mask(cx, cy, s), Mask(cx, cy, s)
    # emaciated torso
    sk.poly([(-.40, -.30), (.40, -.30), (.30, -.78), (.50, -1.16), (.28, -1.30),
             (-.28, -1.30), (-.50, -1.16), (-.30, -.78)])
    sk.ell(-.60, -1.30, -.30, -1.02)
    sk.ell(.30, -1.30, .60, -1.02)
    sk.poly([(-.09, -1.46), (.09, -1.46), (.10, -1.22), (-.10, -1.22)])
    sk.ell(-.19, -1.86, .19, -1.38)
    # arms
    for sg in (-1, 1):
        sk.line([(sg * .48, -1.15), (sg * .70, -.62)], .14)
        sk.line([(sg * .70, -.62), (sg * .84, -.24)], .11)
        sk.ell(sg * .84 - .08, -.30, sg * .84 + .08, -.16)
    # crossed legs + waist wrap + sash
    cl.ell(-1.0, -.42, 1.0, .06)
    cl.poly([(-.42, -.26), (.42, -.26), (.36, -.52), (-.36, -.52)])
    cl.poly([(-.52, -1.18), (-.30, -1.28), (.42, -.44), (.18, -.30)])
    # matted hair: bun + locks
    hr.ell(-.20, -1.90, .20, -1.62)
    hr.ell(-.14, -2.12, .14, -1.84)
    hr.poly([(-.20, -1.72), (-.25, -1.30), (-.17, -1.34), (-.15, -1.66)])
    hr.poly([(.20, -1.72), (.25, -1.30), (.17, -1.34), (.15, -1.66)])
    return sk.arr(), cl.arr(), hr.arr()


def render_seated(img, cx, cy, s, light, lcol, amb=(0.04, 0.04, 0.07), ribs=True,
                  rim=None, alpha=1.0):
    sk, cl, hr = seated_masks(cx, cy, s)
    union = np.clip(sk + cl + hr, 0, 1)
    alb = np.zeros((H, W, 3), F32) + SKIN
    if ribs:
        rb = Mask(cx, cy, s)
        for i in range(4):
            y = -1.05 + i * .09
            for sg in (-1, 1):
                rb.line(rb.arc_pts(sg * .14, y, .16, .05, math.pi * (0.1 if sg > 0 else .55),
                                   math.pi * (.45 if sg > 0 else .9), 8), .018, joints=False)
        alb = alb * (1 - 0.45 * rb.arr(1.2)[..., None])
    folds = 0.75 + 0.5 * noise(31, base=4, sx=0.5, sy=6)[..., None]
    alb = comp(alb, SAFFRON * folds, cl)
    alb = comp(alb, HAIR, hr)
    height = blur(union, s * .09) + blur(sk, s * .03) * .4
    lit = shade(height, alb, light, lcol, amb, k=s * .25, lz=s * 1.5, falloff=s * 6)
    if rim is not None:
        edge = np.clip(union - blur(union, s * .02 + 1), 0, 1) * 3
        lit += np.asarray(rim, F32) * edge[..., None]
    return comp(img, lit, union * alpha), union


# --------------------------------------------------------------- tiger skin
def tiger_skin(img, cx, cy, s, light, lcol):
    m = Mask(cx, cy, s)
    m.poly([(-1.5, -.15), (-1.2, -.3), (1.2, -.3), (1.55, -.12), (1.7, .05), (1.3, .12),
            (-1.3, .12), (-1.75, .02)])
    a = m.arr(1.2)
    stripes = noise(41, base=3, sx=4, sy=.6)
    st = (np.sin(XX / (s * .09) + stripes * 8) > 0.55).astype(F32)
    alb = C(0.62, 0.34, 0.09)[None, None] * (1 - 0.85 * st[..., None])
    lit = shade(blur(a, s * .05), alb, light, lcol, (0.03, 0.03, 0.05), k=s * .2, lz=s,
                falloff=s * 6)
    return comp(img, lit, a)


# -------------------------------------------------------------- oil lamp
def diya(img, x, y, s, t, flick):
    m = Mask(x, y, s)
    m.ell(-1, -.35, 1, .45)
    m.poly([(-1, 0), (1, 0), (.6, .55), (-.6, .55)])
    bowl = m.arr(1)
    img = comp(img, C(0.25, 0.1, 0.04), bowl)
    img = img + C(1.0, .5, .15) * (np.clip(bowl - blur(bowl, 2), 0, 1) * 2)[..., None]
    img = flame(img, x, y - .3 * s, s, t, flick)
    return img


def flame(img, x, y, s, t, flick, col=(2.6, 1.5, .5), hscale=1.0):
    f = Mask(x, y, s)
    hgt = (1.9 + 0.6 * flick) * hscale
    sway = 0.25 * math.sin(t * 7.3) + 0.15 * math.sin(t * 13.1)
    us = np.linspace(0, 1, 18)
    right = [(.38 * math.sin(math.pi * u ** .45) * (1 - u) ** .5 + sway * u * u, -hgt * u) for u in us]
    left = [(-.38 * math.sin(math.pi * u ** .45) * (1 - u) ** .5 + sway * u * u, -hgt * u)
            for u in us[::-1]]
    f.poly(right + left)
    fl = f.arr(1.5)
    core = Mask(x, y, s)
    core.ell(-.14, -hgt * .5, .14, -.02)
    img = img + np.asarray(col, F32) * fl[..., None]
    img = img + C(2.5, 2.3, 1.8) * core.arr(2)[..., None]
    return img


# ------------------------------------------------------------------ the face
def face_masks(cx, cy, s, mouth=0.0, shiva=False):
    """Front face. Units: face oval spans x in [-1,1], y in [-1.3,1.3]."""
    fc, hr, ft, lip, mo = (Mask(cx, cy, s) for _ in range(5))
    fc.ell(-1, -1.3, 1, 1.25)
    fc.poly([(-.95, .2), (.95, .2), (.55, 1.15), (0, 1.38), (-.55, 1.15)])
    fc.poly([(-.55, .9), (.55, .9), (.6, 2.7), (-.6, 2.7)])          # neck
    fc.ell(-3.2, 2.1, 3.2, 4.6)                                       # shoulders
    fc.ell(-1.12, -.25, -.86, .35)                                    # ears
    fc.ell(.86, -.25, 1.12, .35)
    # hair
    if shiva:
        hr.ell(-1.3, -2.0, 1.3, -.55)
        hr.ell(-.9, -3.4, .9, -1.6)
        hr.ell(-.6, -3.9, .6, -2.9)
        for sg in (-1, 1):
            hr.poly([(sg * 1.0, -1.2), (sg * 1.5, -.2), (sg * 1.75, 2.6), (sg * 1.25, 2.8),
                     (sg * 1.1, .4), (sg * .95, -.6)])
    else:
        hr.ell(-1.12, -1.75, 1.12, -.62)
        hr.ell(-.7, -2.6, .7, -1.55)
        for sg in (-1, 1):
            hr.poly([(sg * 1.0, -1.0), (sg * 1.3, 0), (sg * 1.4, 2.2), (sg * 1.05, 2.4),
                     (sg * 1.02, .2), (sg * .92, -.5)])
    # features (dark lines)
    for sg in (-1, 1):
        ft.line([(sg * .14, -.46), (sg * .45, -.55), (sg * .75, -.44)], .07)
        ft.line(ft.arc_pts(sg * .44, -.26, .26, .09, .15 * math.pi, .85 * math.pi, 10), .045)
        ft.ell(sg * .2 - .07, .40, sg * .2 + .07, .46)
    ft.line([(.06, -.25), (.13, .3)], .025, v=110)
    # lips
    o = mouth
    lip.poly([(-.42, .74), (-.16, .65), (0, .69), (.16, .65), (.42, .74), (0, .80)])
    lip.ell(-.32, .78 + o * .16, .32, .98 + o * .2)
    if o > 0.02:
        mo.ell(-.3 * (0.6 + .4 * o), .76, .3 * (0.6 + .4 * o), .78 + o * .2)
    sf = max(1.0, s * .012)
    return fc.arr(), hr.arr(), ft.arr(sf), lip.arr(sf), mo.arr(sf)


def tripundra_mask(cx, cy, s, p=1.0, from_right=True):
    m = Mask(cx, cy, s)
    for i in range(3):
        y = -.98 + i * .15
        pts = m.arc_pts(0, y + .9, .72, .9, -math.pi * .82, -math.pi * .18, 30)
        n = max(2, int(len(pts) * p))
        pts = pts[::-1][:n] if from_right else pts[:n]
        if p > 0.01:
            m.line(pts, .075)
    return m.arr(1.1)


def render_face(img, cx, cy, s, light, lcol, amb=(0.03, 0.03, 0.05), mouth=0.0,
                skin=SKIN, shiva=False, ash=0.0, ash_emit=0.0, ash_from_right=True,
                throat=0.0, alpha=1.0):
    fc, hr, ft, lip, mo = face_masks(cx, cy, s, mouth, shiva)
    union = np.clip(fc + hr, 0, 1)
    alb = np.zeros((H, W, 3), F32) + skin
    alb = alb * (1 - 0.7 * ft[..., None])
    alb = comp(alb, skin * C(0.75, 0.45, 0.42), lip * 0.8)
    alb = comp(alb, C(0.01, 0.0, 0.0), mo)
    locks = 0.6 + 0.8 * noise(51, base=3, sx=10, sy=.3)[..., None]
    alb = comp(alb, HAIR * locks * (1.3 if shiva else 1), hr)
    # height field: oval + nose ridge + brows + cheekbones
    bump = Mask(cx, cy, s)
    bump.line([(0, -.4), (.05, .38)], .24)
    bump.ell(-.78, -.12, -.22, .22, 150)
    bump.ell(.22, -.12, .78, .22, 150)
    bump.line([(-.75, -.5), (.75, -.5)], .2, v=150)
    bump.ell(-.45, .62, .45, 1.05, 90)
    bump.ell(-.35, 1.05, .35, 1.35, 120)
    eyes = Mask(cx, cy, s)
    for sg in (-1, 1):
        eyes.ell(sg * .44 - .3, -.4, sg * .44 + .3, -.05)
    height = (blur(union, s * .3) + blur(bump.arr(0), s * .12) * .18
              - blur(eyes.arr(0), s * .12) * .12 + blur(lip, s * .03) * .03)
    lit = shade(height, alb, light, lcol, amb, k=s * .55, lz=s * 1.1, falloff=s * 14)

    if throat > 0:
        nk = Mask(cx, cy, s)
        nk.ell(-.5, 1.15, .5, 2.4)
        n = nk.arr(s * .08)
        lit = comp(lit, lit * 0.4 + C(0.05, 0.25, 1.1) * throat, n * min(1, throat * 1.3))
    if ash > 0:
        tm = tripundra_mask(cx, cy, s, ash, ash_from_right)
        lit = comp(lit, ASH * (0.6 + 0.4 * (lit.mean(-1, keepdims=True) * 4).clip(0, 1)), tm)
        if ash_emit > 0:
            lit = lit + C(1.6, 1.4, 1.1) * (tm * ash_emit)[..., None]
            lit = lit + C(1.0, 0.7, 0.4) * (blur(tm, s * .12) * ash_emit * 1.5)[..., None]
    return comp(img, lit, union * alpha), union


# ---------------------------------------------------------------- villagers
def villager(sk, mk, x, y, s, point_to, bob=0.0, hunch=0.0):
    sk.cx, sk.cy, sk.s = x, y + bob, s
    mk.cx, mk.cy, mk.s = x, y + bob, s
    sk.poly([(-.45, 0), (.45, 0), (.38, -1.1), (-.38, -1.1)])
    sk.ell(-.42, -1.35, .42, -.95)
    hx = hunch
    sk.ell(-.24 + hx, -1.82, .24 + hx, -1.3)
    # pointing arm
    ang = math.atan2(point_to[1] - (y - 1.2 * s), point_to[0] - x)
    ex = .35 * (1 if math.cos(ang) > 0 else -1)
    sk.line([(ex, -1.2), (ex + .9 * math.cos(ang), -1.2 + .9 * math.sin(ang))], .13)
    # other arm on belly (laughing)
    sk.line([(-ex, -1.15), (-ex * .3, -.65)], .13)
    # grotesque mask face
    mk.ell(-.19 + hx, -1.84, .19 + hx, -1.38)
    mk.poly([(-.15 + hx, -1.5), (.15 + hx, -1.5), (hx, -1.26)])


def mask_features(ft, x, y, s, bob, hunch, grin):
    ft.cx, ft.cy, ft.s = x + hunch * s, y + bob, s
    for sg in (-1, 1):
        ft.poly([(sg * .03, -1.64), (sg * .15, -1.70), (sg * .13, -1.6)])
        ft.line([(sg * .02, -1.7), (sg * .17, -1.79)], .03)
    ft.ell(-.09, -1.52, .09, -1.46 + .1 * grin)
    ft.line([(0, -1.66), (.02, -1.54)], .015)


# --------------------------------------------------------------- standing man
def standing_masks(cx, cy, s, arm_up=0.0):
    sk, cl, hr = Mask(cx, cy, s), Mask(cx, cy, s), Mask(cx, cy, s)
    sk.ell(-.17, -3.42, .17, -2.98)
    sk.poly([(-.08, -3.02), (.08, -3.02), (.09, -2.82), (-.09, -2.82)])
    sk.poly([(-.42, -2.8), (.42, -2.8), (.3, -1.8), (-.3, -1.8)])
    for sg in (-1, 1):
        sk.line([(sg * .4, -2.75), (sg * .5, -2.05), (sg * .52, -1.45)], .11)
    sk.line([(-.15, -.4), (-.17, 0)], .12)
    sk.line([(.15, -.4), (.17, 0)], .12)
    cl.poly([(-.36, -1.9), (.36, -1.9), (.42, -.35), (-.42, -.35)])
    cl.poly([(-.45, -2.78), (-.22, -2.85), (.36, -1.88), (.1, -1.8)])
    hr.ell(-.18, -3.5, .18, -3.18)
    hr.ell(-.12, -3.7, .12, -3.42)
    return sk.arr(), cl.arr(), hr.arr()


# --------------------------------------------------------------- lying figure
def lying_mask(cx, cy, s):
    m = Mask(cx, cy, s)
    m.ell(-2.05, -.3, -1.55, .18)                      # head
    m.ell(-2.1, -.2, -1.85, .25)                       # matted hair spread
    m.poly([(-1.6, -.08), (-1.4, -.1), (-1.4, .1), (-1.6, .1)])          # neck
    m.poly([(-1.42, -.34), (-.9, -.38), (-.3, -.3), (.05, -.27), (.15, -.2),
            (.15, .2), (.05, .24), (-.3, .26), (-.9, .3), (-1.42, .28)])  # torso
    m.poly([(.1, -.24), (.9, -.2), (1.7, -.12), (1.7, .02), (.9, .0), (.1, .02)])  # upper leg
    m.poly([(.1, .02), (.9, .04), (1.7, .04), (1.7, .16), (.9, .18), (.1, .22)])
    m.ell(1.62, -.42, 1.82, .0)                        # feet upright
    m.ell(1.62, -.05, 1.82, .3)
    m.line([(-1.3, -.36), (-.6, -.46), (.05, -.42)], .1)   # arms at sides
    m.line([(-1.3, .34), (-.6, .44), (.05, .4)], .1)
    m.ell(.0, -.56, .26, -.36)                         # upturned palms
    m.ell(.0, .38, .26, .58)
    return m.arr(1.5)


# ------------------------------------------------------- Nataraja shadow
def nataraja_mask(cx, cy, s, ph, kick):
    """Silhouette of a cosmic dancer; ph = dance phase (radians)."""
    m = Mask(cx, cy, s)
    sw = math.sin(ph)
    tilt = 0.08 * sw
    def R(x, y):
        c, sn = math.cos(tilt), math.sin(tilt)
        return (x * c - (y + 1.4) * sn, x * sn + (y + 1.4) * c - 1.4)
    hx, hy = R(0, -2.35)
    m.circ(hx, hy, .2)
    m.poly([R(-.34, -2.05), R(.34, -2.05), R(.2, -1.25), R(-.2, -1.25)])
    m.poly([R(-.28, -1.3), R(.28, -1.3), R(.36, -1.0), R(-.36, -1.0)])
    # flying locks
    for sg in (-1, 1):
        for i in range(7):
            a0 = -0.6 + i * 0.2
            pts = []
            for j in range(9):
                r = .25 + j * .16
                wv = 0.12 * math.sin(ph * 2 + j * .7 + i)
                pts.append((hx + sg * r, hy + a0 * r * .55 + wv))
            m.line(pts, .04 - .002 * i, joints=False)
    # four arms
    shL, shR = R(-.32, -1.95), R(.32, -1.95)
    a = 0.25 * sw
    arms = [
        (shR, [(.75, -2.25 - a), (.95, -2.85 - a)]),        # upper right: damru
        (shL, [(-.75, -2.25 + a), (-.95, -2.85 + a)]),      # upper left: flame
        (shR, [(.7, -1.75 + a * .5), (.75, -2.15 + a * .5)]),  # abhaya
        (shL, [(-.55, -1.6), (.35, -1.45 - .2 * kick)]),    # gaja hasta
    ]
    for sh, pts in arms:
        m.line([sh] + [R(*p) for p in pts], .09)
    dx, dy = R(.95, -2.95 - a)
    m.poly([(dx - .12, dy - .12), (dx + .12, dy - .12), (dx - .12, dy + .12), (dx + .12, dy + .12)])
    fx, fy = R(-.95, -3.0 + a)
    m.poly([(fx - .08, fy + .05), (fx + .08, fy + .05), (fx, fy - .3)])
    for sg, yy in ((1, -2.3), ):
        m.ell(.65, -2.35 + a * .5, .85, -2.05 + a * .5)
    # legs: right planted & bent, left raised across
    m.line([R(.15, -1.05), R(.45, -.55), R(.3, 0)], .12)
    m.line([R(.3, 0), R(.55, 0.02)], .07)
    k = .25 * kick
    m.line([R(-.15, -1.05), R(-.75, -.8 - k), R(-1.15, -.95 - k * 1.6)], .12)
    # ring of fire
    cxr, cyr = R(0, -1.6)
    ring = m.arc_pts(cxr, cyr, 1.55, 1.55, -math.pi * 1.0, math.pi * 1.0, 80)
    m.line(ring, .05, joints=False)
    for i, (x, y) in enumerate(ring[::3]):
        aa = math.atan2(y - cyr, x - cxr)
        L = .14 + .05 * math.sin(ph * 3 + i)
        m.poly([(x + .05 * math.sin(aa), y - .05 * math.cos(aa)),
                (x - .05 * math.sin(aa), y + .05 * math.cos(aa)),
                (x + L * math.cos(aa), y + L * math.sin(aa))])
    return m


# ---------------------------------------------------------------- bilva leaf
def bilva(m, x, y, s, rot=0.0, v=255):
    """Trifoliate leaf drawn into Mask m at (x,y) local coords; returns vein pts."""
    veins = []
    for k, (ang, ln) in enumerate(((-math.pi / 2, 1.0), (-math.pi / 2 - 1.1, .78),
                                   (-math.pi / 2 + 1.1, .78))):
        a = ang + rot
        pts = []
        for th in np.linspace(0, 2 * math.pi, 28):
            u = (1 - math.cos(th)) / 2 * ln * s
            wd = math.sin(th) * .28 * s * math.sin(math.pi * (1 - math.cos(th)) / 2) ** .7
            pts.append((x + u * math.cos(a) - wd * math.sin(a), y + u * math.sin(a) + wd * math.cos(a)))
        m.poly(pts, v)
        mid = [(x, y), (x + ln * s * math.cos(a), y + ln * s * math.sin(a))]
        veins.append(mid)
        for j in range(1, 5):
            u = j / 5 * ln * s
            bx, by = x + u * math.cos(a), y + u * math.sin(a)
            for sg in (-1, 1):
                aa = a + sg * 0.7
                veins.append([(bx, by), (bx + .17 * s * math.cos(aa), by + .17 * s * math.sin(aa))])
    return veins


def lingam_masks(cx, cy, s):
    """Side view lingam on yoni pedestal. cy = ground."""
    ln, yo = Mask(cx, cy, s), Mask(cx, cy, s)
    yo.ell(-1.25, -.85, 1.25, -.45)
    yo.poly([(-1.25, -.65), (1.25, -.65), (1.1, -.2), (-1.1, -.2)])
    yo.poly([(1.1, -.75), (1.9, -.62), (1.9, -.48), (1.1, -.45)])
    yo.ell(-1.1, -.35, 1.1, 0)
    ln.poly([(-.5, -.7), (.5, -.7), (.5, -1.8), (-.5, -1.8)])
    ln.ell(-.5, -2.3, .5, -1.3)
    return ln.arr(1), yo.arr(1)


# ------------------------------------------------------------ profile face
def render_profile(img, cx, cy, s, mouth, light, lcol, amb=(0.004, 0.003, 0.006)):
    """Left-facing profile; mouth 0..1 opens the lips."""
    o = mouth * .09
    face = Mask(cx, cy, s)
    pts = [(0.3, -1.75), (-0.35, -1.45), (-0.55, -0.95), (-0.6, -0.68), (-0.53, -0.5),
           (-0.62, -0.25), (-0.86, 0.06), (-0.88, 0.12), (-0.7, 0.2), (-0.68, 0.3),
           (-0.75, 0.37), (-0.73, 0.43), (-0.64, 0.46), (-0.64, 0.47 + o), (-0.72, 0.52 + o),
           (-0.70, 0.58 + o), (-0.6, 0.66 + o), (-0.66, 0.85 + o * .6), (-0.6, 1.0 + o * .6),
           (-0.4, 1.08 + o * .4), (-0.25, 1.2), (-0.32, 1.6), (-0.4, 2.6), (1.6, 2.6),
           (1.6, -1.75)]
    face.poly(pts)
    fm = face.arr(1.2)
    hair = Mask(cx, cy, s)
    hair.poly([(-0.45, -1.35), (-0.1, -1.85), (0.6, -2.3), (1.1, -2.0), (1.6, -1.6),
               (1.7, 2.6), (0.75, 2.6), (0.55, 1.2), (0.45, .1), (0.1, -0.9), (-0.38, -1.15)])
    hair.ell(0.1, -2.75, 1.0, -1.85)
    hm = hair.arr(1.5)
    feat = Mask(cx, cy, s)
    feat.line([(-0.42, -0.5), (-0.3, -0.47), (-0.2, -0.5)], .025)     # closed eye
    feat.line([(-0.5, -0.68), (-0.2, -0.72)], .04)                    # brow
    feat.ell(-0.72, 0.13, -0.6, 0.19)                                 # nostril
    feat.line([(-0.18, -.05), (-0.25, 0.45)], .02, v=90)              # cheek hollow
    ft = feat.arr(max(1, s * .01))
    lipm = Mask(cx, cy, s)
    lipm.poly([(-0.77, 0.36), (-0.6, 0.35), (-0.6, 0.6 + o), (-0.73, 0.6 + o)])
    lp = lipm.arr(max(1, s * .01)) * fm
    alb = np.zeros((H, W, 3), F32) + SKIN
    alb = alb * (1 - .65 * ft[..., None])
    alb = comp(alb, SKIN * C(.85, .5, .45), lp * .8)
    locks = 0.5 + 0.9 * noise(51, base=3, sx=.3, sy=10)[..., None]
    alb = comp(alb, HAIR * locks * 1.5, hm)
    union = np.clip(fm + hm, 0, 1)
    height = blur(union, s * .12) + blur(fm, s * .04) * .3 - blur(ft, s * .03) * .1
    lit = shade(height, alb, light, lcol, amb, k=s * .9, lz=s * .25, falloff=s * 5, spec=.15)
    return comp(img, lit, union)
