import argparse

def main(args):

    fin = open(args.input)
    print('<svg height=\"400\" width=\"400\" xmlns=\"http://www.w3.org/2000/svg\">')
    print('<style>')
    print('\n \t \t text { \n \t \t \t fill: black; \n \t \t \t font-family: monospace; \n \t \t \t }')
    print('\n \t \t line { \n \t \t \t stroke: black; \n \t \t \t stroke-width: 1; \n \t \t \t }')
    print('\n \t \t circle { \n \t \t \t r: 2.5; \n \t \t \t fill: black; \n \t \t \t }')
    print('</style>')
    for line in fin:
            line = line.strip()
            fields = line.split('\t')
            if fields[0]=="b":
                    print("<text x=\"{0}\" y=\"{1}\" >{2}</text> ".format(fields[1],fields[2],fields[3]))
            elif fields[0]=='l':
                    print("<line x1=\"{0}\" y1=\"{1}\" x2=\"{2}\" y2=\"{3}\" />".format(fields[1],fields[2],fields[3],fields[4]))
            elif fields[0]=='d':
                    print("<circle cx=\"{0}\" cy=\"{1}\" r=\"2\" />".format(fields[1],fields[2]))
            elif fields[0]=='dl':
                    print("<line x1=\"{0}\" y1=\"{1}\" x2=\"{2}\" y2=\"{3}\" stroke-dasharray=\"2\" />".format(fields[1],fields[2],fields[3],fields[4]))
            else:
                print("Unrecognized field code: {0}".format(fields[0]))

    print("</svg>")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', '-i', help='Input for stuff', required=True)
    #parser.add_argument('--out', '-o', help='Output tsv file', default="")

    args = parser.parse_args()
    main(args)