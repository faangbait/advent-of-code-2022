#!/usr/bin/env python
ADVENT_DAY = 4

from io import TextIOWrapper

def is_subset(x_lo: int, x_hi: int, y_lo: int, y_hi: int) -> bool:
    """ Assume False, return True if subset """
    if x_lo >= y_lo and x_hi <= y_hi:
        return True
    if x_lo <= y_lo and x_hi >= y_hi:
        return True
    return False

def main(infile: TextIOWrapper):
    lines = infile.readlines()
    print(lines)

    is_subset_count = 0

    for line in lines:
        assignments = line.split(",")

        x_assign = assignments[0].split("-")
        y_assign = assignments[1].split("-")

        overlaps = is_subset(
            int(x_assign[0].strip()),
            int(x_assign[1].strip()),
            int(y_assign[0].strip()),
            int(y_assign[1].strip())
        )

        if overlaps:
            is_subset_count += 1

        print(f"Elf 1: \t{x_assign[0]} {x_assign[1] :.>6} \tElf 2: \t{y_assign[0]}{y_assign[1].strip() :.>6} \t\t{overlaps}")

    print(f"{is_subset_count} assignments fully overlap")
    return is_subset_count

####

import sys
sys.path.append('..')
import adventify

try:
    with open('.input','r') as infile:
        main(infile)
except OSError:
    adventify.fetch_input(ADVENT_DAY)
    with open('.input') as infile:
        main(infile)
