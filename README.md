# **mt_structural_rna**
Visual representations of mitochondrial tRNA and rRNA using SVG

## Requirements
The scripts to create SVGs use Python 3.6 and the following Python libraries:
- os
- argparse
- csv

## Content

### Programs
- [rrna.py](mt_structural_rna/rrna.py): draws SVG files for mt-rRNA using inputs from tabs separated files
- variant.py: draws SVG files for a given gene showing the variant based on the input of genomic coordinate
- tRNA_add_coord.sh: appends genomic coordinates to tsv files
- reference_tRNA.py: draw reference tRNA in SVG using input of specific TSV files

### Input/Output files
- unappended tsv files: input of mt-tRNA information for each gene, including:
  - Type
    - b = base
    - l = lines
    - d = dots
    - dl = dotted lines
  - Base
  - Coordinates
- appended tsv files: input of mt-tRNA or mt-rRNA containing the information from unappended tsv files and the genomic coordinates that correspond to each base for each gene
- svg files: output of the tsv files for each gene
