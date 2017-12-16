#!/usr/bin/env python

import re
import string

def handle_spin(x):
    pass

def handle_exchange(a, b):
    pass

def handle_partner(a, b):
    pass

def dance(progs, moves):
    for move in moves:
        if move[0] == 's':
             progs = handle_spin()

if __name__ == '__main__':
    progs = list(string.ascii_lowercase)[:16]
    f = open('/Users/kosta/dev/advent-of-code-17/day16/input.txt')
    moves = f.read().split(',')



"""layers = {}
total_layers = 0

for line in lines:
    parsed_layer = re.findall('(\d+):\s(\d+)', line)[0]
    layers[int(parsed_layer[0])] = {'current': 0, 'dir': 1, 'max': int(parsed_layer[1])}
    total_layers = int(parsed_layer[0])

severity = 0

for i in range(0, total_layers+1):
    if i in layers and layers[i]['current'] == 0:
        severity += i * layers[i]['max']
    for depth in layers:
        if layers[depth]['current'] == layers[depth]['max'] - 1:
            layers[depth]['dir'] = -1
        elif layers[depth]['current'] == 0:
            layers[depth]['dir'] = 1
        layers[depth]['current'] += layers[depth]['dir']

print(severity)
"""