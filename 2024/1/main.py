#!/usr/bin/env python3

with open('./input', 'r') as f:
    left = []
    right = []
    # this can probably be a one-liner in a zip
    for line in f.readlines():
        line = line.rstrip('\n')
        line = line.split('   ')
        left.append(int(line[0]))
        right.append(int(line[1]))

    assert len(left) == len(right)
    left.sort()
    right.sort()

    # star 1
    # sum = 0
    # for i in range(0, len(left)):
    #     sum += max(left[i], right[i]) - min(left[i], right[i])
    # print(sum)

    # star 2
    sum = 0
    for num in left:
        sum += right.count(num) * num
    print(sum)
