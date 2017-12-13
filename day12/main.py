#!/usr/bin/env python

import re

f = open('/Users/kosta/dev/advent-of-code-17/day12/input.txt')
links = f.readlines()
graph = {}

def traverse_graph(node):
    if node == 0:
        return True
    node = graph[node]
    node['is_visited'] = True
    for edge in node['edges']:
        if not graph[edge]['is_visited']:
            if traverse_graph(edge):
                return True
    return False

for link in links:
    edges = re.findall('(\d+)\s<->\s(.*)', link)[0]
    node = int(edges[0])
    edges = list(map(int, edges[1].split(',')))
    graph[node] = {'is_visited': False, 'edges': edges}

def clear_graph(graph):
    for key in graph:
        graph[key]['is_visited'] = False

total = 0

for node in graph:
    if traverse_graph(node):
        total += 1
    clear_graph(graph)

print(total)