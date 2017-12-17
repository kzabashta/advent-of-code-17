#!/usr/bin/env python

from knot_hash import knot_hash

NUM_BITS = 4

def build_grid(input):
    hashes = ['%s-%d' % (input, x) for x in range(0, 128)]
    grid = []

    for hash in hashes:
        knot_hash_output = knot_hash(hash)

        # from https://stackoverflow.com/questions/1425493/convert-hex-to-binary
        binary = ''.join([bin(int(x, 16))[2:].zfill(NUM_BITS) for x in knot_hash_output])
        grid.append(list(binary))
    
    return grid

def defrag(grid, x, y):
    is_region = grid[x][y] != '0'
    if not is_region:
        return False
    # clear the cell
    grid[x][y] = '0'
    # clear the adjacent cells
    if x > 0:
        defrag(grid, x-1, y)
    if x < 127:
        defrag(grid, x+1, y)
    if y > 0:
        defrag(grid, x, y-1)
    if y < 127:
        defrag(grid, x, y+1)
    return is_region


if __name__ == '__main__':
    input = 'nbysizxe'
    grid = build_grid(input)
    total_regions = 0
    for i in range(128):
        for j in range(128):
            if defrag(grid, i, j):
                total_regions += 1
    print(total_regions)