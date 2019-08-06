import csv
import os
import argparse
import glob

parser = argparse.ArgumentParser(description="sets file name")
parser.add_argument("destination", help="Enter name of destination file")
args = parser.parse_args()

if os.path.exists(args.destination):
    print "File exists--running program"

startZoom = raw_input("Enter genomic coordinate ") 
mutation = raw_input("Enter the mutation ")

targetFile = '';
targetCoord = '';
targetx1 = '';
targety1= '';
for filename in glob.glob(os.path.join('*.tsv')):
    with open(filename, 'r') as f:
        text = f.read()
        print (filename)
        results = []
        zoomCoord = []
        with open(filename) as tsv:
            reader = csv.DictReader(tsv, delimiter="\t")
            for row in reader:
                infoType = row["Type"]
                x1 = row["x1"]
                y1 = row["y1"]
                normalBase = row["Base"]
                genCoord = row["Genomic Coordinate"]
                x2 = row["x2"]
                y2 = row["y2"]
                pair = row["Pair"]
                result = [infoType, x1, y1, normalBase, genCoord, x2, y2, pair]
                if genCoord == startZoom:
                    targetFile = filename;
                    targetCoord = genCoord;
                    targetx1 = x1;
                    targety1 = y1;
                    break;
print(targetFile);
print(targetCoord);
print(targetx1);
print(targety1);

results = []
zoomCoord = []
with open(targetFile) as tsv:
     reader = csv.DictReader(tsv, delimiter="\t")
     for row in reader:
         infoType = row["Type"]
         x1 = row["x1"]
         y1 = row["y1"]
         normalBase = row["Base"]
         genCoord = row["Genomic Coordinate"]
         x2 = row["x2"]
         y2 = row["y2"]
         pair = row["Pair"]
         result = [infoType, x1, y1, normalBase, genCoord, x2, y2, pair]
         if infoType == "b":
             if genCoord == startZoom:
                 zoomCoord.append(x1)
                 zoomCoord.append(y1)
         results.append(result)
     print 'Writing file...'
     with open(args.destination, 'w') as f:
        f.write('<svg height="2048" width="2048" xmlns="http://www.w3.org/2000/svg">\n\n')
        f.write('\n<!-- MARKERS -->\n')
        f.write('<circle cx="' + zoomCoord[0] +'" cy="' + zoomCoord[1] +'" r="20" style="fill: #42f5f5; fill-opacity: .7" >'
                + '<title>' + zoomCoord[0] + ',' + zoomCoord[1] + '</title> </circle>')
        for sublist in results:
            infoType = sublist[0]
            genCoord = sublist[4]
            normalBase = sublist[3]
            x1 = sublist[1]
            y1 = sublist[2]
            x2 = sublist[5]
            y2 = sublist[6]
            font = "monospace"
            lineColor = "black"
            circleColor = "black"
            if infoType == "b":
                if genCoord == startZoom:
                    textColor = '#ff0000'
                    fontWeight = 'bold'
                    base = mutation
                    title = 'm.' + genCoord + normalBase + '>' + base
                else:
                    textColor = '#000000'
                    fontWeight = 'normal'
                    base = normalBase
                    title = genCoord
                f.write('<text x="' + x1 + '" y="' + y1 + '" style = "font-size: 12; fill: ' + textColor
                        + '; font-family: ' + font + '; font-weight: ' + fontWeight + ';" > '
                        + base + '<title>' + title + '</title> </text>')
            elif infoType == "l":
                title = x1 + ',' + y1 + ' ' + x2 + ',' + y2
                f.write('<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" style="stroke: '
                         + lineColor + '; stroke-width:1; stroke-linecap: round" >' + '<title>' + title + '</title> </line>')
            elif infoType == "d":
                title = x1 + ',' + y1
                f.write('<circle cx="' + x1 + '" cy="' + y1 + '" r="2.5" style="fill: ' + circleColor + ';" >'
                        + '<title>' + title + '</title> </circle>')
        f.write('</svg>')
        print "Finished"