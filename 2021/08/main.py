#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = [line.strip().split(' | ') for line in f.readlines()]

print(sum([
    len([output for output in outputs.split() if len(output) in [2, 3, 4, 7]])
    for _, outputs in data
]))

def create_num_map(digits):
    nums = [None] * 10
    nums[1], nums[7], nums[4], *rest, nums[8] = sorted(digits, key=len)

    for digit in rest[3:]: # 0, 6, 9
        if digit.issuperset(nums[4]): # 9
            nums[9] = digit
        elif digit.issuperset(nums[1]): # 0
            nums[0] = digit
        else: # 6
            nums[6] = digit

    for digit in rest[:3]: # 2, 3, 5
        if digit.issubset(nums[6]): # 5
            nums[5] = digit
        elif digit.issubset(nums[9]): # 3
            nums[3] = digit
        else: # 2
            nums[2] = digit

    return {num: str(i) for i, num in enumerate(nums)}

acc = 0
for digits, outputs in data:
    num_map = create_num_map(map(frozenset, digits.split()))
    acc += int(''.join([num_map[frozenset(output)] for output in outputs.split()]))

print(acc)
