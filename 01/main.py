#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

data = list(map(int, data))
print(sum([x < y for x, y in zip(data, data[1:])]))

data = [x + y + z for x, y, z in zip(data, data[1:], data[2:])]
print(sum([x < y for x, y in zip(data, data[1:])]))
