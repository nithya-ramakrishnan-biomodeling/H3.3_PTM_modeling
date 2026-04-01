PTM Workflow Pipeline

This repository contains a Python workflow to process H3.3 and PTM BED/tab files and generate reordered outputs.

USAGE

python3 workflow_code/workflow_PTM.py \
    --h3_bed path/to/H3.3.bed \
    --ptm_bed path/to/PTM.bed \
    --ptm_tab path/to/PTM_tab.tab \
    --output_dir path/to/output_directory


INPUT FILES
--h3_bed     : H3.3 BED file
--ptm_bed    : PTM BED file
--ptm_tab    : PTM tab file


OUTPUT

The workflow generates:

- common_genes.txt
- ordered_genes.txt
- mapped_rows.txt
- rownum_tab.tab
- rownum_bed.bed
- reordered_bed.bed
- reordered_tab.tab
- reordered_tab_final.tab

All files are saved in the specified output directory.

