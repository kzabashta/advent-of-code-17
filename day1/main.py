#!/usr/bin/env python

f = open('input.txt')
contents = list(f.readline())

def inverse_captcha(chars):
    cumulative = 0
    cur = chars[0]
    for idx, cur in enumerate(chars):
        if idx < len(chars) - 1:
            next = chars[idx+1]
        else:
            next = chars[0]
        
        if cur == next:
            cumulative+=cur
    return cumulative

if __name__ == '__main__':
    f = open('input.txt')
    #print(inverse_captcha([9,1,2,1,2,1,2,9]))
    print(inverse_captcha([int(i) for i in list(f.readline())]))