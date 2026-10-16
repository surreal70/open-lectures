#!/usr/bin/env python3
"""Generate Data Encapsulation diagram."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas (with padding)
WIDTH, HEIGHT = 900, 660
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    font_layer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except:
    font_title = font_layer = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
DATA_COLOR = (100, 149, 237, 255)      # Blue - user data
TCP_COLOR = (60, 179, 113, 255)        # Green - TCP
IP_COLOR = (255, 165, 0, 255)          # Orange - IP
ETH_COLOR = (255, 99, 71, 255)         # Red - Ethernet
FCS_COLOR = (220, 20, 60, 255)         # Dark red - FCS
BITS_COLOR = (138, 43, 226, 255)       # Purple - Bits
TEXT_LIGHT = (245, 245, 245, 255)
TEXT_DARK = (60, 60, 60, 255)
ARROW_COLOR = (100, 100, 100, 255)
LABEL_COLOR = (80, 80, 80, 255)

# Title
draw.text((WIDTH//2, 50), "Datenkapselung (Encapsulation)", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout
start_y = 100
layer_spacing = 95
left_margin = 70
box_start_x = 200

layers = [
    ("Anwendung", [(DATA_COLOR, "Daten", 300)], "Daten"),
    ("Transport", [(TCP_COLOR, "TCP", 60), (DATA_COLOR, "Daten", 240)], "Segment"),
    ("Netzwerk", [(IP_COLOR, "IP", 50), (TCP_COLOR, "TCP", 60), (DATA_COLOR, "Daten", 190)], "Paket"),
    ("Sicherung", [(ETH_COLOR, "ETH", 50), (IP_COLOR, "IP", 50), (TCP_COLOR, "TCP", 50), (DATA_COLOR, "Daten", 130), (FCS_COLOR, "FCS", 40)], "Frame"),
    ("Physikalisch", None, "Bits"),
]

def draw_arrow_down(x, y1, y2):
    """Draw a downward arrow."""
    draw.line([(x, y1), (x, y2 - 10)], fill=ARROW_COLOR, width=2)
    # Arrowhead
    draw.polygon([(x, y2), (x - 8, y2 - 12), (x + 8, y2 - 12)], fill=ARROW_COLOR)

for i, (layer_name, boxes, unit_name) in enumerate(layers):
    y = start_y + i * layer_spacing
    
    # Layer label (left side)
    draw.text((left_margin, y + 20), layer_name, font=font_layer, fill=TITLE_COLOR, anchor="lm")
    
    if boxes is not None:
        # Draw boxes
        x = box_start_x
        for color, label, width in boxes:
            box = [x, y, x + width, y + 45]
            draw.rounded_rectangle(box, radius=6, fill=color, outline=(80, 80, 80, 255), width=2)
            draw.text((x + width//2, y + 22), label, font=font_text, fill=TEXT_LIGHT, anchor="mm")
            x += width + 3
        
        # Unit label (right side with = sign)
        total_width = sum(w for _, _, w in boxes) + (len(boxes) - 1) * 3
        draw.text((box_start_x + total_width + 30, y + 22), f"= {unit_name}", font=font_text, fill=LABEL_COLOR, anchor="lm")
    else:
        # Physical layer - bits
        bits = "01101001 01010110 11001010 00110101 ..."
        draw.text((box_start_x, y + 22), bits, font=font_layer, fill=BITS_COLOR, anchor="lm")
        draw.text((box_start_x + 350, y + 22), f"= {unit_name}", font=font_text, fill=LABEL_COLOR, anchor="lm")
    
    # Arrow to next layer
    if i < len(layers) - 1:
        arrow_x = box_start_x + 150
        draw_arrow_down(arrow_x, y + 50, y + layer_spacing - 5)

# Add sender/receiver labels at bottom
bottom_y = start_y + 5 * layer_spacing + 20
draw.line([(70, bottom_y), (830, bottom_y)], fill=(150, 150, 150, 255), width=1)

# Sender side
draw.text((170, bottom_y + 25), "Sender:", font=font_layer, fill=(100, 100, 100, 255), anchor="lm")
draw.text((240, bottom_y + 25), "Kapselung ↓", font=font_text, fill=(100, 100, 100, 255), anchor="lm")
draw.text((340, bottom_y + 25), "(von oben nach unten)", font=font_small, fill=(130, 130, 130, 255), anchor="lm")

# Receiver side  
draw.text((540, bottom_y + 25), "Empfänger:", font=font_layer, fill=(100, 100, 100, 255), anchor="lm")
draw.text((630, bottom_y + 25), "Entkapselung ↑", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
os.makedirs(output_dir, exist_ok=True)
img.save(f"{output_dir}/datenkapselung_draft.png", "PNG")
print(f"Created: {output_dir}/datenkapselung_draft.png")
