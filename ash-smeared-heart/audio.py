"""Synthesised score and sound design for THE ASH-SMEARED HEART.

Writes build/audio.wav (44.1 kHz stereo). Everything is generated with numpy:
tanpura drone, sitar plucks, temple bells, damru, heartbeat, water, a sung Om,
crowd laughter, thunder and a conch.
"""
import math
import os
import wave

import numpy as np

import timeline as TL

SR = 44100
DUR = TL.DURATION
N = int(SR * DUR)
RNG = np.random.default_rng(2024)
HERE = os.path.dirname(os.path.abspath(__file__))

SA = 138.59  # C#3


def t_axis(n):
    return np.arange(n) / SR


def S(t):
    return int(t * SR)


# ------------------------------------------------------------------ helpers
def band_noise(n, lo, hi, tilt=0.0, seed=None):
    rng = np.random.default_rng(seed) if seed is not None else RNG
    spec = np.fft.rfft(rng.normal(0, 1, n))
    f = np.fft.rfftfreq(n, 1 / SR)
    m = ((f >= lo) & (f <= hi)).astype(float)
    # soft edges
    m = np.convolve(m, np.hanning(64) / np.hanning(64).sum(), mode="same")
    if tilt:
        m *= (np.maximum(f, 20) / 1000.0) ** tilt
    x = np.fft.irfft(spec * m, n)
    return x / (np.abs(x).max() + 1e-9)


def smooth_env(n, points):
    """Piecewise-linear envelope from (time, value) list."""
    ts = np.array([p[0] for p in points]) * SR
    vs = np.array([p[1] for p in points])
    return np.interp(np.arange(n), ts, vs)


class Mix:
    def __init__(self):
        self.L = np.zeros(N)
        self.R = np.zeros(N)

    def add(self, x, t0, gain=1.0, pan=0.0):
        i0 = S(t0)
        if i0 >= N:
            return
        x = x[:N - i0] * gain
        a = (pan + 1) * math.pi / 4
        self.L[i0:i0 + len(x)] += x * math.cos(a)
        self.R[i0:i0 + len(x)] += x * math.sin(a)

    def add_st(self, l, r, t0, gain=1.0):
        i0 = S(t0)
        l = l[:N - i0] * gain
        r = r[:N - i0] * gain
        self.L[i0:i0 + len(l)] += l
        self.R[i0:i0 + len(r)] += r


def reverb(l, r, t60=3.0, wet=0.35, seed=7):
    n_ir = int(SR * t60)
    rng = np.random.default_rng(seed)
    tt = t_axis(n_ir)
    dec = np.exp(-6.9 * tt / t60)
    irs = []
    for k in range(2):
        ir = rng.normal(0, 1, n_ir) * dec
        ir = np.convolve(ir, np.ones(6) / 6, mode="same")  # darken
        ir[:int(SR * .012)] = 0
        irs.append(ir / np.sqrt((ir ** 2).sum()))
    out = []
    for x, ir in zip((l, r), irs):
        blk = 1 << 19
        nfft = 1 << 20
        while nfft < blk + n_ir:
            nfft <<= 1
        IR = np.fft.rfft(ir, nfft)
        y = np.zeros(len(x) + n_ir)
        for s0 in range(0, len(x), blk):
            seg = x[s0:s0 + blk]
            conv = np.fft.irfft(np.fft.rfft(seg, nfft) * IR, nfft)[:len(seg) + n_ir]
            y[s0:s0 + len(conv)] += conv
        out.append(y[:len(x)])
    return l * (1 - wet) + out[0] * wet * 2.2, r * (1 - wet) + out[1] * wet * 2.2


