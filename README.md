# Academic Literature Review Workbench & Skill 📚

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![PRISMA 2020](https://img.shields.io/badge/PRISMA-2020%20Compliant-green.svg)](http://www.prisma-statement.org/)
[![OpenXML Word Tables](https://img.shields.io/badge/Word%20Output-OpenXML%20Tables-1F4E79.svg)](https://python-docx.readthedocs.io/)
[![Figures](https://img.shields.io/badge/Figures-Times%20New%20Roman%20%7C%20300%20DPI-C0392B.svg)](https://matplotlib.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **An end-to-end framework and automation pipeline for conducting publication-grade systematic literature reviews under the PRISMA 2020 protocol, designing high-contrast academic tables, generating 300 DPI Times New Roman figures, and compiling complete Word (`.docx`) manuscripts using Python automation and humanized academic prose standards.**

---

## 🌟 Why This Toolkit?

Most academic literature reviews generated with standard LLMs or manual copy-pasting suffer from common problems:
* **Amateurish Word Tables**: Default Word table formatting looks like raw spreadsheet dumps with no contrast or padding.
* **Low-Res, Sans-Serif Charts**: Matplotlib default charts use generic sans-serif fonts, low DPI, and clipped labels that don't match journal guidelines.
* **Flawed Screening Audits**: Lack of a formal PRISMA 2020 record flow leading to reviewer skepticism.
* **"AI-Smelling" Prose**: Staged openings (*"In this section, we delve into..."*), forced triads, and rhetorical contrasts (*"Not X, but Y"*).

**Academic Literature Review Workbench** solves these issues with a code-driven, reproducible pipeline that pairs rigorous systematic methodology with publication-grade design standards.

---

## 🚀 Key Features

| Feature | Description |
| :--- | :--- |
| **🔍 PRISMA 2020 Protocol Screening** | Automated `.ris` citation parsing (Web of Science / Scopus / PubMed), duplicate removal, eligibility attrition logging, and multi-tab Excel export. |
| **📊 PRISMA 2020 Flow Diagram Generator** | Automated rendering of publication-grade PRISMA 2020 flowcharts (`Identification → Screening → Included`) in Times New Roman at 300 DPI. |
| **📖 APA 7th Reference Auto-Builder** | Formats raw citation metadata into APA 7th references with precise 0.5-inch hanging indents, italicized journal/volume runs, and active DOI hyperlinks. |
| **🛡️ Risk of Bias (RoB) Assessment Matrix** | Fulfills ROBINS-I / Cochrane standards with custom OpenXML tables featuring color-coded risk badge cells (`Low` green, `Moderate` amber, `High` red). |
| **📑 7 Core Review Table Schemas** | Standardized blueprints for practice taxonomy, Boolean search design, screening attrition, empirical synthesis, institutional frictions vs. solutions, and empirical measurement mapping. |
| **🎨 OpenXML High-Contrast Tables** | Programmatic table styling via `python-docx` with Deep Navy (`#1F4E79`) headers, alternating `#F9FBFD` zebra striping, custom cell padding, and bold row identifiers. |
| **📈 Journal-Grade Visualizations** | 300 DPI charts in standard **Times New Roman** (Serif) with STIX math symbols, automatic annotation collision avoidance, and border-protected layouts. |
| **✍️ Humanized Academic Tone** | Strict prose editing guidelines that eliminate LLM cliches, ensuring concise, causal, and quantitative academic English. |
| **⚡ Windows File-Lock Fallback** | Automatic fallback handling for `[Errno 13] PermissionError` when the target `.docx` file is open in Microsoft Word. |

---

## 📂 Repository Layout

```text
Academic-Lit-Review/
├── SKILL.md                          # Antigravity / Agentic AI Skill specification
├── requirements.txt                  # Python dependencies
├── LICENSE                           # MIT License
├── README.md                         # Project documentation
│
├── templates/                        # Modular, production-ready Python templates
│   ├── docx_builder_template.py      # Word manuscript compiler with OpenXML styling
│   ├── figure_generator_template.py  # 300 DPI Times New Roman Matplotlib generator
│   ├── prisma_screening_template.py  # RIS parser & PRISMA Excel screening ledger
│   ├── prisma_flowchart_generator.py # ★ NEW: PRISMA 2020 flow diagram auto-generator
│   ├── apa_reference_builder.py      # ★ NEW: APA 7th bibliography builder with hanging indents
│   └── rob_matrix_template.py        # ★ NEW: ROBINS-I / Cochrane Risk of Bias matrix
│
└── examples/                         # Reference blueprints & runnable demos
    ├── table_blueprints.md           # Schemas & examples for the 7 core academic tables
    └── demo_quickstart.py            # Comprehensive runnable end-to-end demo
```

---

## 📋 The 7 Standard Academic Review Tables

A rigorous empirical review paper should structure its qualitative and quantitative evidence across these 7 standardized tables:

1. **Table 1: Taxonomy & Input Dynamics** — Defines practices through operational resource allocations and immediate variable cash outlays vs. multi-year capital appreciation.
2. **Table 2: Boolean Search Architecture** — PRISMA 2020 Boolean query formulations across conceptual blocks (Practices, Cropping Systems, Geography, Decision Agents, Microeconomic Drivers).
3. **Table 3: Audited Screening Funnel** — Identification, deduplication, and eligibility attrition counts ($N$ values).
4. **Table 4: Thematic Empirical Synthesis Matrix** — Synthesizes quantitative metrics, effect sizes, and landmark citations across core thematic pillars.
5. **Table 5: Institutional & Microeconomic Frictions vs. Solutions** — Detailed mapping of real-world operational bottlenecks against market/contractual mechanisms (e.g., Green Leases, insurance discounts).
6. **Table 6: Empirical Measurement & Survey Parameter Mapping** — Operationalizes review findings into concrete variables, survey scales, and Discrete Choice Experiment (DCE / Conjoint) attributes.
7. **Table 7: Research Scope & Boundary Conditions** — Defines phases, core objectives, and deliverables.

---

## ⚡ Quick Start

### 1. Installation

Clone this repository and install the lightweight dependencies:

```bash
git clone https://github.com/Sh1daKayn/Academic-Lit-Review.git
cd Academic-Lit-Review
pip install -r requirements.txt
```

### 2. Run the Demo

Run the bundled demonstration to generate a publication-ready Word manuscript and a 300 DPI figure in seconds:

```bash
python examples/demo_quickstart.py
```

The compiled document will be saved to `examples/output/Demo_Academic_Literature_Review.docx`.

---

## 🤖 Using as an AI Agent Skill

This repository is formatted as a native **Agent Skill** compatible with **Google Antigravity**, **Cursor**, **Claude Code**, and **Gemini CLI**.

### Option A: Install in Antigravity / Gemini CLI
Copy this repository into your project's `.agents/skills/` directory or global skills:

```bash
# Workspace-specific installation:
git clone https://github.com/Sh1daKayn/Academic-Lit-Review.git .agents/skills/academic-lit-review

# Global installation (available across all projects):
git clone https://github.com/Sh1daKayn/Academic-Lit-Review.git ~/.gemini/config/skills/academic-lit-review
```

### Option B: Prompt Your AI Assistant
Once installed, instruct your AI assistant:
> *"Please conduct a systematic literature review on [Your Topic] following the `academic-lit-review` skill guidelines. Use PRISMA 2020 protocol, construct the 7 core academic tables, generate 300 DPI Times New Roman figures, and compile the final Word manuscript."*

---

## 🎨 Typography & Design Specifications

* **Manuscript Typography**: 1-inch standard margins; Calibri 17pt (Title), 13.5pt (H1, Deep Navy `#102C57`), 11.5pt (H2, `#1F4E79`), 10pt (Body text, 1.18 line spacing).
* **Table OpenXML Properties**: 
  - Header Row: Background `#1F4E79`, Font White Bold 9.5pt, Cell Padding `80 dxa` vertical, `100 dxa` horizontal.
  - Alternating Rows: White (`#FFFFFF`) and Light Tint (`#F9FBFD`), Font 8.5pt, Row-header bold.
* **Visualization Standard**:
  - Matplotlib: `font.family = 'serif'`, `font.serif = ['Times New Roman', 'DejaVu Serif']`, `mathtext.fontset = 'stix'`.
  - Resolution: `dpi = 300`.
  - Annotations: Smart bounding boxes (`bbox_inches='tight'`) and inside-bar labels to eliminate collision with reference benchmark lines.

---

## 📄 License

Distributed under the [MIT License](LICENSE). Copyright (c) 2026 Sh1daKayn.

