"""
Academic Literature Review Word Document (.docx) Generator Template
-------------------------------------------------------------------
A modular, production-grade template using python-docx with OpenXML styling.
Features:
- Professional metadata header box
- Custom OpenXML high-contrast tables (Navy #1F4E79 headers, zebra striping)
- Standard 1-inch margins
- Centered figure embedding with academic captions
- Windows file locking fallback protection (PermissionError Errno 13)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_document():
    doc = docx.Document()
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
    return doc

# --- OpenXML Styling Utilities ---
def set_cell_background(cell, fill_hex):
    """Sets the background fill color of a table cell using OpenXML."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    """Sets internal padding (in dxa) for a table cell."""
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

# --- Typography & Content Builders ---
def add_title(doc, main_title, subtitle=""):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run(main_title)
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(17)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(16, 44, 87)

    if subtitle:
        p_sub = doc.add_paragraph()
        p_sub.paragraph_format.space_after = Pt(12)
        r_sub = p_sub.add_run(subtitle)
        r_sub.font.name = 'Calibri'
        r_sub.font.size = Pt(11)
        r_sub.font.italic = True
        r_sub.font.color.rgb = RGBColor(85, 95, 110)

def add_metadata_box(doc, meta_items):
    """
    Renders an executive metadata box.
    meta_items: list of tuples, e.g. [('Author', 'Jane Doe'), ('Date', '2026-09')]
    """
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)

    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.25

    for idx, (label, val) in enumerate(meta_items):
        r_lbl = p.add_run(f"{label}: ")
        r_lbl.font.name = 'Calibri'
        r_lbl.font.bold = True
        r_lbl.font.size = Pt(9)
        r_lbl.font.color.rgb = RGBColor(16, 44, 87)

        r_val = p.add_run(val)
        r_val.font.name = 'Calibri'
        r_val.font.size = Pt(9)
        r_val.font.color.rgb = RGBColor(40, 50, 60)

        if idx < len(meta_items) - 1:
            p.add_run("  |  ")

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(8)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(16, 44, 87)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(31, 78, 121)
    return p

def add_body(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.18
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(10)
    return p

def add_styled_table(doc, headers, data, header_bg="1F4E79"):
    """
    Renders a publication-grade table with OpenXML shading and borders.
    headers: list of column title strings
    data: list of tuples / rows
    """
    num_rows = len(data) + 1
    num_cols = len(headers)
    tbl = doc.add_table(rows=num_rows, cols=num_cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Format Header Row
    for col_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, col_idx)
        set_cell_background(cell, header_bg)
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        r = p.add_run(h_text)
        r.font.name = 'Calibri'
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    # Format Data Rows (Alternating Zebra Striping)
    for row_idx, row_values in enumerate(data, start=1):
        bg_color = "FFFFFF" if row_idx % 2 == 1 else "F9FBFD"
        for col_idx in range(num_cols):
            cell = tbl.cell(row_idx, col_idx)
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            val = str(row_values[col_idx])
            r = p.add_run(val)
            r.font.name = 'Calibri'
            if col_idx == 0:
                r.bold = True
            r.font.size = Pt(8.5)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)
    return tbl

def add_figure(doc, img_path, caption_text, width=Inches(5.4)):
    """Embeds an image centered with a standardized academic caption."""
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=width)

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Calibri'
        r_cap.font.size = Pt(8.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(85, 95, 110)

def save_document(doc, target_path):
    """
    Saves document with automatic fallback if target file is locked by Word.
    """
    os.makedirs(os.path.dirname(os.path.abspath(target_path)), exist_ok=True)
    try:
        doc.save(target_path)
        print(f"Successfully saved document: {target_path}")
        return target_path
    except PermissionError:
        base, ext = os.path.splitext(target_path)
        fallback_path = f"{base}_Updated{ext}"
        doc.save(fallback_path)
        print(f"Target file is open in Word. Saved fallback copy to: {fallback_path}")
        return fallback_path

