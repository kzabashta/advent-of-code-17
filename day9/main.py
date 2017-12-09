#!/usr/bin/env python

class SimpleStack:
    data = []

    def __init__(self):
        pass
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        last = self.data[len(self.data) - 1]
        self.data = self.data[:-1]
        return last

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[len(self.data) - 1]

if __name__ == '__main__':
    f = open('/Users/kosta/dev/advent-of-code-17/day9/input.txt')
    line = f.readline()
    cumulative = 0
    s = SimpleStack()
    s.push(0)
    
    is_garbage = False
    is_canceling = False

    for char in line:
        if is_canceling:
            is_canceling = False
            continue

        if char == '!':
            is_canceling = True
            continue

        if char == '>':
            is_garbage = False
        if char == '<':
            is_garbage = True

        if not is_garbage:
            if char == '{':
                s.push(s.peek()+1)
            if char == '}':
                cumulative += s.pop()

    print(cumulative)