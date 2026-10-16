#!/usr/bin/env python3
"""Generate OSI Data Encapsulation diagram with ISDN protocol stack."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas (with padding)
WIDTH, HEIGHT = 920, 750
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font_layer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except:
    font_title = font_layer = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
LAYER7_COLOR = (100, 149, 237, 255)    # Blue - Application
LAYER6_COLOR = (123, 104, 238, 255)    # Slate blue - Presentation
LAYER5_COLOR = (138, 43, 226, 255)     # Violet - Session
LAYER4_COLOR = (60, 179, 113, 255)     # Green - Transport
LAYER3_COLOR = (255, 165, 0, 255)      # Orange - Network
LAYER2_COLOR = (255, 99, 71, 255)      # Red - Data Link
LAYER1_COLOR = (220, 20, 60, 255)      # Crimson - Physical
DATA_COLOR = (169, 169, 169, 255)      # Gray - User data
TEXT_LIGHT = (245, 245, 245, 255)
TEXT_DARK = (60, 60, 60, 255)
ARROW_COLOR = (100, 100, 100, 255)
LABEL_COLOR = (80, 80, 80, 255)

# Title
draw.text((WIDTH//2, 45), "OSI-Datenkapselung (ISDN-Beispiel)", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout
start_y = 90
layer_spacing = 80
left_margin = 50
box_start_x = 220

# ISDN protocol stack showing all 7 layers
# Layer 7: X.400 (E-Mail) or X.500 (Directory)
# Layer 6: ASN.1/BER encoding
# Layer 5: ACSE (Association Control)
# Layer 4: TP0-TP4 (Transport Protocol)
# Layer 3: X.25/Q.931 (Network)
# Layer 2: LAPD (Link Access Procedure D-channel)
# Layer 1: I.430/I.431 (Physical)

layers = [
    ("7 Anwendung", [(LAYER7_COLOR, "X.400", 70), (DATA_COLOR, "Nutzdaten", 220)], "PDU", "Application PDU"),
    ("6 Darstellung", [(LAYER6_COLOR, "ASN.1", 55), (LAYER7_COLOR, "X.400", 55), (DATA_COLOR, "Nutzdaten", 180)], "PPDU", "Presentation PDU"),
    ("5 Sitzung", [(LAYER5_COLOR, "ACSE", 50), (LAYER6_COLOR, "ASN.1", 50), (LAYER7_COLOR, "X.400", 50), (DATA_COLOR, "Nutzdaten", 140)], "SPDU", "Session PDU"),
    ("4 Transport", [(LAYER4_COLOR, "TP4", 45), (LAYER5_COLOR, "ACSE", 45), (LAYER6_COLOR, "ASN.1", 45), (LAYER7_COLOR, "X.400", 45), (DATA_COLOR, "Daten", 110)], "TPDU", "Transport PDU"),
    ("3 Vermittlung", [(LAYER3_COLOR, "Q.931", 50), (LAYER4_COLOR, "TP4", 40), (LAYER5_COLOR, "...", 30), (DATA_COLOR, "...", 170)], "Paket", "Network Packet"),
    ("2 Sicherung", [(LAYER2_COLOR, "LAPD", 50), (LAYER3_COLOR, "Q.931", 45), (LAYER4_COLOR, "...", 25), (DATA_COLOR, "...", 140), (LAYER2_COLOR, "FCS", 35)], "Frame", "Data Frame"),
    ("1 Bitübertragung", None, "Bits", "I.430/I.431"),
]

def draw_arrow_down(x, y1, y2):
    """Draw a downward arrow."""
    draw.line([(x, y1), (x, y2 - 8)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x, y2), (x - 6, y2 - 10), (x + 6, y2 - 10)], fill=ARROW_COLOR)

for i, (layer_name, boxes, unit_name, protocol) in enumerate(layers):
    y = start_y + i * layer_spacing
    
    # Layer label (left side)
    draw.text((left_margin, y + 22), layer_name, font=font_layer, fill=TITLE_COLOR, anchor="lm")
    
    if boxes is not None:
        # Draw boxes
        x = box_start_x
        for color, label, width in boxes:
            box = [x, y, x + width, y + 45]
            draw.rounded_rectangle(box, radius=5, fill=color, outline=(80, 80, 80, 255), width=2)
            draw.text((x + width//2, y + 22), label, font=font_small, fill=TEXT_LIGHT, anchor="mm")
            x += width + 2
        
        # Unit label (right side)
        total_width = sum(w for _, _, w in boxes) + (len(boxes) - 1) * 2
        draw.text((box_start_x + total_width + 25, y + 15), f"= {unit_name}", font=font_text, fill=LABEL_COLOR, anchor="lm")
        draw.text((box_start_x + total_width + 25, y + 32), f"({protocol})", font=font_small, fill=(120, 120, 120, 255), anchor="lm")
    else:
        # Physical layer - bits
        bits = "10110010 01101001 11010100 00101101 ..."
        draw.text((box_start_x, y + 22), bits, font=font_layer, fill=LAYER1_COLOR, anchor="lm")
        draw.text((box_start_x + 320, y + 15), f"= {unit_name}", font=font_text, fill=LABEL_COLOR, anchor="lm")
        draw.text((box_start_x + 320, y + 32), f"({protocol})", font=font_small, fill=(120, 120, 120, 255), anchor="lm")
    
    # Arrow to next layer
    if i < len(layers) - 1:
        arrow_x = box_start_x + 150
        draw_arrow_down(arrow_x, y + 50, y + layer_spacing - 5)

# Add explanation at bottom
bottom_y = start_y + 7 * layer_spacing + 15
draw.line([(50, bottom_y), (870, bottom_y)], fill=(150, 150, 150, 255), width=1)

# Legend
draw.text((80, bottom_y + 20), "Sender:", font=font_layer, fill=(100, 100, 100, 255), anchor="lm")
draw.text((150, bottom_y + 20), "Kapselung (Encapsulation) ↓", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

draw.text((450, bottom_y + 20), "Empfänger:", font=font_layer, fill=(100, 100, 100, 255), anchor="lm")
draw.text((540, bottom_y + 20), "Entkapselung (Decapsulation) ↑", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Note about ISDN
draw.text((WIDTH//2, bottom_y + 50), "ISDN verwendet alle 7 OSI-Schichten mit klar getrennten Protokollen", 
          font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
os.makedirs(output_dir, exist_ok=True)
img.save(f"{output_dir}/osi-kapselung-isdn_draft.png", "PNG")
print(f"Created: {output_dir}/osi-kapselung-isdn_draft.png")
