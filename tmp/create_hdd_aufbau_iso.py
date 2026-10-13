#!/usr/bin/env python3
"""
HDD Aufbau Diagram - Isometric 3D View
Shows platter with tracks and sectors in isometric perspective
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon, Wedge, Circle, FancyBboxPatch
import numpy as np

# Colors (theme-agnostic, matching project style)
box_fill = '#3182CE'        # Blue for main components
text_color = '#4A5568'      # Gray for labels
platter_color = '#4A5568'   # Dark gray for platter
platter_edge = '#2D3748'    # Darker for platter edge
track_color = '#718096'     # Lighter gray for tracks
sector_color = '#D69E2E'    # Gold/Yellow for sectors
sector_color_alt = '#ED8936'  # Orange for alternating sector
arm_color = '#2D3748'       # Very dark for arm
spindle_color = '#1A202C'   # Almost black for spindle
head_color = '#E53E3E'      # Red for read/write head

fig, ax = plt.subplots(1, 1, figsize=(12, 10), facecolor='none')
ax.set_xlim(-2, 14)
ax.set_ylim(-2, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Isometric transformation functions
# For isometric view: x stays, y becomes y*cos(30°), z adds to y
iso_angle = 30  # degrees
cos_a = np.cos(np.radians(iso_angle))
sin_a = np.sin(np.radians(iso_angle))

def iso_transform(x, y, z=0):
    """Transform 3D coordinates to isometric 2D"""
    # Isometric projection
    iso_x = x - y * 0.5
    iso_y = y * cos_a + z
    return iso_x, iso_y

def draw_iso_ellipse(ax, cx, cy, cz, rx, ry, color, edge_color=None, alpha=1.0, linewidth=1):
    """Draw an ellipse in isometric view (represents a circle seen from angle)"""
    # For isometric, a circle becomes an ellipse
    # We approximate with polygon points
    theta = np.linspace(0, 2*np.pi, 100)
    x = cx + rx * np.cos(theta)
    y = cy + ry * np.sin(theta)
    
    # Transform to isometric
    iso_points = [iso_transform(xi, yi, cz) for xi, yi in zip(x, y)]
    iso_x = [p[0] for p in iso_points]
    iso_y = [p[1] for p in iso_points]
    
    if edge_color is None:
        edge_color = color
    ax.fill(iso_x, iso_y, facecolor=color, edgecolor=edge_color, 
            linewidth=linewidth, alpha=alpha)
    return iso_x, iso_y

def draw_iso_sector(ax, cx, cy, cz, r_outer, r_inner, angle_start, angle_end, color, alpha=0.8):
    """Draw a sector (pie slice with hole) in isometric view"""
    # Create sector shape
    theta_outer = np.linspace(np.radians(angle_start), np.radians(angle_end), 20)
    theta_inner = np.linspace(np.radians(angle_end), np.radians(angle_start), 20)
    
    # Outer arc
    x_outer = cx + r_outer * np.cos(theta_outer)
    y_outer = cy + r_outer * np.sin(theta_outer)
    
    # Inner arc (reversed)
    x_inner = cx + r_inner * np.cos(theta_inner)
    y_inner = cy + r_inner * np.sin(theta_inner)
    
    # Combine into closed polygon
    x = np.concatenate([x_outer, x_inner])
    y = np.concatenate([y_outer, y_inner])
    
    # Transform to isometric
    iso_points = [iso_transform(xi, yi, cz) for xi, yi in zip(x, y)]
    iso_x = [p[0] for p in iso_points]
    iso_y = [p[1] for p in iso_points]
    
    ax.fill(iso_x, iso_y, facecolor=color, edgecolor='#1A202C', linewidth=0.5, alpha=alpha)

def draw_iso_track(ax, cx, cy, cz, radius, color, linewidth=1, linestyle='--'):
    """Draw a circular track in isometric view"""
    theta = np.linspace(0, 2*np.pi, 100)
    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)
    
    iso_points = [iso_transform(xi, yi, cz) for xi, yi in zip(x, y)]
    iso_x = [p[0] for p in iso_points]
    iso_y = [p[1] for p in iso_points]
    
    ax.plot(iso_x, iso_y, color=color, linewidth=linewidth, linestyle=linestyle, alpha=0.6)

# ============ MAIN PLATTER (Isometric View) ============
platter_cx, platter_cy = 6, 6
platter_radius = 4
platter_thickness = 0.4

# Draw platter edge (side) - creates 3D effect
edge_theta = np.linspace(np.pi, 2*np.pi, 50)  # Bottom half
x_edge_top = platter_cx + platter_radius * np.cos(edge_theta)
y_edge_top = platter_cy + platter_radius * np.sin(edge_theta)
x_edge_bot = platter_cx + platter_radius * np.cos(edge_theta)
y_edge_bot = platter_cy + platter_radius * np.sin(edge_theta)

# Transform edges
edge_top_iso = [iso_transform(x, y, platter_thickness) for x, y in zip(x_edge_top, y_edge_top)]
edge_bot_iso = [iso_transform(x, y, 0) for x, y in zip(x_edge_bot, y_edge_bot)]

# Create side polygon
side_x = [p[0] for p in edge_top_iso] + [p[0] for p in reversed(edge_bot_iso)]
side_y = [p[1] for p in edge_top_iso] + [p[1] for p in reversed(edge_bot_iso)]
ax.fill(side_x, side_y, facecolor=platter_edge, edgecolor=text_color, linewidth=1)

# Draw platter top surface
draw_iso_ellipse(ax, platter_cx, platter_cy, platter_thickness, 
                 platter_radius, platter_radius, platter_color, text_color, linewidth=2)

# Draw tracks (concentric circles)
track_radii = [3.5, 2.9, 2.3, 1.7, 1.1]
for r in track_radii:
    draw_iso_track(ax, platter_cx, platter_cy, platter_thickness + 0.01, r, track_color)

# Draw sectors on outermost track
num_sectors = 8
r_outer = 3.5
r_inner = 2.9

for i in range(num_sectors):
    angle_start = i * (360 / num_sectors) - 90  # Rotate so first sector is at top
    angle_end = (i + 1) * (360 / num_sectors) - 90
    
    # Alternate colors
    color = sector_color if i % 2 == 0 else sector_color_alt
    alpha = 0.9 if i == 1 else 0.6  # Highlight one sector
    
    draw_iso_sector(ax, platter_cx, platter_cy, platter_thickness + 0.02,
                    r_outer, r_inner, angle_start, angle_end, color, alpha)

# Draw sectors on second track (to show pattern continues)
r_outer2 = 2.9
r_inner2 = 2.3
for i in range(num_sectors):
    angle_start = i * (360 / num_sectors) - 90 + 22.5  # Offset slightly
    angle_end = (i + 1) * (360 / num_sectors) - 90 + 22.5
    color = sector_color if i % 2 == 0 else sector_color_alt
    draw_iso_sector(ax, platter_cx, platter_cy, platter_thickness + 0.02,
                    r_outer2, r_inner2, angle_start, angle_end, color, alpha=0.4)

# Spindle hole
draw_iso_ellipse(ax, platter_cx, platter_cy, platter_thickness + 0.03, 
                 0.6, 0.6, spindle_color, text_color, linewidth=1)

# ============ ACTUATOR ARM ============
# Arm coming from bottom-right
arm_base_x, arm_base_y = 11, 2
arm_end_x, arm_end_y = 7.5, 5.5

# Transform arm positions
arm_base_iso = iso_transform(arm_base_x, arm_base_y, platter_thickness + 0.3)
arm_end_iso = iso_transform(arm_end_x, arm_end_y, platter_thickness + 0.3)

# Draw arm
ax.plot([arm_base_iso[0], arm_end_iso[0]], [arm_base_iso[1], arm_end_iso[1]], 
        color=arm_color, linewidth=10, solid_capstyle='round', zorder=10)

# Read/write head
head = Circle(arm_end_iso, 0.25, facecolor=head_color, edgecolor='#1A202C', 
              linewidth=2, zorder=11)
ax.add_patch(head)

# Arm pivot/base (box shape)
pivot_iso = iso_transform(arm_base_x + 0.5, arm_base_y - 0.5, 0)
pivot_box = FancyBboxPatch((pivot_iso[0] - 0.5, pivot_iso[1] - 0.3), 1.2, 2.5,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor=arm_color, edgecolor=text_color, linewidth=1.5)
ax.add_patch(pivot_box)

# ============ LABELS ============
# Title
ax.text(6, 11, 'Festplatten-Aufbau (Isometrische Ansicht)', ha='center', va='center',
        fontsize=16, color=text_color, fontweight='bold')

# Sector label
sector_label_pos = iso_transform(platter_cx + 2.5, platter_cy + 2.5, platter_thickness)
ax.annotate('Sektor', xy=(sector_label_pos[0] + 1, sector_label_pos[1] + 0.8), 
            xytext=(10, 9),
            fontsize=11, color=sector_color, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=sector_color, lw=2))

# Track label
track_label_pos = iso_transform(platter_cx, platter_cy - 2, platter_thickness)
ax.annotate('Spur (Track)', xy=(track_label_pos[0], track_label_pos[1] - 0.3), 
            xytext=(0.5, 3),
            fontsize=11, color=track_color, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=track_color, lw=2))

# Platter label
ax.annotate('Platter\n(Magnetscheibe)', xy=(1.5, 5.5), xytext=(-1, 7),
            fontsize=11, color=text_color, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Head label
ax.annotate('Schreib-/Lesekopf', xy=arm_end_iso, xytext=(9, 8),
            fontsize=11, color=head_color, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=head_color, lw=2))

# Actuator label
ax.annotate('Aktuator-Arm', xy=(arm_base_iso[0], arm_base_iso[1] + 0.5), 
            xytext=(11, 5),
            fontsize=11, color=text_color, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Spindle label
spindle_label_pos = iso_transform(platter_cx, platter_cy, platter_thickness)
ax.annotate('Spindel', xy=spindle_label_pos, xytext=(2, 8.5),
            fontsize=11, color=text_color, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# ============ LEGEND ============
legend_y = -0.5
legend_elements = [
    (2, legend_y, sector_color, 'Sektor (Datenblock)'),
    (6, legend_y, track_color, 'Spur (Track)'),
    (10, legend_y, head_color, 'Schreib-/Lesekopf'),
]

for x, y, color, label in legend_elements:
    rect = mpatches.Rectangle((x - 0.3, y - 0.2), 0.5, 0.4,
                              facecolor=color, edgecolor=text_color, linewidth=1)
    ax.add_patch(rect)
    ax.text(x + 0.5, y, label, ha='left', va='center',
            fontsize=10, color=text_color)

# ============ INFO BOX ============
info_text = "Ein Sektor ist die kleinste\nadressierbare Einheit (512B / 4KB)"
info_box = FancyBboxPatch((9.5, 0.5), 4, 1.2,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#4A5568', edgecolor=sector_color, linewidth=2, alpha=0.9)
ax.add_patch(info_box)
ax.text(11.5, 1.1, info_text, ha='center', va='center',
        fontsize=9, color=text_color, style='italic')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/hdd-aufbau.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: hdd-aufbau.png (Isometric View)")
