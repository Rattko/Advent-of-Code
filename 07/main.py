#!/usr/bin/env python3

import numpy as np

with open('input.txt', 'r') as f:
    data = np.array([int(x) for x in f.read().split(',')])

low, high = np.min(data), np.max(data)

print(np.min([np.sum(np.abs(data - pos)) for pos in range(low, high + 1)]))
print(np.min([
    np.sum([x * (x + 1) / 2 for x in np.abs(data - pos)], dtype=int) for pos in range(low, high + 1)
]))
