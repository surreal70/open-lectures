#!/usr/bin/env python3
"""Generate TCP/IP Model (DoD) diagram with transport/application-oriented markers."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas
WIDTH, HEIGHT = 1000, 580
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except:
    font_title = font_header = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
LAYER_COLORS = [
    (100, 149, 237, 255),  # Layer 4 - Application
    (60, 179, 113, 255),   # Layer 3 - Transport
    (255, 165, 0, 255),    # Layer 2 - Internet
    (220, 20, 60, 255),    # Layer 1 - Network Access
]
TEXT_LIGHT = (240, 240, 240, 255)
BORDER_COLOR = (100, 100, 100, 255)
BRACKET_COLOR = (80, 80, 80, 255)

# Title
draw.text((WIDTH//2, 45), "TCP/IP-Modell (DoD-Modell)", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layer data
layers = [
    ("4", "Anwendung", "Application", "Daten / Nachrichten"),
    ("3", "Transport", "Transport", "Segmente / Datagramme"),
    ("2", "Internet", "Internet", "Pakete"),
    ("1", "Netzzugang", "Network Access", "Frames / Bits"),
]

# Column headers
header_y = 90
draw.text((70, header_y), "Nr.", font=font_header, fill=TITLE_COLOR, anchor="lm")
draw.text((140, header_y), "Schicht", font=font_header, fill=TITLE_COLOR, anchor="lm")
draw.text((350, header_y), "Englisch", font=font_header, fill=TITLE_COLOR, anchor="lm")
draw.text((580, header_y), "Dateneinheit", font=font_header, fill=TITLE_COLOR, anchor="lm")

draw.line([(50, header_y + 20), (820, header_y + 20)], fill=BORDER_COLOR, width=2)

# Draw layers
layer_height = 85
start_y = 130
for i, (num, de, en, data) in enumerate(layers):
    y = start_y + i * layer_height
    color = LAYER_COLORS[i]
    
    # Layer box
    box = [100, y, 540, y + layer_height - 12]
    draw.rounded_rectangle(box, radius=10, fill=color, outline=BORDER_COLOR, width=2)
    
    # Layer number
    draw.text((60, y + (layer_height - 12)//2), num, font=font_header, fill=color, anchor="mm")
    
    # German name
    draw.text((140, y + (layer_height - 12)//2 - 10), de, font=font_header, fill=TEXT_LIGHT, anchor="lm")
    # English name below
    draw.text((140, y + (layer_height - 12)//2 + 12), f"({en})", font=font_small, fill=(220, 220, 220, 255), anchor="lm")
    
    # Data unit (right of box)
    draw.text((580, y + (layer_height - 12)//2), data, font=font_text, fill=color, anchor="lm")

# Draw grouping brackets (right side)
bracket_x = 820

# Application-oriented (Layer 4 only in TCP/IP, but corresponds to OSI 5-7)
bracket_top = start_y
bracket_bottom = start_y + 1 * layer_height - 12
draw.line([(bracket_x, bracket_top), (bracket_x + 15, bracket_top)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x + 15, bracket_top), (bracket_x + 15, bracket_bottom)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, bracket_bottom), (bracket_x + 15, bracket_bottom)], fill=BRACKET_COLOR, width=2)
draw.text((bracket_x + 25, (bracket_top + bracket_bottom)//2), "Anwendungs-\norientiert", 
          font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Transport-oriented (Layers 1-3)
bracket_top2 = start_y + 1 * layer_height
bracket_bottom2 = start_y + 4 * layer_height - 12
draw.line([(bracket_x, bracket_top2), (bracket_x + 15, bracket_top2)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x + 15, bracket_top2), (bracket_x + 15, bracket_bottom2)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, bracket_bottom2), (bracket_x + 15, bracket_bottom2)], fill=BRACKET_COLOR, width=2)
draw.text((bracket_x + 25, (bracket_top2 + bracket_bottom2)//2), "Transport-\norientiert", 
          font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Add OSI comparison note at bottom
bottom_y = start_y + 4 * layer_height + 15
draw.line([(50, bottom_y), (950, bottom_y)], fill=(150, 150, 150, 255), width=1)

note_y = bottom_y + 22
draw.text((WIDTH//2, note_y), "Entspricht OSI-Schichten: 4 ≙ 5-7, 3 ≙ 4, 2 ≙ 3, 1 ≙ 1-2", 
          font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/tcpip-modell_draft.png", "PNG")
print(f"Created: {output_dir}/tcpip-modell_draft.png")
