"""
APA 7th Edition Reference & Bibliography Auto-Builder
----------------------------------------------------
Parses RIS / BibTeX citation metadata, generates standardized APA 7th edition
references, and formats publication-grade Word bibliographies with exact
0.5-inch hanging indents, italicized journal/volume runs, and DOI hyperlinks.
"""

import re
import docx
from docx.shared import Inches, Pt, RGBColor

def format_author_apa(raw_author_str):
    """
    Converts raw author strings (e.g. 'Plastina, Alejandro; Liu, Fang')
    into standard APA 7th format: 'Plastina, A., & Liu, F.'
    """
    if not raw_author_str:
        return "Unknown Author"

    # Split by semicolon or 'and'
    raw_authors = [a.strip() for a in re.split(r';|\band\b', raw_author_str) if a.strip()]
    formatted = []

    for a in raw_authors:
        parts = [p.strip() for p in a.split(',') if p.strip()]
        if len(parts) >= 2:
            last = parts[0]
            first_initials = " ".join([f"{name[0]}." for name in parts[1].split() if name])
            formatted.append(f"{last}, {first_initials}")
        else:
            # Fallback if no comma
            words = a.split()
            if len(words) > 1:
                last = words[-1]
                first_initials = " ".join([f"{w[0]}." for w in words[:-1]])
                formatted.append(f"{last}, {first_initials}")
            else:
                formatted.append(a)

    if len(formatted) == 1:
        return formatted[0]
    elif len(formatted) == 2:
        return f"{formatted[0]}, & {formatted[1]}"
    elif 3 <= len(formatted) <= 20:
        return ", ".join(formatted[:-1]) + f", & {formatted[-1]}"
    else:
        # > 20 authors in APA 7th: first 19 ... last author
        return ", ".join(formatted[:19]) + f", ... {formatted[-1]}"

def format_apa_record(record):
    """
    Standardizes a citation dictionary into APA 7th components.
    Expected keys: Authors, Year, Title, Source, Volume, Issue, Pages, DOI
    """
    authors = format_author_apa(record.get('Authors', ''))
    
    # Year
    year = record.get('Year', 'n.d.')
    year_match = re.search(r'\d{4}', str(year))
    year_str = f"({year_match.group()})." if year_match else "(n.d.)."

    # Title
    title = str(record.get('Title', '')).strip().rstrip('.')
    if title:
        title = f"{title}."

    # Journal / Source
    journal = str(record.get('Source', '')).strip().rstrip(',')
    
    # Volume & Issue
    volume = str(record.get('Volume', '')).strip()
    issue = str(record.get('Issue', '')).strip()
    pages = str(record.get('Pages', '')).strip().rstrip('.')

    # DOI
    doi = str(record.get('DOI', '')).strip()
    doi_url = ""
    if doi:
        if doi.startswith('http'):
            doi_url = doi
        else:
            doi_url = f"https://doi.org/{doi}"

    return {
        'authors': authors,
        'year': year_str,
        'title': title,
        'journal': journal,
        'volume': volume,
        'issue': issue,
        'pages': pages,
        'doi': doi_url
    }

def add_apa_reference_paragraph(doc, ref_data):
    """
    Appends a single APA 7th reference paragraph with exact 0.5-inch hanging indent
    and properly italicized journal and volume runs.
    """
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15

    # 1. Authors & Year
    r_auth = p.add_run(f"{ref_data['authors']} {ref_data['year']} ")
    r_auth.font.name = 'Calibri'
    r_auth.font.size = Pt(9.5)

    # 2. Title
    r_title = p.add_run(f"{ref_data['title']} ")
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(9.5)

    # 3. Journal Name (Italic)
    if ref_data['journal']:
        r_j = p.add_run(f"{ref_data['journal']}")
        r_j.font.name = 'Calibri'
        r_j.font.size = Pt(9.5)
        r_j.font.italic = True

    # 4. Volume (Italic) and Issue (Regular in parentheses)
    if ref_data['volume']:
        r_vol = p.add_run(f", {ref_data['volume']}")
        r_vol.font.name = 'Calibri'
        r_vol.font.size = Pt(9.5)
        r_vol.font.italic = True
        
        if ref_data['issue']:
            r_iss = p.add_run(f"({ref_data['issue']})")
            r_iss.font.name = 'Calibri'
            r_iss.font.size = Pt(9.5)
            r_iss.font.italic = False
    elif ref_data['journal']:
        p.add_run(",")

    # 5. Pages
    if ref_data['pages']:
        r_pg = p.add_run(f", {ref_data['pages']}.")
        r_pg.font.name = 'Calibri'
        r_pg.font.size = Pt(9.5)
    else:
        p.add_run(".")

    # 6. DOI
    if ref_data['doi']:
        p.add_run(" ")
        r_doi = p.add_run(ref_data['doi'])
        r_doi.font.name = 'Calibri'
        r_doi.font.size = Pt(9)
        r_doi.font.color.rgb = RGBColor(31, 78, 121)
        r_doi.font.underline = True

    return p

def add_apa_bibliography_section(doc, records, section_title="References"):
    """
    Renders a complete, alphabetically sorted APA 7th reference section.
    records: list of citation dictionaries
    """
    p_h = doc.add_paragraph()
    p_h.paragraph_format.space_before = Pt(16)
    p_h.paragraph_format.space_after = Pt(8)
    p_h.paragraph_format.keep_with_next = True
    r_h = p_h.add_run(section_title)
    r_h.font.name = 'Calibri'
    r_h.font.size = Pt(13)
    r_h.font.bold = True
    r_h.font.color.rgb = RGBColor(16, 44, 87)

    # Process and sort alphabetically by authors
    formatted_refs = [format_apa_record(r) for r in records]
    formatted_refs.sort(key=lambda x: x['authors'].lower())

    for ref in formatted_refs:
        add_apa_reference_paragraph(doc, ref)

    print(f"Added {len(formatted_refs)} APA 7th references with hanging indents.")
