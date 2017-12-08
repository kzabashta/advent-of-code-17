class Node:
    
    def __init__(self, parent, val, weight, children):
        self.parent = parent
        self.val = val
        self.weight = weight
        self.children = children