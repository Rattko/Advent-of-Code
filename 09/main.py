#!/usr/bin/env python3

from queue import Queue
import numpy as np

with open('input.txt', 'r') as f:
    data = np.array([[int(x) for x in line.strip()] for line in f.readlines()])

def is_valid(x: int, y: int, x_size: int, y_size: int) -> bool:
    return (0 <= x < x_size) and (0 <= y < y_size)

def is_low_point(x: int, y: int, value: int) -> bool:
    for x_direction, y_direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        x_new, y_new = x + x_direction, y + y_direction

        if is_valid(x_new, y_new, *data.shape) and data[x_new, y_new] <= value:
            return False

    return True

low_points = []
for coords, value in np.ndenumerate(data):
    if is_low_point(*coords, value):
        low_points.append((coords, value + 1))

print(np.sum([value for _, value in low_points]))

basins = []
for coords, _ in low_points:
    queue, visited = Queue(), set()
    queue.put(coords)

    while not queue.empty():
        x, y = queue.get()
        visited.add((x, y))

        for x_direction, y_direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x_new, y_new = x + x_direction, y + y_direction

            if (
                is_valid(x_new, y_new, *data.shape)
                and data[x_new, y_new] != 9
                and (x_new, y_new) not in visited
            ):
                queue.put((x_new, y_new))

    basins.append(len(visited))

print(np.prod(sorted(basins, reverse=True)[:3]))
