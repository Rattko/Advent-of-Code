#!/usr/bin/env python3

import numpy as np

with open('input.txt', 'r') as f:
    data = [int(x) for x in f.read().split(',')]
    counts = np.bincount(data, minlength=9)

for _ in range(256):
    counts = np.roll(counts, -1)
    counts[6] += counts[8]

print(np.sum(counts))
