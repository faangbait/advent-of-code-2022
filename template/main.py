#!/usr/bin/env python
ADVENT_DAY = 1

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

import sys
sys.path.append('..')
import adventify

try:
    with open('input','r') as infile:
        main(infile)
except OSError:
    adventify.fetch_input(ADVENT_DAY)
    with open('input') as infile:
        main(infile)
