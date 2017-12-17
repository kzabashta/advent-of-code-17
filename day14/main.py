#!/usr/bin/env python

from knot_hash import knot_hash

INPUT = 'nbysizxe'
NUM_BITS = 4

hashes = ['%s-%d' % (INPUT, x) for x in range(0, 128)]
total = 0

for hash in hashes:
    knot_hash_output = knot_hash(hash)

    # from https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    binary = ''.join([bin(int(x, 16))[2:].zfill(NUM_BITS) for x in knot_hash_output])
    total += binary.count('1')

print(total)