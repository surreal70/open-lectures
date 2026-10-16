#!/usr/bin/env python3
"""Generate OSI Reference Model diagram."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas (with padding)
WIDTH, HEIGHT = 1020, 780
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
except:
    font_title = font_header = font_text = font_small = ImageFont.load_default()

# Colors for both themes
TITLE_COLOR = (70, 130, 180, 255)      # Steel blue
LAYER_COLORS = [
    (100, 149, 237, 255),  # Layer 7 - Cornflower blue
    (123, 104, 238, 255),  # Layer 6 - Medium slate blue
    (138, 43, 226, 255),   # Layer 5 - Blue violet
    (60, 179, 113, 255),   # Layer 4 - Medium sea green
    (255, 165, 0, 255),    # Layer 3 - Orange
    (255, 99, 71, 255),    # Layer 2 - Tomato
    (220, 20, 60, 255),    # Layer 1 - Crimson
]
TEXT_DARK = (50, 50, 50, 255)
TEXT_LIGHT = (240, 240, 240, 255)
BORDER_COLOR = (100, 100, 100, 255)
BRACKET_COLOR = (80, 80, 80, 255)

# Title
draw.text((WIDTH//2, 55), "OSI-Referenzmodell", font=font_title, fill=TITLE_COLOR, anchor="mm")
draw.text((WIDTH//2, 80), "(ISO/IEC 7498)", font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# Layer data
layers = [
    ("7", "Anwendung", "Application", "Daten"),
    ("6", "Darstellung", "Presentation", "Daten"),
    ("5", "Sitzung", "Session", "Daten"),
    ("4", "Transport", "Transport", "Segmente"),
    ("3", "Vermittlung", "Network", "Pakete"),
    ("2", "Sicherung", "Data Link", "Frames"),
    ("1", "Bitübertragung", "Physical", "Bits"),
]

# Column headers
header_y = 110
col_x = [100, 180, 350, 530, 730]
headers = ["Nr.", "Schicht", "Englisch", "Dateneinheit"]
for i, (x, h) in enumerate(zip(col_x, headers)):
    draw.text((x, header_y), h, font=font_header, fill=TITLE_COLOR, anchor="lm")

# Draw separator line
draw.line([(70, header_y + 20), (890, header_y + 20)], fill=BORDER_COLOR, width=2)

# Draw layers
layer_height = 65
start_y = 150
for i, (num, de, en, data) in enumerate(layers):
    y = start_y + i * layer_height
    color = LAYER_COLORS[i]
    
    # Layer box
    box = [110, y, 690, y + layer_height - 8]
    draw.rounded_rectangle(box, radius=8, fill=color, outline=BORDER_COLOR, width=2)
    
    # Layer number (left of box)
    draw.text((80, y + (layer_height - 8)//2), num, font=font_header, fill=color, anchor="mm")
    
    # German name
    draw.text((150, y + (layer_height - 8)//2), de, font=font_text, fill=TEXT_LIGHT, anchor="lm")
    
    # English name
    draw.text((350, y + (layer_height - 8)//2), en, font=font_text, fill=TEXT_LIGHT, anchor="lm")
    
    # Data unit (right of box)
    draw.text((730, y + (layer_height - 8)//2), data, font=font_text, fill=color, anchor="lm")

# Draw grouping brackets
bracket_x = 850

# Application-oriented (5-7)
bracket_top = start_y
bracket_bottom = start_y + 3 * layer_height - 8
draw.line([(bracket_x, bracket_top), (bracket_x + 15, bracket_top)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x + 15, bracket_top), (bracket_x + 15, bracket_bottom)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, bracket_bottom), (bracket_x + 15, bracket_bottom)], fill=BRACKET_COLOR, width=2)
draw.text((bracket_x + 25, (bracket_top + bracket_bottom)//2), "Anwendungs-\norientiert", 
          font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Transport-oriented (1-4)
bracket_top2 = start_y + 3 * layer_height
bracket_bottom2 = start_y + 7 * layer_height - 8
draw.line([(bracket_x, bracket_top2), (bracket_x + 15, bracket_top2)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x + 15, bracket_top2), (bracket_x + 15, bracket_bottom2)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, bracket_bottom2), (bracket_x + 15, bracket_bottom2)], fill=BRACKET_COLOR, width=2)
draw.text((bracket_x + 25, (bracket_top2 + bracket_bottom2)//2), "Transport-\norientiert", 
          font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
os.makedirs(output_dir, exist_ok=True)
img.save(f"{output_dir}/osi-referenzmodell_draft.png", "PNG")
print(f"Created: {output_dir}/osi-referenzmodell_draft.png")
