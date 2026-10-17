#!/usr/bin/env python3
"""
Create pdu.png - PDU (Protocol Data Unit) names per layer.
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

def create_pdu():
    width = 720
    height = 480
    
    root = create_svg_root(width, height)
    
    # Colors
    title_color = "#E8E8E8"
    text_color = "#CCCCCC"
    text_dim = "#888888"
    box_fill = "#2D2D2D"
    box_stroke = "#4A9EFF"
    app_color = "#F39C12"
    transport_color = "#2ECC71"
    internet_color = "#9B59B6"
    netaccess_color = "#4A9EFF"
    bits_color = "#E74C3C"
    
    # Title
    title = etree.SubElement(root, "text", x=str(width//2), y="30",
                             fill=title_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "16",
                                 "font-weight": "bold",
                                 "text-anchor": "middle"
                             })
    title.text = "PDU (Protocol Data Unit) pro Schicht"
    
    # Main container
    etree.SubElement(root, "rect", x="20", y="50", width="680", height="415",
                     fill=box_fill, stroke=box_stroke, rx="8",
                     attrib={"stroke-width": "2"})
    
    # Table headers
    headers = [("DoD-Schicht", 45), ("PDU-Name", 200), ("Enthält", 420)]
    for name, x in headers:
        txt = etree.SubElement(root, "text", x=str(x), y="80",
                               fill=text_dim, attrib={
                                   "font-family": "monospace",
                                   "font-size": "11"
                               })
        txt.text = name
    
    etree.SubElement(root, "line", x1="35", y1="90", x2="685", y2="90",
                     stroke="#444444", attrib={"stroke-width": "1"})
    
    # Table rows
    rows = [
        ("Anwendung", "Daten / Message", "Nutzdaten", app_color),
        ("Transport", "Segment (TCP) / Datagramm (UDP)", "TCP/UDP-Header + Daten", transport_color),
        ("Internet", "Paket / IP-Datagramm", "IP-Header + Segment", internet_color),
        ("Netzzugang", "Frame / Rahmen", "Eth-Header + Paket + FCS", netaccess_color),
        ("(Physikalisch)", "Bits", "0 und 1 auf Medium", bits_color),
    ]
    
    y = 110
    row_height = 35
    for layer, pdu, contains, color in rows:
        # Row background
        etree.SubElement(root, "rect", x="35", y=str(y), width="650", height=str(row_height - 3),
                         fill=color, stroke="none", rx="3",
                         attrib={"fill-opacity": "0.15"})
        
        # Layer name
        txt = etree.SubElement(root, "text", x="45", y=str(y + 22),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "12",
                                   "font-weight": "bold"
                               })
        txt.text = layer
        
        # PDU name
        txt = etree.SubElement(root, "text", x="200", y=str(y + 22),
                               fill=color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "11"
                               })
        txt.text = pdu
        
        # Contains
        txt = etree.SubElement(root, "text", x="420", y=str(y + 22),
                               fill=text_dim, attrib={
                                   "font-family": "monospace",
                                   "font-size": "11"
                               })
        txt.text = contains
        
        y += row_height
    
    # Visual encapsulation diagram
    encap_y = 300
    encap_label = etree.SubElement(root, "text", x="45", y=str(encap_y),
                                   fill=title_color, attrib={
                                       "font-family": "monospace",
                                       "font-size": "12",
                                       "font-weight": "bold"
                                   })
    encap_label.text = "Visuelle Einkapselung:"
    
    # Nested boxes showing encapsulation
    boxes = [
        (45, encap_y + 20, 620, 120, netaccess_color, "Frame"),
        (65, encap_y + 35, 560, 90, internet_color, "Paket"),
        (85, encap_y + 50, 500, 60, transport_color, "Segment"),
        (105, encap_y + 65, 440, 30, app_color, "Daten"),
    ]
    
    for x, y_box, w, h, color, label in boxes:
        etree.SubElement(root, "rect", x=str(x), y=str(y_box), width=str(w), height=str(h),
                         fill=color, stroke=color, rx="4",
                         attrib={"fill-opacity": "0.2", "stroke-width": "2"})
    
    # Labels for visual boxes
    box_labels = [
        (55, encap_y + 130, "Eth", netaccess_color),
        (75, encap_y + 115, "IP", internet_color),
        (95, encap_y + 100, "TCP", transport_color),
        (310, encap_y + 83, "Daten", app_color),
        (605, encap_y + 130, "FCS", netaccess_color),
    ]
    
    for x, y_lbl, text, color in box_labels:
        txt = etree.SubElement(root, "text", x=str(x), y=str(y_lbl),
                               fill=color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "10",
                                   "font-weight": "bold"
                               })
        txt.text = text
    
    return root, width, height

def main():
    output_dir = Path("/media/andhue/Wissen/open-lectures/.kiro/tmp")
    
    root, width, height = create_pdu()
    
    svg_path = output_dir / "pdu.svg"
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_to_string(root))
    print(f"Created: {svg_path}")
    
    png_path = output_dir / "pdu.png"
    export_png(str(svg_path), str(png_path), width, height)
    print(f"Created: {png_path}")
    
    gray_path = output_dir / "pdu_g.png"
    create_grayscale_version(str(png_path), str(gray_path))
    print(f"Created: {gray_path}")

if __name__ == "__main__":
    main()
