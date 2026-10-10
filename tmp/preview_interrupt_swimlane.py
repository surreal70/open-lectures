#!/usr/bin/env python3
"""Preview: Interrupt Flow - Swimlane diagram with 90° arrows"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
program_color = '#48BB78'     # Green
cpu_color = '#4299E1'         # Blue
kernel_color = '#9F7AEA'      # Purple
isr_color = '#ED8936'         # Orange

fig, ax = plt.subplots(1, 1, figsize=(12, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 9.7, 'Interrupt-Ablauf (Swimlane)', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Swimlane columns
lanes = [
    ('Programm', 1.5, program_color),
    ('CPU', 4.5, cpu_color),
    ('Kernel', 7.5, kernel_color),
    ('ISR', 10.5, isr_color),
]

lane_width = 2.6

# Draw lane headers and vertical separators
for label, x, color in lanes:
    header = FancyBboxPatch((x - lane_width/2, 8.8), lane_width, 0.6,
                             boxstyle="square,pad=0",
                             facecolor=color, edgecolor=border_color, linewidth=1.5)
    ax.add_patch(header)
    ax.text(x, 9.1, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color=text_light)
    ax.plot([x + lane_width/2, x + lane_width/2], [0.3, 8.8], 
            color=border_color, lw=1, linestyle='-', alpha=0.5)

# Main frame
ax.plot([0.2, 11.8], [8.8, 8.8], color=border_color, lw=2)
ax.plot([0.2, 11.8], [0.3, 0.3], color=border_color, lw=2)
ax.plot([0.2, 0.2], [0.3, 8.8], color=border_color, lw=2)
ax.plot([11.8, 11.8], [0.3, 8.8], color=border_color, lw=2)

# Box dimensions
box_w = 2.0
box_h = 0.6

# Step 1: Program running
y1 = 8.0
box1 = FancyBboxPatch((1.5 - box_w/2, y1), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=program_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box1)
ax.text(1.5, y1 + box_h/2, 'läuft', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Step 2: Program interrupted (faded)
y2 = 6.8
box2 = FancyBboxPatch((1.5 - box_w/2, y2), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=program_color, edgecolor=border_color, linewidth=1.5, alpha=0.5)
ax.add_patch(box2)
ax.text(1.5, y2 + box_h/2, 'unterbrochen', ha='center', va='center',
        fontsize=8, color=text_light)

# Arrow: Program -> interrupted (vertical down)
ax.annotate('', xy=(1.5, y2 + box_h), xytext=(1.5, y1),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Step 3: CPU finishes instruction
y3 = 6.0
box3 = FancyBboxPatch((4.5 - box_w/2, y3), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=cpu_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box3)
ax.text(4.5, y3 + box_h/2, 'Instr. beenden', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Arrow: interrupted -> CPU (90° angle: down then right to left edge of box, vertically centered)
mid_y = y3 + box_h/2  # Same height as center of target box
ax.plot([1.5, 1.5], [y2, mid_y], color=text_outside, lw=1.5)  # down from unterbrochen
ax.plot([1.5, 4.5 - box_w/2], [mid_y, mid_y], color=text_outside, lw=1.5)  # right to left edge
ax.annotate('', xy=(4.5 - box_w/2, mid_y), xytext=(4.5 - box_w/2 - 0.3, mid_y),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))
ax.text(2.8, mid_y + 0.25, 'Interrupt!', ha='center', va='center',
        fontsize=8, color=text_outside, style='italic')

# Arrow: CPU -> Kernel (90° angle)
y4 = 4.8
mid_y2 = y3 - 0.3
ax.plot([4.5, 4.5], [y3, mid_y2], color=text_outside, lw=1.5)
ax.plot([4.5, 7.5], [mid_y2, mid_y2], color=text_outside, lw=1.5)
ax.annotate('', xy=(7.5, y4 + box_h), xytext=(7.5, mid_y2),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Step 4: Kernel saves state
box4 = FancyBboxPatch((7.5 - box_w/2, y4), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=kernel_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box4)
ax.text(7.5, y4 + box_h/2, 'Zustand sichern', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Arrow: Kernel -> ISR (90° angle)
y5 = 3.6
mid_y3 = y4 - 0.3
ax.plot([7.5, 7.5], [y4, mid_y3], color=text_outside, lw=1.5)
ax.plot([7.5, 10.5], [mid_y3, mid_y3], color=text_outside, lw=1.5)
ax.annotate('', xy=(10.5, y5 + box_h), xytext=(10.5, mid_y3),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Step 5: ISR executes
box5 = FancyBboxPatch((10.5 - box_w/2, y5), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=isr_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box5)
ax.text(10.5, y5 + box_h/2, 'ISR ausführen', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Arrow: ISR -> Kernel (90° angle going left)
y6 = 2.4
mid_y4 = y5 - 0.3
ax.plot([10.5, 10.5], [y5, mid_y4], color=text_outside, lw=1.5)
ax.plot([10.5, 7.5], [mid_y4, mid_y4], color=text_outside, lw=1.5)
ax.annotate('', xy=(7.5, y6 + box_h), xytext=(7.5, mid_y4),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Step 6: Kernel restores state
box6 = FancyBboxPatch((7.5 - box_w/2, y6), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=kernel_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box6)
ax.text(7.5, y6 + box_h/2, 'Zustand laden', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Arrow: Kernel -> CPU (90° angle going left)
y7 = 1.2
mid_y5 = y6 - 0.3
ax.plot([7.5, 7.5], [y6, mid_y5], color=text_outside, lw=1.5)
ax.plot([7.5, 4.5], [mid_y5, mid_y5], color=text_outside, lw=1.5)
ax.annotate('', xy=(4.5, y7 + box_h), xytext=(4.5, mid_y5),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Step 7: CPU dispatch
box7 = FancyBboxPatch((4.5 - box_w/2, y7), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=cpu_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box7)
ax.text(4.5, y7 + box_h/2, 'Dispatch', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Arrow: CPU -> Program (90° angle going left)
y8 = 0.5
mid_y6 = y7 - 0.15
ax.plot([4.5, 4.5], [y7, mid_y6], color=text_outside, lw=1.5)
ax.plot([4.5, 1.5], [mid_y6, mid_y6], color=text_outside, lw=1.5)
ax.annotate('', xy=(1.5, y8 + box_h), xytext=(1.5, mid_y6),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# Step 8: Program continues
box8 = FancyBboxPatch((1.5 - box_w/2, y8), box_w, box_h,
                       boxstyle="round,pad=0.02,rounding_size=0.1",
                       facecolor=program_color, edgecolor=border_color, linewidth=1.5)
ax.add_patch(box8)
ax.text(1.5, y8 + box_h/2, 'fortgesetzt', ha='center', va='center',
        fontsize=9, fontweight='bold', color=text_light)

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-interrupt-swimlane.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
