#!/usr/bin/env python3
"""Generate OSI vs TCP/IP comparison diagram."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas
WIDTH, HEIGHT = 900, 620
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except:
    font_title = font_header = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
OSI_COLORS = [
    (100, 149, 237, 255),  # 7 Application
    (123, 104, 238, 255),  # 6 Presentation
    (138, 43, 226, 255),   # 5 Session
    (60, 179, 113, 255),   # 4 Transport
    (255, 165, 0, 255),    # 3 Network
    (255, 99, 71, 255),    # 2 Data Link
    (220, 20, 60, 255),    # 1 Physical
]
TCPIP_COLORS = [
    (100, 149, 237, 255),  # 4 Application (matches OSI 5-7)
    (60, 179, 113, 255),   # 3 Transport
    (255, 165, 0, 255),    # 2 Internet
    (255, 99, 71, 255),    # 1 Network Access (combined)
]
TEXT_LIGHT = (240, 240, 240, 255)
BORDER_COLOR = (100, 100, 100, 255)
ARROW_COLOR = (120, 120, 120, 255)

# Title
draw.text((WIDTH//2, 40), "OSI-Modell vs. TCP/IP-Modell", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout
osi_x = 120
tcpip_x = 620
box_width = 200
layer_height = 55
start_y = 90

# Headers
draw.text((osi_x + box_width//2, start_y), "OSI-Modell", font=font_header, fill=TITLE_COLOR, anchor="mm")
draw.text((osi_x + box_width//2, start_y + 18), "(7 Schichten)", font=font_small, fill=(120, 120, 120, 255), anchor="mm")

draw.text((tcpip_x + box_width//2, start_y), "TCP/IP-Modell", font=font_header, fill=TITLE_COLOR, anchor="mm")
draw.text((tcpip_x + box_width//2, start_y + 18), "(4 Schichten)", font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# OSI layers
osi_layers = [
    ("7", "Anwendung"),
    ("6", "Darstellung"),
    ("5", "Sitzung"),
    ("4", "Transport"),
    ("3", "Vermittlung"),
    ("2", "Sicherung"),
    ("1", "Bitübertragung"),
]

osi_start_y = start_y + 50
for i, (num, name) in enumerate(osi_layers):
    y = osi_start_y + i * layer_height
    color = OSI_COLORS[i]
    
    box = [osi_x, y, osi_x + box_width, y + layer_height - 8]
    draw.rounded_rectangle(box, radius=6, fill=color, outline=BORDER_COLOR, width=2)
    
    draw.text((osi_x + 25, y + (layer_height - 8)//2), num, font=font_header, fill=TEXT_LIGHT, anchor="mm")
    draw.text((osi_x + 115, y + (layer_height - 8)//2), name, font=font_text, fill=TEXT_LIGHT, anchor="mm")

# TCP/IP layers (with different heights to show mapping)
tcpip_layers = [
    ("4", "Anwendung", 3),      # spans OSI 5-7
    ("3", "Transport", 1),      # spans OSI 4
    ("2", "Internet", 1),       # spans OSI 3
    ("1", "Netzzugang", 2),     # spans OSI 1-2
]

tcpip_positions = [
    (osi_start_y, 3),                          # Layer 4: starts at OSI 7, spans 3
    (osi_start_y + 3 * layer_height, 1),       # Layer 3: starts at OSI 4, spans 1
    (osi_start_y + 4 * layer_height, 1),       # Layer 2: starts at OSI 3, spans 1
    (osi_start_y + 5 * layer_height, 2),       # Layer 1: starts at OSI 2, spans 2
]

for i, ((num, name, span), (y_start, _)) in enumerate(zip(tcpip_layers, tcpip_positions)):
    height = span * layer_height - 8
    color = TCPIP_COLORS[i]
    
    box = [tcpip_x, y_start, tcpip_x + box_width, y_start + height]
    draw.rounded_rectangle(box, radius=6, fill=color, outline=BORDER_COLOR, width=2)
    
    draw.text((tcpip_x + 25, y_start + height//2), num, font=font_header, fill=TEXT_LIGHT, anchor="mm")
    draw.text((tcpip_x + 115, y_start + height//2), name, font=font_text, fill=TEXT_LIGHT, anchor="mm")

# Draw connecting arrows
arrow_pairs = [
    # OSI layer center y -> TCP/IP layer center y
    (osi_start_y + 1 * layer_height - 4, osi_start_y + 1.5 * layer_height - 4),  # OSI 5-7 -> TCP 4
    (osi_start_y + 3 * layer_height + layer_height//2 - 4, osi_start_y + 3 * layer_height + layer_height//2 - 4),  # OSI 4 -> TCP 3
    (osi_start_y + 4 * layer_height + layer_height//2 - 4, osi_start_y + 4 * layer_height + layer_height//2 - 4),  # OSI 3 -> TCP 2
    (osi_start_y + 5.5 * layer_height - 4, osi_start_y + 6 * layer_height - 4),  # OSI 1-2 -> TCP 1
]

for osi_y, tcp_y in arrow_pairs:
    # Draw double-headed arrow
    x1 = osi_x + box_width + 10
    x2 = tcpip_x - 10
    mid_y = (osi_y + tcp_y) // 2
    
    # Line
    draw.line([(x1, osi_y), (x2, tcp_y)], fill=ARROW_COLOR, width=2)
    
    # Arrowhead right
    draw.polygon([(x2, tcp_y), (x2-10, tcp_y-5), (x2-10, tcp_y+5)], fill=ARROW_COLOR)
    # Arrowhead left
    draw.polygon([(x1, osi_y), (x1+10, osi_y-5), (x1+10, osi_y+5)], fill=ARROW_COLOR)

# Labels in middle
draw.text((WIDTH//2, osi_start_y + 1.5 * layer_height - 4), "≙", font=font_header, fill=ARROW_COLOR, anchor="mm")
draw.text((WIDTH//2, osi_start_y + 3.5 * layer_height - 4), "≙", font=font_header, fill=ARROW_COLOR, anchor="mm")
draw.text((WIDTH//2, osi_start_y + 4.5 * layer_height - 4), "≙", font=font_header, fill=ARROW_COLOR, anchor="mm")
draw.text((WIDTH//2, osi_start_y + 6 * layer_height - 4), "≙", font=font_header, fill=ARROW_COLOR, anchor="mm")

# Bottom labels
bottom_y = osi_start_y + 7 * layer_height + 20
draw.line([(50, bottom_y), (850, bottom_y)], fill=(150, 150, 150, 255), width=1)

draw.text((osi_x + box_width//2, bottom_y + 20), "Theoretisches Referenzmodell", font=font_small, fill=(100, 100, 100, 255), anchor="mm")
draw.text((tcpip_x + box_width//2, bottom_y + 20), "Praktisches Implementierungsmodell", font=font_small, fill=(100, 100, 100, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/osi-tcpip-vergleich_draft.png", "PNG")
print(f"Created: {output_dir}/osi-tcpip-vergleich_draft.png")
