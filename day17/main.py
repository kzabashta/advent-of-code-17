#!/usr/bin/env python

TOTAL_ITERS = 2017
STEPS = 345

circle_buffer = [0]
current = 0

for i in range(1, TOTAL_ITERS + 1):
    current = (current + STEPS) % len(circle_buffer)
    current += 1
    circle_buffer = circle_buffer[:current] + [i] + circle_buffer[current:]
    if i == TOTAL_ITERS:
        print(circle_buffer[current+1])