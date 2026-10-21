#!/usr/bin/env python3
"""
Campus-Lageplan für die Übung Campus-Verkabelung
Große Gebäudedarstellung mit 1 Pixel = 0.5 Meter
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Maßstab: 1 Pixel = 0.5 Meter (Gebäude werden groß)
SCALE = 0.5  # Meter pro Pixel

# Canvas - angepasst an Achsenlängen (X bis 250m, Y bis 350m)
# Y-Achse: 350m bei 0.5m/px = 700px + Margins
WIDTH = 1300
HEIGHT = 1000
MARGIN_LEFT = 180
MARGIN_TOP = 200
MARGIN_RIGHT = 520
MARGIN_BOTTOM = 80

DRAW_X = MARGIN_LEFT
DRAW_Y = MARGIN_TOP
DRAW_W = WIDTH - MARGIN_LEFT - MARGIN_RIGHT
DRAW_H = HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# Colors
BG_COLOR = (0, 0, 0, 0)
LINE_COLOR = (80, 80, 80, 255)
TEXT_COLOR = (60, 60, 60, 255)
AXIS_COLOR = (100, 100, 100, 255)
BUILDING_A = (70, 130, 180, 220)
BUILDING_B = (60, 179, 113, 220)
BUILDING_C = (220, 100, 80, 220)
TRASSE_COLOR = (140, 100, 60, 255)
VERTEILER_COLOR = (255, 165, 0, 255)
WARNING_COLOR = (200, 60, 60, 255)

def m_to_px(meters):
    return int(meters / SCALE)

def create_campus_lageplan():
    img = Image.new('RGBA', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
        font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font_title = ImageFont.load_default()
        font_large = font_title
        font_medium = font_title
        font_small = font_title
        font_tiny = font_title
    
    # Title
    draw.text((DRAW_X + DRAW_W//2, 90), "CAMPUS-LAGEPLAN", fill=TEXT_COLOR, font=font_title, anchor="mm")
    draw.text((DRAW_X + DRAW_W//2, 145), "Maßstab: 2 Pixel = 1 Meter", fill=(120, 120, 120, 255), font=font_small, anchor="mm")
    
    # Achsenlängen begrenzen auf beschriftete Werte
    x_max_m = 250  # X-Achse bis 250m (Gebäude B endet bei 220m)
    y_max_m = 350  # Y-Achse bis 350m (Gebäude C endet bei 300m)
    
    # X-Achse - nur bis x_max_m, direkt unter der Grafik
    x_axis_y = DRAW_Y + m_to_px(y_max_m) + 15
    x_axis_end = DRAW_X + m_to_px(x_max_m)
    draw.line([(DRAW_X, x_axis_y), (x_axis_end, x_axis_y)], fill=AXIS_COLOR, width=3)
    
    for m in range(0, x_max_m + 1, 50):
        x = DRAW_X + m_to_px(m)
        draw.line([(x, x_axis_y - 6), (x, x_axis_y + 6)], fill=AXIS_COLOR, width=2)
        draw.text((x, x_axis_y + 25), f"{m}", fill=AXIS_COLOR, font=font_tiny, anchor="mm")
    draw.text((x_axis_end + 15, x_axis_y), "[m]", fill=AXIS_COLOR, font=font_small, anchor="lm")
    
    # Y-Achse - nur bis y_max_m
    y_axis_x = DRAW_X - 20
    y_axis_end = DRAW_Y + m_to_px(y_max_m)
    draw.line([(y_axis_x, DRAW_Y), (y_axis_x, y_axis_end)], fill=AXIS_COLOR, width=3)
    
    for m in range(0, y_max_m + 1, 50):
        y = DRAW_Y + m_to_px(m)
        draw.line([(y_axis_x - 6, y), (y_axis_x + 6, y)], fill=AXIS_COLOR, width=2)
        draw.text((y_axis_x - 12, y), f"{m}", fill=AXIS_COLOR, font=font_tiny, anchor="rm")
    draw.text((y_axis_x, DRAW_Y - 15), "[m]", fill=AXIS_COLOR, font=font_small, anchor="mm")
    
    # === GEBÄUDE A (60×30m) bei (30m, 30m) ===
    geb_a_x = DRAW_X + m_to_px(30)
    geb_a_y = DRAW_Y + m_to_px(30)
    geb_a_w = m_to_px(60)
    geb_a_h = m_to_px(30)
    
    draw.rectangle([geb_a_x, geb_a_y, geb_a_x + geb_a_w, geb_a_y + geb_a_h], 
                   fill=BUILDING_A, outline=LINE_COLOR, width=4)
    draw.text((geb_a_x + geb_a_w//2, geb_a_y - 12), "Gebäude A (60×30m)", fill=TEXT_COLOR, font=font_small, anchor="mb")
    
    # Verteiler A bei (50m, 50m)
    hv_x = DRAW_X + m_to_px(50)
    hv_y = DRAW_Y + m_to_px(50)
    hv_size = 24
    draw.rectangle([hv_x - hv_size//2, hv_y - hv_size//2, hv_x + hv_size//2, hv_y + hv_size//2], 
                   fill=VERTEILER_COLOR, outline=LINE_COLOR, width=2)
    draw.text((hv_x, hv_y), "V", fill=(40, 40, 40, 255), font=font_medium, anchor="mm")
    
    # Kreuzung bei (50m, 110m) - 60m unter HV
    kreuzung_x = DRAW_X + m_to_px(50)
    kreuzung_y = DRAW_Y + m_to_px(110)
    
    # === GEBÄUDE B (80×40m) bei (140m, 85m) ===
    geb_b_x = DRAW_X + m_to_px(140)
    geb_b_y = DRAW_Y + m_to_px(85)
    geb_b_w = m_to_px(80)
    geb_b_h = m_to_px(40)
    
    draw.rectangle([geb_b_x, geb_b_y, geb_b_x + geb_b_w, geb_b_y + geb_b_h], 
                   fill=BUILDING_B, outline=LINE_COLOR, width=4)
    draw.text((geb_b_x + geb_b_w//2, geb_b_y - 12), "Gebäude B (80×40m)", fill=TEXT_COLOR, font=font_small, anchor="mb")
    
    # Verteiler B bei (150m, 110m)
    uv_b_x = DRAW_X + m_to_px(150)
    uv_b_y = DRAW_Y + m_to_px(110)
    draw.rectangle([uv_b_x - hv_size//2, uv_b_y - hv_size//2, uv_b_x + hv_size//2, uv_b_y + hv_size//2], 
                   fill=VERTEILER_COLOR, outline=LINE_COLOR, width=2)
    draw.text((uv_b_x, uv_b_y), "V", fill=(40, 40, 40, 255), font=font_medium, anchor="mm")
    
    # === GEBÄUDE C (50×50m) bei (30m, 250m) ===
    geb_c_x = DRAW_X + m_to_px(30)
    geb_c_y = DRAW_Y + m_to_px(250)
    geb_c_w = m_to_px(50)
    geb_c_h = m_to_px(50)
    
    draw.rectangle([geb_c_x, geb_c_y, geb_c_x + geb_c_w, geb_c_y + geb_c_h], 
                   fill=BUILDING_C, outline=LINE_COLOR, width=4)
    draw.text((geb_c_x + geb_c_w//2, geb_c_y - 12), "Gebäude C (50×50m)", fill=TEXT_COLOR, font=font_small, anchor="mb")
    
    # Verteiler C bei (50m, 270m)
    uv_c_x = DRAW_X + m_to_px(50)
    uv_c_y = DRAW_Y + m_to_px(270)
    draw.rectangle([uv_c_x - hv_size//2, uv_c_y - hv_size//2, uv_c_x + hv_size//2, uv_c_y + hv_size//2], 
                   fill=VERTEILER_COLOR, outline=LINE_COLOR, width=2)
    draw.text((uv_c_x, uv_c_y), "V", fill=(40, 40, 40, 255), font=font_medium, anchor="mm")
    
    # === KABELTRASSEN ===
    trasse_width = 8
    
    # T1: HV → Kreuzung = 60m (skaliert angezeigt als 120m in Aufgabe)
    draw.line([(hv_x, hv_y + hv_size//2), (kreuzung_x, kreuzung_y)], fill=TRASSE_COLOR, width=trasse_width)
    draw.text((hv_x + 25, (hv_y + kreuzung_y)//2), "T1: 120m", fill=TRASSE_COLOR, font=font_small, anchor="lm")
    
    # T2: Kreuzung → UV-B = 100m (skaliert angezeigt als 180m)
    draw.line([(kreuzung_x, kreuzung_y), (uv_b_x - hv_size//2, uv_b_y)], fill=TRASSE_COLOR, width=trasse_width)
    draw.text(((kreuzung_x + uv_b_x)//2, kreuzung_y - 20), "T2: 180m", fill=TRASSE_COLOR, font=font_small, anchor="mm")
    
    # T3: Kreuzung → UV-C = 160m (skaliert angezeigt als 280m)
    draw.line([(kreuzung_x, kreuzung_y), (uv_c_x, uv_c_y - hv_size//2)], fill=TRASSE_COLOR, width=trasse_width)
    draw.text((kreuzung_x + 25, (kreuzung_y + uv_c_y)//2), "T3: 280m", fill=TRASSE_COLOR, font=font_small, anchor="lm")
    
    # Kreuzungspunkt
    draw.ellipse([kreuzung_x - 10, kreuzung_y - 10, kreuzung_x + 10, kreuzung_y + 10], 
                 fill=TRASSE_COLOR, outline=LINE_COLOR, width=2)
    
    # === LEGENDE ===
    legend_x = DRAW_X + DRAW_W + 50
    legend_y = DRAW_Y + 20
    legend_w = MARGIN_RIGHT - 140  # Mehr Abstand zum rechten Rand
    legend_h = 560  # Reduziert weil nur noch ein Verteiler-Eintrag
    
    draw.rectangle([legend_x, legend_y, legend_x + legend_w, legend_y + legend_h], 
                   fill=(245, 245, 245, 220), outline=LINE_COLOR, width=3)
    draw.text((legend_x + legend_w//2, legend_y + 35), "LEGENDE", fill=TEXT_COLOR, font=font_large, anchor="mm")
    
    ly = legend_y + 80
    lx = legend_x + 20
    item_h = 55
    
    draw.rectangle([lx, ly, lx + 45, ly + 28], fill=BUILDING_A, outline=LINE_COLOR, width=2)
    draw.text((lx + 55, ly + 14), "A: Verwaltung", fill=TEXT_COLOR, font=font_small, anchor="lm")
    
    ly += item_h
    draw.rectangle([lx, ly, lx + 45, ly + 28], fill=BUILDING_B, outline=LINE_COLOR, width=2)
    draw.text((lx + 55, ly + 14), "B: Produktion", fill=TEXT_COLOR, font=font_small, anchor="lm")
    
    ly += item_h
    draw.rectangle([lx, ly, lx + 45, ly + 28], fill=BUILDING_C, outline=LINE_COLOR, width=2)
    draw.text((lx + 55, ly + 14), "C: Rechenzentrum", fill=TEXT_COLOR, font=font_small, anchor="lm")
    
    ly += item_h
    draw.rectangle([lx + 8, ly, lx + 36, ly + 28], fill=VERTEILER_COLOR, outline=LINE_COLOR, width=2)
    draw.text((lx + 22, ly + 14), "V", fill=(40, 40, 40, 255), font=font_small, anchor="mm")
    draw.text((lx + 55, ly + 14), "Verteiler", fill=TEXT_COLOR, font=font_small, anchor="lm")
    
    ly += item_h
    draw.line([(lx, ly + 14), (lx + 45, ly + 14)], fill=TRASSE_COLOR, width=8)
    draw.text((lx + 55, ly + 14), "Kabeltrasse", fill=TEXT_COLOR, font=font_small, anchor="lm")
    
    ly += item_h
    draw.ellipse([lx + 12, ly + 4, lx + 32, ly + 24], fill=TRASSE_COLOR, outline=LINE_COLOR, width=2)
    draw.text((lx + 55, ly + 14), "Kreuzungspunkt", fill=TEXT_COLOR, font=font_small, anchor="lm")
    
    # Warning
    ly += item_h + 15
    draw.line([(lx, ly), (lx + legend_w - 40, ly)], fill=WARNING_COLOR, width=2)
    ly += 12
    draw.text((lx, ly), "⚡ ACHTUNG:", fill=WARNING_COLOR, font=font_medium, anchor="lt")
    ly += 35
    draw.text((lx, ly), "Gebäude C hat separate", fill=WARNING_COLOR, font=font_small, anchor="lt")
    ly += 28
    draw.text((lx, ly), "Erdung! (Potentialtrennung", fill=WARNING_COLOR, font=font_small, anchor="lt")
    ly += 28
    draw.text((lx, ly), "erforderlich)", fill=WARNING_COLOR, font=font_small, anchor="lt")
    
    return img

if __name__ == "__main__":
    img = create_campus_lageplan()
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "campus-lageplan-draft.png")
    img.save(output_path, "PNG")
    print(f"Saved to {output_path}")
