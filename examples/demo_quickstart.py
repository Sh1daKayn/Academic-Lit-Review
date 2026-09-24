"""
Academic Literature Review Toolkit - Demo Quickstart
----------------------------------------------------
Run this script to test the end-to-end generation of a complete academic
literature review Word document with custom OpenXML tables, PRISMA 2020
flowchart, 300 DPI figures, Risk of Bias matrix, and APA 7th references.

Usage:
    python examples/demo_quickstart.py
"""

import os
import sys

# Ensure templates can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from docx.shared import Inches
from templates.docx_builder_template import (
    create_document, add_title, add_metadata_box, add_heading_1,
    add_heading_2, add_body, add_styled_table, add_figure, save_document
)
from templates.figure_generator_template import plot_donut_headroom
from templates.prisma_flowchart_generator import generate_prisma_flowchart
from templates.rob_matrix_template import add_rob_matrix_table
from templates.apa_reference_builder import add_apa_bibliography_section

def run_demo():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    print("Step 1: Generating 300 DPI Times New Roman figures...")
    # 1. Donut headroom chart
    fig1_path = os.path.join(output_dir, "demo_adoption_headroom.png")
    plot_donut_headroom(
        labels=['Practices Adopted\n(12.8M Acres, 7.2%)', 'Untapped Headroom\n(165.2M Acres, 92.8%)'],
        sizes=[12.8, 165.2],
        title="Cropland Acreage vs. Practice Adoption Headroom\n(2022 Census Baseline)",
        center_text="178M\nAcres",
        out_path=fig1_path
    )

    # 2. Official PRISMA 2020 flowchart
    fig2_path = os.path.join(output_dir, "demo_prisma_flowchart.png")
    generate_prisma_flowchart(
        identified_count=356,
        duplicate_count=0,
        screened_count=356,
        excluded_details=[
            ("Pre-2004 publications", 43),
            ("Specialty / horticultural trials", 4)
        ],
        included_count=309,
        database_name="Web of Science Core Collection",
        out_path=fig2_path
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

    # 1. Introduction
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
    add_figure(doc, fig1_path, "Figure 1. Qualified Row-Crop Cropland vs. Current Practice Adoption Baseline")

    # 2. Methodology & PRISMA 2020 Flowchart
    add_heading_1(doc, "2. Systematic Review Methodology (PRISMA 2020)")
    add_body(doc, "Literature screening strictly adhered to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) statement. The complete record identification, eligibility screening, and attrition flow are presented in Figure 2.")
    add_figure(doc, fig2_path, "Figure 2. Audited PRISMA 2020 Flow Diagram of Systematic Study Identification, Screening, and Inclusion", width=Inches(5.0))

    # 3. Quality & Risk of Bias Matrix
    add_heading_1(doc, "3. Study Quality & Risk of Bias (RoB) Assessment")
    add_body(doc, "Included empirical studies were evaluated across five methodological bias domains following ROBINS-I criteria: selection bias, confounding control, measurement accuracy, attrition, and selective reporting (Table 2).")

    rob_data = [
        {
            'study': 'Plastina et al. (2020)',
            'design': 'Producer Survey (n=1,200)',
            'selection': 'Low',
            'confounding': 'Low',
            'measurement': 'Low',
            'attrition': 'Moderate',
            'reporting': 'Low',
            'overall': 'Low'
        },
        {
            'study': 'Sawadgo & Plastina (2022)',
            'design': 'Cash Rent Econometrics',
            'selection': 'Low',
            'confounding': 'Moderate',
            'measurement': 'Low',
            'attrition': 'Low',
            'reporting': 'Low',
            'overall': 'Low'
        },
        {
            'study': 'Adhikari et al. (2023)',
            'design': 'Planting Delay Agronomics',
            'selection': 'Low',
            'confounding': 'Low',
            'measurement': 'Low',
            'attrition': 'Low',
            'reporting': 'Low',
            'overall': 'Low'
        },
        {
            'study': 'Wilson (2024)',
            'design': 'Regional Simulation Model',
            'selection': 'Moderate',
            'confounding': 'Moderate',
            'measurement': 'Low',
            'attrition': 'Low',
            'reporting': 'Moderate',
            'overall': 'Moderate'
        }
    ]
    add_rob_matrix_table(doc, rob_data)

    # 4. Institutional Frictions
    add_heading_1(doc, "4. Institutional Frictions & Contractual Solutions")
    add_body(doc, "Table 3 synthesizes microeconomic bottlenecks confronting commercial growers alongside proven institutional solutions.")

    headers_t3 = ["Friction Category", "Empirical Bottleneck", "Contractual / Policy Solution", "Representative Citations"]
    data_t3 = [
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
    add_styled_table(doc, headers_t3, data_t3, header_bg="1F4E79")

    # 5. APA 7th References Section
    sample_references = [
        {
            'Authors': 'Adhikari, S.; Sharma, P.; Jones, M.',
            'Year': '2023',
            'Title': 'Agronomic and economic impacts of spring planting delays in Midwest maize systems',
            'Source': 'Field Crops Research',
            'Volume': '295',
            'Issue': '1',
            'Pages': '108890',
            'DOI': '10.1016/j.fcr.2023.108890'
        },
        {
            'Authors': 'Canales, E.; Bergtold, J. S.; Andrango, G. C.',
            'Year': '2018',
            'Title': 'Valuing investments in soil health: An application of discrete choice experiments to no-till systems',
            'Source': 'Journal of Agricultural and Resource Economics',
            'Volume': '43',
            'Issue': '3',
            'Pages': '432-452',
            'DOI': '10.22004/ag.econ.287265'
        },
        {
            'Authors': 'Plastina, A.; Liu, F.; Sawadgo, W.; Miguez, F. E.; Carlson, S.',
            'Year': '2020',
            'Title': 'Partial budgets for cover crops in Midwest row crop production',
            'Source': 'Agricultural Systems',
            'Volume': '184',
            'Issue': '',
            'Pages': '102919',
            'DOI': '10.1016/j.agsy.2020.102919'
        },
        {
            'Authors': 'Sawadgo, W.; Plastina, A.',
            'Year': '2022',
            'Title': 'Land tenure and cover crop adoption: Evidence from Iowa farmland leases',
            'Source': 'Land Economics',
            'Volume': '98',
            'Issue': '4',
            'Pages': '621-638',
            'DOI': '10.3368/le.98.4.621'
        },
        {
            'Authors': 'Schnitkey, G.',
            'Year': '2023',
            'Title': 'Planting dates and corn yield penalties across the Illinois Corn Belt',
            'Source': 'farmdoc daily',
            'Volume': '13',
            'Issue': '84',
            'Pages': '',
            'DOI': 'https://farmdocdaily.illinois.edu'
        }
    ]
    add_apa_bibliography_section(doc, sample_references, section_title="References")

    target_docx = os.path.join(output_dir, "Demo_Academic_Literature_Review.docx")
    save_document(doc, target_docx)
    print(f"\n[SUCCESS] Comprehensive demo generated! Open: {target_docx}")

if __name__ == "__main__":
    run_demo()
