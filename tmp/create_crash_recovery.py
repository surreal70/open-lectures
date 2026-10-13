#!/usr/bin/env python3
"""
Creates a crash recovery flowchart diagram for 04-Journaling.md
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

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 8.5, 'Crash Recovery', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

ax.text(6, 8.0, 'System bootet nach Absturz', 
        fontsize=11, color=text_color, ha='center', va='center', style='italic')

# ===== Step 1: Read Superblock =====
step1_box = FancyBboxPatch((0.5, 6.5), 4.5, 1.0,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=title_color,
                            linewidth=2)
ax.add_patch(step1_box)
step1_circle = plt.Circle((0.9, 7.3), 0.22, color=title_color, fill=True)
ax.add_patch(step1_circle)
ax.text(0.9, 7.3, '1', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(2.75, 7.2, 'Superblock lesen', fontsize=10, fontweight='bold',
        color='#1A202C', ha='center', va='center')
ax.text(2.75, 6.8, '"Dirty" Flag gesetzt?', fontsize=9, color=text_color,
        ha='center', va='center')

# Decision arrows from step 1
# No branch (clean)
ax.annotate('', xy=(7.5, 7.0), xytext=(5.0, 7.0),
            arrowprops=dict(arrowstyle='->', color=success_color, lw=2))
ax.text(6.2, 7.3, 'Nein', fontsize=9, color=success_color,
        ha='center', va='center', fontweight='bold')

# Clean shutdown box
clean_box = FancyBboxPatch((7.5, 6.5), 4.0, 1.0,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#C6F6D5', edgecolor=success_color,
                            linewidth=2)
ax.add_patch(clean_box)
ax.text(9.5, 7.0, '✓ Sauber beendet', fontsize=10, fontweight='bold',
        color=success_color, ha='center', va='center')
ax.text(9.5, 6.7, 'Normal mounten', fontsize=9, color='#276749',
        ha='center', va='center')

# Yes branch (crash detected)
ax.annotate('', xy=(2.75, 5.5), xytext=(2.75, 6.5),
            arrowprops=dict(arrowstyle='->', color=warning_color, lw=2))
ax.text(3.3, 6.0, 'Ja', fontsize=9, color=warning_color,
        ha='left', va='center', fontweight='bold')

# ===== Step 2: Scan Journal =====
step2_box = FancyBboxPatch((0.5, 4.2), 4.5, 1.3,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=journal_color,
                            linewidth=2)
ax.add_patch(step2_box)
step2_circle = plt.Circle((0.9, 5.2), 0.22, color=journal_color, fill=True)
ax.add_patch(step2_circle)
ax.text(0.9, 5.2, '2', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(2.75, 5.1, 'Journal scannen', fontsize=10, fontweight='bold',
        color=journal_color, ha='center', va='center')
ax.text(2.75, 4.7, '(wenige Sekunden!)', fontsize=9, color='#553C9A',
        ha='center', va='center')
ax.text(2.75, 4.4, 'Crash erkannt → Journal prüfen', fontsize=8, color=text_color,
        ha='center', va='center')

# Journal scan results box
journal_scan_box = FancyBboxPatch((5.5, 3.8), 6.0, 2.0,
                                   boxstyle="round,pad=0.02,rounding_size=0.1",
                                   facecolor='#EDF2F7', edgecolor=border_color,
                                   linewidth=1.5)
ax.add_patch(journal_scan_box)

# Journal entries
ax.text(8.5, 5.5, 'Journal-Inhalt:', fontsize=9, fontweight='bold',
        color=text_color, ha='center', va='center')

entries = [
    ('TXN 100: Begin ... Commit', success_color, '→ OK'),
    ('TXN 101: Begin ... Commit', success_color, '→ OK'),
    ('TXN 102: Begin ... (kein Commit)', danger_color, '→ UNDO'),
    ('TXN 103: Begin ... Commit', warning_color, '→ REDO'),
]
y_pos = 5.1
for entry, color, action in entries:
    ax.text(6.0, y_pos, entry, fontsize=8, color=text_color,
            ha='left', va='center', family='monospace')
    ax.text(10.8, y_pos, action, fontsize=8, color=color,
            ha='left', va='center', fontweight='bold')
    y_pos -= 0.35

# Arrow to step 3
ax.annotate('', xy=(2.75, 3.4), xytext=(2.75, 4.2),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# ===== Step 3: Undo incomplete =====
step3_box = FancyBboxPatch((0.5, 2.4), 4.5, 1.0,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#FED7D7', edgecolor=danger_color,
                            linewidth=2)
ax.add_patch(step3_box)
step3_circle = plt.Circle((0.9, 3.2), 0.22, color=danger_color, fill=True)
ax.add_patch(step3_circle)
ax.text(0.9, 3.2, '3', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(2.75, 3.1, 'Inkomplete TXNs', fontsize=10, fontweight='bold',
        color=danger_color, ha='center', va='center')
ax.text(2.75, 2.7, 'rückgängig machen (UNDO)', fontsize=9, color='#9B2C2C',
        ha='center', va='center')

# Arrow to step 4
ax.annotate('', xy=(5.5, 2.9), xytext=(5.0, 2.9),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# ===== Step 4: Redo committed =====
step4_box = FancyBboxPatch((5.5, 2.4), 4.5, 1.0,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#C6F6D5', edgecolor=warning_color,
                            linewidth=2)
ax.add_patch(step4_box)
step4_circle = plt.Circle((5.9, 3.2), 0.22, color=warning_color, fill=True)
ax.add_patch(step4_circle)
ax.text(5.9, 3.2, '4', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(7.75, 3.1, 'Committed aber', fontsize=10, fontweight='bold',
        color=warning_color, ha='center', va='center')
ax.text(7.75, 2.7, 'nicht applied → REDO', fontsize=9, color='#C05621',
        ha='center', va='center')

# Arrow to step 5
ax.annotate('', xy=(7.75, 1.9), xytext=(7.75, 2.4),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# ===== Step 5: Cleanup =====
step5_box = FancyBboxPatch((5.5, 0.9), 4.5, 1.0,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=title_color,
                            linewidth=2)
ax.add_patch(step5_box)
step5_circle = plt.Circle((5.9, 1.7), 0.22, color=title_color, fill=True)
ax.add_patch(step5_circle)
ax.text(5.9, 1.7, '5', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(7.75, 1.6, 'Journal leeren', fontsize=10, fontweight='bold',
        color='#1A202C', ha='center', va='center')
ax.text(7.75, 1.2, 'Dirty Flag löschen', fontsize=9, color=text_color,
        ha='center', va='center')

# Arrow to step 6
ax.annotate('', xy=(10.5, 1.4), xytext=(10.0, 1.4),
            arrowprops=dict(arrowstyle='->', color=success_color, lw=2))

# ===== Step 6: Normal mount =====
step6_box = FancyBboxPatch((10.3, 0.9), 1.4, 1.0,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#C6F6D5', edgecolor=success_color,
                            linewidth=2)
ax.add_patch(step6_box)
step6_circle = plt.Circle((10.5, 1.7), 0.22, color=success_color, fill=True)
ax.add_patch(step6_circle)
ax.text(10.5, 1.7, '6', fontsize=9, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(11.0, 1.2, '✓', fontsize=14, fontweight='bold',
        color=success_color, ha='center', va='center')

# Duration comparison removed - will be in markdown text

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/crash-recovery.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created crash-recovery.png")
