#!/usr/bin/env python3
"""
Computes windowed averages from a tab-delimited file.

This script reads a tab-delimited input file, skips the first 3 header lines,
computes row-wise averages, and then computes
window-based averages over a specified window size.

Usage:
    python window_average.py \
        --input_file <path_to_input> \
        --output_file <path_to_output> \
        --window_size 100

Example:
    python window_average.py \
        --input_file data/input.tab \
        --output_file results/output.txt \
        --window_size 100
        
Output Snippet

Window Range	Average
1 to 100	5.7996
101 to 200	6.8623
201 to 300	6.2677
301 to 400	7.0659
401 to 500	6.7267


"""

import argparse
import numpy as np


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Compute windowed averages from tabular data."
    )
    parser.add_argument(
        "--input_file",
        required=True,
        help="Path to input tab-delimited file"
    )
    parser.add_argument(
        "--output_file",
        required=True,
        help="Path to output file"
    )
    parser.add_argument(
        "--window_size",
        type=int,
        default=100,
        help="Window size for averaging (default: 100)"
    )
    return parser.parse_args()


def compute_row_averages(lines):
    """
    Computing average for each row 
    Args:
        lines (list): List of lines from input file

    Returns:
        np.ndarray: Array of row averages
    """
    row_averages = []

    for line in lines[3:]:  # skip header lines
        values = line.strip().split()

        nums = []
        for v in values:
            if v.lower() != "nan":
                try:
                    nums.append(float(v))
                except ValueError:
                    continue

        if nums:
            row_averages.append(np.mean(nums))
        else:
            row_averages.append(np.nan)

    return np.array(row_averages)


def compute_window_averages(row_averages, window_size):
    """
    Computing window-based averages.

    Args:
        row_averages (np.ndarray): Array of row averages
        window_size (int): Size of each window

    Returns:
        list: List of tuples (start, end, average)
    """
    results = []

    for i in range(0, len(row_averages), window_size):
        window = row_averages[i:i + window_size]
        avg = np.nanmean(window)

        start = i + 1
        end = i + len(window)

        results.append((start, end, avg))

    return results


def write_output(output_file, results):
    """
    Writing window averages to output file.

    Args:
        output_file (str): Output file path
        results (list): Windowed results
    """
    with open(output_file, "w") as out:
        out.write("Window Range\tAverage\n")
        for start, end, avg in results:
            out.write(f"{start} to {end}\t{avg:.4f}\n")


def main():
    
    args = parse_arguments()

    with open(args.input_file, "r") as f:
        lines = f.readlines()

    row_averages = compute_row_averages(lines)
    results = compute_window_averages(row_averages, args.window_size)

    write_output(args.output_file, results)

    print(f"Saved to {args.output_file}")


if __name__ == "__main__":
    main()
