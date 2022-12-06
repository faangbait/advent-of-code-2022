#!/usr/bin/env python

from io import TextIOWrapper
import re


def main(infile: TextIOWrapper):
    input_lines = infile.readlines()

    res = [
        list(""),
        list("BPNQHDRT"),  # Note: this is technically a stack with T at the 'top'
        list("WGBJTV"),
        list("NRHDSVMQ"),
        list("PZNMC"),
        list("DZB"),
        list("VCWZ"),
        list("GZNCVQLS"),
        list("LGJMDNV"),
        list("TPMFZCG")
    ]

    for curline in input_lines:
        matches = re.match(
            r'^move (?P<count>\d+) from (?P<start_idx>\d+) to (?P<end_idx>\d+)$', curline)
        if matches is not None:
            count = int(matches.groupdict().get("count", None))
            start_idx = int(matches.groupdict().get("start_idx", None))
            end_idx = int(matches.groupdict().get("end_idx", None))

            for _ in range(count):
                crane = res[start_idx].pop()
                res[end_idx].append(crane)
            print(
                f"{count}\t{start_idx}\t{end_idx}\t\t"
                f"{[''.join(i) for i in res]}"
            )
    return ''.join([i[-1] for i in res if len(i) > 0])

####


try:
    with open('.input', 'r') as infile:
        print(main(infile))
except OSError:
    print("No infile detected - fetch <day>")
