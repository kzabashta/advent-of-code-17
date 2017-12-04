#!/usr/bin/env python

f = open('input.txt')
contents = f.readlines()
total = 0
for line in contents:
    words = line.split()
    unique = set()
    no_dupes = True
    for word in words:
        word_char_arr = list(word)
        word_char_arr.sort()
        normalized_word = ''.join(word_char_arr)
        if not normalized_word in unique:
            unique.add(normalized_word)
        else:
            no_dupes = False
            break

    if no_dupes:
        total += 1

print(total)