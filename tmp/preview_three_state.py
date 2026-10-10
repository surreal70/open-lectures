#!/usr/bin/env python3
"""Preview: Three-state process model with proper dual arrows"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
running_color = '#48BB78'
ready_color = '#4299E1'
blocked_color = '#ED8936'

fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# State positions - horizontal layout like 5-state model
ready_pos = (0.5, 3)
running_pos = (4, 3)
blocked_pos = (7.5, 3)

box_w, box_h = 2.2, 1.0

# Draw states
states = [
    (ready_pos, ready_color, 'READY', '(Bereit)'),
    (running_pos, running_color, 'RUNNING', '(Ausführung)'),
    (blocked_pos, blocked_color, 'BLOCKED', '(Wartend)'),
]

for (x, y), color, label, sublabel in states:
    box = FancyBboxPatch((x, y), box_w, box_h,
                          boxstyle="round,pad=0.02,rounding_size=0.12",
                          facecolor=color, edgecolor=border_color, linewidth=2)
    ax.add_patch(box)
    ax.text(x + box_w/2, y + box_h/2 + 0.12, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color=text_light)
    ax.text(x + box_w/2, y + box_h/2 - 0.2, sublabel, ha='center', va='center',
            fontsize=9, color=text_light)

# Arrows - TWO arrows between Ready and Running (offset vertically)
# Ready -> Running (Dispatch) - upper arrow
ax.annotate('', xy=(running_pos[0], running_pos[1] + box_h/2 + 0.15),
            xytext=(ready_pos[0] + box_w, ready_pos[1] + box_h/2 + 0.15),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
ax.text(3.35, 4.0, 'Dispatch', ha='center', va='center',
        fontsize=9, color=text_outside)

# Running -> Ready (Timeout) - lower arrow
ax.annotate('', xy=(ready_pos[0] + box_w, ready_pos[1] + box_h/2 - 0.15),
            xytext=(running_pos[0], running_pos[1] + box_h/2 - 0.15),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
ax.text(3.35, 3.0, 'Timeout', ha='center', va='center',
        fontsize=9, color=text_outside)

# Running -> Blocked (Block)
ax.annotate('', xy=(blocked_pos[0], blocked_pos[1] + box_h/2 + 0.15),
            xytext=(running_pos[0] + box_w, running_pos[1] + box_h/2 + 0.15),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
ax.text(6.85, 4.0, 'Block', ha='center', va='center',
        fontsize=9, color=text_outside)

# Blocked -> Ready (Wakeup) - curved arrow above boxes, bow curves upward
ax.annotate('', xy=(ready_pos[0] + box_w/2, ready_pos[1] + box_h),
            xytext=(blocked_pos[0] + box_w/2, blocked_pos[1] + box_h),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2,
                           connectionstyle='arc3,rad=0.5'))
ax.text(4.85, 5.5, 'Wakeup\n(E/A fertig)', ha='center', va='center',
        fontsize=9, color=text_outside)

# New process arrow
ax.annotate('', xy=(ready_pos[0] + box_w/2, ready_pos[1]),
            xytext=(ready_pos[0] + box_w/2, 1.0),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
ax.text(ready_pos[0] + box_w/2, 0.7, 'Neuer Prozess', ha='center', va='center',
        fontsize=9, color=text_outside)

# Title
ax.text(5, 6.3, 'Drei-Zustands-Modell', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-process-states-3.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
