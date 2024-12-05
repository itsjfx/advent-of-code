#!/usr/bin/env python3

from collections import defaultdict
from functools import cmp_to_key

depends = defaultdict(list)

def get_middle_element(lst):
    mid = len(lst) // 2
    return lst[mid]

def process(numbers):
    seen = []
    for number in numbers:
        if number in depends:
            for dependency in depends[number]:
                if dependency in numbers and dependency not in seen:
                    return
        seen.append(number)
    return True

def compare(item1, item2):
    if item1 not in depends and item2 not in depends:
        return 0

    if item1 in depends and item2 in depends[item1]:
        return 1

    if item2 in depends and item1 in depends[item2]:
        return -1

    return 0

with open("./input2", "r") as f:
    searching_for_deps = True
    for line in f.readlines():
        line = line.rstrip('\n')
        if line == '':
            searching_for_deps = False
            continue

        if searching_for_deps:
            dependency, num = line.split('|')
            depends[num].append(dependency)
            continue

        numbers = line.split(',')
        result = process(numbers)
        # part 1
        # if result:
        #     print(get_middle_element(numbers))
        # part 2
        if not result:
            fixed = sorted(numbers, key=cmp_to_key(compare))
            print(get_middle_element(fixed))
