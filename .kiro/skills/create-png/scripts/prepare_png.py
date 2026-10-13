#!/usr/bin/env python3
"""Prepare transparent color/grayscale PNG pair and a four-way theme preview.

Usage:
  python prepare_png.py draft.png --outdir /tmp/png-stage --stem cpu-scheduler
Requires Pillow: pip install Pillow
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--stem', required=True)
    parser.add_argument('--margin', type=float, default=0.03,
                        help='Minimum transparent margin as fraction of shorter dimension (default 0.03)')
    args = parser.parse_args()
    if not 0 <= args.margin < 0.45:
        parser.error('--margin must be between 0 and 0.45')
    if args.stem.endswith('.png'):
        parser.error('--stem must not include a .png extension')
    args.outdir.mkdir(parents=True, exist_ok=True)

    color = Image.open(args.source).convert('RGBA')
    w, h = color.size
    alpha = color.getchannel('A')
    if alpha.getextrema()[0] == 255:
        raise SystemExit('FAIL: no transparent pixels found in source PNG')
    # Reject forbidden exact RGB values on any visible (alpha > 0) pixel.
    rgb = color.convert("RGB")
    forbidden = 0
    for (r, g, b), a in zip(rgb.getdata(), alpha.getdata()):
        if a > 0 and ((r, g, b) == (0, 0, 0) or (r, g, b) == (255, 255, 255)):
            forbidden += 1
    if forbidden:
        raise SystemExit(f"FAIL: {forbidden} visible pure-black/pure-white pixels found. Replace #000000 and #FFFFFF with theme-compatible colors.")
    bbox = alpha.getbbox()
    if bbox is None:
        raise SystemExit('FAIL: source PNG is completely transparent')
    l, t, r, b = bbox
    min_edge = min(l, t, w-r, h-b)
    required = int(min(w, h) * args.margin)
    if min_edge < required:
        raise SystemExit(f'FAIL: graphic too close to canvas edge (margin {min_edge}px; required >= {required}px). Add canvas padding.')
    grayscale_rgb = ImageOps.grayscale(color.convert('RGB')).convert('RGB')
    gray = grayscale_rgb.copy()
    gray.putalpha(alpha)
    gray = gray.convert('RGBA')

    color_path = args.outdir / f'{args.stem}.png'
    gray_path = args.outdir / f'{args.stem}_g.png'
    color.save(color_path)
    gray.save(gray_path)

    max_side = 640
    scale = min(1.0, max_side / max(w, h))
    pw, ph = max(1, int(w*scale)), max(1, int(h*scale))
    tiles = []
    for title, original, background in (
        ('Color / light theme', color, (250, 250, 250, 255)),
        ('Color / dark theme', color, (24, 26, 30, 255)),
        ('Grayscale / light theme', gray, (250, 250, 250, 255)),
        ('Grayscale / dark theme', gray, (24, 26, 30, 255)),
    ):
        img = original.resize((pw, ph), Image.Resampling.LANCZOS)
        tile = Image.new('RGBA', (pw, ph), background)
        tile.alpha_composite(img)
        tiles.append((title, tile.convert('RGB')))
    gap, label_h = 20, 34
    sheet = Image.new('RGB', (pw * 2 + gap * 3, (ph + label_h) * 2 + gap * 3), '#dddddd')
    draw = ImageDraw.Draw(sheet)
    for i, (title, image) in enumerate(tiles):
        x = gap + (i % 2) * (pw + gap)
        y = gap + (i // 2) * (ph + label_h + gap)
        draw.text((x + 4, y + 8), title, fill='#111111')
        sheet.paste(image, (x, y + label_h))
    preview_path = args.outdir / f'{args.stem}_preview.png'
    sheet.save(preview_path)
    print(f'PASS: RGBA PNGs generated ({w} x {h}), minimum edge margin = {min_edge}px')
    print(f'Color: {color_path}')
    print(f'Grayscale: {gray_path}')
    print(f'Preview: {preview_path}')
    print('MANUAL CHECK REQUIRED: verify theme contrast, semantics, and original source clipping.')


if __name__ == '__main__':
    main()
