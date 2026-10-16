#!/usr/bin/env python3
"""Generate Transport Layer detail diagram."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 580, 320
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
LAYER_COLOR = (60, 179, 113, 255)  # Green for transport
HTTP_COLOR = (100, 149, 237, 255)
BOX_BG = (240, 255, 245, 255)

# Title
draw.rounded_rectangle([20, 15, 560, 45], radius=6, fill=LAYER_COLOR, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 30), "Schritt 2: Transportschicht (Layer 4)", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Content box
draw.rounded_rectangle([20, 55, 560, 290], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# TCP Header details
draw.text((35, 70), "TCP-Header wird hinzugefügt (20 Bytes):", font=font_label, fill=TEXT_DARK, anchor="lm")

# Header fields table
fields = [
    ("Source Port:", "52345", "(ephemeral)"),
    ("Destination Port:", "80", "(HTTP)"),
    ("Sequence Number:", "1000", ""),
    ("Flags:", "SYN/ACK", ""),
    ("Window Size:", "65535", ""),
    ("Checksum:", "0x3A7F", ""),
]

table_y = 92
for i, (field, value, note) in enumerate(fields):
    y = table_y + i * 18
    draw.text((40, y), field, font=font_text, fill=TEXT_DARK, anchor="lm")
    draw.text((165, y), value, font=font_mono, fill=(40, 120, 80, 255), anchor="lm")
    if note:
        draw.text((230, y), note, font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Right side: Layer contribution
contrib_x = 340
draw.text((contrib_x, 70), "Beitrag:", font=font_label, fill=TEXT_DARK, anchor="lm")
contributions = [
    "✓ Portnummern",
    "✓ Verbindungsaufbau",
    "✓ Zuverlässigkeit",
    "✓ Flusskontrolle"
]
for i, c in enumerate(contributions):
    draw.text((contrib_x, 90 + i * 16), c, font=font_small, fill=(60, 120, 60, 255), anchor="lm")

draw.text((contrib_x, 160), "PDU:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((contrib_x, 177), "Segment (TCP)", font=font_text, fill=TEXT_DARK, anchor="lm")
draw.text((contrib_x, 192), "Datagramm (UDP)", font=font_text, fill=TEXT_DARK, anchor="lm")

# Bottom: Packet visualization
packet_y = 230
draw.text((35, packet_y), "Resultat:", font=font_label, fill=TEXT_DARK, anchor="lm")

# TCP + Data
tcp_w = 60
data_w = 180
draw.rectangle([100, packet_y + 18, 100 + tcp_w, packet_y + 45], fill=LAYER_COLOR, outline=BORDER_COLOR, width=1)
draw.text((100 + tcp_w//2, packet_y + 31), "TCP", font=font_small, fill=TEXT_LIGHT, anchor="mm")
draw.rectangle([100 + tcp_w, packet_y + 18, 100 + tcp_w + data_w, packet_y + 45], fill=HTTP_COLOR, outline=BORDER_COLOR, width=1)
draw.text((100 + tcp_w + data_w//2, packet_y + 31), "Daten", font=font_small, fill=TEXT_LIGHT, anchor="mm")

draw.text((100 + tcp_w + data_w + 15, packet_y + 31), "→ an Internetschicht", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/schicht-transport_draft.png", "PNG")
print(f"Created: {output_dir}/schicht-transport_draft.png")
