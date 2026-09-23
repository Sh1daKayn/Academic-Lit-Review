"""
Academic Visualization Generator Template (Matplotlib)
-------------------------------------------------------
Generates publication-quality charts styled in standard Times New Roman
with STIX math fonts, professional academic palettes, and collision avoidance.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

def set_academic_style():
    """Configures matplotlib with publication-grade Times New Roman serif settings."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'figure.titlesize': 13,
        'mathtext.fontset': 'stix',
        'figure.dpi': 300
    })

def plot_donut_headroom(labels, sizes, title, center_text, out_path, colors=None):
    """
    Renders a clean donut chart showing market / adoption headroom.
    Avoids edge clipping via radius tuning and bbox_inches='tight'.
    """
    set_academic_style()
    if colors is None:
        colors = ['#1F4E79', '#D9E1E8']

    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    explode = (0.08, 0)

    wedges, texts, autotexts = ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'fontsize': 10, 'weight': 'bold', 'color': '#102C57'},
        pctdistance=0.62,
        radius=0.85,
        wedgeprops={'edgecolor': '#102C57', 'linewidth': 1.5}
    )
    autotexts[0].set_color('white')
    autotexts[1].set_color('#102C57')

    ax.set_title(title, pad=14, weight='bold', color='#102C57', fontsize=12)

    # Donut center circle
    centre_circle = plt.Circle((0, 0), 0.32, fc='white', edgecolor='#102C57', linewidth=1.2)
    ax.add_artist(centre_circle)
    ax.text(0, 0, center_text, ha='center', va='center', fontsize=11, weight='bold', color='#102C57')

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated donut chart: {out_path}")

def plot_horizontal_benchmarks(categories, values, title, xlabel, out_path, benchmark_lines=None):
    """
    Renders horizontal bars with inside-bar labels to eliminate reference line collision.
    benchmark_lines: list of tuples, e.g. [(7.2, '#C0392B', '--', 'Mean (7.2%)')]
    """
    set_academic_style()
    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    y_pos = np.arange(len(categories))

    primary_color = '#1F4E79'
    secondary_color = '#4A7BB0'
    mean_val = np.mean(values)
    bar_colors = [primary_color if v >= mean_val else secondary_color for v in values]

    bars = ax.barh(y_pos, values, color=bar_colors, edgecolor='#102C57', height=0.65, alpha=0.9)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel, weight='bold', color='#102C57')
    ax.set_xlim(0, max(values) * 1.35)
    ax.set_title(title, pad=14, weight='bold', color='#102C57', fontsize=12)

    if benchmark_lines:
        for val, col, ls, lbl in benchmark_lines:
            ax.axvline(val, color=col, linestyle=ls, linewidth=1.5, label=lbl)

    # Smart label positioning: place inside bar if near benchmark lines
    for bar in bars:
        w = bar.get_width()
        # If within 0.8 units of any benchmark line, put inside
        near_line = False
        if benchmark_lines:
            for line_val, _, _, _ in benchmark_lines:
                if abs(w - line_val) < 0.8:
                    near_line = True
                    break

        if near_line:
            ax.text(w - 0.3, bar.get_y() + bar.get_height()/2, f'{w:.1f}%',
                    ha='right', va='center', fontsize=9.5, weight='bold', color='white')
        else:
            ax.text(w + 0.25, bar.get_y() + bar.get_height()/2, f'{w:.1f}%',
                    ha='left', va='center', fontsize=9.5, weight='bold', color='#102C57')

    if benchmark_lines:
        ax.legend(loc='lower right', frameon=True, facecolor='#F8FAFC', edgecolor='#D0D7DE', fontsize=9.5)
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated benchmark chart: {out_path}")

