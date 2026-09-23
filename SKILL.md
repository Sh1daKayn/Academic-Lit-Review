---
name: academic-lit-review
description: >-
  End-to-end framework and automation pipeline for conducting publication-grade systematic
  literature reviews under the PRISMA 2020 protocol, designing high-contrast academic tables,
  generating 300 DPI Times New Roman figures, and compiling complete Word (.docx) manuscripts
  using Python automation and humanized academic prose standards.
---

# Academic Literature Review & Synthesis Skill

This skill provides an end-to-end blueprint and automated toolchain for creating journal-ready systematic literature reviews. It replaces ad-hoc manual drafting with a reproducible, code-driven methodology that produces publication-grade Word (`.docx`) manuscripts featuring:

1. **PRISMA 2020 Protocol Screening**: Audited identification, deduplication, eligibility filtering, and multi-tier Excel tracking from raw `.ris` database exports.
2. **Standard 7-Table Academic Architecture**: Professional tables designed for empirical synthesis, institutional frictions, contract attributes, and research design.
3. **High-Contrast Typography & XML Styling**: Programmatic table rendering via `python-docx` using custom XML shading (`#1F4E79` navy headers, alternating `#F9FBFD` zebra stripes, exact cell padding, and border hierarchy).
4. **Publication-Grade Visualizations**: 300 DPI charts styled in standard **Times New Roman** (Serif) with STIX math environments, avoiding label collisions and margin clipping.
5. **Humanized Academic Tone**: Direct, empirical, and precise academic English with zero AI tells (no staged openings, no "Not X but Y" tropes, no filler summaries, no excessive em-dashes).

---

## 🛠️ Toolchain Structure & File Layout

When initiating a new literature review project, organize the workspace as follows:

```text
project_root/
├── data/                                 # Raw literature data & screening audits
│   ├── literature_raw.ris                # Exported from WoS / Scopus / PubMed
│   └── PRISMA_Screened_Literature_Pool.xlsx # Multi-tab screening ledger
│
├── docs/                                 # Final deliverables & figures
│   ├── Literature_Review_Final.docx      # Compiled Word document
│   └── figures/                          # 300 DPI figures (Times New Roman)
│       ├── figure1_baseline_headroom.png
│       └── figure2_simulation_curves.png
│
├── scripts/                              # Automated Python pipelines
│   ├── analyze_ris.py                    # RIS parser & PRISMA audit exporter
│   ├── generate_figures.py               # 300 DPI Times New Roman visualizations
│   └── build_literature_review_docx.py   # Word document compiler
│
└── README.md                             # Methodology & reproduction guide
```

---

## 📋 The 7 Standard Academic Review Tables

A rigorous empirical review paper should structure its qualitative and quantitative evidence across these 7 standardized tables:

| Table # | Table Title | Primary Academic Purpose | Key Columns |
| :--- | :--- | :--- | :--- |
| **Table 1** | **Taxonomy & Input Dynamics** | Defines the core practices or technologies through an economic / operational lens rather than purely ecological/theoretical. | `Category`, `Operational Nature & Inputs`, `Transformation Dynamics`, `Empirical Grounding` |
| **Table 2** | **Boolean Query Architecture** | Fully documents the search strategy across database index blocks under PRISMA 2020. | `Conceptual Block`, `Boolean Query Formulation (WoS/Scopus Syntax)` |
| **Table 3** | **Audited Screening Funnel** | Reports exact record volumes and attrition criteria at each screening stage. | `Screening Stage`, `Record Volume (N)`, `Attrition Criteria & Audit Details` |
| **Table 4** | **Empirical Synthesis Matrix** | Synthesizes the core body of literature across identified thematic pillars. | `Thematic Pillar`, `Included Studies (N)`, `Empirical Findings & Metrics`, `Key Citations` |
| **Table 5** | **Microeconomic Frictions & Solutions** | Synthesizes institutional, contractual, financial, and behavioral barriers and their empirical solutions. | `Friction Category`, `Empirical Bottleneck`, `Contractual / Policy Solution`, `Key Citations` |
| **Table 6** | **Empirical Measurement Mapping** | Translates review findings into concrete variables, survey scales, or experiment attributes (e.g. DCE / Conjoint). | `Construct`, `Operational Metric / Scale`, `Literature Precedent` |
| **Table 7** | **Synthesis Scope & Boundaries** | Defines what questions the review answers and sets boundary conditions for subsequent empirical work. | `Research Phase`, `Core Objective`, `Methodology`, `Deliverable` |

