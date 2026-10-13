#!/usr/bin/env python3
"""
Mount Concept Diagram
Shows: Before and After mounting a filesystem
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Theme-agnostic colors (work on dark and light backgrounds)
# Using colors with good contrast in both modes
text_color = '#4A5568'       # Medium gray for text (works on both)
title_color = '#2B6CB0'      # Medium blue for titles
border_color = '#718096'     # Gray for borders
highlight_bg = '#E2E8F0'     # Light gray with some opacity for boxes
journal_color = '#805AD5'    # Purple for journal
disk_color = '#3182CE'       # Blue for disk
metadata_color = '#DD6B20'   # Orange for metadata  
data_color = '#38A169'       # Green for data
success_color = '#38A169'    # Green for success
warning_color = '#DD6B20'    # Orange for warnings
danger_color = '#E53E3E'     # Red for danger
old_color = '#E53E3E'        # Red for old data
new_color = '#38A169'        # Green for new data
pointer_color = '#805AD5'    # Purple for pointer
fs_color = '#3182CE'         # Blue for filesystem
commit_color = '#38A169'     # Green for commit
desc_color = '#DD6B20'       # Orange for descriptor
# Script-specific colors
dir_color = '#3182CE'        # Blue for directories
mount_color = '#38A169'      # Green for mount points
device_color = '#DD6B20'     # Orange for devices
usb_color = '#E53E3E'        # Red for USB

fig, axes = plt.subplots(1, 2, figsize=(14, 9), facecolor='none')

# ============ LEFT: Before Mount ============
ax1 = axes[0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 11)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

ax1.text(5, 10.3, 'Vor dem Mount', ha='center', va='center',
         fontsize=16, color=text_color, fontweight='bold')

# Main tree
def draw_tree_node(ax, x, y, label, color=dir_color, is_empty=False):
    box = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8,
                         boxstyle="round,pad=0.03,rounding_size=0.1",
                         facecolor=color, edgecolor=text_color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, color='#1A202C', fontweight='bold')
    if is_empty:
        ax.text(x, y-0.6, '(leer)', ha='center', va='top', fontsize=8, color=text_color, style='italic')

# Root tree before
nodes_before = [
    ('/', 5, 9),
    ('home', 2, 7),
    ('etc', 5, 7),
    ('mnt', 8, 7),
    ('user', 2, 5),
    ('usb', 8, 5),
]
edges_before = [('/', 'home'), ('/', 'etc'), ('/', 'mnt'), ('home', 'user'), ('mnt', 'usb')]

for label, x, y in nodes_before:
    is_empty = label == 'usb'
    draw_tree_node(ax1, x, y, label, is_empty=is_empty)

for parent, child in edges_before:
    px, py = [(x, y) for l, x, y in nodes_before if l == parent][0]
    cx, cy = [(x, y) for l, x, y in nodes_before if l == child][0]
    ax1.plot([px, cx], [py - 0.4, cy + 0.4], color=text_color, linewidth=2)

# USB Stick (separate)
usb_box = FancyBboxPatch((1, 0.5), 4, 2.5,
                         boxstyle="round,pad=0.1,rounding_size=0.2",
                         facecolor='#4A5568', edgecolor=usb_color, linewidth=2)
ax1.add_patch(usb_box)
ax1.text(3, 2.6, 'USB-Stick', ha='center', va='center', fontsize=11, color=usb_color, fontweight='bold')
ax1.text(3, 1.9, '/dev/sdb1', ha='center', va='center', fontsize=9, color=text_color, family='monospace')
ax1.text(2, 1.2, 'doc.txt', ha='left', va='center', fontsize=9, color=mount_color)
ax1.text(2, 0.8, 'foto.jpg', ha='left', va='center', fontsize=9, color=mount_color)

# ============ RIGHT: After Mount ============
ax2 = axes[1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(-1, 11)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

ax2.text(5, 10.3, 'Nach dem Mount', ha='center', va='center',
         fontsize=16, color=text_color, fontweight='bold')

# Same tree but usb has content
nodes_after = [
    ('/', 5, 9, dir_color),
    ('home', 2, 7, dir_color),
    ('etc', 5, 7, dir_color),
    ('mnt', 8, 7, dir_color),
    ('user', 2, 5, dir_color),
    ('usb', 8, 5, mount_color),  # Highlighted as mount point
]

for label, x, y, color in nodes_after:
    box = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8,
                         boxstyle="round,pad=0.03,rounding_size=0.1",
                         facecolor=color, edgecolor=text_color, linewidth=2 if label == 'usb' else 1.5)
    ax2.add_patch(box)
    ax2.text(x, y, label, ha='center', va='center', fontsize=10, color='#1A202C', fontweight='bold')

for parent, child in edges_before:
    px, py = [(x, y) for l, x, y, c in nodes_after if l == parent][0]
    cx, cy = [(x, y) for l, x, y, c in nodes_after if l == child][0]
    ax2.plot([px, cx], [py - 0.4, cy + 0.4], color=text_color, linewidth=2)

# Files under mounted usb
ax2.plot([8, 7], [4.6, 3.8], color=text_color, linewidth=2)
ax2.plot([8, 9], [4.6, 3.8], color=text_color, linewidth=2)
ax2.text(7, 3.4, 'doc.txt', ha='center', va='center', fontsize=9, color=mount_color)
ax2.text(9, 3.4, 'foto.jpg', ha='center', va='center', fontsize=9, color=mount_color)

# Mount command
cmd_box = FancyBboxPatch((1, 0.5), 8, 1.5,
                         boxstyle="round,pad=0.1,rounding_size=0.2",
                         facecolor='#4A5568', edgecolor=mount_color, linewidth=2, alpha=0.9)
ax2.add_patch(cmd_box)
ax2.text(5, 1.5, 'mount /dev/sdb1 /mnt/usb', ha='center', va='center',
         fontsize=12, color=mount_color, fontweight='bold', family='monospace')
ax2.text(5, 0.9, 'USB-Inhalt erscheint unter /mnt/usb/', ha='center', va='center',
         fontsize=9, color=text_color)

# Arrow between diagrams
fig.text(0.5, 0.5, '→', ha='center', va='center', fontsize=40, color=mount_color, fontweight='bold')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/mount-concept.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: mount-concept.png")
