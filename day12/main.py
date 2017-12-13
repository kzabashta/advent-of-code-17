#!/usr/bin/env python

import re

f = open('/Users/kosta/dev/advent-of-code-17/day12/input.txt')
links = f.readlines()
graph = {}

def traverse_graph(node):
    node['is_visited'] = True
    for edge in node['edges']:
        if graph[edge] == 0:
            return True
        if not graph[edge]['is_visited']:
            traverse_graph(graph[edge])
    return False

for link in links:
    edges = re.findall('(\d+)\s<->\s(.*)', link)[0]
    node = edges[0]
    edges = list(map(int, edges[1].split(',')))
    graph[node] = {'is_visited': False, 'edges': edges}

def clear_graph(graph):
    for key in graph:
        graph[key]['is_visited'] = False

for node in graph:
    print(traverse_graph(graph[node]))
    clear_graph(graph)