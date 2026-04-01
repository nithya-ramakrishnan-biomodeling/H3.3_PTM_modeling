#!/usr/bin/env python3

"""
Adds a row_number column to two tab-delimited input files.
For Tab and Bed files of the Compute Matrix outputs of a PTM
"""

def run(file1, file2, output1, output2):
    """
    Parameters:
        file1   : Path to File 1
        file2   : Path to File 2
        output1 : Output path for updated File 1
        output2 : Output path for updated File 2
    """

    # Reading file 1 and add row number column
    with open(file1) as f:
        file1_lines = f.readlines()

    with open(output1, 'w') as out:
        header1 = file1_lines[0].strip() + "\trow_number"
        out.write(header1 + "\n")
        for row_number, line in enumerate(file1_lines[1:], start=1):
            out.write(line.strip() + f"\t{row_number + 1}\n")

    print(f"[adding_rownums] Updated file 1 saved: {output1}")

    # Reading file 2 and add row number column
    with open(file2) as f:
        file2_lines = f.readlines()

    with open(output2, 'w') as out:
        header2 = file2_lines[0].strip() + "\trow_number"
        out.write(header2 + "\n")
        for row_number, line in enumerate(file2_lines[1:], start=1):
            out.write(line.strip() + f"\t{row_number + 1}\n")

    print(f"[adding_rownums] Updated file 2 saved: {output2}")
