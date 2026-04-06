#!/usr/bin/env python3

"""
Reorders common genes according to H3.3 BED file order.
"""

def run(input_common_genes, h3_bed_file, output_file):
    """
    Parameters:
        input_common_genes : path to common genes file     sample ex: common_genes.txt
        h3_bed_file        : path to H3.3 BED file         sample ex: H3.3_CT0.bed
        output_file        : path to save reordered file   sample ex: ordered_genes.txt

        Output Snippet (head -10 ordered_genes.txt)

        2	NR_046233
        3	NM_177780
        4	NM_001362405
        5	NR_155555
        6	NM_001362404
        7	NM_178640
        9	NM_001164256
        10	NM_001164252
        11	NM_001164254
        12	NM_001164253

    """
    
    # Reading common genes
    with open(input_common_genes, 'r') as f:
        common_genes = set(line.strip() for line in f)

    output_lines = []

    # Processing the BED file
    with open(h3_bed_file, 'r') as f:
        f.readline()  # Skip header
        for i, line in enumerate(f, start=2):  # start=2 since header is line 1
            parts = line.rstrip('\n').split('\t')
            gene_name = parts[3]  # 4th column = gene name
            if gene_name in common_genes:
                output_lines.append(f"{i}\t{gene_name}")

    # Writing to output file
    with open(output_file, 'w') as out:
        out.write("\n".join(output_lines))

    print(f"[order_on_H3_3] File with common genes and row numbers saved: {output_file}")
