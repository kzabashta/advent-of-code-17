#!/usr/bin/env python

import re

f = open('/Users/kosta/dev/advent-of-code-17/day8/input.txt')
contents = f.readlines()

registers = {}

for line in contents:
    struct = re.findall(
        '([a-z]+)\s(inc|dec)\s(-?\d+)\sif\s([a-z]+)\s(.*)\s(-?\d+)', line)[0]

    register = struct[0]
    operand = struct[1]
    change = int(struct[2])
    cond_register = struct[3]
    cond_operand = struct[4]
    cond_val = int(struct[5])

    if not cond_register in registers:
        registers[cond_register] = 0

    if not register in registers:
        registers[register] = 0

    condition = eval('registers[\'%s\'] %s %i' %
                     (cond_register, cond_operand, cond_val))

    if condition:
        registers[register] += change if operand == 'inc' else -change

    maximum_register = max(registers, key=registers.get)

print(registers[maximum_register])