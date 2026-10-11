#!/usr/bin/env python3
"""
Diagram: Synchronisationsmechanismen - Three-level hierarchy
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Colors (theme-agnostic)
box_fill = '#3182CE'
box_fill_light = '#4299E1'
text_color = '#A0AEC0'
arrow_color = '#A0AEC0'

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_alpha(0)
ax.set_facecolor('none')

def draw_level_box(ax, y_center, title, items, level_num):
    """Draw a level box with title and bullet items"""
    box_height = 1.8
    box_width = 8
    x_center = 5
    
    # Main box
    box = FancyBboxPatch((x_center - box_width/2, y_center - box_height/2), 
                         box_width, box_height,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=box_fill, edgecolor=text_color, linewidth=1.5)
    ax.add_patch(box)
    
    # Level indicator circle
    circle = plt.Circle((1.3, y_center), 0.3, facecolor=box_fill_light, 
                        edgecolor=text_color, linewidth=1)
    ax.add_patch(circle)
    ax.text(1.3, y_center, str(level_num), ha='center', va='center',
            fontsize=12, color='white', fontweight='bold')
    
    # Title
    ax.text(5, y_center + 0.5, title, ha='center', va='center',
            fontsize=12, color='white', fontweight='bold')
    
    # Items (two columns)
    if len(items) <= 2:
        for i, item in enumerate(items):
            ax.text(3 + i*4, y_center - 0.3, f'• {item}', ha='center', va='center',
                    fontsize=9, color='white')
    else:
        # First column
        for i, item in enumerate(items[:2]):
            ax.text(3, y_center - 0.2 - i*0.4, f'• {item}', ha='center', va='center',
                    fontsize=9, color='white')
        # Second column
        for i, item in enumerate(items[2:]):
            ax.text(7, y_center - 0.2 - i*0.4, f'• {item}', ha='center', va='center',
                    fontsize=9, color='white')

def draw_arrow_down(ax, y_start, y_end):
    ax.annotate('', xy=(5, y_end), xytext=(5, y_start),
                arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Title
ax.text(5, 9.5, 'Synchronisationsmechanismen', ha='center', va='center',
        fontsize=16, color=text_color, fontweight='bold')

# Level 1: Hardware
draw_level_box(ax, 7.5, 'HARDWARE-EBENE', 
               ['Unterbrechungssperre', 'Atomare Operationen (TAS, CAS)', 'Spinlocks'], 1)

# Arrow
draw_arrow_down(ax, 6.5, 5.7)

# Level 2: Betriebssystem
draw_level_box(ax, 4.8, 'BETRIEBSSYSTEM-EBENE',
               ['Semaphore (P/V)', 'Mutexe'], 2)

# Arrow
draw_arrow_down(ax, 3.8, 3.0)

# Level 3: Programmiersprache
draw_level_box(ax, 2.1, 'PROGRAMMIERSPRACHEN-EBENE',
               ['Monitore', 'Condition Variables', 'synchronized (Java)', 'lock (C#), with (Python)'], 3)

# Bottom note
ax.text(5, 0.4, 'Jede Ebene baut auf der darunterliegenden auf',
        ha='center', va='center', fontsize=10, color=text_color, style='italic')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/tmp/preview-sync-mechanisms.png',
            dpi=150, bbox_inches='tight', transparent=True, pad_inches=0.1)
plt.close()
print("Created: preview-sync-mechanisms.png")
