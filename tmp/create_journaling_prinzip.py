#!/usr/bin/env python3
"""
Creates a journaling principle diagram comparing with/without journaling
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(13, 9))

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
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6.5, 8.5, 'Journaling-Prinzip: Write-Ahead Logging', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== LEFT SIDE: WITHOUT JOURNALING =====
left_x = 0.5

ax.text(left_x + 2.3, 7.8, 'OHNE Journaling', fontsize=14, fontweight='bold',
        color=danger_color, ha='center', va='center')

# Filesystem box (without journal)
fs_left = FancyBboxPatch((left_x, 3.5), 4.5, 3.5,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#4A5568', edgecolor=fs_color,
                          linewidth=2)
ax.add_patch(fs_left)
ax.text(left_x + 2.25, 6.7, 'Dateisystem', fontsize=12, fontweight='bold',
        color=fs_color, ha='center', va='center')

# Show data being written
ax.text(left_x + 2.25, 5.8, 'Daten werden', fontsize=10, color=text_color,
        ha='center', va='center')
ax.text(left_x + 2.25, 5.4, 'direkt geschrieben', fontsize=10, color=text_color,
        ha='center', va='center')

# Crash indicator
crash_box = FancyBboxPatch((left_x + 0.8, 4.2), 2.9, 0.8,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#9B2C2C', edgecolor=danger_color,
                            linewidth=2, alpha=0.8)
ax.add_patch(crash_box)
ax.text(left_x + 2.25, 4.6, '⚡ CRASH', fontsize=11, fontweight='bold',
        color='#1A202C', ha='center', va='center')

# Result: Inconsistent
result_left = FancyBboxPatch((left_x, 1.5), 4.5, 1.5,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FED7D7', edgecolor=danger_color,
                              linewidth=2)
ax.add_patch(result_left)
ax.text(left_x + 2.25, 2.5, 'Inkonsistent!', fontsize=12, fontweight='bold',
        color=danger_color, ha='center', va='center')
ax.text(left_x + 2.25, 1.9, 'fsck nötig (Stunden)', fontsize=10, color=text_color,
        ha='center', va='center')

# Arrow down
arrow_left = FancyArrowPatch((left_x + 2.25, 3.5), (left_x + 2.25, 3.0),
                              arrowstyle='->', mutation_scale=15,
                              color=danger_color, linewidth=2)
ax.add_patch(arrow_left)

# ===== RIGHT SIDE: WITH JOURNALING =====
right_x = 7

ax.text(right_x + 2.75, 7.8, 'MIT Journaling', fontsize=14, fontweight='bold',
        color=success_color, ha='center', va='center')

# Step 1: Journal
journal_box = FancyBboxPatch((right_x, 6.0), 5.5, 1.5,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#4A5568', edgecolor=journal_color,
                              linewidth=2)
ax.add_patch(journal_box)
ax.text(right_x + 2.75, 7.1, '1. Journal', fontsize=11, fontweight='bold',
        color=journal_color, ha='center', va='center')
ax.text(right_x + 2.75, 6.5, 'Änderungen protokollieren', fontsize=10, color=text_color,
        ha='center', va='center')

# Step number
step1_circle = plt.Circle((right_x - 0.3, 6.75), 0.25, color=journal_color, fill=True)
ax.add_patch(step1_circle)
ax.text(right_x - 0.3, 6.75, '1', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')

# Arrow to commit
arrow_commit = FancyArrowPatch((right_x + 2.75, 6.0), (right_x + 2.75, 5.5),
                                arrowstyle='->', mutation_scale=12,
                                color=journal_color, linewidth=2)
ax.add_patch(arrow_commit)
ax.text(right_x + 4.0, 5.75, '2. Commit', fontsize=9, color=journal_color,
        ha='left', va='center', fontweight='bold')

# Step 2: Filesystem
fs_right = FancyBboxPatch((right_x, 3.5), 5.5, 2.2,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=fs_color,
                           linewidth=2)
ax.add_patch(fs_right)
ax.text(right_x + 2.75, 5.3, '3. Dateisystem', fontsize=11, fontweight='bold',
        color=fs_color, ha='center', va='center')
ax.text(right_x + 2.75, 4.8, 'Änderungen anwenden', fontsize=10, color=text_color,
        ha='center', va='center')

# Crash indicator (same style as left side, centered below text)
crash_box2 = FancyBboxPatch((right_x + 1.3, 3.8), 2.9, 0.8,
                             boxstyle="round,pad=0.01,rounding_size=0.05",
                             facecolor='#9B2C2C', edgecolor=danger_color,
                             linewidth=2, alpha=0.8)
ax.add_patch(crash_box2)
ax.text(right_x + 2.75, 4.2, '⚡ CRASH', fontsize=11, fontweight='bold',
        color='#1A202C', ha='center', va='center')

# Arrow to recovery
arrow_recover = FancyArrowPatch((right_x + 2.75, 3.5), (right_x + 2.75, 2.8),
                                 arrowstyle='->', mutation_scale=12,
                                 color=success_color, linewidth=2)
ax.add_patch(arrow_recover)
ax.text(right_x + 4.0, 3.15, '4. Replay', fontsize=9, color=success_color,
        ha='left', va='center', fontweight='bold')

# Result: Recovery
result_right = FancyBboxPatch((right_x, 1.5), 5.5, 1.1,
                               boxstyle="round,pad=0.02,rounding_size=0.1",
                               facecolor='#C6F6D5', edgecolor=success_color,
                               linewidth=2)
ax.add_patch(result_right)
ax.text(right_x + 2.75, 2.1, '✓ Wiederherstellung (Sekunden)', fontsize=11, fontweight='bold',
        color='#1A202C', ha='center', va='center')

# ===== Bottom explanation =====
info_box = FancyBboxPatch((0.3, 0.2), 12.4, 1.0,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=border_color,
                           linewidth=1.5, alpha=0.9)
ax.add_patch(info_box)

ax.text(0.6, 0.85, 'Recovery:', fontsize=10, fontweight='bold', 
        color=title_color, ha='left', va='center')
ax.text(1.7, 0.85, 'Journal lesen → unfertige Transaktionen finden →', fontsize=9, 
        color=text_color, ha='left', va='center')

ax.text(0.6, 0.45, 'Vor Commit:', fontsize=9, fontweight='bold', 
        color=danger_color, ha='left', va='center')
ax.text(1.8, 0.45, 'Verwerfen (undo)', fontsize=9, color=text_color,
        ha='left', va='center')

ax.text(4.5, 0.45, '|', fontsize=10, color=border_color, ha='center', va='center')

ax.text(5.0, 0.45, 'Nach Commit:', fontsize=9, fontweight='bold', 
        color=success_color, ha='left', va='center')
ax.text(6.5, 0.45, 'Wiederholen (redo)', fontsize=9, color=text_color,
        ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/journaling-prinzip.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created journaling-prinzip.png")
