#!/usr/bin/env python
#import pandas as pd

#df = pd.read_table('data.tsv')

import pandas as pd
import sys

df = pd.read_csv("data.txt", header=None, delimiter=r"\s+")
mx = df.as_matrix()
cum = 0

for row in mx:
    res = 0
    for i in row:
        for j in row:
            if i % j == 0 and i!=j:
                res = i / j

    cum += res

print(cum)