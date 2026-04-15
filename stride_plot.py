#!/usr/bin/env python3
"""
Plot stride-based (windowed) averages from a file.

Usage:
    python stride_plot.py --input_file <path_to_input>

Example:
    python stride_plot.py --input_file stride_avg_100_output.txt
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser(
        description="Plot stride/window-based averages."
    )
    parser.add_argument(
        "--input_file",
        required=True,
        help="Path to input file (tab-delimited)"
    )
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.input_file, sep="\t")
    df["Index"] = range(len(df))

    x = df["Index"]
    y = df["Average"]

    # Plot
    plt.figure(figsize=(14, 6))
    plt.plot(x, y, linewidth=1)

    plt.title("Stride-based Average per Interval", fontsize=10)
    plt.xlabel("Window Index", fontsize=9)
    plt.ylabel("Average Value", fontsize=9)

    plt.xticks(np.arange(0, len(x) + 1, 10))
    plt.yticks(np.arange(0, 11.5, 0.5))

    plt.grid(True, which='major', linestyle='-', linewidth=0.5)
    plt.tick_params(axis='both', which='major', labelsize=8)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
