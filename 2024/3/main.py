#!/usr/bin/env python3

import re

with open("./input2", "r") as f:
    res = 0
    for line in f.readlines():
        line = line.rstrip('\n')
        line = re.sub(r"don't\(\).*?do\(\)", '', line)
        line = re.sub(r"don't\(\).*", '', line)
        muls = re.findall(r'mul\((\d+),(\d+)\)', line)
        for x, y in muls:
            res += int(x) * int(y)
    print(res)
