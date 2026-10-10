#!/usr/bin/env python3
"""Preview: Interrupt Flow - How interrupts work"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
program_color = '#48BB78'     # Green
isr_color = '#9F7AEA'         # Purple

fig, ax = plt.subplots(1, 1, figsize=(11, 7))
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(5.5, 6.5, 'Interrupt-Funktionsweise', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Left side: Program A (running)
prog_box1 = FancyBboxPatch((0.5, 4.5), 2.5, 1.2,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor=program_color, edgecolor=border_color, linewidth=2)
ax.add_patch(prog_box1)
ax.text(1.75, 5.25, 'Programm A', ha='center', va='center',
        fontsize=10, fontweight='bold', color=text_light)
ax.text(1.75, 4.85, '(läuft)', ha='center', va='center',
        fontsize=9, color=text_light)

# Right side: ISR
isr_box = FancyBboxPatch((7.5, 4.5), 3, 1.2,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=isr_color, edgecolor=border_color, linewidth=2)
ax.add_patch(isr_box)
ax.text(9, 5.25, 'Interrupt', ha='center', va='center',
        fontsize=10, fontweight='bold', color=text_light)
ax.text(9, 4.85, 'Service Routine', ha='center', va='center',
        fontsize=9, color=text_light)

# Bidirectional arrow between them
ax.annotate('', xy=(7.3, 5.1), xytext=(3.2, 5.1),
            arrowprops=dict(arrowstyle='<->', color=text_outside, lw=2))
ax.text(5.25, 5.5, 'Interrupt Signal', ha='center', va='center',
        fontsize=9, color=text_outside)

# Steps in the middle
steps = [
    '1. CPU beendet aktuelle Instruktion',
    '2. Zustand (PC, Register) sichern',
    '3. ISR-Adresse aus IVT laden',
    '4. ISR ausführen',
    '5. Zustand wiederherstellen',
    '6. Programm fortsetzen',
]

for i, step in enumerate(steps):
    y = 4.0 - i * 0.45
    ax.text(5.5, y, step, ha='center', va='center',
            fontsize=9, color=text_outside, family='monospace')

# Bottom left: Program A (continued)
prog_box2 = FancyBboxPatch((0.5, 0.8), 2.5, 1.2,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor=program_color, edgecolor=border_color, linewidth=2)
ax.add_patch(prog_box2)
ax.text(1.75, 1.55, 'Programm A', ha='center', va='center',
        fontsize=10, fontweight='bold', color=text_light)
ax.text(1.75, 1.15, '(fortgesetzt)', ha='center', va='center',
        fontsize=9, color=text_light)

# Bottom right: Reaction executed
react_box = FancyBboxPatch((7.5, 0.8), 3, 1.2,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor=isr_color, edgecolor=border_color, linewidth=2)
ax.add_patch(react_box)
ax.text(9, 1.55, 'Reaktion', ha='center', va='center',
        fontsize=10, fontweight='bold', color=text_light)
ax.text(9, 1.15, 'ausgeführt', ha='center', va='center',
        fontsize=9, color=text_light)

# Arrows down
ax.annotate('', xy=(1.75, 2.0), xytext=(1.75, 4.5),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))
ax.annotate('', xy=(9, 2.0), xytext=(9, 4.5),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-interrupt-flow.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
