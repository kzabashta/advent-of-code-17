#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day5/input.txt')
#contents = list(map(int, f.readlines()))
contents = [int(i) for i in f.readlines()]
print (contents)

exited = False
cur = 0
step = 0

while(not exited):
    next = contents[cur] + cur
    if next > len(contents) - 1:
        exited = True
    if contents[cur] < 3:
        contents[cur]+=1
    else:
        contents[cur]-=1
    cur = next
    step += 1

print(step)