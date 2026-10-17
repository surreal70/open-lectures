#!/usr/bin/env python3
"""
Create paketfluss.png - Complete packet flow from client through router to server.
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

def create_paketfluss():
    width = 800
    height = 550
    
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
    arrow_color = "#4A9EFF"
    router_fill = "#1E3A5F"
    
    # Title
    title = etree.SubElement(root, "text", x=str(width//2), y="30",
                             fill=title_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "16",
                                 "font-weight": "bold",
                                 "text-anchor": "middle"
                             })
    title.text = "KOMPLETTER PAKETFLUSS"
    
    # Main container
    etree.SubElement(root, "rect", x="20", y="50", width="760", height="485",
                     fill=box_fill, stroke=box_stroke, rx="8",
                     attrib={"stroke-width": "2"})
    
    # Column headers
    cols = [
        ("CLIENT", "192.168.1.10", 120),
        ("ROUTER", "192.168.1.1 / 10.0.0.1", 400),
        ("SERVER", "10.0.0.5", 680)
    ]
    
    for name, ip, x in cols:
        txt = etree.SubElement(root, "text", x=str(x), y="80",
                               fill=title_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "13",
                                   "font-weight": "bold",
                                   "text-anchor": "middle"
                               })
        txt.text = name
        
        ip_txt = etree.SubElement(root, "text", x=str(x), y="95",
                                  fill=text_dim, attrib={
                                      "font-family": "monospace",
                                      "font-size": "10",
                                      "text-anchor": "middle"
                                  })
        ip_txt.text = ip
    
    # CLIENT stack
    client_x = 50
    client_y = 115
    layer_height = 45
    layer_width = 140
    
    layers = [
        ("Application", app_color, "HTTP-Request erstellen"),
        ("Transport", transport_color, "+TCP (Port 52345→80)"),
        ("Internet", internet_color, "+IP (→10.0.0.5)"),
        ("Net Access", netaccess_color, "+Eth (AA:AA→BB:BB)")
    ]
    
    for i, (name, color, desc) in enumerate(layers):
        y = client_y + i * layer_height
        
        etree.SubElement(root, "rect", x=str(client_x), y=str(y), 
                         width=str(layer_width), height=str(layer_height - 5),
                         fill=color, stroke="#333333", rx="4",
                         attrib={"fill-opacity": "0.3", "stroke-width": "1"})
        
        txt = etree.SubElement(root, "text", x=str(client_x + 8), y=str(y + 18),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "10",
                                   "font-weight": "bold"
                               })
        txt.text = name
        
        desc_txt = etree.SubElement(root, "text", x=str(client_x + 8), y=str(y + 32),
                                    fill=text_dim, attrib={
                                        "font-family": "monospace",
                                        "font-size": "9"
                                    })
        desc_txt.text = desc
    
    # Arrow: Client -> Router (LAN 1)
    arrow_y = client_y + 4 * layer_height - 20
    etree.SubElement(root, "line", x1=str(client_x + layer_width + 10), y1=str(arrow_y),
                     x2="310", y2=str(arrow_y),
                     stroke=arrow_color, attrib={"stroke-width": "3"})
    etree.SubElement(root, "polygon",
                     points=f"310,{arrow_y-6} 310,{arrow_y+6} 322,{arrow_y}",
                     fill=arrow_color)
    
    lan1_txt = etree.SubElement(root, "text", x="230", y=str(arrow_y - 10),
                                fill=text_dim, attrib={
                                    "font-family": "monospace",
                                    "font-size": "9",
                                    "text-anchor": "middle"
                                })
    lan1_txt.text = "Ethernet LAN 1"
    
    # ROUTER box
    router_x = 330
    router_y = 180
    router_w = 140
    router_h = 120
    
    etree.SubElement(root, "rect", x=str(router_x), y=str(router_y),
                     width=str(router_w), height=str(router_h),
                     fill=router_fill, stroke=box_stroke, rx="6",
                     attrib={"stroke-width": "2"})
    
    # Router layers (only Internet and Net Access)
    router_layers = [
        ("Internet", internet_color, "Routing, TTL--"),
        ("Net Access", netaccess_color, "MAC ändern")
    ]
    
    for i, (name, color, desc) in enumerate(router_layers):
        y = router_y + 15 + i * 50
        
        etree.SubElement(root, "rect", x=str(router_x + 10), y=str(y),
                         width=str(router_w - 20), height="40",
                         fill=color, stroke="#333333", rx="3",
                         attrib={"fill-opacity": "0.3", "stroke-width": "1"})
        
        txt = etree.SubElement(root, "text", x=str(router_x + 18), y=str(y + 16),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "10",
                                   "font-weight": "bold"
                               })
        txt.text = name
        
        desc_txt = etree.SubElement(root, "text", x=str(router_x + 18), y=str(y + 30),
                                    fill=text_dim, attrib={
                                        "font-family": "monospace",
                                        "font-size": "9"
                                    })
        desc_txt.text = desc
    
    # Arrow: Router -> Server (LAN 2)
    etree.SubElement(root, "line", x1=str(router_x + router_w + 10), y1=str(arrow_y),
                     x2="590", y2=str(arrow_y),
                     stroke=arrow_color, attrib={"stroke-width": "3"})
    etree.SubElement(root, "polygon",
                     points=f"590,{arrow_y-6} 590,{arrow_y+6} 602,{arrow_y}",
                     fill=arrow_color)
    
    lan2_txt = etree.SubElement(root, "text", x="540", y=str(arrow_y - 10),
                                fill=text_dim, attrib={
                                    "font-family": "monospace",
                                    "font-size": "9",
                                    "text-anchor": "middle"
                                })
    lan2_txt.text = "Ethernet LAN 2"
    
    # SERVER stack
    server_x = 610
    server_y = 115
    
    server_layers = [
        ("Application", app_color, "HTTP verarbeiten"),
        ("Transport", transport_color, "-TCP"),
        ("Internet", internet_color, "-IP"),
        ("Net Access", netaccess_color, "-Eth (CC:CC)")
    ]
    
    for i, (name, color, desc) in enumerate(server_layers):
        y = server_y + i * layer_height
        
        etree.SubElement(root, "rect", x=str(server_x), y=str(y),
                         width=str(layer_width), height=str(layer_height - 5),
                         fill=color, stroke="#333333", rx="4",
                         attrib={"fill-opacity": "0.3", "stroke-width": "1"})
        
        txt = etree.SubElement(root, "text", x=str(server_x + 8), y=str(y + 18),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "10",
                                   "font-weight": "bold"
                               })
        txt.text = name
        
        desc_txt = etree.SubElement(root, "text", x=str(server_x + 8), y=str(y + 32),
                                    fill=text_dim, attrib={
                                        "font-family": "monospace",
                                        "font-size": "9"
                                    })
        desc_txt.text = desc
    
    # Summary section
    summary_y = 350
    etree.SubElement(root, "line", x1="40", y1=str(summary_y), x2="760", y2=str(summary_y),
                     stroke="#444444", attrib={"stroke-width": "1"})
    
    summary_items = [
        ("Client:", "Vollständige Einkapselung (alle 4 Schichten)", 60),
        ("Router:", "Nur Layer 1-3, IP-Adressen unverändert, MAC-Adressen ändern", 60),
        ("Server:", "Vollständige Entkapselung (alle 4 Schichten)", 60)
    ]
    
    for i, (label, desc, x) in enumerate(summary_items):
        y = summary_y + 25 + i * 22
        
        lbl = etree.SubElement(root, "text", x=str(x), y=str(y),
                               fill="#FFB347", attrib={
                                   "font-family": "monospace",
                                   "font-size": "11",
                                   "font-weight": "bold"
                               })
        lbl.text = label
        
        desc_txt = etree.SubElement(root, "text", x=str(x + 70), y=str(y),
                                    fill=text_color, attrib={
                                        "font-family": "monospace",
                                        "font-size": "11"
                                    })
        desc_txt.text = desc
    
    # Visual flow arrows on left side
    flow_x = 35
    for i in range(3):
        y1 = client_y + i * layer_height + 20
        y2 = y1 + layer_height - 10
        etree.SubElement(root, "line", x1=str(flow_x), y1=str(y1), x2=str(flow_x), y2=str(y2),
                         stroke="#555555", attrib={"stroke-width": "1"})
        etree.SubElement(root, "polygon",
                         points=f"{flow_x-3},{y2} {flow_x+3},{y2} {flow_x},{y2+5}",
                         fill="#555555")
    
    # Legend
    legend_y = 460
    legend_items = [
        (app_color, "Anwendung"),
        (transport_color, "Transport"),
        (internet_color, "Internet"),
        (netaccess_color, "Netzzugang")
    ]
    
    legend_x = 100
    for color, name in legend_items:
        etree.SubElement(root, "rect", x=str(legend_x), y=str(legend_y),
                         width="15", height="15", fill=color, rx="2",
                         attrib={"fill-opacity": "0.3"})
        
        txt = etree.SubElement(root, "text", x=str(legend_x + 22), y=str(legend_y + 12),
                               fill=text_dim, attrib={
                                   "font-family": "monospace",
                                   "font-size": "10"
                               })
        txt.text = name
        
        legend_x += 140
    
    return root, width, height

def main():
    output_dir = Path("/media/andhue/Wissen/open-lectures/.kiro/tmp")
    
    root, width, height = create_paketfluss()
    
    svg_path = output_dir / "paketfluss.svg"
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_to_string(root))
    print(f"Created: {svg_path}")
    
    png_path = output_dir / "paketfluss.png"
    export_png(str(svg_path), str(png_path), width, height)
    print(f"Created: {png_path}")
    
    gray_path = output_dir / "paketfluss_g.png"
    create_grayscale_version(str(png_path), str(gray_path))
    print(f"Created: {gray_path}")

if __name__ == "__main__":
    main()
