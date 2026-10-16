#!/usr/bin/env python3
"""Generate Internet/Network Layer detail diagram."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 580, 340
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
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
BORDER_COLOR = (100, 100, 100, 255)
LAYER_COLOR = (255, 165, 0, 255)  # Orange for network
TCP_COLOR = (60, 179, 113, 255)
HTTP_COLOR = (100, 149, 237, 255)
BOX_BG = (255, 250, 240, 255)

# Title
draw.rounded_rectangle([20, 15, 560, 45], radius=6, fill=LAYER_COLOR, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 30), "Schritt 3: Internetschicht (Layer 3)", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Content box
draw.rounded_rectangle([20, 55, 560, 310], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# IP Header details
draw.text((35, 70), "IP-Header wird hinzugefügt (20 Bytes):", font=font_label, fill=TEXT_DARK, anchor="lm")

# Header fields
fields = [
    ("Version:", "4", "(IPv4)"),
    ("TTL:", "64", "(max. Hops)"),
    ("Protocol:", "6", "(TCP)"),
    ("Source IP:", "192.168.1.10", "(Client)"),
    ("Destination IP:", "10.0.0.5", "(Server)"),
]

table_y = 92
for i, (field, value, note) in enumerate(fields):
    y = table_y + i * 18
    draw.text((40, y), field, font=font_text, fill=TEXT_DARK, anchor="lm")
    draw.text((155, y), value, font=font_mono, fill=(180, 120, 0, 255), anchor="lm")
    draw.text((260, y), note, font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Routing decision box
route_y = 195
draw.rectangle([35, route_y, 320, route_y + 35], fill=(255, 245, 220, 255), outline=(200, 150, 50, 255), width=1)
draw.text((40, route_y + 8), "Routing-Entscheidung:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((40, route_y + 22), "10.0.0.5 nicht lokal → Gateway 192.168.1.1", font=font_small, fill=(150, 100, 0, 255), anchor="lm")

# Right side: Layer contribution
contrib_x = 355
draw.text((contrib_x, 70), "Beitrag:", font=font_label, fill=TEXT_DARK, anchor="lm")
contributions = [
    "✓ IP-Adressen",
    "✓ Routing",
    "✓ Fragmentierung",
    "✓ TTL (Schleifen)"
]
for i, c in enumerate(contributions):
    draw.text((contrib_x, 90 + i * 16), c, font=font_small, fill=(60, 120, 60, 255), anchor="lm")

draw.text((contrib_x, 165), "PDU:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((contrib_x, 182), "Paket / Datagramm", font=font_text, fill=TEXT_DARK, anchor="lm")

# Bottom: Packet visualization
packet_y = 250
draw.text((35, packet_y), "Resultat:", font=font_label, fill=TEXT_DARK, anchor="lm")

# IP + TCP + Data
ip_w = 45
tcp_w = 50
data_w = 150
draw.rectangle([100, packet_y + 18, 100 + ip_w, packet_y + 45], fill=LAYER_COLOR, outline=BORDER_COLOR, width=1)
draw.text((100 + ip_w//2, packet_y + 31), "IP", font=font_small, fill=TEXT_LIGHT, anchor="mm")
draw.rectangle([100 + ip_w, packet_y + 18, 100 + ip_w + tcp_w, packet_y + 45], fill=TCP_COLOR, outline=BORDER_COLOR, width=1)
draw.text((100 + ip_w + tcp_w//2, packet_y + 31), "TCP", font=font_small, fill=TEXT_LIGHT, anchor="mm")
draw.rectangle([100 + ip_w + tcp_w, packet_y + 18, 100 + ip_w + tcp_w + data_w, packet_y + 45], fill=HTTP_COLOR, outline=BORDER_COLOR, width=1)
draw.text((100 + ip_w + tcp_w + data_w//2, packet_y + 31), "Daten", font=font_small, fill=TEXT_LIGHT, anchor="mm")

draw.text((100 + ip_w + tcp_w + data_w + 15, packet_y + 31), "→ an Sicherungsschicht", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/schicht-internet_draft.png", "PNG")
print(f"Created: {output_dir}/schicht-internet_draft.png")
