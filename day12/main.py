#!/usr/bin/env python

import re

f = open('/Users/kosta/dev/advent-of-code-17/day12/input.txt')
links = f.readlines()
graph = {}
    
for link in links:
    edges = re.findall('(\d+)\s<->\s(.*)', link)[0]
    node = edges[0]
    edges = list(map(int, edges[1].split(',')))