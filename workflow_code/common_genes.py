#!/usr/bin/env python3

import argparse
import pandas as pd


def run(bed1_path, bed2_path, output_path):
    """Find common genes between two BED files (based on 'name' column)."""

    # Reading BED files
    bed1 = pd.read_csv(bed1_path, sep="\t")
    bed2 = pd.read_csv(bed2_path, sep="\t")

    # Checking if 'name' column exists
    if "name" not in bed1.columns or "name" not in bed2.columns:
        raise ValueError("Both BED files must contain a 'name' column")

    # Finding intersection
    common_genes = set(bed1["name"]).intersection(set(bed2["name"]))

    # Writing output
    with open(output_path, "w") as f:
        for gene in common_genes:
            f.write(f"{gene}\n")

    print(f"Common genes saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find common genes from two BED files")

    parser.add_argument("--bed1", required=True, help="First BED file")
    parser.add_argument("--bed2", required=True, help="Second BED file")
    parser.add_argument("--output", required=True, help="Output file")

    args = parser.parse_args()

    run(args.bed1, args.bed2, args.output)
