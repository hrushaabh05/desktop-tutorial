"""Shared timeline for picture and sound (seconds)."""
import math

SCENES = [
    ("title", 0.0, 12.0),
    ("ghats", 12.0, 40.0),      # Act I
    ("cosmos", 40.0, 62.0),     # Act I (cosmic void)
    ("offering", 62.0, 90.0),   # Act II
    ("village", 90.0, 118.0),   # Act III
    ("tandava", 118.0, 146.0),  # Act IV
    ("throat", 146.0, 170.0),   # Act V
    ("snow", 170.0, 190.0),     # Act VI
    ("return", 190.0, 216.0),   # Act VII
    ("credits", 216.0, 224.0),
]
DURATION = SCENES[-1][2]

CHAPTERS = {
    "ghats": ("I", "THE RUDRAKSHA WORLDS"),
    "offering": ("II", "THE OFFERING"),
    "village": ("III", "THE MADNESS OF THE VILLAGE"),
    "tandava": ("IV", "THE TANDAVA"),
    "throat": ("V", "THE BLUE THROAT"),
    "snow": ("VI", "THE FINAL SNOW"),
    "return": ("VII", "THE DROP RETURNS"),
}

# Act I close-up: heartbeat that becomes the damru
GHAT_CLOSEUP = 17.5            # local time of cut to the lips


def heartbeats():
    """Global times of heartbeat 'lub' in Act I close-up."""
    t0 = SCENES[1][1] + GHAT_CLOSEUP
    out, t, period = [], t0 + 0.3, 1.0
    while t < SCENES[1][2] - 0.2:
        out.append(t)
        period = max(0.42, period * 0.93)
        t += period
    return out


def tandava_beats():
    """Global times of damru strikes in Act IV, accelerating."""
    s, e = SCENES[5][1], SCENES[5][2]
    out, t = [], s + 3.0
    while t < e - 2.2:
        out.append(t)
        u = (t - s) / (e - s)
        bpm = 70 + 150 * u ** 1.6
        t += 60.0 / bpm
    return out


def thunder_time():
    return SCENES[5][2] - 2.0


def scene_at(t):
    for name, a, b in SCENES:
        if a <= t < b:
            return name, t - a, b - a
    return SCENES[-1][0], t - SCENES[-1][1], SCENES[-1][2] - SCENES[-1][1]


def beat_env(t, beats, decay=7.0):
    v = 0.0
    for b in beats:
        if b <= t:
            v = max(v, math.exp(-(t - b) * decay))
    return v
