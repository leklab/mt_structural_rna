import csv
import os
import argparse

parser = argparse.ArgumentParser(description="sets file name")
parser.add_argument("startfile", help="Enter name of data file")
parser.add_argument("destination", help="Enter name of destination file")
parser.add_argument("coordinate", help="Enter genomic coordinate")
parser.add_argument("direction", help="Enter direction")
args = parser.parse_args()

if os.path.exists(args.startfile) and os.path.exists(args.destination):
    print "All files exist--running program"

    with open(args.startfile) as tsv:
        reader = csv.DictReader(tsv, delimiter="\t")
        with open(args.destination, 'w') as f:

            f.write('Type\tGenomic Coordinate\tx1\ty1\tBase\tx2\ty2')
            genom_coord = int(args.coordinate)
            for row in reader:
                infoType = row["Type"]
                x1 = row["x1"]
                y1 = row["y1"]
                base = row["Base"]
                x2 = row["x2"]
                y2 = row["y2"]
                if infoType == "b":
                    if args.direction == "+" or args.direction == "pos":
                        genom_coord = genom_coord + 1
                    elif args.direction == "-" or args.direction == "neg":
                        genom_coord = genom_coord - 1
                elif infoType == "l":
                    f.write('\n' + infoType + '\t\t' + x1 + '\t' + y1 + '\t\t' + x2 + '\t' + y2)
                elif infoType == "d":
                    f.write('\n' + infoType + '\t\t' + x1 + '\t' + y1)
                elif infoType == "dl":
                    f.write('\n' + infoType + '\t\t' + x1 + '\t' + y1 + '\t\t' + x2 + '\t' + y2)
            print "Finished"
else:
    print "error"