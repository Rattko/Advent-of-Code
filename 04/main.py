#!/usr/bin/env python3

import numpy as np

with open('input.txt', 'r') as f:
    nums = map(int, f.readline().strip().split(','))
    tables = np.loadtxt(f, dtype=np.int16)
    tables = np.vsplit(tables, len(tables) / 5)

for num in nums:
    for table in tables:
        table[table == num] = -1

        if np.any([np.all(table[i] == -1) or np.all(table[:, i] == -1) for i in range(len(table))]):
            score = (np.sum(table) + (table == -1).sum()) * num
            break
    else:
        continue
    break

print(score)

for num in nums:
    tables_to_remove = []

    for index, table in enumerate(tables):
        table[table == num] = -1

        if np.any([np.all(table[i] == -1) or np.all(table[:, i] == -1) for i in range(len(table))]):
            tables_to_remove.append(index)
            score = (np.sum(table) + (table == -1).sum()) * num

    tables = np.delete(tables, tables_to_remove, axis=0)

print(score)
