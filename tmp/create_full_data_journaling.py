#!/usr/bin/env python3
"""
Creates a full data journaling diagram for 04-Journaling.md
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
ax.text(6, 6.5, 'Full Data Journaling', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

ax.text(6, 6.0, 'Maximale Sicherheit – alle Daten werden geloggt', 
        fontsize=11, color=text_color, ha='center', va='center', style='italic')

# ===== Step 1: Write everything to Journal =====
step1_y = 3.5
step1_height = 2.2

# Journal box
journal_box = FancyBboxPatch((0.5, step1_y - step1_height/2), 4.5, step1_height,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#4A5568', edgecolor=journal_color,
                              linewidth=2)
ax.add_patch(journal_box)

# Step 1 circle
step1_circle = plt.Circle((0.9, step1_y + step1_height/2 - 0.3), 0.25, color=journal_color, fill=True)
ax.add_patch(step1_circle)
ax.text(0.9, step1_y + step1_height/2 - 0.3, '1', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')

ax.text(2.75, step1_y + 0.8, 'Alles ins Journal', fontsize=11, fontweight='bold',
        color=journal_color, ha='center', va='center')

# Transaction content in journal
items = [
    ('TXN Begin', '#9F7AEA'),
    ('Metadaten', metadata_color),
    ('Datenblöcke', data_color),
    ('TXN Commit', '#48BB78'),
]
y_pos = step1_y + 0.3
for text, color in items:
    ax.text(2.75, y_pos, text, fontsize=10, color=color,
            ha='center', va='center')
    y_pos -= 0.4

ax.text(2.75, step1_y - 0.9, 'Journal', fontsize=9, color=text_color,
        ha='center', va='center', style='italic')

# Arrow from step 1 to disk
arrow1 = FancyArrowPatch((5.0, step1_y), (6.5, step1_y),
                          arrowstyle='->', mutation_scale=15,
                          color=journal_color, linewidth=2.5)
ax.add_patch(arrow1)

# ===== Step 2: Checkpoint =====
step2_y = 3.5
checkpoint_box = FancyBboxPatch((6.5, step2_y - 0.8), 5.0, 1.6,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='#4A5568', edgecolor=disk_color,
                                 linewidth=2)
ax.add_patch(checkpoint_box)

# Step 2 circle
step2_circle = plt.Circle((6.9, step2_y + 0.5), 0.25, color=disk_color, fill=True)
ax.add_patch(step2_circle)
ax.text(6.9, step2_y + 0.5, '2', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')

ax.text(9.0, step2_y + 0.5, 'Checkpoint: Übertragen auf Disk', fontsize=10, fontweight='bold',
        color=disk_color, ha='center', va='center')

# Content
ax.text(9.0, step2_y - 0.1, 'Metadaten + Daten', fontsize=10, color=text_color,
        ha='center', va='center')
ax.text(9.0, step2_y - 0.5, '→ Disk (FS-Bereich)', fontsize=10, color=text_color,
        ha='center', va='center')

# ===== Warning box: Write Amplification =====
warning_box = FancyBboxPatch((0.5, 0.8), 11.0, 1.2,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FED7D7', edgecolor=warning_color,
                              linewidth=2)
ax.add_patch(warning_box)

ax.text(6, 1.6, '⚠️  Jedes Byte wird ZWEIMAL geschrieben!', 
        fontsize=12, fontweight='bold', color=warning_color,
        ha='center', va='center')

ax.text(6, 1.1, 'Write Amplification: 2× (oder mehr)', 
        fontsize=10, color=text_color, ha='center', va='center')

# ===== Visual representation of double write =====
# First write (to journal)
write1_box = FancyBboxPatch((1.5, 5.2), 2.0, 0.6,
                             boxstyle="round,pad=0.01,rounding_size=0.05",
                             facecolor='#C6F6D5', edgecolor=data_color,
                             linewidth=1.5)
ax.add_patch(write1_box)
ax.text(2.5, 5.5, 'Daten', fontsize=9, color='#1A202C',
        ha='center', va='center', fontweight='bold')

# Arrow to journal
ax.annotate('', xy=(4.0, 5.5), xytext=(3.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=journal_color, lw=1.5))
ax.text(4.3, 5.5, '1× Journal', fontsize=9, color=journal_color,
        ha='left', va='center')

# Second write (to disk)
write2_box = FancyBboxPatch((7.5, 5.2), 2.0, 0.6,
                             boxstyle="round,pad=0.01,rounding_size=0.05",
                             facecolor='#C6F6D5', edgecolor=data_color,
                             linewidth=1.5)
ax.add_patch(write2_box)
ax.text(8.5, 5.5, 'Daten', fontsize=9, color='#1A202C',
        ha='center', va='center', fontweight='bold')

# Arrow to disk
ax.annotate('', xy=(10.0, 5.5), xytext=(9.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=disk_color, lw=1.5))
ax.text(10.3, 5.5, '2× Disk', fontsize=9, color=disk_color,
        ha='left', va='center')

# Plus sign between
ax.text(6.5, 5.5, '+', fontsize=16, fontweight='bold', color=text_color,
        ha='center', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/full-data-journaling.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created full-data-journaling.png")
