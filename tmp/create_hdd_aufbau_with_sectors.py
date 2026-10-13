#!/usr/bin/env python3
"""
HDD Aufbau Diagram with Sectors Visualization
Shows platter structure with tracks and sectors highlighted
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Wedge, Circle, FancyArrowPatch, Arc
import numpy as np

# Colors (theme-agnostic, matching project style)
box_fill = '#3182CE'        # Blue for main components
box_text = '#E2E8F0'        # Light text on blue
text_color = '#4A5568'      # Gray for labels
platter_color = '#4A5568'   # Dark gray for platter
track_color = '#718096'     # Lighter gray for tracks
sector_color = '#D69E2E'    # Gold/Yellow for sectors (distinct!)
sector_color_alt = '#ED8936'  # Orange for alternating sector
arm_color = '#2D3748'       # Very dark for arm
spindle_color = '#1A202C'   # Almost black for spindle
head_color = '#E53E3E'      # Red for read/write head

fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor='none')

# ============ LEFT: Top View (Draufsicht) ============
ax1 = axes[0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 11)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

# Title for left panel
ax1.text(5, 10.3, 'Draufsicht', ha='center', va='center',
         fontsize=14, color=text_color, fontweight='bold')

# Platter center
platter_center = (5, 5)
platter_radius = 4

# Draw platter (outer disk)
platter = Circle(platter_center, platter_radius, 
                 facecolor=platter_color, edgecolor=text_color, linewidth=2)
ax1.add_patch(platter)

# Draw tracks (concentric circles representing data tracks)
track_radii = [3.6, 3.0, 2.4, 1.8]
for r in track_radii:
    track = Circle(platter_center, r, 
                   facecolor='none', edgecolor=track_color, linewidth=1, linestyle='--', alpha=0.6)
    ax1.add_patch(track)

# Draw sectors on one track (highlighted in gold/orange)
# Sectors are pie-shaped segments - we'll show them on the outer track
num_sectors = 8
sector_track_radius_outer = 3.6
sector_track_radius_inner = 3.0

for i in range(num_sectors):
    angle_start = i * (360 / num_sectors)
    angle_end = (i + 1) * (360 / num_sectors)
    
    # Alternate colors for visibility
    color = sector_color if i % 2 == 0 else sector_color_alt
    alpha = 0.8 if i == 2 else 0.5  # Highlight one sector more
    
    # Create wedge for sector
    wedge = Wedge(platter_center, sector_track_radius_outer, angle_start, angle_end,
                  width=sector_track_radius_outer - sector_track_radius_inner,
                  facecolor=color, edgecolor='#1A202C', linewidth=0.5, alpha=alpha)
    ax1.add_patch(wedge)

# Label for one sector
ax1.annotate('Sektor', xy=(6.8, 7.2), xytext=(8.5, 8.5),
             fontsize=10, color=sector_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=sector_color, lw=1.5))

# Label for track
ax1.annotate('Spur (Track)', xy=(5, 1.4), xytext=(7.5, 0.5),
             fontsize=10, color=track_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=track_color, lw=1.5))

# Spindle (center hole)
spindle = Circle(platter_center, 0.5, 
                 facecolor=spindle_color, edgecolor=text_color, linewidth=1)
ax1.add_patch(spindle)

# Actuator arm (from bottom-left corner)
arm_pivot = (0.5, 0.5)
arm_end = (5.5, 5.3)  # Near center of platter

# Draw arm
ax1.plot([arm_pivot[0], arm_end[0]], [arm_pivot[1], arm_end[1]], 
         color=arm_color, linewidth=8, solid_capstyle='round')

# Read/write head at end of arm
head = Circle(arm_end, 0.25, facecolor=head_color, edgecolor='#1A202C', linewidth=1.5)
ax1.add_patch(head)

# Label for head
ax1.annotate('Schreib-/Lesekopf', xy=arm_end, xytext=(7.5, 3),
             fontsize=10, color=head_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=head_color, lw=1.5))

# Label for actuator
ax1.annotate('Aktuator', xy=(2, 2), xytext=(0.3, 3.5),
             fontsize=10, color=text_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))

# Rotation arrow
arc = Arc(platter_center, 1.5, 1.5, angle=0, theta1=30, theta2=330,
          color=text_color, linewidth=2)
ax1.add_patch(arc)
# Arrow head for rotation
ax1.annotate('', xy=(5.6, 5.6), xytext=(5.4, 5.75),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Label for platter
ax1.text(5, -0.5, 'Platter (Magnetscheibe)', ha='center', va='center',
         fontsize=10, color=text_color, fontweight='bold')

# ============ RIGHT: Side View (Seitenansicht) ============
ax2 = axes[1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(-1, 11)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

# Title for right panel
ax2.text(5, 10.3, 'Seitenansicht (Plattenstapel)', ha='center', va='center',
         fontsize=14, color=text_color, fontweight='bold')

# Draw multiple platters (stacked)
platter_y_positions = [3, 4.5, 6, 7.5]
platter_width = 6
platter_height = 0.3

for i, y in enumerate(platter_y_positions):
    # Platter as ellipse (side view)
    ellipse = mpatches.Ellipse((5, y), platter_width, platter_height,
                               facecolor=platter_color, edgecolor=text_color, linewidth=1.5)
    ax2.add_patch(ellipse)
    
    # Show sectors on edge of platter (as colored segments)
    # Small colored rectangles on the right edge to indicate sectors
    sector_y = y + 0.05
    for s in range(4):
        color = sector_color if s % 2 == 0 else sector_color_alt
        rect = mpatches.Rectangle((7.8, sector_y - 0.1 + s*0.08), 0.15, 0.06,
                                   facecolor=color, edgecolor='none', alpha=0.8)
        ax2.add_patch(rect)

# Spindle (vertical shaft)
spindle_rect = mpatches.Rectangle((4.7, 2), 0.6, 6.5,
                                  facecolor=spindle_color, edgecolor=text_color, linewidth=1)
ax2.add_patch(spindle_rect)

# Actuator arm assembly (multiple arms for each platter surface)
arm_x_start = 9
arm_x_end = 5.5

# Draw arm base
arm_base = mpatches.Rectangle((9, 2), 1.5, 7,
                              facecolor=arm_color, edgecolor=text_color, linewidth=1.5)
ax2.add_patch(arm_base)

# Draw individual arms going to each surface
for y in platter_y_positions:
    # Upper surface arm
    ax2.plot([arm_x_start, arm_x_end], [y + 0.25, y + 0.25], 
             color=arm_color, linewidth=3)
    # Head on upper surface
    head_upper = Circle((arm_x_end, y + 0.25), 0.12, 
                        facecolor=head_color, edgecolor='#1A202C', linewidth=1)
    ax2.add_patch(head_upper)
    
    # Lower surface arm (except for bottom platter)
    if y != platter_y_positions[0]:
        ax2.plot([arm_x_start, arm_x_end], [y - 0.25, y - 0.25], 
                 color=arm_color, linewidth=3)
        head_lower = Circle((arm_x_end, y - 0.25), 0.12,
                           facecolor=head_color, edgecolor='#1A202C', linewidth=1)
        ax2.add_patch(head_lower)

# Labels
ax2.annotate('Aktuator-Arm', xy=(9.5, 8.5), xytext=(7, 9.5),
             fontsize=10, color=text_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))

ax2.annotate('Spindel', xy=(5, 5.2), xytext=(2, 5.5),
             fontsize=10, color=text_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))

ax2.annotate('Köpfe', xy=(5.5, 6.25), xytext=(3, 8),
             fontsize=10, color=head_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=head_color, lw=1.5))

ax2.annotate('Platter\n(4 Scheiben)', xy=(5, 3), xytext=(1.5, 1.5),
             fontsize=10, color=text_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))

# Sector label on side view
ax2.annotate('Sektoren', xy=(8, 6), xytext=(8.5, 6.8),
             fontsize=9, color=sector_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=sector_color, lw=1.5))

# ============ LEGEND ============
# Add a small legend at the bottom
legend_y = 0.3
legend_elements = [
    (1.5, legend_y, sector_color, 'Sektor'),
    (4, legend_y, track_color, 'Spur'),
    (6.5, legend_y, head_color, 'Schreib-/Lesekopf'),
    (9.5, legend_y, platter_color, 'Platter'),
]

for x, y, color, label in legend_elements:
    rect = mpatches.Rectangle((x - 0.3, y - 0.15), 0.4, 0.3,
                              facecolor=color, edgecolor=text_color, linewidth=1)
    ax2.add_patch(rect)
    ax2.text(x + 0.4, y, label, ha='left', va='center',
             fontsize=9, color=text_color)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/hdd-aufbau.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: hdd-aufbau.png with sectors visualization")
