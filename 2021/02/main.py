#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

horizontal_pos, vertical_pos = 0, 0
for instr in data:
    direction, length = instr.split()

    if direction == 'forward':
        horizontal_pos += int(length)
    elif direction == 'down':
        vertical_pos += int(length)
    else:
        vertical_pos -= int(length)

print(horizontal_pos * vertical_pos)

horizontal_pos, vertical_pos, aim = 0, 0, 0
for instr in data:
    direction, length = instr.split()

    if direction == 'forward':
        horizontal_pos += int(length)
        vertical_pos += aim * int(length)
    elif direction == 'down':
        aim += int(length)
    else:
        aim -= int(length)

print(horizontal_pos * vertical_pos)
