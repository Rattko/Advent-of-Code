#!/usr/bin/env python3

import numpy as np
from scipy.stats import mode

with open('input.txt', 'r') as f:
    data = np.array(list(map(list, f.read().split('\n')[:-1])), dtype=np.int16)

gamma = list(map(str, mode(data, axis=0)[0][0]))
epsilon = [str(ord(x) ^ ord(y)) for x, y in zip('1' * len(gamma), gamma)]
print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))

generator_rating = np.copy(data)
for i in range(generator_rating.shape[1]):
    most_common = mode(generator_rating, axis=0)[0][0]
    condition = generator_rating[:, i] == int(most_common[i])

    if np.sum(condition) == len(generator_rating) / 2:
        condition = generator_rating[:, i] == 1

    generator_rating = generator_rating[condition]

    if len(generator_rating) == 1:
        break

scrubber_rating = np.copy(data)
for i in range(scrubber_rating.shape[1]):
    most_common = mode(scrubber_rating, axis=0)[0][0]
    condition = scrubber_rating[:, i] != int(most_common[i])

    if np.sum(condition) == len(scrubber_rating) / 2:
        condition = scrubber_rating[:, i] == 0

    scrubber_rating = scrubber_rating[condition]

    if len(scrubber_rating) == 1:
        break

print(
    int(''.join(map(str, generator_rating[0])), 2) * int(''.join(map(str, scrubber_rating[0])), 2)
)