# ------------------------------------------------------------- instruments
def tanpura_note(f, dur=6.0, bright=1.0):
    n = int(dur * SR)
    t = t_axis(n)
    out = np.zeros(n)
    swell = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.5
    for k in range(1, 36):
        fk = f * k * (1 + 0.0004 * k)
        if fk > 9000:
            break
        amp = 1 / k ** .85
        jaw = (0.25 + 1.6 * swell * min(1, k / 8)) if k > 2 else 1.0
        dec = np.exp(-t * (0.35 + 0.05 * k))
        ph = RNG.uniform(0, 2 * np.pi)
        out += amp * jaw * dec * np.sin(2 * np.pi * fk * t + ph) * (1 if k < 4 else bright)
    att = np.clip(t / .01, 0, 1)
    return out * att / np.abs(out).max()


def pluck(f, dur=2.5, glide=None, bright=1.0):
    """Sitar-like pluck; glide = (t_start, ratio) meend."""
    n = int(dur * SR)
    t = t_axis(n)
    ff = np.full(n, f)
    if glide:
        gs, ratio = glide
        ff = f * np.where(t < gs, 1, 1 + (ratio - 1) * np.clip((t - gs) / .25, 0, 1))
    ff = ff * (1 + 0.003 * np.sin(2 * np.pi * 5.5 * t) * np.clip(t - .3, 0, 1))
    phase = 2 * np.pi * np.cumsum(ff) / SR
    out = np.zeros(n)
    for k in range(1, 28):
        amp = (1 / k ** .7) * (0.6 + 0.4 * math.sin(k * 1.7) ** 2)
        out += amp * np.exp(-t * (1.2 + .22 * k / bright)) * np.sin(k * phase)
    out *= np.clip(t / .004, 0, 1)
    return out / np.abs(out).max()


def bell(f=560.0, dur=7.0):
    n = int(dur * SR)
    t = t_axis(n)
    ratios = [0.5, 1.0, 1.19, 1.56, 2.0, 2.51, 2.66, 3.01, 4.1, 5.4]
    amps = [.6, 1.0, .5, .55, .35, .4, .25, .2, .15, .1]
    decs = [.25, .45, .7, .9, 1.1, 1.5, 1.7, 2.0, 2.8, 3.5]
    out = np.zeros(n)
    for r, a, d in zip(ratios, amps, decs):
        beat = 1 + .15 * np.sin(2 * np.pi * (0.8 + r * .3) * t)
        out += a * beat * np.exp(-t * d) * np.sin(2 * np.pi * f * r * t + RNG.uniform(0, 6))
    strike = band_noise(int(.05 * SR), 2000, 9000) * np.exp(-t_axis(int(.05 * SR)) * 120)
    out[:len(strike)] += strike * .4
    return out / np.abs(out).max()


def drum(f0=200.0, f1=110.0, dec=12.0, noise=.35, dur=.6):
    n = int(dur * SR)
    t = t_axis(n)
    f = f1 + (f0 - f1) * np.exp(-t * 30)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t * dec) + .4 * np.sin(2.3 * ph) * np.exp(-t * dec * 1.6)
    nz = band_noise(n, 300, 5000, seed=int(f0)) * np.exp(-t * 40) * noise
    return body + nz


def damru(strength=1.0):
    a = drum(240, 170, 14, .5)
    b = drum(250, 175, 16, .45)
    out = np.zeros(int(.7 * SR))
    out[:len(a)] += a
    off = int(.055 * SR)
    out[off:off + len(b)] += b[:len(out) - off] * .8
    return out * strength


def heartbeat():
    lub = drum(70, 45, 9, .05, .5)
    dub = drum(80, 52, 11, .05, .5)
    out = np.zeros(int(.8 * SR))
    out[:len(lub)] += lub
    o = int(.22 * SR)
    out[o:o + len(dub)] += dub[:len(out) - o] * .7
    return out


