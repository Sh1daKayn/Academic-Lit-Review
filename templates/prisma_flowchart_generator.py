"""
PRISMA 2020 Protocol Flowchart Auto-Generator
---------------------------------------------
Generates publication-quality, journal-standard PRISMA 2020 flow diagrams
using Matplotlib with Times New Roman typography, 300 DPI, and precise geometry.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def set_prisma_style():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'font.size': 10,
        'mathtext.fontset': 'stix',
        'figure.dpi': 300
    })

def generate_prisma_flowchart(
    identified_count=356,
    duplicate_count=0,
    screened_count=356,
    excluded_details=None,
    retrieved_count=356,
    not_retrieved_count=0,
    eligibility_assessed_count=356,
    included_count=309,
    database_name="Web of Science Core Collection",
    out_path="prisma_2020_flowchart.png"
):
    """
    Renders an audited PRISMA 2020 flow diagram compliant with journal standards.
    """
    set_prisma_style()
    if excluded_details is None:
        excluded_details = [
            ("Pre-2004 publications", 43),
            ("Specialty / non-row crops", 4)
        ]

    total_excluded = sum(cnt for _, cnt in excluded_details)

    fig, ax = plt.subplots(figsize=(8.5, 9.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis('off')

    # Color Palette
    navy_border = '#1F4E79'
    navy_fill = '#F0F4F8'
    red_border = '#C0392B'
    red_fill = '#FDEDEC'
    green_border = '#2E7D32'
    green_fill = '#E8F5E9'
    gray_phase = '#556370'

    # Title
    ax.text(5.0, 10.5, "PRISMA 2020 Flow Diagram for Systematic Reviews", 
            ha='center', va='center', fontsize=12.5, weight='bold', color=navy_border)

    # Left Section Phase Banners
    phases = [
        (9.4, 7.8, "IDENTIFICATION"),
        (7.4, 3.4, "SCREENING"),
        (3.0, 1.2, "INCLUDED")
    ]
    for y_top, y_bot, p_name in phases:
        y_center = (y_top + y_bot) / 2
        ax.plot([0.5, 0.5], [y_bot, y_top], color=navy_border, linewidth=3.5, solid_capstyle='round')
        ax.text(0.3, y_center, p_name, ha='center', va='center', rotation=90, 
                fontsize=9.5, weight='bold', color=gray_phase)

    # Box 1: Identification (Databases)
    b1_text = (
        f"Records identified from:\n"
        f"Databases ({database_name})\n"
        f"(n = {identified_count})"
    )
    b1 = patches.FancyBboxPatch((1.2, 8.4), 3.8, 1.2, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=navy_border, fc=navy_fill, lw=1.5)
    ax.add_patch(b1)
    ax.text(3.1, 9.0, b1_text, ha='center', va='center', fontsize=9.5, linespacing=1.3)

    # Box 2: Deduplication
    b2_text = (
        f"Records removed before screening:\n"
        f"Duplicate records removed (n = {duplicate_count})\n"
        f"Ineligible records removed (n = 0)"
    )
    b2 = patches.FancyBboxPatch((5.6, 8.4), 3.8, 1.2, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=navy_border, fc=navy_fill, lw=1.5)
    ax.add_patch(b2)
    ax.text(7.5, 9.0, b2_text, ha='center', va='center', fontsize=9, linespacing=1.3)

    # Arrow from B1 to B2 (Horizontal)
    ax.annotate("", xy=(5.6, 9.0), xytext=(5.0, 9.0),
                arrowprops=dict(facecolor=navy_border, edgecolor=navy_border, width=1.5, headwidth=6, shrink=0.05))

    # Box 3: Records Screened
    b3_text = f"Records screened\n(n = {screened_count})"
    b3 = patches.FancyBboxPatch((1.2, 6.7), 3.8, 0.9, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=navy_border, fc=navy_fill, lw=1.5)
    ax.add_patch(b3)
    ax.text(3.1, 7.15, b3_text, ha='center', va='center', fontsize=9.5, weight='bold', linespacing=1.3)

    # Arrow from B1 down to B3
    ax.annotate("", xy=(3.1, 7.6), xytext=(3.1, 8.4),
                arrowprops=dict(facecolor=navy_border, edgecolor=navy_border, width=1.5, headwidth=6, shrink=0.05))

    # Box 4: Reports Sought for Retrieval
    b4_text = f"Reports sought for retrieval\n(n = {retrieved_count})"
    b4 = patches.FancyBboxPatch((1.2, 5.2), 3.8, 0.9, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=navy_border, fc=navy_fill, lw=1.5)
    ax.add_patch(b4)
    ax.text(3.1, 5.65, b4_text, ha='center', va='center', fontsize=9.5, linespacing=1.3)

    # Arrow from B3 down to B4
    ax.annotate("", xy=(3.1, 6.1), xytext=(3.1, 6.7),
                arrowprops=dict(facecolor=navy_border, edgecolor=navy_border, width=1.5, headwidth=6, shrink=0.05))

    # Box 5: Reports Assessed for Eligibility
    b5_text = f"Reports assessed for eligibility\n(n = {eligibility_assessed_count})"
    b5 = patches.FancyBboxPatch((1.2, 3.6), 3.8, 0.9, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=navy_border, fc=navy_fill, lw=1.5)
    ax.add_patch(b5)
    ax.text(3.1, 4.05, b5_text, ha='center', va='center', fontsize=9.5, weight='bold', linespacing=1.3)

    # Arrow from B4 down to B5
    ax.annotate("", xy=(3.1, 4.5), xytext=(3.1, 5.2),
                arrowprops=dict(facecolor=navy_border, edgecolor=navy_border, width=1.5, headwidth=6, shrink=0.05))

    # Box 6: Excluded Records with Reasons (Side Box)
    reason_lines = "\n".join([f"• {reason} (n = {cnt})" for reason, cnt in excluded_details])
    b6_text = (
        f"Reports excluded:\n"
        f"{reason_lines}\n"
        f"Total excluded (n = {total_excluded})"
    )
    b6 = patches.FancyBboxPatch((5.6, 3.4), 3.8, 1.3, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=red_border, fc=red_fill, lw=1.5)
    ax.add_patch(b6)
    ax.text(7.5, 4.05, b6_text, ha='center', va='center', fontsize=8.8, color=red_border, linespacing=1.3)

    # Arrow from B5 to B6 (Horizontal)
    ax.annotate("", xy=(5.6, 4.05), xytext=(5.0, 4.05),
                arrowprops=dict(facecolor=red_border, edgecolor=red_border, width=1.5, headwidth=6, shrink=0.05))

    # Box 7: Final Studies Included in Synthesis
    b7_text = (
        f"Final Studies Included in Synthesis\n"
        f"Review & Empirical Pool\n"
        f"(n = {included_count})"
    )
    b7 = patches.FancyBboxPatch((1.2, 1.4), 3.8, 1.2, boxstyle="round,pad=0.1,rounding_size=0.15",
                                ec=green_border, fc=green_fill, lw=2.0)
    ax.add_patch(b7)
    ax.text(3.1, 2.0, b7_text, ha='center', va='center', fontsize=10, weight='bold', color=green_border, linespacing=1.3)

    # Arrow from B5 down to B7
    ax.annotate("", xy=(3.1, 2.6), xytext=(3.1, 3.6),
                arrowprops=dict(facecolor=green_border, edgecolor=green_border, width=1.8, headwidth=7, shrink=0.05))

    plt.tight_layout()
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated PRISMA 2020 Flowchart: {out_path}")

if __name__ == '__main__':
    generate_prisma_flowchart(out_path="output/test_prisma_flowchart.png")
