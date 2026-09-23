"""Build a frame-locked Ken Burns chain for the scroll-world engine.

Monid/Higgsfield are not installed, so dives are zoom-ins of the scene stills
and connectors dissolve from one dive's actual last frame to the next dive's
actual first frame. Seam frames are copied, not regenerated.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
STILLS = ROOT / "assets" / "stills"
VID = ROOT / "assets" / "vid"
FRAMES = ROOT / "assets" / "frames"
FFMPEG = r"C:\Users\Arnav Singh\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe"

SCENES = ["desk", "terminal", "gateway", "memory", "launch"]
W, H = 960, 540
FPS = 16
DIVE_FRAMES = 80   # 5s @ 16fps
CONN_FRAMES = 56   # 3.5s @ 16fps


def crop_16x9(im: Image.Image) -> Image.Image:
    im = im.convert("RGB")
    src_w, src_h = im.size
    target = 16 / 9
    cur = src_w / src_h
    if cur > target:
        new_w = int(src_h * target)
        left = (src_w - new_w) // 2
        im = im.crop((left, 0, left + new_w, src_h))
    else:
        new_h = int(src_w / target)
        top = (src_h - new_h) // 2
        im = im.crop((0, top, src_w, top + new_h))
    return im.resize((W * 2, H * 2), Image.Resampling.LANCZOS)


def encode(pattern: Path, out: Path, frames: int) -> None:
    subprocess.run(
        [
            FFMPEG, "-y",
            "-framerate", str(FPS),
            "-i", str(pattern),
            "-frames:v", str(frames),
            "-an",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-preset", "veryfast",
            "-crf", "28",
            "-g", "2",
            "-keyint_min", "2",
            "-sc_threshold", "0",
            "-movflags", "+faststart",
            str(out),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )


def zoom_frame(base: Image.Image, z: float) -> Image.Image:
    bw, bh = base.size
    zw, zh = int(bw / z), int(bh / z)
    left = (bw - zw) // 2
    top = (bh - zh) // 2
    return base.crop((left, top, left + zw, top + zh)).resize((W, H), Image.Resampling.LANCZOS)


def ease(t: float) -> float:
    # settle a little in the middle, then finish the move
    return t * t * (3 - 2 * t)


def main() -> None:
    VID.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    work = ROOT / "assets" / "_work"
    work.mkdir(parents=True, exist_ok=True)

    bases: dict[str, Image.Image] = {}
    firsts: dict[str, Image.Image] = {}
    lasts: dict[str, Image.Image] = {}

    for name in SCENES:
        base = crop_16x9(Image.open(STILLS / f"{name}.png"))
        bases[name] = base
        scene_dir = work / name
        scene_dir.mkdir(parents=True, exist_ok=True)
        print(f"dive {name}")
        for i in range(DIVE_FRAMES):
            t = ease(i / (DIVE_FRAMES - 1))
            z = 1.0 + 0.16 * t
            zoom_frame(base, z).save(scene_dir / f"f{i:04d}.png")
        first = Image.open(scene_dir / "f0000.png").convert("RGB")
        last = Image.open(scene_dir / f"f{DIVE_FRAMES - 1:04d}.png").convert("RGB")
        first.save(FRAMES / f"{name}-first.png")
        last.save(FRAMES / f"{name}-last.png")
        first.save(ROOT / "assets" / f"{name}.webp", "WEBP", quality=86, method=4)
        firsts[name] = first
        lasts[name] = last
        encode(scene_dir / "f%04d.png", VID / f"{name}.mp4", DIVE_FRAMES)

    for i in range(len(SCENES) - 1):
        a, b = SCENES[i], SCENES[i + 1]
        print(f"connector {i + 1} {a}->{b}")
        conn_dir = work / f"conn{i + 1}"
        conn_dir.mkdir(parents=True, exist_ok=True)
        start = lasts[a]
        end = firsts[b]
        for n in range(CONN_FRAMES):
            t = 0.0 if n == 0 else (1.0 if n == CONN_FRAMES - 1 else ease(n / (CONN_FRAMES - 1)))
            if t <= 0:
                frame = start
            elif t >= 1:
                frame = end
            else:
                frame = Image.blend(start, end, t)
            frame.save(conn_dir / f"f{n:04d}.png")
        encode(conn_dir / "f%04d.png", VID / f"conn{i + 1}.mp4", CONN_FRAMES)

    print("done")


if __name__ == "__main__":
    main()
