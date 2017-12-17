#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day10/input.txt')
lengths = list(map(int, f.readline().split(',')))

hash_list = list(range(256))
skip = 0
cur_index = 0

for length in lengths:
    if cur_index + length > len(hash_list):
        sub_list = hash_list[cur_index:]
        sub_list.extend(hash_list[:cur_index + length - len(hash_list)])
        sub_list.reverse()
        hash_list[cur_index:] = sub_list[:len(hash_list) - cur_index]
        hash_list[:cur_index + length - len(hash_list)] = sub_list[(len(hash_list) - cur_index):]
        cur_index = (cur_index + length + skip) % len(hash_list)
    else:
        sub_list = hash_list[cur_index:cur_index+length]
        sub_list.reverse()
        hash_list[cur_index:cur_index+length] = sub_list
        cur_index += length + skip
    skip+=1

result = hash_list[0] * hash_list[1]
print(result)