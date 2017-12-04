#!/usr/bin/env python

f = open('input.txt')
contents = f.readlines()
total = 0
for line in contents:
    words = line.split()
    unique = set()
    no_dupes = True
    for word in words:
        if not word in unique:
            unique.add(word)
        else:
            no_dupes = False
            break
    if no_dupes:
        total += 1

print(total)