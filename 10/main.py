#!/usr/bin/env python3

from collections import deque
from functools import reduce

with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

def complete(line: str) -> str:
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = deque()

    for char in line:
        if char in brackets.keys():
            stack.append(char)
            continue

        if brackets[stack.pop()] != char:
            return char

    closing_chars = ''
    while stack:
        closing_chars += brackets[stack.pop()]

    return closing_chars

corrupted_score_table = {')': 3, ']': 57, '}': 1197, '>' : 25137}
incomplete_score_table = {')': 1, ']': 2, '}': 3, '>' : 4}
corrupted_score, incomplete_scores = 0, []

for line in data:
    ret = complete(line)

    if len(ret) == 1:
        corrupted_score += corrupted_score_table[ret]
    else:
        incomplete_scores.append(
            reduce(lambda score, x: 5 * score + incomplete_score_table[x], [0] + list(ret))
        )

incomplete_scores.sort()

print(corrupted_score)
print(incomplete_scores[len(incomplete_scores) // 2])
