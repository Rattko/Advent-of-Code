#!/usr/bin/env python3

from collections import Counter

with open('input.txt', 'r') as f:
    template, _ = f.readline().strip(), f.readline()

    rules = {}
    for line in f.readlines():
        pair, new = line.strip().split(' -> ')
        rules[pair] = new

pairs = Counter(x + y for x, y in zip(template, template[1:]))
for _ in range(40):
    counter = Counter()

    for (x, y), count in pairs.most_common():
        new = rules[x + y]
        counter[x + new] += count
        counter[new + y] += count

    pairs = counter

counts = Counter()
for (x, y), count in pairs.most_common() + [((template[0], template[-1]), 1)]:
    counts[x] += count
    counts[y] += count

print(counts.most_common()[0][1] // 2 - counts.most_common()[-1][1] // 2)
