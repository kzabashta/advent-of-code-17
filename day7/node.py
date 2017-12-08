class Node:
    
    def __init__(self):
        self.weight = 0.0
        self.children = []

    def __init__(self, weight, children):
        self.weight = weight
        self.children = children