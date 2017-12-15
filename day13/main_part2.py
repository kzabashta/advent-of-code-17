#!/usr/bin/env python

import re
from copy import deepcopy

f = open('/Users/kosta/dev/advent-of-code-17/day13/input.txt')
lines = f.readlines()

g_layers = {}
total_layers = 0

for line in lines:
    parsed_layer = re.findall('(\d+):\s(\d+)', line)[0]
    g_layers[int(parsed_layer[0])] = {'current': 0, 'dir': 1, 'max': int(parsed_layer[1])}
    total_layers = int(parsed_layer[0])

def move_sensors(_layers):
    for depth in _layers:
        if _layers[depth]['current'] == _layers[depth]['max'] - 1:
            _layers[depth]['dir'] = -1
        elif _layers[depth]['current'] == 0:
            _layers[depth]['dir'] = 1
        _layers[depth]['current'] += _layers[depth]['dir']
    return _layers

def can_traverse_layers(_layers):
    for i in range(0, total_layers+1):
        if i in _layers and _layers[i]['current'] == 0:
            return False
        for depth in _layers:
            if _layers[depth]['current'] == _layers[depth]['max'] - 1:
                _layers[depth]['dir'] = -1
            elif _layers[depth]['current'] == 0:
                _layers[depth]['dir'] = 1
            _layers[depth]['current'] += _layers[depth]['dir']
    return True

total_wait = 0

while True:
    if can_traverse_layers(deepcopy(g_layers)):
        break
    else:
        g_layers = move_sensors(g_layers)
        total_wait += 1
        
print(total_wait)