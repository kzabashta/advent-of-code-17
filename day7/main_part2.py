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

for child in root.children:
    print (get_cumulative_weight(child))