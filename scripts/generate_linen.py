"""Render Asya's dark bookcloth: one seamless 420 CSS px tile at 3x.

Rebuild with Python, NumPy, and Pillow. The browser only repeats opaque
pixels; thread shading and quantization dither require no CSS filters.
"""

from pathlib import Path

import numpy as np
from PIL import Image


CSS_SIZE = 420
SCALE = 3
PITCH = 6
THREADS = CSS_SIZE // PITCH  # Even, so the over/under pattern wraps.
RNG = np.random.default_rng(260905)
OUTPUT = Path(__file__).resolve().parents[1] / "linen-weave.png"

y, x = np.mgrid[:CSS_SIZE * SCALE, :CSS_SIZE * SCALE] / SCALE
x += 0.5 / SCALE
y += 0.5 / SCALE
def thread_edges():
    spacing = RNG.uniform(0.80, 1.25, THREADS)
    return np.concatenate([[0.0], np.cumsum(spacing)]) * CSS_SIZE / spacing.sum()


x_edges = thread_edges()
y_edges = thread_edges()
i = np.searchsorted(x_edges, x % CSS_SIZE, "right") - 1
j = np.searchsorted(y_edges, y % CSS_SIZE, "right") - 1


def yarn(across, along, index, edges, thickness):
    """Rounded threads with periodic thickness, slubs, and fine fibres."""
    phase = RNG.uniform(0, 2 * np.pi, (3, THREADS))
    strength = RNG.uniform(0.9, 1.1, THREADS)[index]
    wave = (
        np.sin(2 * np.pi * 3 * along / CSS_SIZE + phase[0][index])
        + np.sin(2 * np.pi * 7 * along / CSS_SIZE + phase[1][index])
    ) / 2
    slub = np.clip((wave - 0.78) / 0.22, 0, 1)
    base = RNG.uniform(*thickness, THREADS)[index]
    width = base * (1 + 0.15 * slub + 0.035 * wave)
    centre = 0.5 + (
        0.055 * np.sin(2 * np.pi * 2 * along / CSS_SIZE + phase[2][index])
        + 0.030 * np.sin(2 * np.pi * 5 * along / CSS_SIZE + phase[0][index])
    )
    fraction = (across % CSS_SIZE - edges[index]) / (edges[index + 1] - edges[index])
    position = (fraction - centre) / width + 0.5
    profile = np.maximum(np.sin(np.pi * np.clip(position, 0, 1)), 0)
    profile = profile ** 0.8
    # Tiny fibres follow the yarn rather than covering it with random grit.
    twist = 2 * np.pi * 2 * along / CSS_SIZE
    fibres = 1 + 0.06 * np.sin(2 * np.pi * 3 * position + twist + phase[2][index])
    return profile * (strength + 0.10 * slub) * fibres, profile


warp, warp_profile = yarn(x, y, i, x_edges, (0.84, 1.02))
weft, weft_profile = yarn(y, x, j, y_edges, (0.90, 1.06))
warp_over = (i + j) % 2 == 0

# The lower yarn darkens where the upper yarn covers it; in the gaps it
# becomes visible again. Alternating crossings read as woven material.
visible_warp = warp * np.where(warp_over, 1, 1 - 0.58 * weft_profile)
visible_weft = weft * np.where(warp_over, 1 - 0.58 * warp_profile, 1)
weft_visible = visible_weft > visible_warp
light = 255 * (0.050 + 0.082 * np.maximum(visible_warp, visible_weft))
# Triangular luminance dither is baked before quantization, not composited
# by the browser. Two small warm palettes keep the opaque PNG lightweight
# without lossy compression or a second texture for each screen resolution.
light += RNG.triangular(-1.2, 0, 1.2, light.shape)
indices = np.clip(np.rint(light), 0, 63).astype(np.uint8)
indices += weft_visible.astype(np.uint8) * 64
palette = []
# Deep warm brown: retain the accepted yarn geometry and baked dither.
for warm in (False, True):
    for value in range(64):
        palette.extend((
            round(value * 1.08 * (1.03 if warm else 1)),
            round(value * 0.66),
            round(value * 0.43 * (0.94 if warm else 1)),
        ))
texture = Image.fromarray(indices).convert("P")
texture.putpalette(palette)
texture.save(OUTPUT, optimize=True)
print(f"{OUTPUT.name}: {CSS_SIZE * SCALE}px, {OUTPUT.stat().st_size:,} bytes")
