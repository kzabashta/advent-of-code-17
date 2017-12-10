#!/usr/bin/env python

f = open('/Users/kosta/dev/advent-of-code-17/day10/input.txt')
lengths = list(map(int, f.readline().split(',')))

hash_list = list(range(0,256))
skip = 0
cur_index = 0

for length in lengths:
    if cur_index + length > len(hash_list) - 1:
        sub_list = hash_list[cur_index:]
        sub_list.extend(hash_list[:cur_index + length - len(hash_list)])
        sub_list.reverse()
        
        hash_list[cur_index:] = sub_list[:len(hash_list) - cur_index]
        hash_list[:cur_index + length - len(hash_list)] = sub_list[(len(hash_list) - cur_index):]

        cur_index += length + skip
    else:
        sub_list = hash_list[cur_index:length]
        sub_list.reverse()
        hash_list[cur_index:length] = sub_list
        cur_index += length + skip
    
    if cur_index > len(hash_list) - 1:
        cur_index = cur_index % len(hash_list)
    skip+=1

result = hash_list[0] * hash_list[1]
print(result)