#!/usr/bin/env python

f = open('input.txt')
contents = list(f.readline())

def inverse_captcha(chars):
    cumulative = 0
    cur = chars[0]
    for idx, cur in enumerate(chars):
        
        if idx < int(len(chars) / 2) - 1:
            next = chars[int(len(chars) / 2) + idx]
        else:
            next = chars[idx - int(len(chars) / 2)]
        
        if cur == next:
            cumulative+=cur
    return cumulative

if __name__ == '__main__':
    f = open('input.txt')
    #print(inverse_captcha([1,2,3,1,2,3]))
    print(inverse_captcha([int(i) for i in list(f.readline())]))