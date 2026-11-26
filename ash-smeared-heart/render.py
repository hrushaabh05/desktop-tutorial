"""Render THE ASH-SMEARED HEART.

  python render.py stills 13 30 45 ...   -> stills/*.png (quick checks)
  python render.py video [start end]     -> build/video.mp4 (silent picture)
"""
import os
import subprocess
import sys
import time
from multiprocessing import Pool

import numpy as np
from PIL import Image

import timeline as TL
from engine import FPS, H, W, finish

HERE = os.path.dirname(os.path.abspath(__file__))


def render_frame(i):
    import scenes
    T = i / FPS
    img = scenes.frame(T)
    return finish(img, T).tobytes()


def stills(times):
    import scenes
    os.makedirs(os.path.join(HERE, "stills"), exist_ok=True)
    for T in times:
        t0 = time.time()
        img = finish(scenes.frame(T), T)
        p = os.path.join(HERE, "stills", f"t{T:07.2f}.png")
        Image.fromarray(img).save(p)
        print(f"{p}  {time.time() - t0:.2f}s", flush=True)


def video(start=0.0, end=TL.DURATION, out=None):
    out = out or os.path.join(HERE, "build", "video.mp4")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    frames = range(int(round(start * FPS)), int(round(end * FPS)))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
           "-crf", "19", "-pix_fmt", "yuv420p", "-tune", "film", out]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    t0 = time.time()
    with Pool(os.cpu_count()) as pool:
        for n, buf in enumerate(pool.imap(render_frame, frames, chunksize=4)):
            ff.stdin.write(buf)
            if n % 48 == 0:
                el = time.time() - t0
                eta = el / (n + 1) * (len(frames) - n - 1)
                print(f"frame {n}/{len(frames)}  {el:.0f}s elapsed, eta {eta:.0f}s", flush=True)
    ff.stdin.close()
    ff.wait()
    print("wrote", out, f"in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "stills":
        stills([float(x) for x in sys.argv[2:]])
    elif mode == "video":
        a = [float(x) for x in sys.argv[2:4]]
        video(*a)
