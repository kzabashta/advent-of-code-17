#!/usr/bin/env python

class SimpleQueue:
    data = []

    def __init__(self):
        pass
    
    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        head = self.data[0]
        self.data = self.data[1:]
        print(self.data)
        return head

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[0]

if __name__ == '__main__':
    f = open('/Users/kosta/dev/advent-of-code-17/day9/input.txt')
    line = f.readline()
