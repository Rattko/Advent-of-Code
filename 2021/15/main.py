#!/usr/bin/env python3

from dataclasses import dataclass, field
from heapq import heappop, heappush

import numpy as np

@dataclass(order=True)
class Point:
    coords: tuple[int, int] = field(compare=False)
    dist: int = field(compare=True)

def is_valid(x: int, y: int, x_size: int, y_size: int) -> bool:
    return (0 <= x < x_size) and (0 <= y < y_size)

def get_value(x: int, y: int) -> int:
    x_size, y_size = cavern.shape

    x_shift, x_base = divmod(x, x_size)
    y_shift, y_base = divmod(y, y_size)

    return (cavern[x_base, y_base] + x_shift + y_shift - 1) % 9 + 1

with open('input.txt', 'r') as f:
    cavern = np.array([list(line.strip()) for line in f.readlines()], dtype=int)

x_size, y_size = cavern.shape if False else (cavern.shape[0] * 5, cavern.shape[1] * 5)
start, end = (0, 0), (x_size - 1, y_size - 1)

heap = [Point(start, 0)]
visited = set([start])

while heap:
    node = heappop(heap)

    if node.coords == end:
        print(node.dist)
        break

    x, y = node.coords
    for x_direction, y_direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x_new, y_new = x + x_direction, y + y_direction

        if is_valid(x_new, y_new, x_size, y_size) and (x_new, y_new) not in visited:
            heappush(heap, Point((x_new, y_new), node.dist + get_value(x_new, y_new)))
            visited.add((x_new, y_new))
