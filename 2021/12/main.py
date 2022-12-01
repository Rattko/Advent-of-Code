#!/usr/bin/env python3

from collections import Counter, defaultdict

with open('input.txt', 'r') as f:
    adjacency_list = defaultdict(list)

    for path in f.readlines():
        start, end = path.strip().split('-')

        adjacency_list[start].append(end)
        adjacency_list[end].append(start)

def explore(cave: str, visited: list[str] = None, paths: list[list[str]] = []) -> list[list[str]]:
    visited = [cave] if visited is None else visited

    for next_cave in adjacency_list[cave]:
        if next_cave == 'start':
            continue

        if next_cave == 'end':
            paths.append(visited + [next_cave])
            continue

        if (
            next_cave.islower() and next_cave in visited and
            any([count >= 2 for cave, count in Counter(visited).most_common() if cave.islower()])
        ):
            continue

        explore(next_cave, visited + [next_cave], paths)

    return paths

paths = explore('start')

print(len([
    path for path in paths if all(path.count(cave) == 1 for cave in path if cave.islower())
]))
print(len(paths))
