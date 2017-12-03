#!/usr/bin/env python

num = 265149

i = 0
y = 0
x = 0
while True:
    n = 2*i + 1
    if n*n > num:
        y = i
        break
    i+=1

counter = 0

for j in range(n*n, n*n-8*i+1,-1):
    if j == num:
        x = int(n / 2) - counter
        break
    counter += 1
    if counter == n-1:
        counter = 0

total = x+y
print(total)