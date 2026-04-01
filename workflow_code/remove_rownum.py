#!/usr/bin/env python3

"""
Removes the 201st column from a tab-delimited file, starting from line 4.
This is for computeMatrix tab files generated with 200 bins.

- The first three lines (headers) are preserved as-is.
- For all subsequent lines, the 201st column (index 200) is removed if it exists.
- The modified file is written to the specified output path.
"""

def run(input_file, output_file):
    """
    Parameters:
        input_file  :Path to the input tab file
        output_file : Path to save the modified file
    """

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Copying first three header lines as-is
        for _ in range(3):
            outfile.write(infile.readline())

        # Processing the rest of the lines
        for line in infile:
            columns = line.strip().split('\t')
            if len(columns) > 200:  # Removing 201st column (index 200)
                del columns[200]
            outfile.write('\t'.join(columns) + '\n')

    print(f"[remove_rownum] File processing complete. Modified file saved: {output_file}")
