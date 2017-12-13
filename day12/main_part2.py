#!/usr/bin/env python

import re

f = open('/Users/kosta/dev/advent-of-code-17/day12/input.txt')
links = f.readlines()
graph = {}
groups = []

def traverse_graph(node, key):
    if node == key:
        return True
    node = graph[node]
    node['is_visited'] = True
    for edge in node['edges']:
        if not graph[edge]['is_visited']:
            if traverse_graph(edge, key):
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

nodes = list(graph.keys())

while len(nodes) > 0:
    lookup = nodes[0]
    to_remove = []
    for node in nodes:
        clear_graph(graph)
        if traverse_graph(node, lookup):
            to_remove.append(node)
    for node in to_remove:
        nodes.remove(node)
    total+=1

print(total)