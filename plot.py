#!/usr/bin/env python3

"""
Generates a heatmap for a computeMatrix tab file containing PTM signal data.

Usage:
    python3 plot_ptm_heatmap.py --input_ptm_tab path/to/PTM_tab.tab

Features:
- Skips the first 3 header lines in the tab file.
- Converts signal values to numeric and fills missing values with 0.
- X-axis: positions relative to TSS (-1kb, TSS, +1kb).
- Y-axis: genes (rows), shown every 1000 rows.
- Color-coded signal with a colorbar.
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Generate heatmap for PTM computeMatrix tab file")
    parser.add_argument("--input_ptm_tab", required=True, help="Path to reordered PTM tab file")
    args = parser.parse_args()

    # Loadind the tab file, skipping the first 3 header lines
    df = pd.read_csv(
        args.input_ptm_tab,
        sep='\t',
        comment='#',
        header=None,
        skiprows=3
    )
    df = df.replace('nan', np.nan).fillna(0)

    # Convert dataframe to float safely
    data = df.apply(pd.to_numeric, errors='coerce').fillna(0).values

    # Plot heatmap
    plt.figure(figsize=(3, 12))
    im = plt.imshow(data, cmap='bwr', aspect='auto', vmin=0, vmax=1.5) #adjust vmax as needed

    # X-axis labels
    plt.xticks([0, 100, 200], ['-1kb', 'TSS', '+1kb'])

    # Y-axis ticks every 1000 rows
    yticks = np.arange(0, data.shape[0], 1000)
    plt.yticks(yticks, yticks.tolist())
    plt.yticks([])  # Hide y-tick labels if needed
    plt.xlabel('Region relative to TSS')
    plt.ylabel('Genes')
    plt.title('PTM Signal Heatmap')

    # Colorbar
    plt.colorbar(im, label='Signal', fraction=0.02, pad=0.04)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()