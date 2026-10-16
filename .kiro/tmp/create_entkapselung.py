#!/usr/bin/env python3
"""
Create entkapselung.png - Shows decapsulation process on server side.
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

def create_entkapselung():
    width = 750
    height = 580
    
    root = create_svg_root(width, height)
    
    # Colors
    title_color = "#E8E8E8"
    text_color = "#CCCCCC"
    box_fill = "#2D2D2D"
    box_stroke = "#4A9EFF"
    eth_color = "#4A9EFF"
    ip_color = "#9B59B6"
    tcp_color = "#2ECC71"
    http_color = "#F39C12"
    fcs_color = "#E74C3C"
    arrow_color = "#888888"
    removed_color = "#666666"
    
    # Title
    title = etree.SubElement(root, "text", x=str(width//2), y="30",
                             fill=title_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "16",
                                 "font-weight": "bold",
                                 "text-anchor": "middle"
                             })
    title.text = "ENTKAPSELUNG (DECAPSULATION) – SERVER"
    
    # Main container
    etree.SubElement(root, "rect", x="20", y="50", width="710", height="455",
                     fill=box_fill, stroke=box_stroke, rx="8",
                     attrib={"stroke-width": "2"})
    
    # Bits on medium
    bits_y = 75
    bits_txt = etree.SubElement(root, "text", x="40", y=str(bits_y),
                                fill=text_color, attrib={
                                    "font-family": "monospace",
                                    "font-size": "11"
                                })
    bits_txt.text = "Empfangener Frame auf dem Medium:"
    
    bits_line = etree.SubElement(root, "text", x="40", y=str(bits_y + 20),
                                 fill="#888888", attrib={
                                     "font-family": "monospace",
                                     "font-size": "10"
                                 })
    bits_line.text = "0110100101010101010101010101010101010101010101010101010..."
    
    # Frame levels - increased spacing to avoid overlap
    frame_data = [
        # (y, label, segments)
        (120, "Netzzugangsschicht entfernt Ethernet-Header/Trailer", [
            (40, 80, "Eth-Hdr", eth_color, False),
            (120, 80, "IP-Hdr", ip_color, False),
            (200, 80, "TCP-Hdr", tcp_color, False),
            (280, 350, "HTTP-Request", http_color, False),
            (630, 60, "FCS", fcs_color, False),
        ]),
        (220, "Internetschicht entfernt IP-Header", [
            (40, 80, "IP-Hdr", ip_color, True),
            (120, 80, "TCP-Hdr", tcp_color, False),
            (200, 430, "HTTP-Request", http_color, False),
        ]),
        (320, "Transportschicht entfernt TCP-Header", [
            (40, 80, "TCP-Hdr", tcp_color, True),
            (120, 510, "HTTP-Request", http_color, False),
        ]),
        (420, "Anwendungsschicht erhält reine Nutzdaten", [
            (40, 590, "HTTP-Request: \"GET /index.html HTTP/1.1...\"", http_color, False),
        ]),
    ]
    
    for y, label, segments in frame_data:
        # Arrow and label
        arrow_y = y - 25
        
        # Down arrow
        etree.SubElement(root, "line", x1="375", y1=str(arrow_y - 15), x2="375", y2=str(arrow_y + 5),
                         stroke=arrow_color, attrib={"stroke-width": "2"})
        etree.SubElement(root, "polygon", 
                         points=f"370,{arrow_y + 5} 380,{arrow_y + 5} 375,{arrow_y + 12}",
                         fill=arrow_color)
        
        # Label
        lbl = etree.SubElement(root, "text", x="40", y=str(y - 5),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "10"
                               })
        lbl.text = label
        
        # Frame box background
        etree.SubElement(root, "rect", x="35", y=str(y), width="660", height="50",
                         fill="#252525", stroke="#444444", rx="3",
                         attrib={"stroke-width": "1"})
        
        # Segments
        for sx, sw, slabel, scolor, removed in segments:
            fill_opacity = "0.15" if removed else "0.3"
            stroke_style = "5,3" if removed else "none"
            
            rect_attribs = {
                "fill-opacity": fill_opacity,
                "stroke-width": "1"
            }
            if removed:
                rect_attribs["stroke-dasharray"] = stroke_style
            
            etree.SubElement(root, "rect", x=str(sx), y=str(y + 8), width=str(sw), height="35",
                             fill=scolor, stroke=scolor if removed else "#333333", rx="2",
                             attrib=rect_attribs)
            
            txt_color = removed_color if removed else text_color
            txt = etree.SubElement(root, "text", x=str(sx + sw//2), y=str(y + 30),
                                   fill=txt_color, attrib={
                                       "font-family": "monospace",
                                       "font-size": "10",
                                       "text-anchor": "middle"
                                   })
            txt.text = slabel
            
            # Strikethrough for removed
            if removed:
                etree.SubElement(root, "line", x1=str(sx + 5), y1=str(y + 26),
                                 x2=str(sx + sw - 5), y2=str(y + 26),
                                 stroke=removed_color, attrib={"stroke-width": "1"})
    
    # Final result highlight
    final_y = 520
    result = etree.SubElement(root, "text", x=str(width//2), y=str(final_y),
                              fill="#4ADE80", attrib={
                                  "font-family": "monospace",
                                  "font-size": "12",
                                  "font-weight": "bold",
                                  "text-anchor": "middle"
                              })
    result.text = "→ Webserver verarbeitet HTTP-Request"
    
    return root, width, height

def main():
    output_dir = Path("/media/andhue/Wissen/open-lectures/.kiro/tmp")
    
    root, width, height = create_entkapselung()
    
    svg_path = output_dir / "entkapselung.svg"
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_to_string(root))
    print(f"Created: {svg_path}")
    
    png_path = output_dir / "entkapselung.png"
    export_png(str(svg_path), str(png_path), width, height)
    print(f"Created: {png_path}")
    
    gray_path = output_dir / "entkapselung_g.png"
    create_grayscale_version(str(png_path), str(gray_path))
    print(f"Created: {gray_path}")

if __name__ == "__main__":
    main()
