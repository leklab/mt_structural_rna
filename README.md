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
- [RNR.py](RNR/RNR.py): draws SVG files for mt-rRNA using inputs from tabs separated values files
- [RNR1.svg](RNR/RNR1.svg): SVG file for mt-rRNA1
- [RNR1.tsv](RNR/RNR1.tsv): input file for bases, lines, and dots for mt-rRNA1
- [RNR1_pairs.tsv](RNR/RNR1_pairs.tsv): input file for bases for mt-rRNA1 with extra column of the genomic coordinates of the pair of each base
- [RNR2.svg](RNR/RNR2.svg): SVG file for mt-rRNA2
- [RNR2.tsv](RNR/RNR2.tsv): input file for bases for mt-rRNA2
- [RNR2_pairs.tsv](RNR/RNR2_pairs.tsv): input file for bases for mt-rRNA2 with extra column of the genomic coordinates of the pair of each base

### tRNA
- [appended](tRNA/appended): all files of or relating to genomic coordinates of tRNA bases
  - [svg_appended](tRNA/svg_appended): SVG files of tRNA that show the genomic coordinates when you hover your mouse over each base
  - [MT-T()_ appended.tsv](tRNA/appended): input of each mt-tRNA containing the information from unappended tsv files and the genomic coordinates that correspond to each base
  - [pop_data.py](tRNA/appended/pop_data.py): upon input of the tsv file of a certain tRNA, produces a SVG image that represents bases with common mutations from [pop_data.tsv](tRNA/appended/pop_data.tsv) in red and other bases in black
  - [pop_data.tsv](tRNA/appended/pop_data.tsv): Gnomad population data of the common mutations at every base from a study of ~17000 individuals
  - [reference_tRNA.py](tRNA/appended/reference_tRNA.py): draws reference tRNA in SVG using input of specific TSV files
  - [tRNA.py](tRNA/appended/tRNA.py): another code to draw reference tRNA in SVG using input of specific TSV files
  - [tRNA_add_coord.sh](tRNA/appended/tRNA_add_coord.sh): appends ALL genomic coordinates to tsv files in the same directory
  - [tRNA_genes.txt](tRNA/appended/tRNA_genes.txt): information of start and end genomic coordinates and direction of each tRNA used in [tRNA_add_coord.sh](tRNA/appended/tRNA_add_coord.sh)
  - [variant_all_genes.py](tRNA/appended/variant_all_genes.py): upon insert of the genomic coordinate and base of a mutation, searches through all tRNA tsv files to produce a SVG image of the tRNA on which the mutation lies with the mutated base highlighted and changed
  - [variant_single_gene.py](tRNA/appended/variant_single_gene.py): upon insert of the genomic coordinate and base of a mutation and the tRNA on which it lies, produces a SVG image of the tRNA on which the mutation lies with the mutated base highlighted and changed
  
- [unappended](tRNA/unappended): input of mt-tRNA information for each gene, including:
  - Type
    - b = base
    - l = lines (Watson-Crick pairs)
    - d = dots (non Watson-Crick pairs)
    - dl = dotted lines (other bonds)
  - Base
  - Coordinates
  
### Command line inputs
-  [reference_tRNA.py](tRNA/appended/reference_tRNA.py): python reference_tRNA.py -i MT-T().tsv
- every other python script: python   ().py   (input file).tsv   (output file).svg
- [tRNA_add_coord.sh](tRNA/appended/tRNA_add_coord.sh): source tRNA_add_coord.sh * .tsv

### variant scripts will prompt for
- Genomic Coordinate: The genomic coordinate of the mutation
- Mutation: Resulting base of the mutation
- Direction: whether the tRNA is on the positive or negative strand (pos/neg, +/-, positive/negative)
