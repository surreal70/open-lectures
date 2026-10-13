#!/usr/bin/env python3
"""
Creates a journal transaction flow diagram for 04-Journaling.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(13, 7))

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
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6.5, 6.5, 'Journal-Transaktion: Ablauf', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Journal Area (Ring Buffer visualization) =====
journal_box = FancyBboxPatch((0.5, 4.2), 12, 2.0,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#4A5568', edgecolor=journal_color,
                              linewidth=2)
ax.add_patch(journal_box)
ax.text(1.0, 5.95, 'Journal (Log Area)', fontsize=12, fontweight='bold',
        color=journal_color, ha='left', va='center')

# Transaction blocks in journal
# TXN Begin
begin_box = FancyBboxPatch((1.0, 4.5), 2.0, 1.2,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#E9D8FD', edgecolor=journal_color,
                            linewidth=2)
ax.add_patch(begin_box)
ax.text(2.0, 5.4, 'TXN', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(2.0, 4.95, 'Begin', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(2.0, 4.55, 'ID=42', fontsize=8, color='#553C9A',
        ha='center', va='center', family='monospace')

# Log Records
log_box = FancyBboxPatch((3.3, 4.5), 5.4, 1.2,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=border_color,
                          linewidth=1.5)
ax.add_patch(log_box)
ax.text(6.0, 5.4, 'Log Records', fontsize=10, fontweight='bold', color=text_color,
        ha='center', va='center')
ax.text(6.0, 4.9, '(geplante Änderungen:', fontsize=9, color='#718096',
        ha='center', va='center')
ax.text(6.0, 4.55, 'Inode, Bitmap, Directory...)', fontsize=9, color='#718096',
        ha='center', va='center')

# TXN Commit
commit_box = FancyBboxPatch((9.0, 4.5), 2.0, 1.2,
                             boxstyle="round,pad=0.01,rounding_size=0.05",
                             facecolor='#C6F6D5', edgecolor=success_color,
                             linewidth=2)
ax.add_patch(commit_box)
ax.text(10.0, 5.4, 'TXN', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(10.0, 4.95, 'Commit', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(10.0, 4.55, 'ID=42', fontsize=8, color='#276749',
        ha='center', va='center', family='monospace')

# Arrows between journal blocks
ax.annotate('', xy=(3.2, 5.1), xytext=(3.05, 5.1),
            arrowprops=dict(arrowstyle='->', color=journal_color, lw=2))
ax.annotate('', xy=(8.9, 5.1), xytext=(8.75, 5.1),
            arrowprops=dict(arrowstyle='->', color=journal_color, lw=2))

# ===== Steps below =====
steps_y = 3.0

# Step 1
step1_box = FancyBboxPatch((0.8, steps_y - 0.6), 2.4, 1.0,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#4A5568', edgecolor=journal_color,
                            linewidth=1.5)
ax.add_patch(step1_box)
step1_circle = plt.Circle((1.1, steps_y + 0.15), 0.22, color=journal_color, fill=True)
ax.add_patch(step1_circle)
ax.text(1.1, steps_y + 0.15, '1', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(2.0, steps_y + 0.15, 'Transaktion', fontsize=9, color=text_color,
        ha='center', va='center')
ax.text(2.0, steps_y - 0.2, 'starten', fontsize=9, color=text_color,
        ha='center', va='center')

# Step 2
step2_box = FancyBboxPatch((3.6, steps_y - 0.6), 2.4, 1.0,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#4A5568', edgecolor=border_color,
                            linewidth=1.5)
ax.add_patch(step2_box)
step2_circle = plt.Circle((3.9, steps_y + 0.15), 0.22, color=border_color, fill=True)
ax.add_patch(step2_circle)
ax.text(3.9, steps_y + 0.15, '2', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(4.8, steps_y + 0.15, 'Änderungen', fontsize=9, color=text_color,
        ha='center', va='center')
ax.text(4.8, steps_y - 0.2, 'loggen', fontsize=9, color=text_color,
        ha='center', va='center')

# Step 3
step3_box = FancyBboxPatch((6.4, steps_y - 0.6), 2.4, 1.0,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#4A5568', edgecolor=success_color,
                            linewidth=1.5)
ax.add_patch(step3_box)
step3_circle = plt.Circle((6.7, steps_y + 0.15), 0.22, color=success_color, fill=True)
ax.add_patch(step3_circle)
ax.text(6.7, steps_y + 0.15, '3', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(7.6, steps_y + 0.15, 'Commit', fontsize=9, color=text_color,
        ha='center', va='center')
ax.text(7.6, steps_y - 0.2, 'schreiben', fontsize=9, color=text_color,
        ha='center', va='center')

# Step 4
step4_box = FancyBboxPatch((9.2, steps_y - 0.6), 2.8, 1.0,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#4A5568', edgecolor=title_color,
                            linewidth=1.5)
ax.add_patch(step4_box)
step4_circle = plt.Circle((9.5, steps_y + 0.15), 0.22, color=title_color, fill=True)
ax.add_patch(step4_circle)
ax.text(9.5, steps_y + 0.15, '4', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(10.6, steps_y + 0.15, 'Checkpoint:', fontsize=9, color=text_color,
        ha='center', va='center')
ax.text(10.6, steps_y - 0.2, 'auf FS anwenden', fontsize=9, color=text_color,
        ha='center', va='center')

# Arrows between steps
for x in [3.25, 6.05, 8.85]:
    ax.annotate('', xy=(x + 0.25, steps_y), xytext=(x, steps_y),
                arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))

# ===== Step 5 at bottom =====
step5_box = FancyBboxPatch((3.5, 0.4), 6, 0.9,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#4A5568', edgecolor='#718096',
                            linewidth=1.5)
ax.add_patch(step5_box)
step5_circle = plt.Circle((3.8, 0.85), 0.22, color='#718096', fill=True)
ax.add_patch(step5_circle)
ax.text(3.8, 0.85, '5', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(6.5, 0.85, 'Journal-Eintrag als "abgeschlossen" markieren (oder löschen)', 
        fontsize=9, color=text_color, ha='center', va='center')

# Arrow from step 4 to step 5 (curved to connect properly)
arrow_4_to_5 = FancyArrowPatch((10.6, 2.4), (9.5, 1.35),
                                arrowstyle='->', mutation_scale=12,
                                color=text_color, linewidth=1.5,
                                connectionstyle="arc3,rad=-0.3")
ax.add_patch(arrow_4_to_5)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/journal-transaktion.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created journal-transaktion.png")
