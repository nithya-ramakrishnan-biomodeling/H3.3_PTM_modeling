#!/usr/bin/env python3

"""
Main PTM gene processing pipeline script, to order PTM values according to H3.3 order 

Runs the full workflow by importing and calling individual modular scripts
from the 'workflow_code' package.

Usage example:
    python3 workflow_code/workflow_PTM.py \
        --h3_bed path/to/H3.3.bed \
        --ptm_bed path/to/PTM.bed \
        --ptm_tab path/to/PTM_tab.tab \
        --output_dir path/to/output_directory
"""

import argparse
from pathlib import Path

# Importing all the run functions from workflow_code modules
from common_genes import run as find_common_genes
from order_on_H33 import run as order_genes
from map_order_PTM_rows import run as map_rows
from adding_rows import run as add_rownums
from reordering_bed import run as reorder_bed
from reodering_tab import run as reorder_tab
from remove_rownum import run as remove_rownum

def main():
    parser = argparse.ArgumentParser(description="Run PTM gene processing pipeline")
    parser.add_argument("--h3_bed", required=True, help="Path to H3.3 BED file")
    parser.add_argument("--ptm_bed", required=True, help="Path to PTM BED file")
    parser.add_argument("--ptm_tab", required=True, help="Input PTM tab file")
    parser.add_argument("--output_dir", required=True, help="Directory to save outputs")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Finding common genes between two BED files
    find_common_genes(args.h3_bed, args.ptm_bed, output_dir / "common_genes.txt")

    # Step 2: Ordering common genes according to H3.3 BED file order
    order_genes(output_dir / "common_genes.txt", args.h3_bed, output_dir / "ordered_genes.txt")

    # Step 3: Mapping gene names to row numbers from PTM BED file
    map_rows(output_dir / "ordered_genes.txt", args.ptm_bed, output_dir / "mapped_rows.txt")

    # Step 4: Adding row numbers to PTM tab and bed files
    add_rownums(args.ptm_tab, args.ptm_bed, output_dir / "rownum_tab.tab", output_dir / "rownum_bed.bed")

    # Step 5: Reordering BED file according to mapped rows
    reorder_bed(output_dir / "mapped_rows.txt", output_dir / "rownum_bed.bed", output_dir / "reordered_bed.bed")

    # Step 6: Reordering tab file according to mapped rows
    reorder_tab(output_dir / "mapped_rows.txt", output_dir / "rownum_tab.tab", output_dir / "reordered_tab.tab")

    # Step 7: Removing row number column from reordered tab file
    remove_rownum(output_dir / "reordered_tab.tab", output_dir / "reordered_tab_final.tab")

    print(f"[Pipeline] Completed. Outputs saved in {output_dir}")

if __name__ == "__main__":
    main()
