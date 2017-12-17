#!/usr/bin/env python

TOTAL_ITERS = 50000000
STEPS = 345

circle_buffer_length = 1
current = 0
current_short_circuit_val = 0

for i in range(1, TOTAL_ITERS + 1):
    current = (current + STEPS) % circle_buffer_length
    current += 1
    # it always grows by 1
    circle_buffer_length += 1
    # capture latest known value at position 1
    if current == 1:
        current_short_circuit_val = i

print(current_short_circuit_val)