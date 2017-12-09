#!/usr/bin/env python

INPUT = 265149

squares = {}
squares[(0,0)] = 1
squares[(1,0)] = 1

current_ring = 1

x = 1
y = 0

triggered = False

def find_neighbors(x,y):
    cumulative = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if (x+i, y+j) in squares:
                    cumulative += squares[(x+i,y+j)]
    return cumulative

while(not triggered):
    n = 8 * current_ring
    for i in range(0, n):
        if x == current_ring and y == current_ring:
            x-=1
        elif x == -current_ring and y == current_ring:
            y-=1
        elif x == -current_ring and y == -current_ring:
            x+=1
        elif x == current_ring and abs(y) < current_ring:
            y+=1
        elif y == current_ring and abs(x) < current_ring:
            x-=1
        elif x == -current_ring and abs(y) < current_ring:
            y-=1
        elif y == -current_ring and abs(x) < current_ring:
            x+=1
        cumulative = find_neighbors(x, y)
        squares[(x,y)] = cumulative

        if cumulative > INPUT:
            print(cumulative)
            triggered = True
            break
    if not triggered:
        x = x + 1
        cumulative = find_neighbors(x, y)
        squares[(x,y)] = cumulative

        if cumulative > INPUT:
            print(cumulative)
            break

        current_ring+=1