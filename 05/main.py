#!/usr/bin/env python3

from collections import Counter
from dataclasses import dataclass
from itertools import takewhile

import numpy as np

SECOND_PART = True

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    start: Point
    end: Point

    def get_points(self):
        if self.start.x == self.end.x:
            low = min(self.start.y, self.end.y)
            high = max(self.start.y, self.end.y)

            points = [(self.start.x, y) for y in range(low, high + 1)]
        elif self.start.y == self.end.y:
            low = min(self.start.x, self.end.x)
            high = max(self.start.x, self.end.x)

            points = [(x, self.start.y) for x in range(low, high + 1)]
        else:
            points = list(zip(
                range(self.start.x, self.end.x, np.sign(self.end.x - self.start.x)),
                range(self.start.y, self.end.y, np.sign(self.end.y - self.start.y))
            )) + [(self.end.x, self.end.y)] if SECOND_PART else []

        return points

with open('input.txt', 'r') as f:
    data = [line.split(' -> ') for line in f.read().split('\n')[:-1]]
    lines = [
        Line(Point(*map(int, start.split(','))), Point(*map(int, end.split(','))))
        for start, end in data
    ]

print(len(list(takewhile(
    lambda x: x[1] > 1,
    Counter([point for line in lines for point in line.get_points()]).most_common())))
)
