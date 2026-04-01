#!/usr/bin/env python3

"""
Maps gene names from file1 to their corresponding row numbers in file2.
For each gene in file1, all occurrences in file2 (BED file) are recorded.
The output preserves the order of genes from file1 and lists all row indices.
"""

def run(file1, file2, output):
    """
    Parameters:
        file1 : Path to File 1 (gene names)
        file2 : Path to File 2 (BED file)
        output: Path to save output
    """

    # Reading file 1 and extracting gene names
    gene_names = []
    with open(file1) as f:
        for line in f:
            parts = line.strip().split("\t")
            gene_names.append(parts[1])  # Gene name is in 2nd column

    # Reading file 2 and creating a mapping from gene name to row numbers
    gene_to_row_numbers = {gene: [] for gene in gene_names}

    with open(file2) as f:
        f.readline()  # Skip header
        for row_number, line in enumerate(f, start=2):  # Starting from row 2
            parts = line.strip().split("\t")
            gene_id = parts[3]  # Gene ID in 4th column
            if gene_id in gene_to_row_numbers:
                gene_to_row_numbers[gene_id].append(row_number)

    # Writing the output file
    with open(output, 'w') as out:
        for gene in gene_names:
            row_numbers = ", ".join(map(str, gene_to_row_numbers[gene]))
            out.write(f"{gene}\t{row_numbers}\n")

    print(f"[map_order_PTM_rows] Output file saved: {output}")
