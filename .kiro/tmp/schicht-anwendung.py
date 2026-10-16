#!/usr/bin/env python3
"""Generate Application Layer detail diagram."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 550, 280
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 9)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
except:
    font_title = font_label = font_text = font_mono = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
BORDER_COLOR = (100, 100, 100, 255)
LAYER_COLOR = (100, 149, 237, 255)  # Blue for application
BOX_BG = (240, 245, 255, 255)

# Title with layer number
draw.rounded_rectangle([20, 15, 530, 45], radius=6, fill=LAYER_COLOR, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 30), "Schritt 1: Anwendungsschicht (Layer 7-5)", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Content box
draw.rounded_rectangle([20, 55, 530, 250], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# HTTP Request example
draw.text((35, 70), "Browser erzeugt HTTP-Request:", font=font_label, fill=TEXT_DARK, anchor="lm")

# Code block
code_y = 90
draw.rectangle([35, code_y, 380, code_y + 85], fill=(50, 50, 60, 255), outline=BORDER_COLOR, width=1)
http_lines = [
    "GET /index.html HTTP/1.1",
    "Host: 10.0.0.5",
    "User-Agent: Mozilla/5.0",
    "Accept: text/html",
    "Connection: keep-alive"
]
for i, line in enumerate(http_lines):
    draw.text((42, code_y + 8 + i * 15), line, font=font_mono, fill=(180, 220, 180, 255), anchor="lm")

# Right side: Layer contribution
contrib_x = 400
draw.text((contrib_x, 70), "Beitrag:", font=font_label, fill=TEXT_DARK, anchor="lm")
contributions = [
    "✓ Protokollauswahl",
    "✓ Datenformat",
    "✓ Benutzerinteraktion"
]
for i, c in enumerate(contributions):
    draw.text((contrib_x, 90 + i * 16), c, font=font_small, fill=(60, 120, 60, 255), anchor="lm")

# PDU info
draw.text((contrib_x, 145), "PDU:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((contrib_x, 162), "Daten / Nachricht", font=font_text, fill=TEXT_DARK, anchor="lm")

# Bottom: Data packet visualization
packet_y = 195
draw.text((35, packet_y), "Übergabe an Transportschicht:", font=font_label, fill=TEXT_DARK, anchor="lm")

# HTTP data block
draw.rectangle([35, packet_y + 18, 280, packet_y + 45], fill=LAYER_COLOR, outline=BORDER_COLOR, width=1)
draw.text((157, packet_y + 31), "HTTP-Request (Daten)", font=font_small, fill=TEXT_LIGHT, anchor="mm")
draw.text((290, packet_y + 31), "~200 Bytes", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/schicht-anwendung_draft.png", "PNG")
print(f"Created: {output_dir}/schicht-anwendung_draft.png")
