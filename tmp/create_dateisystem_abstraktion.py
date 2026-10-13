#!/usr/bin/env python3
"""
Dateisystem Abstraktion Diagram
Shows layers: Application -> Filesystem -> Physical Storage
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
app_color = '#3182CE'        # Blue for application
fs_color = '#805AD5'         # Purple for filesystem
hw_color = '#38A169'         # Green for hardware
arrow_color = '#718096'      # Gray for arrows
storage_color = '#DD6B20'    # Orange for storage

fig, ax = plt.subplots(1, 1, figsize=(12, 9), facecolor='none')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(6, 11.3, 'Dateisystem-Abstraktion', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Layer 1: Application
app_box = FancyBboxPatch((1, 8), 10, 2.5,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         facecolor=app_color, edgecolor=text_color, linewidth=2)
ax.add_patch(app_box)
ax.text(6, 9.7, 'Anwendung', ha='center', va='center',
        fontsize=14, color='#1A202C', fontweight='bold')
ax.text(6, 8.8, 'open("/home/user/doc.txt", O_RDONLY)', ha='center', va='center',
        fontsize=11, color='#1A202C', family='monospace')

# Arrow 1
ax.annotate('', xy=(6, 6.8), xytext=(6, 7.9),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=3))
ax.text(7.5, 7.35, 'Abstraktion', ha='left', va='center',
        fontsize=10, color=text_color, style='italic')

# Layer 2: Filesystem
fs_box = FancyBboxPatch((1, 3.5), 10, 2.5,
                        boxstyle="round,pad=0.05,rounding_size=0.2",
                        facecolor=fs_color, edgecolor=text_color, linewidth=2)
ax.add_patch(fs_box)
ax.text(6, 5.5, 'Dateisystem', ha='center', va='center',
        fontsize=14, color='#1A202C', fontweight='bold')
ax.text(6, 4.8, 'Verzeichnis → Inode → Blöcke', ha='center', va='center',
        fontsize=11, color='#1A202C')

# Sub-boxes in filesystem layer
for i, (label, x) in enumerate([('VFS', 2.5), ('ext4/NTFS', 6), ('Buffer Cache', 9.5)]):
    sub_box = FancyBboxPatch((x-1.2, 3.7), 2.4, 0.6,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#C6F6D5', edgecolor='#1A202C', linewidth=1)
    ax.add_patch(sub_box)
    ax.text(x, 4, label, ha='center', va='center',
            fontsize=9, color='#1A202C')

# Arrow 2
ax.annotate('', xy=(6, 2.3), xytext=(6, 3.4),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=3))
ax.text(7.5, 2.85, 'Abstraktion', ha='left', va='center',
        fontsize=10, color=text_color, style='italic')

# Layer 3: Physical Storage
storage_box = FancyBboxPatch((1, -0.3), 10, 2.3,
                             boxstyle="round,pad=0.05,rounding_size=0.2",
                             facecolor=storage_color, edgecolor=text_color, linewidth=2)
ax.add_patch(storage_box)
ax.text(6, 1.6, 'Physischer Speicher', ha='center', va='center',
        fontsize=14, color='#1A202C', fontweight='bold')

# Block visualization
block_y = 0.3
for i, block in enumerate([4711, 4712, 8823, 9001]):
    bx = 2.5 + i * 2.2
    block_rect = FancyBboxPatch((bx, block_y), 1.8, 0.6,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                facecolor='#C05621', edgecolor='#1A202C', linewidth=1)
    ax.add_patch(block_rect)
    ax.text(bx + 0.9, block_y + 0.3, str(block), ha='center', va='center',
            fontsize=9, color='#1A202C')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/dateisystem-abstraktion.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: dateisystem-abstraktion.png")
