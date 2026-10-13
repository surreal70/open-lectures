#!/usr/bin/env python3
"""
Evolution of Directory Structure
Shows: Flat -> Two-Level -> Hierarchical -> Acyclic Graph
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
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
dir_color = '#3182CE'        # Blue for directory
file_color = '#38A169'       # Green for file
flat_color = '#DD6B20'       # Orange for flat
hier_color = '#805AD5'       # Purple for hierarchical
link_color = '#718096'       # Gray for links

fig, axes = plt.subplots(2, 2, figsize=(14, 10), facecolor='none')

# ============ 1. FLAT (Single Directory) ============
ax1 = axes[0, 0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 9)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

ax1.text(5, 8.3, '1. Flach (Ein Verzeichnis)', ha='center', va='center',
         fontsize=12, color=text_color, fontweight='bold')

# Root directory
root1 = FancyBboxPatch((2, 3), 6, 4,
                       boxstyle="round,pad=0.05,rounding_size=0.2",
                       facecolor='#4A5568', edgecolor=dir_color, linewidth=2)
ax1.add_patch(root1)
ax1.text(5, 6.5, 'Root', ha='center', va='center', fontsize=11, color=dir_color, fontweight='bold')

# Files
files = ['file1.txt', 'file2.txt', 'data.bin', 'prog.exe']
for i, f in enumerate(files):
    ax1.text(3, 5.5 - i * 0.8, f, ha='left', va='center', fontsize=10, color=file_color)

ax1.text(5, 0.5, 'Problem: Namenskollisionen,\nkeine Organisation', ha='center', va='center',
         fontsize=9, color=text_color, style='italic')

# ============ 2. TWO-LEVEL ============
ax2 = axes[0, 1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(-1, 9)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

ax2.text(5, 8.3, '2. Zweistufig (Pro Benutzer)', ha='center', va='center',
         fontsize=12, color=text_color, fontweight='bold')

# Root
root2 = FancyBboxPatch((3.5, 6), 3, 1.2,
                       boxstyle="round,pad=0.05,rounding_size=0.15",
                       facecolor=dir_color, edgecolor=text_color, linewidth=2)
ax2.add_patch(root2)
ax2.text(5, 6.6, 'Root', ha='center', va='center', fontsize=10, color='#1A202C', fontweight='bold')

# User directories
for i, (user, x) in enumerate([('User A', 2), ('User B', 8)]):
    ax2.plot([5, x], [6, 4.5], color=text_color, linewidth=2)
    user_box = FancyBboxPatch((x-1.5, 3), 3, 1.2,
                              boxstyle="round,pad=0.05,rounding_size=0.15",
                              facecolor=dir_color, edgecolor=text_color, linewidth=1.5)
    ax2.add_patch(user_box)
    ax2.text(x, 3.6, user, ha='center', va='center', fontsize=10, color='#1A202C')
    
    # Files
    ax2.text(x, 2.2, 'f1.txt', ha='center', va='center', fontsize=9, color=file_color)
    ax2.text(x, 1.6, 'f2.txt', ha='center', va='center', fontsize=9, color=file_color)

ax2.text(5, 0.5, 'Benutzer isoliert,\naber keine Unterverzeichnisse', ha='center', va='center',
         fontsize=9, color=text_color, style='italic')

# ============ 3. HIERARCHICAL (Tree) ============
ax3 = axes[1, 0]
ax3.set_xlim(-1, 11)
ax3.set_ylim(-1, 9)
ax3.set_aspect('equal')
ax3.axis('off')
ax3.set_facecolor('none')

ax3.text(5, 8.3, '3. Hierarchisch (Baum)', ha='center', va='center',
         fontsize=12, color=text_color, fontweight='bold')

# Tree structure
nodes = {
    '/': (5, 7),
    'home': (2, 5), 'etc': (5, 5), 'usr': (8, 5),
    'user1': (1, 3), 'user2': (3, 3),
    'docs': (1, 1.5)
}
edges = [('/', 'home'), ('/', 'etc'), ('/', 'usr'),
         ('home', 'user1'), ('home', 'user2'),
         ('user1', 'docs')]

for parent, child in edges:
    px, py = nodes[parent]
    cx, cy = nodes[child]
    ax3.plot([px, cx], [py - 0.3, cy + 0.3], color=text_color, linewidth=2)

for name, (x, y) in nodes.items():
    box = FancyBboxPatch((x-0.6, y-0.3), 1.2, 0.6,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=dir_color, edgecolor=text_color, linewidth=1.5)
    ax3.add_patch(box)
    ax3.text(x, y, name, ha='center', va='center', fontsize=9, color='#1A202C')

ax3.text(5, 0.3, 'Standard heute: beliebig tiefe\nVerschachtelung möglich', ha='center', va='center',
         fontsize=9, color=text_color, style='italic')

# ============ 4. ACYCLIC GRAPH (with links) ============
ax4 = axes[1, 1]
ax4.set_xlim(-1, 11)
ax4.set_ylim(-1, 9)
ax4.set_aspect('equal')
ax4.axis('off')
ax4.set_facecolor('none')

ax4.text(5, 8.3, '4. Azyklischer Graph (mit Links)', ha='center', va='center',
         fontsize=12, color=text_color, fontweight='bold')

# Similar tree but with shared node
nodes4 = {
    '/': (5, 7),
    'home': (2, 5), 'usr': (8, 5),
    'alice': (1, 3), 'bob': (3, 3), 'shared': (8, 3),
    'data': (5, 1.5)
}
edges4 = [('/', 'home'), ('/', 'usr'),
          ('home', 'alice'), ('home', 'bob'),
          ('usr', 'shared')]

for parent, child in edges4:
    px, py = nodes4[parent]
    cx, cy = nodes4[child]
    ax4.plot([px, cx], [py - 0.3, cy + 0.3], color=text_color, linewidth=2)

# Links to shared data (dashed)
ax4.plot([1, 5], [2.7, 1.8], color=link_color, linewidth=2, linestyle='--')
ax4.plot([3, 5], [2.7, 1.8], color=link_color, linewidth=2, linestyle='--')
ax4.plot([8, 5], [2.7, 1.8], color=link_color, linewidth=2, linestyle='--')

for name, (x, y) in nodes4.items():
    color = link_color if name == 'data' else dir_color
    box = FancyBboxPatch((x-0.6, y-0.3), 1.2, 0.6,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=color, edgecolor=text_color, linewidth=1.5)
    ax4.add_patch(box)
    ax4.text(x, y, name, ha='center', va='center', fontsize=9, color='#1A202C')

ax4.text(5, 0.3, 'Hard/Soft Links ermöglichen\ngemeinsame Dateien', ha='center', va='center',
         fontsize=9, color=text_color, style='italic')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/verzeichnis-evolution.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: verzeichnis-evolution.png")
