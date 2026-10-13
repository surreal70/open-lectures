#!/usr/bin/env python3
"""
Creates a Copy-on-Write (COW) comparison diagram for 04-Journaling.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(12, 7))

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

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 6.5, 'Copy-on-Write (COW)', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Traditional (In-Place Update) =====
trad_y = 5.0
ax.text(1.5, trad_y + 0.7, 'Traditionell (In-Place Update):', fontsize=11, fontweight='bold',
        color=text_color, ha='left', va='center')

# Block X with old data
block_old = FancyBboxPatch((1.0, trad_y - 0.4), 2.0, 0.8,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#FED7D7', edgecolor=old_color,
                            linewidth=2)
ax.add_patch(block_old)
ax.text(2.0, trad_y + 0.25, 'Block X:', fontsize=9, color=old_color,
        ha='center', va='center', fontweight='bold')
ax.text(2.0, trad_y - 0.1, 'alte Daten', fontsize=9, color='#9B2C2C',
        ha='center', va='center')

# Arrow
ax.annotate('', xy=(4.5, trad_y), xytext=(3.2, trad_y),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Block X with new data (overwritten)
block_new_trad = FancyBboxPatch((4.5, trad_y - 0.4), 2.0, 0.8,
                                 boxstyle="round,pad=0.01,rounding_size=0.05",
                                 facecolor='#C6F6D5', edgecolor=new_color,
                                 linewidth=2)
ax.add_patch(block_new_trad)
ax.text(5.5, trad_y + 0.25, 'Block X:', fontsize=9, color=new_color,
        ha='center', va='center', fontweight='bold')
ax.text(5.5, trad_y - 0.1, 'neue Daten', fontsize=9, color='#276749',
        ha='center', va='center')

ax.text(5.5, trad_y - 0.7, '(überschrieben)', fontsize=8, color=text_color,
        ha='center', va='center', style='italic')

# ===== Copy-on-Write =====
cow_y = 2.5
ax.text(1.5, cow_y + 1.5, 'Copy-on-Write:', fontsize=11, fontweight='bold',
        color=title_color, ha='left', va='center')

cow_box_y = cow_y - 0.2
box_width = 2.2
box_height = 1.2

# Block X - alte Daten (bleibt)
block_x_cow = FancyBboxPatch((0.5, cow_box_y), box_width, box_height,
                              boxstyle="round,pad=0.01,rounding_size=0.05",
                              facecolor='#FED7D7', edgecolor=old_color,
                              linewidth=2)
ax.add_patch(block_x_cow)
ax.text(0.5 + box_width/2, cow_box_y + 0.85, 'Block X:', fontsize=9, color=old_color,
        ha='center', va='center', fontweight='bold')
ax.text(0.5 + box_width/2, cow_box_y + 0.5, 'alte Daten', fontsize=9, color='#9B2C2C',
        ha='center', va='center')
ax.text(0.5 + box_width/2, cow_box_y + 0.15, '(bleibt)', fontsize=8, color=text_color,
        ha='center', va='center', style='italic')

# Arrow 1
ax.annotate('', xy=(3.0, cow_box_y + box_height/2), xytext=(2.7, cow_box_y + box_height/2),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Block Y - neue Daten (neu geschrieben)
block_y_x = 3.2
block_y_cow = FancyBboxPatch((block_y_x, cow_box_y), box_width, box_height,
                              boxstyle="round,pad=0.01,rounding_size=0.05",
                              facecolor='#C6F6D5', edgecolor=new_color,
                              linewidth=2)
ax.add_patch(block_y_cow)
ax.text(block_y_x + box_width/2, cow_box_y + 0.85, 'Block Y:', fontsize=9, color=new_color,
        ha='center', va='center', fontweight='bold')
ax.text(block_y_x + box_width/2, cow_box_y + 0.5, 'neue Daten', fontsize=9, color='#276749',
        ha='center', va='center')
ax.text(block_y_x + box_width/2, cow_box_y + 0.15, '(neu geschrieben)', fontsize=8, color=text_color,
        ha='center', va='center', style='italic')

# Arrow 2
ax.annotate('', xy=(5.7, cow_box_y + box_height/2), xytext=(5.4, cow_box_y + box_height/2),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Pointer Box
pointer_x = 5.9
pointer_box = FancyBboxPatch((pointer_x, cow_box_y), box_width + 0.5, box_height,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#4A5568', edgecolor=pointer_color,
                              linewidth=2)
ax.add_patch(pointer_box)
ax.text(pointer_x + (box_width + 0.5)/2, cow_box_y + 0.85, 'Pointer:', fontsize=9, color=pointer_color,
        ha='center', va='center', fontweight='bold')
ax.text(pointer_x + (box_width + 0.5)/2, cow_box_y + 0.45, 'X → Y', fontsize=11, color='#1A202C',
        ha='center', va='center', family='monospace')

# "atomar aktualisiert" below pointer box
ax.text(pointer_x + (box_width + 0.5)/2, cow_box_y - 0.35, '(atomar aktualisiert)', 
        fontsize=9, color=text_color, ha='center', va='center', style='italic')

# Advantages and Disadvantages removed - will be in markdown table

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/copy-on-write.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created copy-on-write.png")
