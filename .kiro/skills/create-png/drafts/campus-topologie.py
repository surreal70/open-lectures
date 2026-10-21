#!/usr/bin/env python3
"""
Campus-Topologie-Diagramme für die Musterlösung
Drei Varianten: Full Mesh, Ring, WLAN-Hybrid
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas-Einstellungen
WIDTH = 800
HEIGHT = 500
MARGIN = 80

# Colors
BG_COLOR = (0, 0, 0, 0)
LINE_COLOR = (80, 80, 80, 255)
TEXT_COLOR = (60, 60, 60, 255)
BUILDING_A = (70, 130, 180, 220)
BUILDING_B = (60, 179, 113, 220)
BUILDING_C = (220, 100, 80, 220)
LINK_COLOR = (140, 100, 60, 255)
LINK_REDUNDANT = (100, 160, 100, 255)


def get_fonts():
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        font_title = ImageFont.load_default()
        font_large = font_title
        font_medium = font_title
        font_small = font_title
    return font_title, font_large, font_medium, font_small


def draw_building(draw, x, y, width, height, color, name, subtitle, fonts):
    font_large, font_medium = fonts[1], fonts[2]
    
    # Building box
    draw.rectangle([x, y, x + width, y + height], fill=color, outline=LINE_COLOR, width=3)
    
    # Building name
    draw.text((x + width//2, y + height//2 - 12), name, fill=TEXT_COLOR, font=font_large, anchor="mm")
    draw.text((x + width//2, y + height//2 + 12), subtitle, fill=TEXT_COLOR, font=font_medium, anchor="mm")


def draw_link(draw, x1, y1, x2, y2, color, label, fonts, label_offset=(0, 0)):
    font_small = fonts[3]
    
    # Draw line
    draw.line([(x1, y1), (x2, y2)], fill=color, width=4)
    
    # Draw label at midpoint
    mid_x = (x1 + x2) // 2 + label_offset[0]
    mid_y = (y1 + y2) // 2 + label_offset[1]
    
    # Background for label
    bbox = draw.textbbox((mid_x, mid_y), label, font=font_small, anchor="mm")
    padding = 4
    draw.rectangle([bbox[0]-padding, bbox[1]-padding, bbox[2]+padding, bbox[3]+padding], 
                   fill=(250, 250, 250, 220))
    draw.text((mid_x, mid_y), label, fill=color, font=font_small, anchor="mm")


def create_full_mesh():
    """Variante A: Vollvermaschung (Full Mesh)"""
    img = Image.new('RGBA', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    
    # Title
    draw.text((WIDTH//2, 40), "Variante A: Vollvermaschung (Full Mesh)", 
              fill=TEXT_COLOR, font=fonts[0], anchor="mm")
    
    # Building positions
    bw, bh = 140, 80  # Building width/height
    
    # V-A top left
    ax, ay = 120, 120
    # V-B top right
    bx, by = WIDTH - 120 - bw, 120
    # V-C bottom center
    cx, cy = WIDTH//2 - bw//2, HEIGHT - 100 - bh
    
    # Draw links first (behind buildings)
    # A <-> B
    draw_link(draw, ax + bw, ay + bh//2, bx, by + bh//2, LINK_COLOR, 
              "40G OM4\n150m", fonts, (0, -25))
    
    # A <-> C
    draw_link(draw, ax + bw//2, ay + bh, cx + bw//4, cy, LINK_COLOR,
              "40G OS2\n350m", fonts, (-45, 0))
    
    # B <-> C
    draw_link(draw, bx + bw//2, by + bh, cx + 3*bw//4, cy, LINK_REDUNDANT,
              "40G OM4\n200m", fonts, (45, 0))
    
    # Draw buildings
    draw_building(draw, ax, ay, bw, bh, BUILDING_A, "V-A", "(Geb. A)", fonts)
    draw_building(draw, bx, by, bw, bh, BUILDING_B, "V-B", "(Geb. B)", fonts)
    draw_building(draw, cx, cy, bw, bh, BUILDING_C, "V-C", "(Geb. C)", fonts)
    
    # Legend
    ly = HEIGHT - 35
    draw.text((MARGIN, ly), "● 3 unabhängige Verbindungen  ● Ausfall von 2 Leitungen tolerierbar  ● Höchste Kosten",
              fill=(100, 100, 100, 255), font=fonts[3], anchor="lm")
    
    return img


def create_ring():
    """Variante B: Ring-Topologie"""
    img = Image.new('RGBA', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    
    # Title
    draw.text((WIDTH//2, 40), "Variante B: Ring-Topologie", 
              fill=TEXT_COLOR, font=fonts[0], anchor="mm")
    
    # Building positions (same as full mesh)
    bw, bh = 140, 80
    ax, ay = 120, 120
    bx, by = WIDTH - 120 - bw, 120
    cx, cy = WIDTH//2 - bw//2, HEIGHT - 100 - bh
    
    # Draw links - Ring: A -> B -> C -> A
    # A <-> B
    draw_link(draw, ax + bw, ay + bh//2, bx, by + bh//2, LINK_COLOR, 
              "10G OM3\n150m", fonts, (0, -25))
    
    # A <-> C
    draw_link(draw, ax + bw//2, ay + bh, cx + bw//4, cy, LINK_COLOR,
              "10G OS2\n350m", fonts, (-45, 0))
    
    # B <-> C
    draw_link(draw, bx + bw//2, by + bh, cx + 3*bw//4, cy, LINK_COLOR,
              "10G OM3\n200m", fonts, (45, 0))
    
    # Draw buildings
    draw_building(draw, ax, ay, bw, bh, BUILDING_A, "V-A", "(Geb. A)", fonts)
    draw_building(draw, bx, by, bw, bh, BUILDING_B, "V-B", "(Geb. B)", fonts)
    draw_building(draw, cx, cy, bw, bh, BUILDING_C, "V-C", "(Geb. C)", fonts)
    
    # Ring arrows/flow indicator
    draw.text((WIDTH//2, 95), "Ring: A → B → C → A", fill=(100, 100, 100, 255), 
              font=fonts[2], anchor="mm")
    
    # Legend
    ly = HEIGHT - 35
    draw.text((MARGIN, ly), "● Eine Leitung kann ausfallen  ● STP verhindert Schleifen  ● Günstiger als Mesh",
              fill=(100, 100, 100, 255), font=fonts[3], anchor="lm")
    
    return img


def create_wlan_hybrid():
    """Variante C: WLAN-Hybrid mit Stern und Backup"""
    img = Image.new('RGBA', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    
    # Title
    draw.text((WIDTH//2, 40), "Variante C: WLAN-Hybrid (Stern + Backup)", 
              fill=TEXT_COLOR, font=fonts[0], anchor="mm")
    
    # Building positions
    bw, bh = 140, 80
    ax, ay = 120, 120
    bx, by = WIDTH - 120 - bw, 120
    cx, cy = WIDTH//2 - bw//2, HEIGHT - 100 - bh
    
    # Primary links (solid) - Stern from A
    # A <-> B
    draw_link(draw, ax + bw, ay + bh//2, bx, by + bh//2, LINK_COLOR, 
              "10G OM3\n150m", fonts, (0, -25))
    
    # A <-> C
    draw_link(draw, ax + bw//2, ay + bh, cx + bw//4, cy, LINK_COLOR,
              "10G OS2\n350m", fonts, (-45, 0))
    
    # Backup link (dashed style - we simulate with lighter color and dots)
    # B <-> C as backup
    backup_color = (150, 180, 150, 200)
    draw_link(draw, bx + bw//2, by + bh, cx + 3*bw//4, cy, backup_color,
              "Backup\n(WLAN/LWL)", fonts, (45, 0))
    
    # Draw buildings with WLAN indicators
    draw_building(draw, ax, ay, bw, bh, BUILDING_A, "V-A", "WLAN-Ctrl", fonts)
    draw_building(draw, bx, by, bw, bh, BUILDING_B, "V-B", "WLAN APs", fonts)
    draw_building(draw, cx, cy, bw, bh, BUILDING_C, "V-C", "RZ + WLAN", fonts)
    
    # Legend
    ly = HEIGHT - 35
    draw.text((MARGIN, ly), "● Primär: Stern zu V-A  ● Backup: Ring oder WLAN-Mesh  ● Outdoor-APs möglich",
              fill=(100, 100, 100, 255), font=fonts[3], anchor="lm")
    
    return img


if __name__ == "__main__":
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate all three topologies
    topologies = [
        ("topologie-fullmesh", create_full_mesh),
        ("topologie-ring", create_ring),
        ("topologie-wlan", create_wlan_hybrid),
    ]
    
    for name, create_func in topologies:
        img = create_func()
        output_path = os.path.join(output_dir, f"{name}-draft.png")
        img.save(output_path, "PNG")
        print(f"Saved: {output_path}")
