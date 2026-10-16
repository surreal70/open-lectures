#!/usr/bin/env python3
"""Generate Network Access/Data Link Layer detail diagram."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 600, 380
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
ETH_COLOR = (255, 99, 71, 255)  # Red for data link
FCS_COLOR = (220, 20, 60, 255)
IP_COLOR = (255, 165, 0, 255)
TCP_COLOR = (60, 179, 113, 255)
HTTP_COLOR = (100, 149, 237, 255)
BOX_BG = (255, 245, 245, 255)

# Title
draw.rounded_rectangle([20, 15, 580, 45], radius=6, fill=ETH_COLOR, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 30), "Schritt 4: Netzzugangsschicht (Layer 2+1)", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Content box
draw.rounded_rectangle([20, 55, 580, 350], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# ARP info
draw.text((35, 70), "ARP-Auflösung (falls nötig):", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.rectangle([35, 88, 340, 120], fill=(255, 250, 245, 255), outline=(200, 150, 150, 255), width=1)
draw.text((40, 96), "Gateway 192.168.1.1 → MAC: BB:BB:BB:BB:BB:BB", font=font_mono, fill=(150, 80, 80, 255), anchor="lm")

# Ethernet Header
draw.text((35, 135), "Ethernet-Header (14 Bytes):", font=font_label, fill=TEXT_DARK, anchor="lm")
fields = [
    ("Destination MAC:", "BB:BB:BB:BB:BB:BB", "(Router)"),
    ("Source MAC:", "AA:AA:AA:AA:AA:AA", "(Client)"),
    ("EtherType:", "0x0800", "(IPv4)"),
]
table_y = 153
for i, (field, value, note) in enumerate(fields):
    y = table_y + i * 17
    draw.text((40, y), field, font=font_text, fill=TEXT_DARK, anchor="lm")
    draw.text((155, y), value, font=font_mono, fill=(180, 70, 70, 255), anchor="lm")
    draw.text((295, y), note, font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# FCS
draw.text((35, 210), "Frame Check Sequence (4 Bytes):", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((40, 228), "CRC-32: 0xA1B2C3D4", font=font_mono, fill=(180, 40, 40, 255), anchor="lm")

# Right side: Layer contribution
contrib_x = 390
draw.text((contrib_x, 70), "Beitrag:", font=font_label, fill=TEXT_DARK, anchor="lm")
contributions = [
    "✓ MAC-Adressen",
    "✓ ARP-Auflösung",
    "✓ Medienzugriff",
    "✓ Fehlererkennung",
    "✓ Bitübertragung"
]
for i, c in enumerate(contributions):
    draw.text((contrib_x, 90 + i * 16), c, font=font_small, fill=(60, 120, 60, 255), anchor="lm")

draw.text((contrib_x, 180), "PDU:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((contrib_x, 197), "Frame (Rahmen)", font=font_text, fill=TEXT_DARK, anchor="mm")

# Bottom: Complete Frame visualization
packet_y = 260
draw.text((35, packet_y), "Kompletter Ethernet-Frame:", font=font_label, fill=TEXT_DARK, anchor="lm")

# Eth + IP + TCP + Data + FCS
eth_w = 35
ip_w = 35
tcp_w = 35
data_w = 100
fcs_w = 30
start_x = 60
draw.rectangle([start_x, packet_y + 20, start_x + eth_w, packet_y + 47], fill=ETH_COLOR, outline=BORDER_COLOR, width=1)
draw.text((start_x + eth_w//2, packet_y + 33), "Eth", font=font_small, fill=TEXT_LIGHT, anchor="mm")

draw.rectangle([start_x + eth_w, packet_y + 20, start_x + eth_w + ip_w, packet_y + 47], fill=IP_COLOR, outline=BORDER_COLOR, width=1)
draw.text((start_x + eth_w + ip_w//2, packet_y + 33), "IP", font=font_small, fill=TEXT_LIGHT, anchor="mm")

draw.rectangle([start_x + eth_w + ip_w, packet_y + 20, start_x + eth_w + ip_w + tcp_w, packet_y + 47], fill=TCP_COLOR, outline=BORDER_COLOR, width=1)
draw.text((start_x + eth_w + ip_w + tcp_w//2, packet_y + 33), "TCP", font=font_small, fill=TEXT_LIGHT, anchor="mm")

draw.rectangle([start_x + eth_w + ip_w + tcp_w, packet_y + 20, start_x + eth_w + ip_w + tcp_w + data_w, packet_y + 47], fill=HTTP_COLOR, outline=BORDER_COLOR, width=1)
draw.text((start_x + eth_w + ip_w + tcp_w + data_w//2, packet_y + 33), "Daten", font=font_small, fill=TEXT_LIGHT, anchor="mm")

draw.rectangle([start_x + eth_w + ip_w + tcp_w + data_w, packet_y + 20, start_x + eth_w + ip_w + tcp_w + data_w + fcs_w, packet_y + 47], fill=FCS_COLOR, outline=BORDER_COLOR, width=1)
draw.text((start_x + eth_w + ip_w + tcp_w + data_w + fcs_w//2, packet_y + 33), "FCS", font=font_small, fill=TEXT_LIGHT, anchor="mm")

# Size info
total_w = eth_w + ip_w + tcp_w + data_w + fcs_w
draw.text((start_x + total_w + 15, packet_y + 33), "~258 Bytes", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Physical transmission
draw.text((35, packet_y + 58), "Übertragung auf Medium:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.rectangle([35, packet_y + 75, 400, packet_y + 95], fill=(200, 200, 200, 255), outline=BORDER_COLOR, width=1)
draw.text((217, packet_y + 85), "01101001010101010101... (elektrische Signale)", font=font_small, fill=TEXT_DARK, anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/schicht-netzzugang_draft.png", "PNG")
print(f"Created: {output_dir}/schicht-netzzugang_draft.png")