def voice(dur, f0_fn, formant_fn, breath=0.03, nh=48, block=1024):
    """Additive vocal synth. f0_fn(t)->Hz (array), formant_fn(t)->[(F,B,g),...]"""
    n = int(dur * SR)
    t = t_axis(n)
    f0 = f0_fn(t)
    phase = 2 * np.pi * np.cumsum(f0) / SR
    out = np.zeros(n)
    nb = n // block + 1
    tb = np.arange(nb) * block / SR
    for k in range(1, nh + 1):
        amps = np.zeros(nb)
        for i, tt in enumerate(tb):
            fk = k * f0_fn(np.array([tt]))[0]
            g = 0.0
            for F, B, gg in formant_fn(tt):
                g += gg / (1 + ((fk - F) / B) ** 2)
            amps[i] = g / k ** .9
        a = np.interp(t, tb, amps)
        out += a * np.sin(k * phase)
    out += band_noise(n, 300, 6000) * breath
    return out / (np.abs(out).max() + 1e-9)


def om(dur=6.5):
    def f0(t):
        return 98 * (1 + .006 * np.sin(2 * np.pi * 4.8 * t) * np.clip(t - .6, 0, 1))

    def form(tt):
        if tt < .7:
            return [(700, 120, 1.0), (1150, 140, .6), (2600, 200, .2)]
        if tt < 3.0:
            u = min(1, (tt - .7) / .6)
            return [(700 - 300 * u, 110, 1.0), (1150 - 350 * u, 130, .5 - .2 * u), (2500, 220, .12)]
        u = min(1, (tt - 3.0) / .5)
        return [(400 - 160 * u, 80, 1.0), (800, 140, .3 * (1 - u)), (2500, 300, .1 * (1 - u))]

    x = voice(dur, f0, form, breath=.01)
    t = t_axis(len(x))
    env = np.clip(t / .5, 0, 1) * np.clip((dur - t) / 1.6, 0, 1)
    return x * env


def laugh(f0, n_ha=5, rate=6.5, seed=0):
    rng = np.random.default_rng(seed)
    dur = n_ha / rate + .4
    def ff(t):
        return f0 * (1 + .12 * np.sin(2 * np.pi * rate * t)) * (1 - .15 * t / dur)

    def form(tt):
        return [(780, 130, 1.0), (1250, 150, .55), (2600, 250, .2)]
    x = voice(dur, ff, form, breath=.25, nh=30, block=512)
    t = t_axis(len(x))
    env = np.zeros(len(x))
    for i in range(n_ha):
        tt = i / rate + rng.uniform(0, .02)
        env += np.exp(-((t - tt - .05) / .045) ** 2)
    return x * np.clip(env, 0, 1)


def conch(dur=4.0, f=233.0):
    n = int(dur * SR)
    t = t_axis(n)
    ff = f * (0.94 + 0.06 * np.clip(t / .5, 0, 1)) * (1 + .004 * np.sin(2 * np.pi * 5 * t))
    ph = 2 * np.pi * np.cumsum(ff) / SR
    out = np.zeros(n)
    for k in range(1, 20):
        out += (1 / k ** 1.1) * np.sin(k * ph) * (1 if k % 2 else .55)
    env = np.clip(t / .35, 0, 1) * np.clip((dur - t) / 1.2, 0, 1)
    out = out * env + band_noise(n, 800, 4000) * .03 * env
    return out / np.abs(out).max()


