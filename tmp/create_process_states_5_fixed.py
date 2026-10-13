#!/usr/bin/env python3
"""
Fünf-Zustands-Modell für Prozesse - KORRIGIERT
Block-Pfeil geht von RUNNING nach BLOCKED (nicht von READY)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Theme-agnostic colors
TEXT_COLOR = '#4A5568'
ARROW_COLOR = '#718096'

# State colors (saturated but not too dark)
COLOR_NEW = '#9F7AEA'        # Purple
COLOR_READY = '#4299E1'      # Blue
COLOR_RUNNING = '#48BB78'    # Green
COLOR_BLOCKED = '#ED8936'    # Orange
COLOR_TERMINATED = '#E53E3E' # Red

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_alpha(0)
ax.set_facecolor('none')

# Title
ax.text(7, 9.5, 'Fünf-Zustands-Modell', fontsize=20, fontweight='bold',
        ha='center', va='center', color=TEXT_COLOR)

# State positions
positions = {
    'NEW': (7, 7.5),
    'READY': (7, 4.5),
    'RUNNING': (11, 4.5),
    'BLOCKED': (3, 4.5),
    'TERMINATED': (11, 1.5)
}

# State labels (English + German)
labels = {
    'NEW': ('NEW', 'Erzeugt'),
    'READY': ('READY', 'Bereit'),
    'RUNNING': ('RUNNING', 'Ausführung'),
    'BLOCKED': ('BLOCKED', 'Wartend'),
    'TERMINATED': ('TERMINATED', 'Beendet')
}

colors = {
    'NEW': COLOR_NEW,
    'READY': COLOR_READY,
    'RUNNING': COLOR_RUNNING,
    'BLOCKED': COLOR_BLOCKED,
    'TERMINATED': COLOR_TERMINATED
}

# Draw states as rounded rectangles
box_width = 2.4
box_height = 1.2

for state, (x, y) in positions.items():
    # Draw box
    box = FancyBboxPatch(
        (x - box_width/2, y - box_height/2),
        box_width, box_height,
        boxstyle="round,pad=0.05,rounding_size=0.2",
        facecolor=colors[state],
        edgecolor='none',
        alpha=0.95
    )
    ax.add_patch(box)
    
    # Draw labels
    eng_label, ger_label = labels[state]
    ax.text(x, y + 0.15, eng_label, fontsize=14, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(x, y - 0.3, f'({ger_label})', fontsize=10,
            ha='center', va='center', color='white', alpha=0.9)

def draw_arrow(start, end, label, label_pos='above', curved=0, offset=(0, 0)):
    """Draw an arrow with label"""
    style = f"Simple,tail_width=0.5,head_width=4,head_length=6"
    
    if curved != 0:
        connectionstyle = f"arc3,rad={curved}"
    else:
        connectionstyle = "arc3,rad=0"
    
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle='-|>',
        mutation_scale=15,
        color=ARROW_COLOR,
        linewidth=2,
        connectionstyle=connectionstyle
    )
    ax.add_patch(arrow)
    
    # Calculate label position
    mid_x = (start[0] + end[0]) / 2 + offset[0]
    mid_y = (start[1] + end[1]) / 2 + offset[1]
    
    if label_pos == 'above':
        mid_y += 0.3
    elif label_pos == 'below':
        mid_y -= 0.3
    elif label_pos == 'left':
        mid_x -= 0.3
    elif label_pos == 'right':
        mid_x += 0.3
    
    ax.text(mid_x, mid_y, label, fontsize=11, ha='center', va='center',
            color=TEXT_COLOR, style='italic')

# Draw transitions

# 1. "Prozess erzeugt" -> NEW (entry arrow)
ax.annotate('', xy=(5.8, 7.5), xytext=(4.2, 8.2),
            arrowprops=dict(arrowstyle='-|>', color=ARROW_COLOR, lw=2))
ax.text(3.8, 8.0, 'Prozess\nerzeugt', fontsize=11, ha='center', va='center',
        color=TEXT_COLOR, style='italic')

# 2. NEW -> READY (Admitted)
draw_arrow((7, 6.9), (7, 5.1), 'Admitted', label_pos='right', offset=(0.5, 0))

# 3. READY -> RUNNING (Dispatch)
draw_arrow((8.2, 4.5), (9.8, 4.5), 'Dispatch', label_pos='above')

# 4. RUNNING -> READY (Timeout) - curved arrow below
draw_arrow((9.8, 4.2), (8.2, 4.2), 'Timeout', label_pos='below', curved=0)

# 5. RUNNING -> BLOCKED (Block) - Arrow from RUNNING to BLOCKED
draw_arrow((9.8, 4.0), (4.2, 4.0), 'Block', label_pos='below', curved=-0.25, offset=(0, -0.4))

# 6. BLOCKED -> READY (Wakeup) - Arrow from BLOCKED to READY
draw_arrow((4.2, 5.0), (5.8, 5.0), 'Wakeup', label_pos='above')

# 7. RUNNING -> TERMINATED (Exit)
draw_arrow((11, 3.9), (11, 2.1), 'Exit', label_pos='right', offset=(0.4, 0))

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/03-Prozesse/assets/process-states-5.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("✓ process-states-5.png created (FIXED: Block arrow from RUNNING to BLOCKED)")
