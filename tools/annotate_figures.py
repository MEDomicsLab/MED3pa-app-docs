"""Draw numbered callouts onto the demonstration figures.

The walkthrough in `demonstration/` is written as a numbered procedure, and each
figure carries badges keyed to the steps that appear beside it. Numbering
restarts at 1 on every figure.

Run from the repository root:

    python tools/annotate_figures.py

The script overwrites the figures in `.gitbook/assets/demo/` in place, so it must
be run against a clean crop. A figure that has already been annotated has to be
restored first, for example:

    git show <commit-before-annotation>:.gitbook/assets/demo/03-import-csv.png > .gitbook/assets/demo/03-import-csv.png

Coordinates are in the pixel space of the cropped figure, and mark the centre of
each badge. When a screenshot is retaken, re-crop it to the same framing and
adjust the entries below.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

ASSETS = os.path.join(".gitbook", "assets", "demo")

BLUE = (24, 95, 165)
WHITE = (255, 255, 255)

# figure -> (badge radius, [(x, y, label), ...])
FIGURES = {
    "01-workspace-gate.png": (13, [
        (252, 308, "1"),          # Open workspace...
    ]),
    "02-workspace-overview.png": (16, [
        (1320, 26, "1"),          # server status indicator
    ]),
    "03-import-csv.png": (22, [
        (2195, 40, "1"),          # Data & Models, in the header
        (810, 689, "2"),          # Datasets tab
        (820, 777, "3"),          # Import CSV...
        (824, 62, "4"),           # Open, in the file chooser
    ]),
    "04-import-model-form.png": (15, [
        (222, 84, "1"),           # Base models tab
        (50, 355, "2"),           # Choose file...
        (50, 493, "3"),           # Model name
        (50, 611, "4"),           # Target column
        (50, 730, "5"),           # Features
    ]),
    "05-onnx-options.png": (13, [
        (20, 78, "1"),            # Decision threshold
        (20, 210, "2"),           # Outputs are raw logits
        (20, 346, "3"),           # Probability output name
        (20, 466, "4"),           # Import model
    ]),
}


def font_for(radius):
    size = int(radius * 1.35)
    for name in ("arialbd.ttf", "DejaVuSans-Bold.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def annotate(path, radius, badges):
    img = Image.open(path).convert("RGB")
    # supersample so the circles and digits keep clean edges
    scale = 4
    layer = Image.new("RGBA", (img.width * scale, img.height * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    fnt = font_for(radius * scale)

    for x, y, label in badges:
        cx, cy, r = x * scale, y * scale, radius * scale
        draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                     fill=BLUE + (255,), outline=WHITE + (255,), width=max(2, scale))
        box = draw.textbbox((0, 0), label, font=fnt)
        draw.text((cx - (box[2] - box[0]) / 2 - box[0],
                   cy - (box[3] - box[1]) / 2 - box[1]), label, font=fnt, fill=WHITE + (255,))

    layer = layer.resize(img.size, Image.LANCZOS)
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    img.save(path, optimize=True)
    return len(badges)


def main():
    if not os.path.isdir(ASSETS):
        sys.exit("run this from the repository root")
    for name, (radius, badges) in FIGURES.items():
        path = os.path.join(ASSETS, name)
        if not os.path.exists(path):
            print(f"  missing, skipped: {name}")
            continue
        n = annotate(path, radius, badges)
        print(f"  {name}: {n} callouts")


if __name__ == "__main__":
    main()
