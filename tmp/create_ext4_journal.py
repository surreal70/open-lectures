#!/usr/bin/env python3
"""
Creates an ext4 journal (JBD2) structure diagram for 04-Journaling.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Arc
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
ax.text(6, 6.5, 'EXT4 Journal (JBD2)', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Journal Superblock =====
superblock_box = FancyBboxPatch((0.5, 4.8), 11.0, 1.0,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='#4A5568', edgecolor=journal_color,
                                 linewidth=2)
ax.add_patch(superblock_box)
ax.text(1.0, 5.5, 'Journal Superblock:', fontsize=10, fontweight='bold',
        color=journal_color, ha='left', va='center')
ax.text(6, 5.1, 'Magic Number, Block Size, Max Transactions, First/Last Sequence, ...', 
        fontsize=9, color=text_color, ha='center', va='center', family='monospace')

# ===== Ring Buffer Label =====
ax.text(6, 4.3, 'Journal Blocks (Ring Buffer):', fontsize=10, fontweight='bold',
        color=journal_color, ha='center', va='center')

# ===== Journal Blocks (Ring Buffer) =====
block_width = 1.2
block_height = 1.5
block_y = 1.8  # Moved down
gap = 0.15

blocks = [
    ('Desc', desc_color, 'Descriptor\nBlock'),
    ('Data', data_color, 'Data\nBlock'),
    ('Data', data_color, 'Data\nBlock'),
    ('Commit', commit_color, 'Commit\nBlock'),
    ('Desc', desc_color, 'Descriptor\nBlock'),
    ('Data', data_color, 'Data\nBlock'),
    ('Commit', commit_color, 'Commit\nBlock'),
    ('...', border_color, ''),
]

start_x = 0.5
for i, (label, color, sublabel) in enumerate(blocks):
    x = start_x + i * (block_width + gap)
    
    if label == '...':
        ax.text(x + block_width/2, block_y + block_height/2, '...', 
                fontsize=16, color=text_color, ha='center', va='center')
    else:
        block = FancyBboxPatch((x, block_y), block_width, block_height,
                                boxstyle="round,pad=0.01,rounding_size=0.05",
                                facecolor='#4A5568', edgecolor=color,
                                linewidth=2)
        ax.add_patch(block)
        
        # Label
        text_color_for_block = 'white' if color in [commit_color, desc_color] else text_color
        ax.text(x + block_width/2, block_y + block_height - 0.3, label,
                fontsize=9, fontweight='bold', color=color,
                ha='center', va='center')
        ax.text(x + block_width/2, block_y + 0.5, sublabel,
                fontsize=7, color=text_color,
                ha='center', va='center')

# ===== Ring buffer arrows (showing circular nature) =====
# Curved arrow below the blocks going back to show circular nature (flatter, inverted radius)
arrow_ring = FancyArrowPatch((10.5, block_y - 0.3), (1.0, block_y - 0.3),
                              arrowstyle='->', mutation_scale=12,
                              color=journal_color, linewidth=1.5,
                              connectionstyle="arc3,rad=-0.15")
ax.add_patch(arrow_ring)

# Small vertical lines connecting blocks to the arrow
ax.plot([10.5, 10.5], [block_y, block_y - 0.3], 
        color=journal_color, linewidth=1.5, linestyle=':')
ax.plot([1.0, 1.0], [block_y, block_y - 0.3], 
        color=journal_color, linewidth=1.5, linestyle=':')

# ===== Annotations (moved to top of blocks) =====
# Descriptor annotation - above
ax.annotate('', xy=(0.5 + block_width/2, block_y + block_height + 0.1), 
            xytext=(0.5 + block_width/2, block_y + block_height + 0.7),
            arrowprops=dict(arrowstyle='->', color=desc_color, lw=1.5))
ax.text(0.5 + block_width/2, block_y + block_height + 1.0, 'Welche FS-Blöcke\nin dieser TXN', 
        fontsize=8, color=desc_color, ha='center', va='center')

# Commit annotation - above
commit_x = start_x + 3 * (block_width + gap)
ax.annotate('', xy=(commit_x + block_width/2, block_y + block_height + 0.1), 
            xytext=(commit_x + block_width/2, block_y + block_height + 0.7),
            arrowprops=dict(arrowstyle='->', color=commit_color, lw=1.5))
ax.text(commit_x + block_width/2, block_y + block_height + 1.0, 'TXN\nabgeschlossen', 
        fontsize=8, color=commit_color, ha='center', va='center')

# Ring Buffer explanation removed - will be in markdown table

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/ext4-journal.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created ext4-journal.png")
