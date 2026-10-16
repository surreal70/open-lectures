#!/usr/bin/env python3
"""
Create router-schichten.png - Shows which layers a router processes vs. doesn't process.
"""

from pathlib import Path
from lxml import etree
from PIL import Image
import cairosvg

NSMAP = {None: "http://www.w3.org/2000/svg"}

def create_svg_root(width, height):
    root = etree.Element("svg", nsmap=NSMAP)
    root.set("width", str(width))
    root.set("height", str(height))
    root.set("viewBox", f"0 0 {width} {height}")
    etree.SubElement(root, "rect", x="0", y="0", width=str(width), height=str(height), fill="#1A1A1A")
    return root

def export_png(svg_path, png_path, width, height):
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width, output_height=height)

def create_grayscale_version(color_path, gray_path):
    img = Image.open(color_path)
    if img.mode == 'RGBA':
        gray = img.convert('LA').convert('RGBA')
    else:
        gray = img.convert('L').convert('RGB')
    gray.save(gray_path)

def svg_to_string(root):
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode('utf-8')

def create_router_schichten():
    width = 700
    height = 340
    
    root = create_svg_root(width, height)
    
    # Colors
    title_color = "#E8E8E8"
    text_color = "#CCCCCC"
    box_fill = "#2D2D2D"
    box_stroke = "#4A9EFF"
    not_processed_fill = "#4A4A4A"
    not_processed_pattern = "#666666"
    processed_fill = "#1E5631"
    layer3_fill = "#1E3A5F"
    check_color = "#4ADE80"
    warning_color = "#FFB347"
    
    # Title
    title = etree.SubElement(root, "text", x=str(width//2), y="30",
                             fill=title_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "16",
                                 "font-weight": "bold",
                                 "text-anchor": "middle"
                             })
    title.text = "ROUTER – SCHICHTENVERARBEITUNG"
    
    # Main container
    etree.SubElement(root, "rect", x="20", y="50", width="660", height="275",
                     fill=box_fill, stroke=box_stroke, rx="8",
                     attrib={"stroke-width": "2"})
    
    # Column headers
    col_x = [50, 200, 480]
    headers = ["Schicht", "Verarbeitung", "Status"]
    for i, h in enumerate(headers):
        txt = etree.SubElement(root, "text", x=str(col_x[i]), y="75",
                               fill="#888888", attrib={
                                   "font-family": "monospace",
                                   "font-size": "11"
                               })
        txt.text = h
    
    # Separator line
    etree.SubElement(root, "line", x1="35", y1="85", x2="665", y2="85",
                     stroke="#444444", attrib={"stroke-width": "1"})
    
    # Layers data
    layers = [
        ("Anwendung", not_processed_fill, "░░░░░░░░░░░░░░░░░░░░", "Nicht verarbeitet", False),
        ("Transport", not_processed_fill, "░░░░░░░░░░░░░░░░░░░░", "Nicht verarbeitet", False),
        ("Internet", layer3_fill, "✓ Routing-Entscheidung", "Layer 3", True),
        ("Netzzugang", processed_fill, "✓ MAC-Adressen ändern\n✓ Frame neu aufbauen", "Layer 1-2", True),
    ]
    
    y_start = 100
    row_height = 50
    
    for i, (name, fill, action, status, processed) in enumerate(layers):
        y = y_start + i * row_height
        
        # Row background
        etree.SubElement(root, "rect", x="35", y=str(y), width="630", height=str(row_height - 5),
                         fill=fill, stroke="#444444", rx="4",
                         attrib={"stroke-width": "1"})
        
        # Layer name
        txt = etree.SubElement(root, "text", x="50", y=str(y + 28),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "13",
                                   "font-weight": "bold"
                               })
        txt.text = name
        
        # Action/description
        if processed:
            lines = action.split('\n')
            for j, line in enumerate(lines):
                txt = etree.SubElement(root, "text", x="200", y=str(y + 22 + j * 16),
                                       fill=check_color, attrib={
                                           "font-family": "monospace",
                                           "font-size": "12"
                                       })
                txt.text = line
        else:
            # Strikethrough pattern for not processed
            txt = etree.SubElement(root, "text", x="200", y=str(y + 28),
                                   fill=not_processed_pattern, attrib={
                                       "font-family": "monospace",
                                       "font-size": "12"
                                   })
            txt.text = action
        
        # Status
        status_color = check_color if processed else "#888888"
        txt = etree.SubElement(root, "text", x="480", y=str(y + 28),
                               fill=status_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "12"
                               })
        txt.text = status
    
    # Note at bottom
    note_y = 270
    etree.SubElement(root, "rect", x="35", y=str(note_y), width="630", height="45",
                     fill="#2A2A2A", stroke=warning_color, rx="4",
                     attrib={"stroke-width": "1"})
    
    note1 = etree.SubElement(root, "text", x="50", y=str(note_y + 18),
                             fill=warning_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "11",
                                 "font-weight": "bold"
                             })
    note1.text = "Router \"sehen\" nicht in TCP-Header oder HTTP-Daten!"
    
    note2 = etree.SubElement(root, "text", x="50", y=str(note_y + 35),
                             fill=text_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "10"
                             })
    note2.text = "(Ausnahme: Deep Packet Inspection bei Firewalls)"
    
    return root, width, height

def main():
    output_dir = Path("/media/andhue/Wissen/open-lectures/.kiro/tmp")
    
    root, width, height = create_router_schichten()
    
    svg_path = output_dir / "router-schichten.svg"
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_to_string(root))
    print(f"Created: {svg_path}")
    
    png_path = output_dir / "router-schichten.png"
    export_png(str(svg_path), str(png_path), width, height)
    print(f"Created: {png_path}")
    
    gray_path = output_dir / "router-schichten_g.png"
    create_grayscale_version(str(png_path), str(gray_path))
    print(f"Created: {gray_path}")

if __name__ == "__main__":
    main()
