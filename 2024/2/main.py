#!/usr/bin/env python3

def process(numbers):
    increasing = False
    if numbers[1] == numbers[0]:
        return False
    if numbers[1] > numbers[0]:
        increasing = True
    for i in range(0, len(numbers)):
        if i == 0: continue
        if not increasing and ((numbers[i] < numbers[i-1] - 3) or (numbers[i] >= numbers[i-1])):
            return False
        if increasing and ((numbers[i] > numbers[i-1] + 3) or (numbers[i] <= numbers[i-1])):
            print(numbers[i], numbers[i-1], increasing)
            return False
    return True

def _process(numbers):
    # brute force, remove numbers until it works
    for i in range(len(numbers)):
        _numbers = numbers[:i] + numbers[i+1:]
        if process(_numbers):
            return True

with open("./input", "r") as f:
    for line in f.readlines():
        numbers = line.rstrip('\n').split(' ')
        numbers = [int(x) for x in numbers]
        res = process(numbers)
        if res:
            print('safe')
        if not res:
            if _process(numbers):
                print('safe')

