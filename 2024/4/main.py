#!/usr/bin/env python3

def get(lines, x, y):
    if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        return lines[y][x]
    return None

# cursed
def is_xmas(lines, i, j):
    # horizontal
    times = 0
    if get(lines, i - 1, j) == 'M' and get(lines, i - 2, j) == 'A' and get(lines, i - 3, j) == 'S':
        times += 1
    if get(lines, i + 1, j) == 'M' and get(lines, i + 2, j) == 'A' and get(lines, i + 3, j) == 'S':
        times += 1
    # vertical
    if get(lines, i, j + 1) == 'M' and get(lines, i, j + 2) == 'A' and get(lines, i, j + 3) == 'S':
        times += 1
    if get(lines, i, j - 1) == 'M' and get(lines, i, j - 2) == 'A' and get(lines, i, j - 3) == 'S':
        times += 1
    # diagonal
    if get(lines, i + 1, j + 1) == 'M' and get(lines, i + 2, j + 2) == 'A' and get(lines, i + 3, j + 3) == 'S':
        times += 1
    if get(lines, i - 1, j + 1) == 'M' and get(lines, i - 2, j + 2) == 'A' and get(lines, i - 3, j + 3) == 'S':
        times += 1
    if get(lines, i + 1, j - 1) == 'M' and get(lines, i + 2, j - 2) == 'A' and get(lines, i + 3, j - 3) == 'S':
        times += 1
    if get(lines, i - 1, j - 1) == 'M' and get(lines, i - 2, j - 2) == 'A' and get(lines, i - 3, j - 3) == 'S':
        times += 1
    return times

def is_mas(lines, i, j):
    times = 0

    if ( (get(lines, i - 1, j + 1) == 'M' and get(lines, i + 1, j - 1) == 'S') or (get(lines, i - 1, j + 1) == 'S' and get(lines, i + 1, j - 1) == 'M') ) and ( (get(lines, i + 1, j + 1) == 'S' and get(lines, i - 1, j - 1) == 'M') or (get(lines, i + 1, j + 1) == 'M' and get(lines, i - 1, j - 1) == 'S') ):
        return 1
    return times

with open("./input", "r") as f:
    found = 0
    lines = [line.rstrip('\n') for line in f.readlines()]
    # horizontal, vertical, diagonal, written backwards, or even overlapping other words
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            # begin search
            # part 1
            # if letter == 'X':
            #     if times := is_xmas(lines, x, y):
            #         print('found at least 1 xmas at', x, y)
            #     found += times
            # part 2
            if letter == 'A':
                if times := is_mas(lines, x, y):
                    print('found mas at', x, y)
                found += times
    print(found)
