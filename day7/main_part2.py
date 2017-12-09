#!/usr/bin/env python

import re

from node import Node

f = open('/Users/kosta/dev/advent-of-code-17/day7/input.txt')
contents = f.readlines()

nodes = {}

for line in contents:
    struct = re.findall('([a-z]+)\s\((\d+)\)\s*(?:->)?\s*(.*)', line)[0]
    children = []
    if not struct[2] == '':
        children = [x.strip() for x in struct[2].split(',')]
    node = Node(None, struct[0], int(struct[1]), children)
    nodes[node.val] = node

for key, node in nodes.items():
    for idx, val in enumerate(node.children):
        node.children[idx] = nodes[val]
        node.children[idx].parent = node

root = None

for key, node in nodes.items():
    if node.parent == None:
        root = node
        break

def get_cumulative_weight(node):
    if len(node.children) == 0:
        return node.weight
    else:
        total = node.weight
        for child in node.children:
            total += get_cumulative_weight(child)
        return total

def find_offender(node):
    unique_weights = {}
    for child in node.children:
        sub_weights = get_cumulative_weight(child)
        if not sub_weights in unique_weights:
            unique_weights[sub_weights] = 1
        else:
            unique_weights[sub_weights] += 1
    
    offender = None

    for key, val in unique_weights.items():
        if val == 1:
            for child in node.children:
                if key == get_cumulative_weight(child):
                    offender = child
    
    if offender != None:
        print (offender.weight)
        print (unique_weights)
        return find_offender(offender)
    else:
        print (node.weight)
        return node

find_offender(root)