# ======================================================================= SCORE
def build():
    mx = Mix()
    sc = {name: (a, b) for name, a, b in TL.SCENES}

    # --- tanpura drone bed (cycle Pa Sa Sa Sa-low) with level automation
    notes = [tanpura_note(SA * .75, 6.5), tanpura_note(SA, 6.5), tanpura_note(SA, 6.5),
             tanpura_note(SA / 2, 6.5)]
    drone_lvl = smooth_env(N, [
        (0, 0), (3, .28), (11, .3), (12.5, .12), (16, .22), (29.5, .2), (30, .08), (40, .1),
        (40.5, .22), (60, .3), (62, .1), (63, .2), (90, .2), (91, .12), (117, .08),
        (118, .16), (140, .22), (144, .1), (146.5, .14), (169, .14), (170, 0), (190, 0),
        (191.5, .18), (205, .3), (214, .3), (216, .18), (223, .0), (224, 0)])
    pans = [-.35, .15, .3, -.1]
    t = 0.0
    k = 0
    while t < DUR:
        mx.add(notes[k % 4], t, gain=1.0, pan=pans[k % 4])
        t += 1.25 + .02 * math.sin(k)
        k += 1
    mx.L *= drone_lvl
    mx.R *= drone_lvl

    # --- deep sustained Sa pad (sine + fifth), for the cosmic & final sections
    pad_t = t_axis(N)
    pad = (np.sin(2 * np.pi * SA / 2 * pad_t) + .5 * np.sin(2 * np.pi * SA * .75 * pad_t + 1)
           + .3 * np.sin(2 * np.pi * SA * pad_t * 1.002))
    pad_lvl = smooth_env(N, [(0, 0), (40, 0), (42, .08), (58, .12), (61.5, .2), (62, 0),
                             (146, 0), (150, .05), (169, .05), (170, 0), (203, 0),
                             (207, .1), (214, .14), (216, 0)])
    mx.L += pad * pad_lvl
    mx.R += pad * pad_lvl

    # --- title: bell + ember crackles
    mx.add(bell(520), 2.2, .5, -.2)
    mx.add(bell(780), 7.5, .25, .3)

    # --- ACT I: water lapping, lamp, heartbeat -> damru
    a, b = sc["ghats"]
    wl = band_noise(S(b - a + 2), 150, 1400, tilt=-.6, seed=11)
    tt = t_axis(len(wl))
    lap = (0.55 + 0.45 * np.sin(2 * np.pi * .23 * tt) * np.sin(2 * np.pi * .61 * tt + 1)) ** 2
    wl *= lap * np.clip(tt / 1.5, 0, 1) * np.clip((b - a + 1 - tt) / 2, 0, 1)
    mx.add(wl, a, .22, -.3)
    mx.add(wl[::-1].copy(), a, .16, .4)
    mx.add(bell(640, 6), a + 4.5, .18, .5)
    hb = TL.heartbeats()
    for i, tb in enumerate(hb):
        u = i / max(1, len(hb) - 1)
        if u < .6:
            mx.add(heartbeat(), tb, .9, 0)
        else:
            mx.add(heartbeat(), tb, .9 * (1 - (u - .6) / .4), 0)
            mx.add(damru(), tb, .55 * (u - .6) / .4 + .15, .1)
    mx.add(drum(90, 40, 4, .3, 1.2), b - .02, 1.0, 0)  # smash cut thump

    # --- ACT I cosmos: shimmering riser to the third eye
    a, b = sc["cosmos"]
    rs = band_noise(S(b - a), 2000, 9000, seed=12)
    tt = t_axis(len(rs))
    riser = np.clip((tt - 12) / 9, 0, 1) ** 2.5 * (tt < 21.7)
    mx.add(rs * riser, a, .25, 0)
    for i in range(7):
        f = SA * [4, 6, 4.5, 8, 6.75, 9, 12][i]
        x = pluck(f, 4, bright=3)
        mx.add(x, a + 2 + i * 2.1, .08, -.6 + i * .2)
    mx.add(drum(60, 30, 2.2, .6, 3.0), b - .4, 1.0, 0)
    mx.add(bell(1040, 6), b - .4, .35, 0)

    # --- ACT II: bells for each panel, sitar phrase, the pour
    a, b = sc["offering"]
    for i, ta in enumerate((0.6, 4.4, 8.2)):
        mx.add(bell([620, 700, 830][i], 6), a + ta, .28, [-.5, .5, .1][i])
    phrase = [(1.0, 1.0), (1.067, 1.0), (1.26, 1.0), (1.5, 1.0), (1.6, 1.0), (1.5, 1.067),
              (1.26, 1.0), (1.0, 1.0)]
    for i, (r, g) in enumerate(phrase):
        gl = (.4, g) if g != 1.0 else None
        mx.add(pluck(SA * 2 * r, 2.8, glide=gl), a + 1.5 + i * 1.45, .22, .25)
    pour = band_noise(S(14.5), 250, 5000, tilt=-.3, seed=13)
    tt = t_axis(len(pour))
    pour *= (0.75 + .25 * np.sin(2 * np.pi * 3.1 * tt)) * np.clip((tt - .3) / 1.5, 0, 1) * np.clip((14.2 - tt) / 2, 0, 1)
    mx.add(pour, a + 14.0, .12, 0)
    rng = np.random.default_rng(3)
    for _ in range(26):
        tt0 = a + 14.6 + rng.uniform(0, 12)
        f = rng.uniform(1400, 3400)
        n = int(.35 * SR)
        x = np.sin(2 * np.pi * f * (1 + 1.5 * t_axis(n)) * t_axis(n)) * np.exp(-t_axis(n) * 18)
        mx.add(x, tt0, .05, rng.uniform(-.7, .7))

    # --- ACT III: murmur, mocking laughter, spin whoosh, ash ignites
    a, b = sc["village"]
    mur = band_noise(S(b - a), 200, 1800, seed=14)
    tt = t_axis(len(mur))
    syl = (0.5 + 0.5 * np.sin(2 * np.pi * 4.3 * tt + 2 * np.sin(2 * np.pi * .7 * tt))) ** 2
    murl = smooth_env(len(mur), [(0, 0), (1, .5), (8.5, .5), (9, .15), (11, .2), (20, .25), (24, .05), (28, 0)])
    mx.add(mur * syl * murl, a, .3, 0)
    for i in range(16):
        tl = a + .4 + i * .5 + rng.uniform(0, .3)
        if tl > a + 8.2:
            break
        mx.add(laugh(rng.uniform(150, 260), int(rng.integers(3, 6)), rng.uniform(5.5, 7.5), i),
               tl, .16, rng.uniform(-.8, .8))
    for i in range(10):
        tl = a + 9 + i * 1.3
        mx.add(laugh(rng.uniform(140, 240), 4, 6.5, 50 + i), tl, .06, rng.uniform(-.9, .9))
    wh = band_noise(S(14), 300, 6000, seed=15)
    tt = t_axis(len(wh))
    vel = np.array([TL_spin_vel(x) for x in np.linspace(9, 23, 200)])
    vel = np.interp(tt, np.linspace(0, 14, 200), vel) / 2600
    sweep = np.sin(2 * np.pi * np.cumsum(.8 + 2.2 * vel) / SR)
    mx.add_st(wh * vel * (0.6 + .4 * sweep), wh[::-1] * vel * (0.6 - .4 * sweep), a + 9, .35)
    fire = band_noise(S(4.5), 500, 7000, seed=16)
    tt = t_axis(len(fire))
    crack = (RNG.random(len(fire)) < .002).astype(float)
    crack = np.convolve(crack, np.exp(-np.arange(200) / 25), mode="same")
    fe = np.clip(tt / .4, 0, 1) * np.clip((4.5 - tt) / 1.5, 0, 1)
    mx.add((fire * .4 + crack * .8) * fe, a + 19.8, .25, 0)
    mx.add(drum(120, 60, 3, .4, 2.0), a + 19.8, .5, 0)
    mx.add(bell(470, 7), a + 11.0, .22, 0)

    # --- ACT IV: the Tandava -- damru accelerating, thunder
    a, b = sc["tandava"]
    beats = TL.tandava_beats()
    for i, tb in enumerate(beats):
        u = (tb - a) / (b - a)
        mx.add(damru(.5 + .6 * u), tb, .55, .15 * math.sin(i))
        if i % 2 == 0:
            mx.add(drum(110, 55, 6, .2, .8), tb, .35 + .4 * u, 0)
    for i in range(int((b - a - 6) / 2.5)):
        mx.add(bell(900 + 60 * (i % 4), 4), a + 5 + i * 2.5, .05 + .004 * i, .5 - (i % 2))
    th = TL.thunder_time()
    rum = band_noise(S(8), 20, 300, tilt=-1.2, seed=17)
    tt = t_axis(len(rum))
    rum *= np.exp(-tt * .55) * (0.6 + .4 * band_noise(len(rum), 1, 8, seed=18))
    crackn = band_noise(S(.6), 300, 8000, seed=19) * np.exp(-t_axis(S(.6)) * 8)
    mx.add(rum, th, 1.3, 0)
    mx.add(crackn, th, .5, .2)

    # --- ACT V: water, glassy tones, poison throb
    a, b = sc["throat"]
    wl2 = band_noise(S(b - a), 120, 1100, tilt=-.6, seed=20)
    tt = t_axis(len(wl2))
    wl2 *= (0.5 + .5 * np.sin(2 * np.pi * .17 * tt) ** 2) * np.clip(tt / 2, 0, 1) * np.clip((b - a - tt) / 2, 0, 1)
    mx.add(wl2, a, .16, -.2)
    for i, (dt, f) in enumerate(((5.0, SA * 4), (6.0, SA * 6), (7.0, SA * 5.04), (8.0, SA * 8),
                                (9.2, SA * 9), (11.0, SA * 6))):
        mx.add(pluck(f, 5, bright=4), a + dt, .09, -.5 + i * .2)
    mx.add(bell(415, 8), a + 8.2, .25, 0)
    thr = np.sin(2 * np.pi * 46 * t_axis(S(8.5))) * (0.5 + .5 * np.sin(2 * np.pi * .52 * t_axis(S(8.5))))
    thr *= np.clip(t_axis(len(thr)) / 2, 0, 1) * np.clip((8.5 - t_axis(len(thr))) / 2, 0, 1)
    mx.add(thr, a + 15.5, .35, 0)

    # --- ACT VI: silence, then a single distant Om
    a, b = sc["snow"]
    mx.add(om(6.5), a + 12.8, .55, 0)

    # --- ACT VII: door bells, return of the drone, conch & Har Har Mahadev
    a, b = sc["return"]
    mx.add(bell(560, 8), a + 2.0, .3, -.2)
    mx.add(bell(840, 7), a + 2.4, .18, .3)
    mx.add(drum(70, 35, 2, .3, 3), a + 6.5, .4, 0)
    phrase2 = [1.0, 1.26, 1.5, 1.6, 2.0, 1.6, 1.5, 1.26, 1.5, 1.0]
    for i, r in enumerate(phrase2):
        mx.add(pluck(SA * 2 * r, 3.2), a + 12 + i * 1.0, .17, -.2 + .05 * i)
    mx.add(conch(4.5), a + 11.5 + 7.6, .32, 0)
    mx.add(bell(520, 9), a + 11.5 + 8.0, .4, -.3)
    mx.add(bell(780, 9), a + 11.5 + 8.4, .25, .3)
    for i in range(12):
        mx.add(damru(.4 + i * .05), a + 11.5 + 8.0 + i * .14, .25, 0)

    # --- credits
    a, b = sc["credits"]
    mx.add(bell(520, 8), a + .6, .3, 0)

    L, R = reverb(mx.L, mx.R, t60=3.2, wet=.32)
    peak = max(np.abs(L).max(), np.abs(R).max())
    L, R = L / peak * 1.2, R / peak * 1.2
    L, R = np.tanh(L) * .92, np.tanh(R) * .92
    fade_out = np.clip((DUR - t_axis(N)) / 1.0, 0, 1)
    return L * fade_out, R * fade_out


def TL_spin_vel(t):
    return 2600 * float(np.clip((t - 11) / 3, 0, 1) ** 2) * (1 - float(np.clip((t - 20.5) / 3.5, 0, 1)))


def write(path, L, R):
    data = np.stack([L, R], 1)
    data = (np.clip(data, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "build"), exist_ok=True)
    L, R = build()
    out = os.path.join(HERE, "build", "audio.wav")
    write(out, L, R)
    print("wrote", out)
