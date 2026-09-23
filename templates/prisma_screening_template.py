"""
PRISMA 2020 Protocol RIS Parser and Screening Ledger Template
--------------------------------------------------------------
Parses raw citation exports (.ris) from Web of Science, Scopus, or PubMed,
applies documented eligibility filters, and exports an audited multi-tab Excel ledger.
"""

import os
import re
import pandas as pd

def parse_ris(file_path):
    """Parses a standard RIS citation file into a list of record dictionaries."""
    records = []
    current = {}
    
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('ER  -') or line == 'ER':
                if current:
                    records.append(current)
                    current = {}
                continue
            
            match = re.match(r'^([A-Z0-9]{2})\s*-\s*(.*)$', line)
            if match:
                tag, val = match.groups()
                tag = tag.strip()
                val = val.strip()
                if tag in current:
                    current[tag] += '; ' + val
                else:
                    current[tag] = val

    if current:
        records.append(current)

    # Standardize field names
    standard_records = []
    for r in records:
        rec = {
            'Title': r.get('TI', r.get('T1', '')),
            'Authors': r.get('AU', r.get('A1', '')),
            'Year': r.get('PY', r.get('Y1', '')),
            'Source': r.get('SO', r.get('JF', r.get('T2', ''))),
            'Abstract': r.get('AB', r.get('N2', '')),
            'Keywords': r.get('KW', ''),
            'DOI': r.get('DO', ''),
        }
        standard_records.append(rec)

    return pd.DataFrame(standard_records)

def apply_prisma_screening(df, min_year=2004, max_year=2026, exclusion_keywords=None):
    """
    Applies eligibility screening rules and tracks exact attrition reasons.
    """
    if exclusion_keywords is None:
        exclusion_keywords = ['vegetable', 'orchard', 'vineyard', 'greenhouse']

    def screen_row(row):
        title = str(row['Title']).lower()
        abstract = str(row['Abstract']).lower()
        year_str = str(row['Year'])
        
        # Check Year
        try:
            year = int(re.search(r'\d{4}', year_str).group())
            if year < min_year or year > max_year:
                return 'EXCLUDED', f'Publication year out of scope (<{min_year} or >{max_year})'
        except:
            pass

        # Check Specialty / Scope Outliers
        for kw in exclusion_keywords:
            if kw in title:
                return 'EXCLUDED', f'Specialty topic out of scope ({kw})'

        return 'INCLUDED', 'Meets systematic eligibility criteria'

    results = df.apply(screen_row, axis=1)
    df['Screening_Status'] = [r[0] for r in results]
    df['Screening_Reason'] = [r[1] for r in results]

    included_df = df[df['Screening_Status'] == 'INCLUDED'].copy()
    excluded_df = df[df['Screening_Status'] == 'EXCLUDED'].copy()

    print(f"Total Records: {len(df)}")
    print(f"Included Synthesis Pool: {len(included_df)}")
    print(f"Excluded Records: {len(excluded_df)}")

    return included_df, excluded_df

def export_prisma_excel(all_df, included_df, excluded_df, out_excel_path):
    """Exports multi-tab audited Excel ledger."""
    os.makedirs(os.path.dirname(os.path.abspath(out_excel_path)), exist_ok=True)
    with pd.ExcelWriter(out_excel_path, engine='openpyxl') as writer:
        all_df.to_excel(writer, sheet_name='All_Records', index=False)
        included_df.to_excel(writer, sheet_name='Included_Synthesis_Pool', index=False)
        excluded_df.to_excel(writer, sheet_name='Excluded_Records', index=False)
    print(f"Saved PRISMA screening ledger to: {out_excel_path}")

