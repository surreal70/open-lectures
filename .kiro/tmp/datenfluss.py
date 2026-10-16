#!/usr/bin/env python3
"""Generate data flow diagram showing encapsulation/decapsulation with headers."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 900, 420
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
except:
    font_title = font_label = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
BORDER_COLOR = (100, 100, 100, 255)
ARROW_COLOR = (80, 80, 80, 255)

# Header colors
HTTP_COLOR = (100, 149, 237, 255)    # Blue - Application data
TCP_COLOR = (60, 179, 113, 255)      # Green - Transport
IP_COLOR = (255, 165, 0, 255)        # Orange - Network
ETH_COLOR = (255, 99, 71, 255)       # Red - Data Link
FCS_COLOR = (220, 20, 60, 255)       # Crimson - FCS

# Title
draw.text((WIDTH//2, 22), "Datenfluss durch die Schichten", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Column positions
col_client = 50
col_router = 380
col_server = 660
col_width = 200

# Labels
draw.text((col_client + col_width//2, 45), "CLIENT", font=font_label, fill=TEXT_DARK, anchor="mm")
draw.text((col_client + col_width//2, 56), "(Einkapselung)", font=font_small, fill=(120, 120, 120, 255), anchor="mm")
draw.text((col_router + 80, 45), "ROUTER", font=font_label, fill=TEXT_DARK, anchor="mm")
draw.text((col_server + col_width//2 - 30, 45), "SERVER", font=font_label, fill=TEXT_DARK, anchor="mm")
draw.text((col_server + col_width//2 - 30, 56), "(Entkapselung)", font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# Row positions
row_start = 75
row_height = 55

def draw_packet(x, y, segments, label_left="", label_right=""):
    """Draw a packet with colored segments."""
    seg_height = 22
    total_width = sum(s[1] for s in segments)
    
    # Draw label on left
    if label_left:
        draw.text((x - 5, y + seg_height//2), label_left, font=font_label, fill=TEXT_DARK, anchor="rm")
    
    # Draw segments
    current_x = x
    for name, width, color in segments:
        draw.rectangle([current_x, y, current_x + width, y + seg_height], fill=color, outline=BORDER_COLOR, width=1)
        draw.text((current_x + width//2, y + seg_height//2), name, font=font_small, fill=TEXT_LIGHT, anchor="mm")
        current_x += width
    
    # Draw label on right
    if label_right:
        draw.text((current_x + 5, y + seg_height//2), label_right, font=font_text, fill=(100, 100, 100, 255), anchor="lm")
    
    return total_width

def draw_down_arrow(x, y1, y2):
    """Draw downward arrow."""
    draw.line([(x, y1), (x, y2 - 5)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x, y2), (x - 4, y2 - 6), (x + 4, y2 - 6)], fill=ARROW_COLOR)

def draw_up_arrow(x, y1, y2):
    """Draw upward arrow."""
    draw.line([(x, y1), (x, y2 + 5)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x, y2), (x - 4, y2 + 6), (x + 4, y2 + 6)], fill=ARROW_COLOR)

def draw_right_arrow(x1, y, x2):
    """Draw right arrow."""
    draw.line([(x1, y), (x2 - 5, y)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x2, y), (x2 - 6, y - 4), (x2 - 6, y + 4)], fill=ARROW_COLOR)

# CLIENT SIDE - Encapsulation
# Layer 7: HTTP Data
y = row_start
draw_packet(col_client + 60, y, [("HTTP-Daten", 100, HTTP_COLOR)], "7", "Daten erzeugen")
draw_down_arrow(col_client + 110, y + 24, y + row_height - 8)

# Layer 4: TCP + Data
y += row_height
draw_packet(col_client + 40, y, [("TCP", 35, TCP_COLOR), ("Daten", 80, HTTP_COLOR)], "4", "+TCP-Header")
draw_down_arrow(col_client + 100, y + 24, y + row_height - 8)

# Layer 3: IP + TCP + Data
y += row_height
draw_packet(col_client + 25, y, [("IP", 30, IP_COLOR), ("TCP", 30, TCP_COLOR), ("Daten", 70, HTTP_COLOR)], "3", "+IP-Header")
draw_down_arrow(col_client + 95, y + 24, y + row_height - 8)

# Layer 2: Eth + IP + TCP + Data + FCS
y += row_height
draw_packet(col_client + 10, y, [("Eth", 25, ETH_COLOR), ("IP", 25, IP_COLOR), ("TCP", 25, TCP_COLOR), ("Daten", 55, HTTP_COLOR), ("FCS", 20, FCS_COLOR)], "2", "+Eth-Header/FCS")
draw_down_arrow(col_client + 90, y + 24, y + row_height - 8)

# Layer 1: Bits
y += row_height
draw.text((col_client + 10, y + 11), "1", font=font_label, fill=TEXT_DARK, anchor="rm")
draw.rectangle([col_client + 15, y, col_client + 165, y + 22], fill=(180, 180, 180, 255), outline=BORDER_COLOR, width=1)
draw.text((col_client + 90, y + 11), "Bits auf Medium", font=font_small, fill=TEXT_DARK, anchor="mm")

# Arrow to Router
bits_y = y + 11
draw_right_arrow(col_client + 170, bits_y, col_router - 10)

# ROUTER - Only processes L1-3
router_x = col_router

# Incoming frame at L2
y_router = row_start + 3 * row_height
draw_packet(router_x - 10, y_router, [("Eth", 22, ETH_COLOR), ("IP", 22, IP_COLOR), ("TCP", 22, TCP_COLOR), ("Daten", 45, HTTP_COLOR), ("FCS", 18, FCS_COLOR)], "", "")
draw.text((router_x + 40, y_router + 28), "Empfang", font=font_small, fill=(100, 100, 100, 255), anchor="mm")

# Arrow UP from L2 to L3 (left side - incoming)
draw_up_arrow(router_x + 30, y_router - 8, y_router - row_height + 25)

# Layer 3 processing
y_router_l3 = row_start + 2 * row_height
draw_packet(router_x + 10, y_router_l3, [("IP", 25, IP_COLOR), ("TCP", 25, TCP_COLOR), ("Daten", 50, HTTP_COLOR)], "", "")
draw.text((router_x + 130, y_router_l3 + 11), "Routing\nTTL--", font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Arrow DOWN from L3 to L2 (right side - outgoing)
draw_down_arrow(router_x + 100, y_router_l3 + 24, y_router - 8)

# Outgoing frame at L2
draw.text((router_x + 100, y_router + 28), "Senden", font=font_small, fill=(100, 100, 100, 255), anchor="mm")
draw.text((router_x + 5, y_router + 40), "Neue MAC-Adressen", font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Arrow to Server
draw_right_arrow(router_x + 135, bits_y, col_server - 40)

# SERVER SIDE - Decapsulation
# Layer 1: Bits
y = row_start + 4 * row_height
draw.rectangle([col_server - 30, y, col_server + 120, y + 22], fill=(180, 180, 180, 255), outline=BORDER_COLOR, width=1)
draw.text((col_server + 45, y + 11), "Bits vom Medium", font=font_small, fill=TEXT_DARK, anchor="mm")
draw.text((col_server + 135, y + 11), "1", font=font_label, fill=TEXT_DARK, anchor="lm")
draw_up_arrow(col_server + 45, y - 5, y - row_height + 25)

# Layer 2: Eth + IP + TCP + Data + FCS
y -= row_height
draw_packet(col_server - 30, y, [("Eth", 25, ETH_COLOR), ("IP", 25, IP_COLOR), ("TCP", 25, TCP_COLOR), ("Daten", 55, HTTP_COLOR), ("FCS", 20, FCS_COLOR)], "", "")
draw.text((col_server + 135, y + 11), "2", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((col_server + 150, y + 11), "-Eth/FCS", font=font_text, fill=(100, 100, 100, 255), anchor="lm")
draw_up_arrow(col_server + 50, y - 5, y - row_height + 25)

# Layer 3: IP + TCP + Data
y -= row_height
draw_packet(col_server - 15, y, [("IP", 30, IP_COLOR), ("TCP", 30, TCP_COLOR), ("Daten", 70, HTTP_COLOR)], "", "")
draw.text((col_server + 130, y + 11), "3", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((col_server + 145, y + 11), "-IP-Header", font=font_text, fill=(100, 100, 100, 255), anchor="lm")
draw_up_arrow(col_server + 55, y - 5, y - row_height + 25)

# Layer 4: TCP + Data
y -= row_height
draw_packet(col_server, y, [("TCP", 35, TCP_COLOR), ("Daten", 80, HTTP_COLOR)], "", "")
draw.text((col_server + 130, y + 11), "4", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((col_server + 145, y + 11), "-TCP-Header", font=font_text, fill=(100, 100, 100, 255), anchor="lm")
draw_up_arrow(col_server + 60, y - 5, y - row_height + 25)

# Layer 7: HTTP Data
y -= row_height
draw_packet(col_server + 20, y, [("HTTP-Daten", 100, HTTP_COLOR)], "", "")
draw.text((col_server + 135, y + 11), "7", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((col_server + 150, y + 11), "Daten lesen", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Legend at bottom
legend_y = HEIGHT - 35
legend_x = 40
draw.text((legend_x, legend_y), "Legende:", font=font_label, fill=TEXT_DARK, anchor="lm")

items = [
    ("Daten", HTTP_COLOR),
    ("TCP", TCP_COLOR),
    ("IP", IP_COLOR),
    ("Eth", ETH_COLOR),
    ("FCS", FCS_COLOR),
]
lx = legend_x + 60
for name, color in items:
    draw.rectangle([lx, legend_y - 8, lx + 30, legend_y + 8], fill=color, outline=BORDER_COLOR, width=1)
    draw.text((lx + 15, legend_y), name, font=font_small, fill=TEXT_LIGHT, anchor="mm")
    lx += 45

# Info text
draw.text((WIDTH - 40, legend_y), "IP-Adressen bleiben unverändert, nur MAC-Adressen ändern sich", 
          font=font_small, fill=(100, 100, 100, 255), anchor="rm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/datenfluss_draft.png", "PNG")
print(f"Created: {output_dir}/datenfluss_draft.png")
