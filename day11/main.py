#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day11/input.txt')
steps = f.readline().split(',')

moves = {
    'n': (0, 1),
    's': (0, -1),
    'ne': (1, 0.5),
    'nw': (-1, 0.5),
    'sw': (-1, -0.5),
    'se': (1, -0.5)
}

x_total = 0
y_total = 0

for step in steps:
    x_total += moves[step][0]
    y_total += moves[step][1]

normalized_x = abs(x_total)
normalized_y = abs(y_total)

total_steps = 0

while(True):
    total_steps += 1
    normalized_x -= 1
    normalized_y -= 0.5
    
    if normalized_x == 0:
        total_steps += normalized_y
        break

print(total_steps)
