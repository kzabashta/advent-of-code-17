#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day6/input.txt')
banks = list(map(int, f.readline().split()))

i = 0
loops = 1
patterns = {}
circuit_breaker = False

while(True):
    largest_index = 0
    largest = banks[0]
    # find largest index
    for idx, bank in enumerate(banks):
        if bank > largest:
            largest = bank
            largest_index = idx
    # re-distribute
    j = largest_index + 1
    banks[largest_index] = 0
    while (largest > 0):
        if j > len(banks) - 1:
            j = 0
        banks[j] += 1
        largest -= 1
        j+=1
    if tuple(banks) in patterns:
        loops -= patterns[tuple(banks)]
        break
    patterns[tuple(banks)] = loops
    loops += 1
print(loops)