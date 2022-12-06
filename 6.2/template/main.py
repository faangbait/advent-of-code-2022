#!/usr/bin/env python

from io import TextIOWrapper

def main(infile: TextIOWrapper):
    input_lines = infile.readlines()

    res = 0
    
    for curline in input_lines:
        data = curline.split(",")
        pass

    print(f"{res}")
    return res

####

try:
    with open('.input','r') as infile:
        main(infile)
except OSError:
    print("No infile detected - fetch <day>")
