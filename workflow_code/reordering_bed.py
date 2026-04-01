#!/usr/bin/env python3

"""
Reorders rows in File 2 based on row numbers provided in File 1.

File 1 is expected to contain gene names and a list of corresponding row numbers
in the second column. These row numbers represent the original
positions of entries in File 2.

File 2 must contain a 'row_number' column (as the last column), which is used to
map and retrieve rows.

The script:
- Extracts row numbers from File 1 in order
- Matches them to rows in File 2 using the row_number column
- Outputs a reordered version of File 2 based on this mapping
"""

def run(file1, file2, output):
    """
    Parameters:
        file1 : File with gene names and row numbers
        file2 : BED file with row_number column (last column)
        output: Path to save reordered file
    """

    # Reading file 1 and extract row numbers
    row_numbers = []
    with open(file1) as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) > 1:
                row_nums = parts[1].split(",")
                row_numbers.extend([int(num.strip()) for num in row_nums])

    print(f"[reordering_bed] Total row numbers extracted: {len(row_numbers)}")

    # Reading file 2 and store rows in a dictionary keyed by row_number
    file2_data = {}
    with open(file2) as f:
        header = f.readline().strip()
        for line in f:
            parts = line.strip().split("\t")
            row_number = int(parts[-1])  # last column = row number
            file2_data[row_number] = line.strip()

    # Reordering file 2 based on row numbers from file 1
    reordered_data = [header]
    for row_number in row_numbers:
        if row_number in file2_data:
            reordered_data.append(file2_data[row_number])

    # Writing reordered data to output file
    with open(output, 'w') as out:
        out.write("\n".join(reordered_data))

    print(f"[reordering_bed] Reordered File 2 saved: {output}")
