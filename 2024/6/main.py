#!/usr/bin/env python3

def get(lines, x, y):
    if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        return lines[y][x]
    return None

def find_guard(lines):
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == '^':
                return (x, y)
    raise

def translate(x, y, direction):
    if direction == 'up':
        y -= 1
    elif direction == 'down':
        y += 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1
    return (x, y)

def change_direction(direction):
    if direction == 'up':
        direction = 'right'
    elif direction == 'down':
        direction = 'left'
    elif direction == 'left':
        direction = 'up'
    elif direction == 'right':
        direction = 'down'
    return direction

# part 1
# with open("./input", "r") as f:
#     lines = [line.rstrip('\n') for line in f.readlines()]
#     # horizontal, vertical, diagonal, written backwards, or even overlapping other words
#     spots = 0
#     x, y = find_guard(lines)
#     direction = 'up'
#     visited = set()
#     visited.add((x, y))
#     while True:
#         new_x, new_y = translate(x, y, direction)
#         thing = get(lines, new_x, new_y)
#         if thing == '.' or thing == '^':
#             spots += 1
#             x, y = new_x, new_y
#             visited.add((x, y))
#         elif thing == '#':
#             direction = change_direction(direction)
#         elif thing is None:
#             print(len(visited))
#             break

# part 2
def check(lines, x, y):
    times = 0
    visited = set()
    visited.add((x, y))
    direction = 'up'
    while True:
        new_x, new_y = translate(x, y, direction)
        thing = get(lines, new_x, new_y)
        # are we in an infinite loop (?) lol
        if times == 99999:
            return True
        if thing == '.' or thing == '^':
            x, y = new_x, new_y
            visited.add((x, y))
            times += 1
        elif thing == '#':
            direction = change_direction(direction)
        elif thing is None:
            return False

with open("./input", "r") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    guard_x, guard_y = find_guard(lines)
    times = 0
    # brute force the puzzle
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == '^':
                continue
            _lines = lines.copy()
            _lines[y] = line[:x] + '#' + line[x+1:]
            if check(_lines, guard_x, guard_y):
                times += 1
    print(times)
