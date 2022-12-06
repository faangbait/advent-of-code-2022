#!/usr/bin/env python

from io import TextIOWrapper

def main(infile: TextIOWrapper):
    input_line = infile.readline()
    res = []

    for idx, char in enumerate(input_line):
        res.append(char)

        if idx < 14:
            continue
        
        marker = True
        for j in res[-14:]:
            if res[-14:].count(j) > 1:
                marker = False

        if marker:
            return idx + 1

####

try:
    with open('.input','r') as infile:
        print(main(infile))
except OSError:
    print("No infile detected - fetch <day>")
