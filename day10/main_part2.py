#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day10/input.txt')
lengths = list(map(ord, f.readline()))
EXTRA_SEQUENCE = [17, 31, 73, 47, 23]
lengths.extend(EXTRA_SEQUENCE)
NUM_ROUNDS = 64

hash_list = list(range(256))
skip = 0
cur_index = 0

for i in range(NUM_ROUNDS):
    for length in lengths:
        if cur_index + length > len(hash_list):
            sub_list = hash_list[cur_index:]
            sub_list.extend(hash_list[:cur_index + length - len(hash_list)])
            sub_list.reverse()
            hash_list[cur_index:] = sub_list[:len(hash_list) - cur_index]
            hash_list[:cur_index + length - len(hash_list)] = sub_list[(len(hash_list) - cur_index):]
        else:
            sub_list = hash_list[cur_index:cur_index+length]
            sub_list.reverse()
            hash_list[cur_index:cur_index+length] = sub_list
        cur_index = (cur_index + length + skip) % len(hash_list)
        skip+=1
hash = ''
for block in range(0, 256, 16):
    part = hash_list[block]^hash_list[block + 1]^hash_list[block + 2]^hash_list[block + 3]^hash_list[block + 4]^hash_list[block + 5]^hash_list[block + 6]^hash_list[block + 7]^hash_list[block + 8]^hash_list[block + 9]^hash_list[block + 10]^hash_list[block + 11]^hash_list[block + 12]^hash_list[block + 13]^hash_list[block + 14]^hash_list[block + 15]
    hash_part = ('%x' % part)
    if len(hash_part) < 2:
        hash_part = '0' + hash_part
    hash += hash_part
print(hash)