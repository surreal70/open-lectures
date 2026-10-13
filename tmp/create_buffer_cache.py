#!/usr/bin/env python3
"""
Creates a buffer cache diagram for 03-Implementierung.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(12, 9))

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
cache_color = '#38A169'      # Green for cache
kernel_color = '#805AD5'     # Purple for kernel
dirty_color = '#E53E3E'      # Red for dirty
clean_color = '#38A169'      # Green for clean
bg_color = 'none'            # Transparent background

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 8.5, 'Buffer Cache (Page Cache)', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Application Layer =====
app_box = FancyBboxPatch((4, 7.0), 4, 1.0,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#4A5568', edgecolor=app_color,
                          linewidth=2)
ax.add_patch(app_box)
ax.text(6, 7.5, 'Anwendung', fontsize=12, fontweight='bold',
        color=app_color, ha='center', va='center')

# read()/write() arrows
arrow_app_cache = FancyArrowPatch((6, 7.0), (6, 6.0),
                                   arrowstyle='<->', mutation_scale=15,
                                   color=app_color, linewidth=2)
ax.add_patch(arrow_app_cache)
ax.text(6.5, 6.5, 'read() / write()', fontsize=9, color=app_color,
        ha='left', va='center', family='monospace')

# ===== Buffer Cache =====
cache_box = FancyBboxPatch((1.5, 3.5), 9, 2.3,
                            boxstyle="round,pad=0.02,rounding_size=0.15",
                            facecolor='#4A5568', edgecolor=cache_color,
                            linewidth=3)
ax.add_patch(cache_box)
ax.text(6, 5.5, 'Buffer Cache (RAM)', fontsize=12, fontweight='bold',
        color=cache_color, ha='center', va='center')

# Cache blocks
blocks = [
    ('Blk 5', True),   # dirty
    ('Blk 8', False),  # clean
    ('Blk 2', False),  # clean
    ('Blk 99', True),  # dirty
    ('Blk 12', False), # clean
    ('Blk 47', True),  # dirty
]

block_width = 1.3
block_height = 1.1
start_x = 2.0

for i, (label, is_dirty) in enumerate(blocks):
    x = start_x + i * (block_width + 0.15)
    color = dirty_color if is_dirty else clean_color
    
    rect = FancyBboxPatch((x, 3.9), block_width, block_height,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor=bg_color, edgecolor=color,
                          linewidth=2)
    ax.add_patch(rect)
    
    ax.text(x + block_width/2, 4.55, label, fontsize=9, color='#1A202C',
            ha='center', va='center', fontweight='bold')
    
    status = 'dirty' if is_dirty else 'clean'
    ax.text(x + block_width/2, 4.15, status, fontsize=8, color=color,
            ha='center', va='center', style='italic')

# ===== Disk =====
disk_box = FancyBboxPatch((2.5, 0.8), 7, 1.2,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=disk_color,
                           linewidth=2)
ax.add_patch(disk_box)
ax.text(6, 1.4, 'Festplatte / SSD', fontsize=12, fontweight='bold',
        color=disk_color, ha='center', va='center')

# Arrows between cache and disk
# Cache Miss arrow (left)
arrow_miss = FancyArrowPatch((3.0, 3.5), (3.0, 2.0),
                              arrowstyle='<-', mutation_scale=15,
                              color=disk_color, linewidth=2)
ax.add_patch(arrow_miss)
ax.text(3.6, 2.75, 'Cache Miss', fontsize=9, color='#718096',
        ha='left', va='center', style='italic')

# Write-Back arrow (center)
arrow_writeback = FancyArrowPatch((6, 3.5), (6, 2.0),
                                   arrowstyle='->', mutation_scale=15,
                                   color=dirty_color, linewidth=2)
ax.add_patch(arrow_writeback)
ax.text(6.5, 2.75, 'Write-Back', fontsize=9, color=dirty_color,
        ha='left', va='center', fontweight='bold')

# Cache Miss arrow (right)
arrow_miss2 = FancyArrowPatch((9.0, 3.5), (9.0, 2.0),
                               arrowstyle='<-', mutation_scale=15,
                               color=disk_color, linewidth=2)
ax.add_patch(arrow_miss2)
ax.text(9.5, 2.75, 'Cache Miss', fontsize=9, color='#718096',
        ha='left', va='center', style='italic')

# ===== Legend =====
legend_box = FancyBboxPatch((0.3, 0.1), 5.0, 0.55,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=border_color,
                             linewidth=1.5)
ax.add_patch(legend_box)

# Dirty legend
rect_dirty = Rectangle((0.5, 0.25), 0.35, 0.25,
                         facecolor=bg_color, edgecolor=dirty_color, linewidth=2)
ax.add_patch(rect_dirty)
ax.text(1.0, 0.38, 'dirty = modifiziert', fontsize=9, color=text_color,
        ha='left', va='center')

# Clean legend
rect_clean = Rectangle((3.0, 0.25), 0.35, 0.25,
                         facecolor=bg_color, edgecolor=clean_color, linewidth=2)
ax.add_patch(rect_clean)
ax.text(3.5, 0.38, 'clean', fontsize=9, color=text_color,
        ha='left', va='center')

# ===== Write Strategies Box =====
strat_box = FancyBboxPatch((5.6, 0.1), 6.1, 0.55,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=border_color,
                            linewidth=1.5)
ax.add_patch(strat_box)

ax.text(5.9, 0.38, 'Strategien:', fontsize=9, fontweight='bold',
        color=title_color, ha='left', va='center')
ax.text(7.0, 0.38, 'Write-Through | Write-Back | Write-Behind', fontsize=8, 
        color=text_color, ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/buffer-cache.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created buffer-cache.png")
