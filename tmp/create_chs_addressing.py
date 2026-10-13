#!/usr/bin/env python3
"""
CHS Addressing Diagram
Shows Cylinder, Head, Sector addressing concept
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Wedge, Circle, Ellipse, FancyArrowPatch
import numpy as np

# Colors (theme-agnostic, matching project style)
box_fill = '#3182CE'        # Blue for main components
text_color = '#4A5568'      # Gray for labels
platter_color = '#4A5568'   # Dark gray for platter
cylinder_color = '#9F7AEA'  # Purple for cylinder highlight
head_color = '#E53E3E'      # Red for head indicator
sector_color = '#D69E2E'    # Gold for sectors
sector_alt = '#ED8936'      # Orange for alternate sector
track_color = '#718096'     # Gray for tracks
spindle_color = '#1A202C'   # Dark for spindle

fig, axes = plt.subplots(1, 2, figsize=(14, 9), facecolor='none')

# ============ LEFT: Cylinder Concept (3 Platters Side View) ============
ax1 = axes[0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(-2, 12)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

ax1.text(5, 11.3, 'Zylinder (Cylinder)', ha='center', va='center',
         fontsize=14, color=text_color, fontweight='bold')

# Draw 3 platters stacked (vertically aligned)
platter_y_positions = [4, 6, 8]  # y positions moved up
platter_width = 5
platter_height = 0.4

for i, y in enumerate(platter_y_positions):
    # Platter ellipse (all at same x position)
    ellipse = Ellipse((5, y), platter_width, platter_height * 2,
                      facecolor=platter_color, edgecolor=text_color, linewidth=1.5)
    ax1.add_patch(ellipse)
    
    # Track circles on platter (shown as lines in side view)
    # Outer track (cylinder 0)
    ax1.plot([2.8, 7.2], [y, y], 
             color=cylinder_color, linewidth=3, alpha=0.8)
    # Inner track (cylinder 1)
    ax1.plot([3.5, 6.5], [y, y], 
             color=track_color, linewidth=2, linestyle='--', alpha=0.6)
    
    # Label
    ax1.text(0.5, y, f'Platte {i}', ha='right', va='center',
             fontsize=10, color=text_color)

# Vertical lines connecting same track across platters (the "cylinder")
# Left side of outer track
ax1.plot([2.8, 2.8], [platter_y_positions[0], platter_y_positions[-1]], 
         color=cylinder_color, linewidth=2, linestyle=':', alpha=0.8)

# Right side of outer track
ax1.plot([7.2, 7.2], [platter_y_positions[0], platter_y_positions[-1]], 
         color=cylinder_color, linewidth=2, linestyle=':', alpha=0.8)

# Cylinder brace/bracket
ax1.annotate('', xy=(8.5, 8), xytext=(8.5, 4),
             arrowprops=dict(arrowstyle='<->', color=cylinder_color, lw=2))
ax1.text(9.2, 6, 'Zylinder 0\n(alle Spuren mit\ngleichem Radius)', 
         ha='left', va='center', fontsize=9, color=cylinder_color)

# Head indicators
for i, y in enumerate(platter_y_positions):
    # Top surface head
    head_top = Circle((7.5, y + 0.25), 0.15, 
                      facecolor=head_color, edgecolor='#1A202C', linewidth=1)
    ax1.add_patch(head_top)
    # Bottom surface head (except bottom platter)
    if i > 0:
        head_bot = Circle((7.5, y - 0.25), 0.15,
                          facecolor=head_color, edgecolor='#1A202C', linewidth=1)
        ax1.add_patch(head_bot)

# Head label (text above top head, no arrow)
ax1.text(7.5, 9.2, 'Köpfe\n(Heads)', ha='center', va='bottom',
         fontsize=9, color=head_color, fontweight='bold')

# Explanation box (moved down)
info_box = FancyBboxPatch((0.5, -1.2), 9, 1.8,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#4A5568', edgecolor=cylinder_color, linewidth=2, alpha=0.9)
ax1.add_patch(info_box)
ax1.text(5, -0.3, 'Zylinder = Alle Spuren mit gleichem Radius\nauf allen Plattenoberflächen', 
         ha='center', va='center', fontsize=10, color=text_color, style='italic')

# ============ RIGHT: Sector Concept (Top View of Single Platter) ============
ax2 = axes[1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(-2, 12)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

ax2.text(5, 11.3, 'Sektor (Sector)', ha='center', va='center',
         fontsize=14, color=text_color, fontweight='bold')

# Platter
platter_center = (5, 6)
platter_radius = 4

platter = Circle(platter_center, platter_radius,
                 facecolor=platter_color, edgecolor=text_color, linewidth=2)
ax2.add_patch(platter)

# Draw tracks
track_radii = [3.6, 3.0, 2.4, 1.8]
for r in track_radii:
    track = Circle(platter_center, r,
                   facecolor='none', edgecolor=track_color, linewidth=1, linestyle='--', alpha=0.5)
    ax2.add_patch(track)

# Draw sectors on outer track
num_sectors = 8
r_outer = 3.6
r_inner = 3.0

for i in range(num_sectors):
    angle_start = i * (360 / num_sectors)
    angle_end = (i + 1) * (360 / num_sectors)
    
    # Alternate colors, highlight sector 2
    if i == 2:
        color = sector_color
        alpha = 0.95
    elif i % 2 == 0:
        color = sector_color
        alpha = 0.4
    else:
        color = sector_alt
        alpha = 0.4
    
    wedge = Wedge(platter_center, r_outer, angle_start, angle_end,
                  width=r_outer - r_inner,
                  facecolor=color, edgecolor='#1A202C', linewidth=0.5, alpha=alpha)
    ax2.add_patch(wedge)

# Sector numbers
for i in range(num_sectors):
    angle = np.radians(i * (360 / num_sectors) + (360 / num_sectors) / 2)
    r_text = 3.3
    x = platter_center[0] + r_text * np.cos(angle)
    y = platter_center[1] + r_text * np.sin(angle)
    ax2.text(x, y, str(i), ha='center', va='center', fontsize=8, color='#1A202C', fontweight='bold')

# Spindle
spindle = Circle(platter_center, 0.5,
                 facecolor=spindle_color, edgecolor=text_color, linewidth=1)
ax2.add_patch(spindle)

# Label highlighted sector (sector 2 is at angle 90-135 degrees, center ~112.5 deg)
# Calculate actual position of sector 2
sector2_angle = np.radians(2 * (360 / 8) + (360 / 8) / 2)  # center of sector 2
sector2_r = 3.3
sector2_x = platter_center[0] + sector2_r * np.cos(sector2_angle)
sector2_y = platter_center[1] + sector2_r * np.sin(sector2_angle)
ax2.annotate('Sektor 2', xy=(sector2_x, sector2_y), xytext=(9, 9.5),
             fontsize=11, color=sector_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=sector_color, lw=2))

# Label track/spur
ax2.annotate('Spur\n(Track)', xy=(5, 2.4), xytext=(7.5, 1),
             fontsize=10, color=track_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=track_color, lw=1.5))

# CHS Address example box (moved down)
addr_box = FancyBboxPatch((0.5, -1.2), 9, 1.8,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#4A5568', edgecolor=box_fill, linewidth=2, alpha=0.9)
ax2.add_patch(addr_box)
ax2.text(5, -0.3, 'Beispiel-Adresse: (Zylinder=42, Kopf=1, Sektor=7)\n→ Spur 42 auf Oberfläche 1, siebtes Segment', 
         ha='center', va='center', fontsize=10, color=text_color, style='italic')

# ============ LEGEND at very bottom ============
fig.text(0.5, 0.02, '█ Zylinder (gleiche Spur auf allen Platten)   █ Sektor (Datensegment einer Spur)   ● Schreib-/Lesekopf',
         ha='center', va='center', fontsize=10, color=text_color,
         bbox=dict(boxstyle='round', facecolor='#1A202C', edgecolor=text_color, alpha=0.8))

plt.tight_layout()
plt.subplots_adjust(bottom=0.06)
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/chs-adressierung.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: chs-adressierung.png")
