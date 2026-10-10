#!/usr/bin/env python3
"""Generate Process State diagrams as PNG - Theme-agnostic version"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as path_effects

# Theme-agnostic colors
text_outside = '#A0AEC0'      # Light gray for text outside boxes
text_light = '#F7FAFC'        # Off-white for text in boxes
border_color = '#718096'      # Medium gray for borders

# State colors
running_color = '#48BB78'     # Green for Running
ready_color = '#4299E1'       # Blue for Ready
blocked_color = '#ED8936'     # Orange for Blocked
new_color = '#9F7AEA'         # Purple for New
terminated_color = '#E53E3E'  # Red for Terminated


def create_three_state_diagram():
    """Create the basic three-state process model diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # State positions - triangle layout
    running_pos = (3.75, 5.5)
    ready_pos = (1, 2)
    blocked_pos = (6.5, 2)
    
    box_w, box_h = 2.5, 1.2
    
    # Calculate box centers
    running_center = (running_pos[0] + box_w/2, running_pos[1] + box_h/2)
    ready_center = (ready_pos[0] + box_w/2, ready_pos[1] + box_h/2)
    blocked_center = (blocked_pos[0] + box_w/2, blocked_pos[1] + box_h/2)
    
    # Draw states
    states = [
        (running_pos, running_color, 'RUNNING', '(Ausführung)'),
        (ready_pos, ready_color, 'READY', '(Bereit)'),
        (blocked_pos, blocked_color, 'BLOCKED', '(Wartend)'),
    ]
    
    for (x, y), color, label, sublabel in states:
        box = FancyBboxPatch((x, y), box_w, box_h,
                              boxstyle="round,pad=0.02,rounding_size=0.15",
                              facecolor=color, edgecolor=border_color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + box_w/2, y + box_h/2 + 0.15, label, ha='center', va='center',
                fontsize=12, fontweight='bold', color=text_light)
        ax.text(x + box_w/2, y + box_h/2 - 0.25, sublabel, ha='center', va='center',
                fontsize=9, color=text_light)
    
    # Straight arrows connecting box edges at center height
    # Ready -> Running (right edge of Ready to left edge of Running)
    ax.annotate('', xy=(running_pos[0], running_center[1]),
                xytext=(ready_pos[0] + box_w, ready_center[1]),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(2.5, 4.3, 'Scheduler\nwählt aus', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Running -> Blocked (right edge of Running to left edge of Blocked)
    ax.annotate('', xy=(blocked_pos[0], blocked_center[1]),
                xytext=(running_pos[0] + box_w, running_center[1]),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(7.5, 4.3, 'E/A-Anfrage\noder Warten', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Blocked -> Ready (left edge of Blocked to right edge of Ready)
    ax.annotate('', xy=(ready_pos[0] + box_w, ready_center[1]),
                xytext=(blocked_pos[0], blocked_center[1]),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(5, 2.15, 'E/A fertig', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # New process arrow - bottom edge center of Ready
    ax.annotate('', xy=(ready_center[0], ready_pos[1]),
                xytext=(ready_center[0], 0.5),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(ready_center[0], 0.2, 'Neuer Prozess', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Title
    ax.text(5, 7.5, 'Drei-Zustands-Modell', ha='center', va='center',
            fontsize=14, fontweight='bold', color=text_outside)
    
    # Save
    output_path = "/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/03-Prozesse/assets/process-states-3.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight', 
                transparent=True, pad_inches=0.2)
    plt.close()
    print(f"Saved: {output_path}")


def create_five_state_diagram():
    """Create the extended five-state process model diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # State positions
    new_pos = (5, 6.5)
    ready_pos = (4.5, 4)
    running_pos = (8, 4)
    blocked_pos = (1, 4)
    terminated_pos = (10, 1.5)
    
    box_w, box_h = 2.2, 1.0
    
    # Draw states
    states = [
        (new_pos, new_color, 'NEW', '(Erzeugt)'),
        (ready_pos, ready_color, 'READY', '(Bereit)'),
        (running_pos, running_color, 'RUNNING', '(Ausführung)'),
        (blocked_pos, blocked_color, 'BLOCKED', '(Wartend)'),
        (terminated_pos, terminated_color, 'TERMINATED', '(Beendet)'),
    ]
    
    for (x, y), color, label, sublabel in states:
        box = FancyBboxPatch((x, y), box_w, box_h,
                              boxstyle="round,pad=0.02,rounding_size=0.12",
                              facecolor=color, edgecolor=border_color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + box_w/2, y + box_h/2 + 0.12, label, ha='center', va='center',
                fontsize=11, fontweight='bold', color=text_light)
        ax.text(x + box_w/2, y + box_h/2 - 0.2, sublabel, ha='center', va='center',
                fontsize=8, color=text_light)
    
    # Arrows with labels
    # New -> Ready (Admitted)
    ax.annotate('', xy=(ready_pos[0] + box_w/2, ready_pos[1] + box_h),
                xytext=(new_pos[0] + box_w/2, new_pos[1]),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(5.3, 5.6, 'Admitted', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Ready -> Running (Dispatch)
    ax.annotate('', xy=(running_pos[0], running_pos[1] + box_h/2),
                xytext=(ready_pos[0] + box_w, ready_pos[1] + box_h/2),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(7.3, 4.8, 'Dispatch', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Running -> Ready (Timeout)
    ax.annotate('', xy=(ready_pos[0] + box_w, ready_pos[1] + box_h/2 - 0.2),
                xytext=(running_pos[0], running_pos[1] + box_h/2 - 0.2),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(7.3, 4.0, 'Timeout', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Running -> Blocked (Block)
    ax.annotate('', xy=(blocked_pos[0] + box_w, blocked_pos[1] + box_h/2),
                xytext=(ready_pos[0], ready_pos[1] + box_h/2),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2,
                               connectionstyle='arc3,rad=0.3'))
    ax.text(3.2, 5.0, 'Block', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Blocked -> Ready (Wakeup)
    ax.annotate('', xy=(ready_pos[0], ready_pos[1] + box_h/2 - 0.2),
                xytext=(blocked_pos[0] + box_w, blocked_pos[1] + box_h/2 - 0.2),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(3.2, 4.0, 'Wakeup', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Running -> Terminated (Exit)
    ax.annotate('', xy=(terminated_pos[0] + box_w/2, terminated_pos[1] + box_h),
                xytext=(running_pos[0] + box_w/2, running_pos[1]),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(9.8, 3.0, 'Exit', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Process created arrow
    ax.annotate('', xy=(new_pos[0], new_pos[1] + box_h/2),
                xytext=(new_pos[0] - 1.5, new_pos[1] + box_h/2),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
    ax.text(2.8, 7.0, 'Prozess\nerzeugt', ha='center', va='center',
            fontsize=9, color=text_outside)
    
    # Title
    ax.text(6, 7.7, 'Fünf-Zustands-Modell', ha='center', va='center',
            fontsize=14, fontweight='bold', color=text_outside)
    
    # Save
    output_path = "/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/03-Prozesse/assets/process-states-5.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight', 
                transparent=True, pad_inches=0.2)
    plt.close()
    print(f"Saved: {output_path}")


if __name__ == '__main__':
    create_three_state_diagram()
    create_five_state_diagram()
