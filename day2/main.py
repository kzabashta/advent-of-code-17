#!/usr/bin/env python
#import pandas as pd

#df = pd.read_table('data.tsv')

import pandas as pd
import sys

df = pd.read_csv("data.txt", header=None, delimiter=r"\s+")
mx = df.as_matrix()
cum = 0

for row in mx:
    smallest = sys.maxsize
    largest = -sys.maxsize

    for i in row:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    
    diff = largest - smallest
    cum += diff

print(cum)