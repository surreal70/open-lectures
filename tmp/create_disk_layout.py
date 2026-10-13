#!/usr/bin/env python3
"""
Disk Layout Diagram
Shows: Boot Block, Superblock, Free Space Mgmt, Inode Table, Data Blocks
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
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
free_color = '#E2E8F0'       # Light gray for free
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
boot_color = '#E53E3E'       # Red for boot
super_color = '#DD6B20'      # Orange for superblock
inode_color = '#805AD5'      # Purple for inodes
data_color = '#38A169'       # Green for data
free_color = '#E2E8F0'       # Light gray for free

fig, ax = plt.subplots(1, 1, figsize=(14, 8), facecolor='none')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-0.5, 10)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(7, 9.3, 'Typisches Disk-Layout', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Main disk representation - horizontal bar divided into sections
disk_y = 6.5
disk_height = 1.8

# Boot Block
boot = FancyBboxPatch((0.5, disk_y), 1.5, disk_height,
                      boxstyle="round,pad=0.02,rounding_size=0.1",
                      facecolor=boot_color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
ax.add_patch(boot)
ax.text(1.25, disk_y + disk_height/2, 'Boot\nBlock', ha='center', va='center',
        fontsize=10, color='#1A202C', fontweight='bold')

# Superblock
super_block = FancyBboxPatch((2, disk_y), 1.5, disk_height,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor=super_color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
ax.add_patch(super_block)
ax.text(2.75, disk_y + disk_height/2, 'Super\nBlock', ha='center', va='center',
        fontsize=10, color='#1A202C', fontweight='bold')

# Free Space Management
free_block = FancyBboxPatch((3.5, disk_y), 2, disk_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor=free_color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
ax.add_patch(free_block)
ax.text(4.5, disk_y + disk_height/2, 'Free Space\nMgmt', ha='center', va='center',
        fontsize=10, color='#1A202C', fontweight='bold')

# Inode Table
inode_block = FancyBboxPatch((5.5, disk_y), 2.5, disk_height,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor=inode_color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
ax.add_patch(inode_block)
ax.text(6.75, disk_y + disk_height/2, 'Inode\nTable', ha='center', va='center',
        fontsize=10, color='#1A202C', fontweight='bold')

# Data Blocks (larger area)
data_block = FancyBboxPatch((8, disk_y), 5, disk_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor=data_color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
ax.add_patch(data_block)
ax.text(10.5, disk_y + disk_height/2, 'Datenblöcke', ha='center', va='center',
        fontsize=12, color='#1A202C', fontweight='bold')

# Descriptions below each section
descriptions = [
    (1.25, 'Bootloader\n(falls bootbar)'),
    (2.75, 'Dateisystem-\nMetadaten'),
    (4.5, 'Bitmap oder\nFree List'),
    (6.75, 'Alle Inodes des\nDateisystems'),
    (10.5, 'Eigentliche\nDateiinhalte'),
]

for x, desc in descriptions:
    # Arrow down
    ax.annotate('', xy=(x, disk_y - 0.3), xytext=(x, disk_y - 0.1),
                arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))
    ax.text(x, disk_y - 1.2, desc, ha='center', va='top',
            fontsize=9, color=text_color)

# Info box at bottom
info_box = FancyBboxPatch((0.5, 0.3), 12.5, 2.8,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#4A5568', edgecolor=text_color, linewidth=1, alpha=0.9)
ax.add_patch(info_box)

# Info text
info_items = [
    (boot_color, 'Boot Block:', 'Enthält Bootloader-Code zum Starten des Systems'),
    (super_color, 'Superblock:', 'Magic Number, Blockgröße, Anzahl Blöcke/Inodes, Mount-Status'),
    (free_color, 'Free Space:', 'Verwaltung freier Blöcke (Bitmap oder verkettete Liste)'),
    (inode_color, 'Inode Table:', 'Feste Anzahl Inodes mit Metadaten und Blockzeigern'),
    (data_color, 'Datenblöcke:', 'Eigentliche Dateiinhalte, nimmt den größten Bereich ein'),
]

for i, (color, label, desc) in enumerate(info_items):
    y = 2.7 - i * 0.5
    # Color indicator
    indicator = Rectangle((1, y - 0.15), 0.3, 0.3, facecolor=color, edgecolor='none')
    ax.add_patch(indicator)
    ax.text(1.5, y, label, ha='left', va='center', fontsize=9, color='#1A202C', fontweight='bold')
    ax.text(4.2, y, desc, ha='left', va='center', fontsize=9, color=text_color)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/disk-layout.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: disk-layout.png")
