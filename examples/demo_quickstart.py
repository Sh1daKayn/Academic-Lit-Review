"""
Academic Literature Review Toolkit - Demo Quickstart
----------------------------------------------------
Run this script to test the end-to-end generation of a sample academic
literature review Word document with custom OpenXML tables and 300 DPI figures.

Usage:
    python examples/demo_quickstart.py
"""

import os
import sys

# Ensure templates can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from templates.docx_builder_template import (
    create_document, add_title, add_metadata_box, add_heading_1,
    add_heading_2, add_body, add_styled_table, add_figure, save_document
)
from templates.figure_generator_template import (
    plot_donut_headroom, plot_horizontal_benchmarks
)

def run_demo():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    print("Step 1: Generating 300 DPI Times New Roman figure...")
    fig_path = os.path.join(output_dir, "demo_adoption_headroom.png")
    plot_donut_headroom(
        labels=['Practices Adopted\n(12.8M Acres, 7.2%)', 'Untapped Headroom\n(165.2M Acres, 92.8%)'],
        sizes=[12.8, 165.2],
        title="Cropland Acreage vs. Practice Adoption Headroom\n(2022 Census Baseline)",
        center_text="178M\nAcres",
        out_path=fig_path
    )

    print("Step 2: Compiling publication-grade Word document...")
    doc = create_document()

    add_title(
        doc,
        "Systematic Review of Production Economics & Adoption Determinants",
        "An Applied Microeconomic Synthesis Under PRISMA 2020 Protocol"
    )

    add_metadata_box(doc, [
        ("Author", "Research Group"),
        ("Protocol", "PRISMA 2020"),
        ("Database", "Web of Science Core Collection"),
        ("Date", "2026-09")
    ])

    add_heading_1(doc, "1. Executive Introduction & Operational Grounding")
    add_body(doc, "Adopting conservation practices on commercial grain operations represents an investment decision made under price, yield, and contract uncertainty. Farm operators maximize expected net returns across their planning horizon subject to cash flow liquidity, equipment capacity, and lease terms.")

    add_heading_2(doc, "1.1 Practice Taxonomy & Microeconomic Input Dynamics")
    add_body(doc, "Table 1 classifies working-lands practices by operational nature, distinguishing upfront variable cash outflows from multi-year soil capital accumulation.")

    # Table 1: Practice Taxonomy
    headers_t1 = ["Practice Category", "Input Allocation & Operations", "Economic Transformation & Asset Dynamics", "Empirical Literature Grounding"]
    data_t1 = [
        ("Conservation Tillage\n(No-till, Strip-till)",
         "Replaces deep tillage implements with specialized coulters, row cleaners, and no-till seed drills.",
         "Lowers machinery wear, fuel consumption, and field labor per acre; stabilizes soil aggregates.",
         "Canales et al. (2018);\nDerpsch et al. (2024)"),
        ("Living Cover Crops\n(Cereal rye, legumes)",
         "Adds annual variable costs for seed stock ($20–$40/ac), late-summer seeding ($12–$18/ac), and chemical termination ($12–$15/ac).",
         "Builds soil organic matter and scavenges nitrate, but creates initial net cash flow deficits in Years 1–3.",
         "Plastina et al. (2020);\nRoth et al. (2018)"),
        ("4R Nutrient Management\n(CPS 590)",
         "Uses precision variable-rate fertilizer placement and split nitrogen timing.",
         "Replaces 15%–30% of synthetic nitrogen, compressing operating expenditures.",
         "Nevins et al. (2020);\nSnapp et al. (2024)")
    ]
    add_styled_table(doc, headers_t1, data_t1, header_bg="1F4E79")

    add_heading_2(doc, "1.2 Eligible Cropland Baseline and Market Headroom")
    add_body(doc, "Figure 1 illustrates the aggregate adoption disparity: over 92.8% of prime cropland remains unenrolled, creating substantial headroom for private supply-chain insetting and policy incentives.")

    # Embed Figure
    add_figure(doc, fig_path, "Figure 1. Qualified Row-Crop Cropland vs. Current Practice Adoption Baseline")

    add_heading_1(doc, "2. Institutional Frictions & Contractual Solutions")
    add_body(doc, "Table 2 summarizes microeconomic bottlenecks confronting commercial growers alongside proven institutional solutions.")

    # Table 2: Frictions vs Solutions
    headers_t2 = ["Friction Category", "Empirical Bottleneck", "Contractual / Policy Solution", "Representative Citations"]
    data_t2 = [
        ("Short-Term Cash Deficit",
         "Upfront costs ($45–$75/ac) create net cash flow deficits in Years 1–3; payback requires 4–6 years.",
         "Stack practices: contract grazing ($30–$60/ac) or 4R nitrogen reduction (15%–30%) for Year 1 liquidity.",
         "Plastina et al. (2020);\nSummers et al. (2025)"),
        ("Spring Planting Bottleneck",
         "Termination delays past early May trigger 1.0%–2.2%/day corn yield penalty, erasing annual profit margins.",
         "Deploy high-clearance inter-seeders, 'planting green' protocols, or winter wheat rotations.",
         "Schnitkey (2023);\nAdhikari et al. (2023)"),
        ("1-Year Cash Lease Friction",
         "Over 50% of cropland is rented under 1-year leases; tenants bear 100% risk while landowners capture asset appreciation.",
         "Adopt Multi-Year Green Leases (3–5 year terms, 50% seed cost-share, $10–$20 rent reductions).",
         "Sawadgo & Plastina (2022);\nUpadhaya et al. (2023)")
    ]
    add_styled_table(doc, headers_t2, data_t2, header_bg="1F4E79")

    target_docx = os.path.join(output_dir, "Demo_Academic_Literature_Review.docx")
    save_document(doc, target_docx)
    print(f"\n[SUCCESS] Demo successfully generated! Open: {target_docx}")

if __name__ == "__main__":
    run_demo()
