#!/usr/bin/env python3

import numpy as np
from collections import deque

with open('input.txt', 'r') as f:
    data = np.array([list(map(int, line.strip())) for line in f.readlines()])

def is_valid(x: int, y: int, x_size: int, y_size: int) -> bool:
    return (0 <= x < x_size) and (0 <= y < y_size)

total_flashes = 0
adjacent_octopuses = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
]

for i in range(300):
    flashed = []
    data += 1

    to_flash = deque([index for index, value in np.ndenumerate(data) if value > 9])

    while to_flash:
        x, y = to_flash.pop()
        flashed.append((x, y))

        data[x, y] = 0

        for x_direction, y_direction in adjacent_octopuses:
            x_new, y_new = x + x_direction, y + y_direction

            if is_valid(x_new, y_new, *data.shape) and (x_new, y_new) not in flashed:
                data[x_new, y_new] += 1

        to_flash.extend([
            index for index, value in np.ndenumerate(data)
            if value > 9 and index not in to_flash and index not in flashed
        ])

    total_flashes += len(flashed)

    if i == 99:
        print(total_flashes)

    if data.size == len(flashed):
        print(i + 1)
        break
