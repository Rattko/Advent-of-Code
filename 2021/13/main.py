#!/usr/bin/env python3

import numpy as np

class Colors:
    RED = '\033[91m'
    END = '\033[0m'

def unpack(line: np.ndarray) -> str:
    return ' '.join(
        f'{dot:02}' if dot == 0 else f'{Colors.RED}{dot:02}{Colors.END}' for dot in line
    )

with open('input.txt', 'r') as f:
    xs, ys = [], []

    while (line := f.readline().strip()) != '':
        x, y = [int(num) for num in line.split(',')]
        xs.append(x)
        ys.append(y)

    folds = [line.strip().removeprefix('fold along ').split('=') for line in f.readlines()]

paper = np.zeros((np.max(ys) + 1, np.max(xs) + 1), dtype=int)
paper[ys, xs] = 1

for direction, position in folds:
    half, other_half = np.split(paper, [int(position)], axis=0 if direction == 'y' else 1)
    paper = half + np.flip(
        other_half[1:] if direction == 'y' else other_half[:, 1:],
        axis=0 if direction == 'y' else 1
    )
    print(np.sum(paper > 0))

for line in paper:
    print(f'{unpack(line)}')
