#!/usr/bin/env python3
"""
Hard Links vs Symbolic Links Diagram
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
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
file_color = '#38A169'       # Green for files
link_color = '#805AD5'       # Purple for links
inode_color = '#DD6B20'      # Orange for inodes

fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor='none')

# ============ LEFT: HARD LINK ============
ax1 = axes[0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(0, 11)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

ax1.text(5, 10.3, 'Hard Link', ha='center', va='center',
         fontsize=16, color=text_color, fontweight='bold')

# Directory A
dir_a = FancyBboxPatch((0.5, 7), 4, 2,
                       boxstyle="round,pad=0.05,rounding_size=0.2",
                       facecolor='#4A5568', edgecolor=dir_color, linewidth=2)
ax1.add_patch(dir_a)
ax1.text(2.5, 8.5, 'Verzeichnis A', ha='center', va='center', fontsize=10, color=dir_color)
ax1.text(2.5, 7.7, 'file1 →', ha='center', va='center', fontsize=10, color=text_color)

# Directory B
dir_b = FancyBboxPatch((5.5, 7), 4, 2,
                       boxstyle="round,pad=0.05,rounding_size=0.2",
                       facecolor='#4A5568', edgecolor=dir_color, linewidth=2)
ax1.add_patch(dir_b)
ax1.text(7.5, 8.5, 'Verzeichnis B', ha='center', va='center', fontsize=10, color=dir_color)
ax1.text(7.5, 7.7, 'file2 →', ha='center', va='center', fontsize=10, color=text_color)

# Inode (shared)
inode_box = FancyBboxPatch((3, 4), 4, 1.8,
                           boxstyle="round,pad=0.05,rounding_size=0.2",
                           facecolor=inode_color, edgecolor=text_color, linewidth=2)
ax1.add_patch(inode_box)
ax1.text(5, 5.3, 'Inode 123', ha='center', va='center', fontsize=11, color='#1A202C', fontweight='bold')
ax1.text(5, 4.5, 'Link Count: 2', ha='center', va='center', fontsize=10, color='#1A202C')

# Data blocks
data_box = FancyBboxPatch((3, 1), 4, 2,
                          boxstyle="round,pad=0.05,rounding_size=0.2",
                          facecolor=data_color, edgecolor=text_color, linewidth=2)
ax1.add_patch(data_box)
ax1.text(5, 2.3, 'Datenblöcke', ha='center', va='center', fontsize=11, color='#1A202C', fontweight='bold')
ax1.text(5, 1.5, '(physische Daten)', ha='center', va='center', fontsize=9, color='#1A202C')

# Arrows
ax1.annotate('', xy=(4, 5.8), xytext=(2.5, 7),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))
ax1.annotate('', xy=(6, 5.8), xytext=(7.5, 7),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))
ax1.annotate('', xy=(5, 3), xytext=(5, 4),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Info box - removed text, will be in markdown
# info1 = FancyBboxPatch(...)
# Removed

# ============ RIGHT: SYMBOLIC LINK ============
ax2 = axes[1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(0, 11)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

ax2.text(5, 10.3, 'Symbolic Link (Symlink)', ha='center', va='center',
         fontsize=16, color=text_color, fontweight='bold')

# Directory A
dir_a2 = FancyBboxPatch((0.5, 7), 4, 2,
                        boxstyle="round,pad=0.05,rounding_size=0.2",
                        facecolor='#4A5568', edgecolor=dir_color, linewidth=2)
ax2.add_patch(dir_a2)
ax2.text(2.5, 8.5, 'Verzeichnis A', ha='center', va='center', fontsize=10, color=dir_color)
ax2.text(2.5, 7.7, 'original →', ha='center', va='center', fontsize=10, color=text_color)

# Directory B with symlink
dir_b2 = FancyBboxPatch((5.5, 7), 4, 2,
                        boxstyle="round,pad=0.05,rounding_size=0.2",
                        facecolor='#4A5568', edgecolor=link_color, linewidth=2)
ax2.add_patch(dir_b2)
ax2.text(7.5, 8.5, 'Verzeichnis B', ha='center', va='center', fontsize=10, color=link_color)
ax2.text(7.5, 7.7, 'link →', ha='center', va='center', fontsize=10, color=text_color)

# Symlink file (contains path as text)
symlink_box = FancyBboxPatch((5.5, 4.5), 4, 1.5,
                             boxstyle="round,pad=0.05,rounding_size=0.2",
                             facecolor=link_color, edgecolor=text_color, linewidth=2)
ax2.add_patch(symlink_box)
ax2.text(7.5, 5.5, 'Symlink-Inode', ha='center', va='center', fontsize=10, color='#1A202C', fontweight='bold')
ax2.text(7.5, 4.9, '"/dir_a/original"', ha='center', va='center', fontsize=9, color='#1A202C', family='monospace')

# Inode of original file
inode_box2 = FancyBboxPatch((0.5, 4), 4, 1.8,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor=inode_color, edgecolor=text_color, linewidth=2)
ax2.add_patch(inode_box2)
ax2.text(2.5, 5.3, 'Inode 456', ha='center', va='center', fontsize=11, color='#1A202C', fontweight='bold')
ax2.text(2.5, 4.5, 'Link Count: 1', ha='center', va='center', fontsize=10, color='#1A202C')

# Data blocks
data_box2 = FancyBboxPatch((0.5, 1), 4, 2,
                           boxstyle="round,pad=0.05,rounding_size=0.2",
                           facecolor=data_color, edgecolor=text_color, linewidth=2)
ax2.add_patch(data_box2)
ax2.text(2.5, 2.3, 'Datenblöcke', ha='center', va='center', fontsize=11, color='#1A202C', fontweight='bold')
ax2.text(2.5, 1.5, '(physische Daten)', ha='center', va='center', fontsize=9, color='#1A202C')

# Arrows
ax2.annotate('', xy=(2.5, 5.8), xytext=(2.5, 7),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))
ax2.annotate('', xy=(7.5, 6), xytext=(7.5, 7),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))
ax2.annotate('', xy=(2.5, 3), xytext=(2.5, 4),
             arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Dashed arrow from symlink to original (indirection)
ax2.annotate('', xy=(4.5, 5), xytext=(5.5, 5),
             arrowprops=dict(arrowstyle='->', color=link_color, lw=2, linestyle='--'))

# Info box - removed text, will be in markdown
# info2 = FancyBboxPatch(...)
# Removed

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/hard-vs-soft-links.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: hard-vs-soft-links.png")
