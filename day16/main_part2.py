#!/usr/bin/env python

import re
import string

SPIN_REGEX     = r's(\d+)'
EXCHANGE_REGEX = r'x(\d+)/(\d+)'
PARTNER_REGEX  = r'p(\w+)/(\w+)'

def handle_spin(move, progs):
    r = re.search(SPIN_REGEX, move)
    spin_by = int(r.group(1))
    spun = progs[-spin_by:]
    spun.extend(progs[:len(progs)-spin_by])
    return spun

def handle_exchange(move, progs):
    r = re.search(EXCHANGE_REGEX, move)
    a = int(r.group(1))
    b = int(r.group(2))

    temp = progs[a]
    progs[a] = progs[b]
    progs[b] = temp

    return progs

def handle_partner(move, progs):
    r = re.search(PARTNER_REGEX, move)
    a = r.group(1)
    b = r.group(2)

    a = progs.index(a)
    b = progs.index(b)

    temp = progs[a]
    progs[a] = progs[b]
    progs[b] = temp

    return progs

def dance(progs, moves):
    for move in moves:
        if move[0] == 's':
            progs = handle_spin(move, progs)
        elif move[0] == 'x':
            progs = handle_exchange(move, progs)
        elif move[0] == 'p':
            progs = handle_partner(move, progs)
    return progs

if __name__ == '__main__':
    progs = list(string.ascii_lowercase)[:16]
    f = open('/Users/kosta/dev/advent-of-code-17/day16/input.txt', 'r')
    moves = f.read().split(',')
    f.close()

    cache = []
    for i in range(1000000000):
        progs_s = ''.join(progs)
        if progs_s in cache:
            print(cache[1000000000 % len(cache)])
            break
        else:
            cache.append(progs_s)
        progs = dance(progs, moves)
        print(i)