---

## 🎨 High-Contrast Table Styling Standard (`python-docx`)

Never rely on Word's default table styles, which look amateurish. Use custom OpenXML cell properties:

### 1. Header Row Styling
- **Background**: Deep Navy (`#1F4E79` or `#2B4C7E`)
- **Font**: White, Bold, 9.5 pt, Calibri or Times New Roman
- **Padding**: Top/Bottom 80 dxa (~4 pt), Left/Right 100 dxa (~5 pt)

### 2. Alternating Row (Zebra) Striping
- **Odd Data Rows**: White (`#FFFFFF`)
- **Even Data Rows**: Soft Tint (`#F9FBFD` or `#F2F4F7`)
- **Font**: Regular, 8.5 pt, Left-aligned, Row-header bold

### 3. XML Helper Functions in Python
```python
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)
```

---

## 📈 Academic Visualization Standards (`matplotlib`)

All review figures must adhere to journal publication standards:

1. **Font Family**: Set `font.family: 'serif'` and `font.serif: ['Times New Roman', 'DejaVu Serif']`.
2. **Math Font**: Set `mathtext.fontset: 'stix'` to ensure symbols ($ \pm, \alpha, \$, \% $) harmonize with Times New Roman.
3. **Resolution**: `dpi=300`.
4. **Collision Avoidance**:
   - For bar charts, place percentage text inside the bar end (in white bold) if bars cross reference lines.
   - For annotations and callouts, place text boxes in open whitespace with explicit bounding boxes (`bbox=dict(...)`) and arrows pointing to the curve.
   - Always export with `bbox_inches='tight'` to eliminate edge clipping on donut/pie charts.

---

## ✍️ Humanized Academic Writing Standard

The synthesized prose must sound like a seasoned researcher writing directly for peers, not an LLM producing marketing summaries. Follow these rules:

1. **No Staged Introductions**: Never write "In this section, we delve into...", "It is important to remember that...", or "A tapestry of factors...". State findings directly: "Commercial producers face immediate cash outlays of $45 to $75 per acre...".
2. **No "Not X, but Y" Formulations**: Replace rhetorical contrasts with direct statements of fact.
3. **No Forced Triads**: Do not force arguments into three poetic adjectives or bullet points. Present the exact empirical evidence.
4. **Concrete Microeconomic Metrics**: Replace vague qualifiers ("significant cost", "major loss", "substantial delay") with specific numbers ("1.5% daily yield penalty", "$50,625 revenue shock across 750 acres", "7.2% regional adoption").
5. **No Em-Dash Connectors**: Avoid using dashes (`—`) as catch-all sentence joiners. Use semicolons, periods, or appropriate conjunctive adverbs.

---

## 🔄 End-to-End Workflow Execution

1. **Step 1: Export RIS**: Pull citation records from Web of Science or Scopus, save as `data/literature_raw.ris`.
2. **Step 2: Run PRISMA Screening**:
   ```bash
   python scripts/analyze_ris.py
   ```
   Audit exclusions and confirm the final synthesis pool count.
3. **Step 3: Generate Figures**:
   ```bash
   python scripts/generate_figures.py
   ```
   Outputs 300 DPI Times New Roman images to `docs/figures/`.
4. **Step 4: Compile Word Manuscript**:
   ```bash
   python scripts/build_literature_review_docx.py
   ```
   Renders the formatted Word document with all tables, callouts, figures, and metadata.

