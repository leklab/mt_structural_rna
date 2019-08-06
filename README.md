# **mt_structural_rna**
Visual representations of mitochondrial tRNA and rRNA using SVG

## Requirements
The scripts to create SVGs use Python 3.6 and the following Python libraries:
- os
- argparse
- csv
- glob

## Contents

### RNR
- [RNR.py](RNR/RNR.py): draws SVG files for mt-rRNA using inputs from tabs separated files
- [RNR1.svg](RNR/RNR1.svg): SVG file for mt-rRNA1
- [RNR1.tsv](RNR/RNR1.tsv): input file for bases, lines, and dots for mt-rRNA1
- [RNR2.svg](RNR/RNR2.svg): SVG file for mt-rRNA2
- [RNR2.tsv](RNR/RNR2.tsv): input file for bases for mt-rRNA2
- [RNR2_pairs.tsv](RNR/RNR2_pairs.tsv): input file for bases for mt-rRNA2 with extra column of the genomic coordinates of the pair of each base

### tRNA
- [appended](tRNA/appended): all files with genomic coordinates of bases
  - [svg_appended](tRNA/svg_appended): SVG files of tRNA that shows the genomic coordinates when you hover your mouse over each base
  - [MT-T()_ appended.tsv](tRNA/appended): input of mt-tRNA containing the information from unappended tsv files and the genomic coordinates that correspond to each base for each gene
  - [pop_data.py](tRNA/appended/pop_data.py): 
  - [pop_data.tsv](tRNA/appended/pop_data.tsv): 
  - [reference_tRNA.py](tRNA/appended/reference_tRNA.py): draw reference tRNA in SVG using input of specific TSV files
  - [tRNA.py](tRNA/appended/tRNA.py): draw reference tRNA in SVG using input of specific TSV files
  - [tRNA_add_coord.sh](tRNA/appended/tRNA_add_coord.sh): appends ALL genomic coordinates to tsv files in the same directory
  - [tRNA_genes.txt](tRNA/appended/tRNA_genes.txt): 
  - [variant_all_genes.py](tRNA/appended/variant_all_genes.py): draws SVG files for a given gene showing the variant based on the input of genomic coordinate
  - [variant_single_gene.py](variant_single_gene.py): draws SVG files for a given gene showing the variant based on the input of genomic coordinate
  
- [unappended](tRNA/unappended): input of mt-tRNA information for each gene, including:
  - Type
    - b = base
    - l = lines (Watson-Crick pairs)
    - d = dots (non Watson-Crick pairs)
    - dl = dotted lines (other bonds)
  - Base
  - Coordinates

### Scripts will also prompt for
- -i: input tsv file
- Genomic Coordinate: The genomic coordinate of the mutation
- Mutation: Resulting base of the mutation
- Direction: whether the tRNA is on the positive or negative strand (pos/neg, +/-, positive/negative)

### Input/Output files
- [unappended tsv files](https://github.com/leklab/mt_structural_rna/tree/master/tsv): input of mt-tRNA information for each gene, including:
  - Type
    - b = base
    - l = lines (Watson-Crick pairs)
    - d = dots (non Watson-Crick pairs)
    - dl = dotted lines (other bonds)
  - Base
  - Coordinates
- [appended tsv files](https://github.com/leklab/mt_structural_rna/tree/master/tsv/tsv_appended): input of mt-tRNA or mt-rRNA containing the information from unappended tsv files and the genomic coordinates that correspond to each base for each gene
- [svg files](https://github.com/leklab/mt_structural_rna/tree/master/svg): output of the tsv files for each gene
