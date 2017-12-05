#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day5/input.txt')
contents = list(map(int, f.readlines()))

exited = False
cur = 0
step = 0

while(not exited):
    next = contents[cur] + cur
    if next > len(contents) - 1:
        exited = True
    contents[cur]+=1
    cur = next
    step += 1

print(step)