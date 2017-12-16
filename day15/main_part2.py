#!/usr/bin/env python

input_a = 591
input_b = 393

FACTOR_A = 16807
FACTOR_B = 48271

DIVIDER = 2147483647

MASK = int('1111111111111111', 2)

counter = 0

for i in range(0, 5000000):
    while True:
        input_a = input_a * FACTOR_A % DIVIDER
        if input_a % 4 == 0:
            break
    
    while True:
        input_b = input_b * FACTOR_B % DIVIDER
        if input_b % 8 == 0:
            break

    if input_a & MASK == input_b & MASK:
        counter += 1

print(counter)