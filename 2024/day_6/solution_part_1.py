"""
Solution to Advent of Code 2024 day 6 part 1
Solved by doing some magic
"""
import time
import sys
from itertools import cycle


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()

    entries = entries.strip().splitlines()
    visited = set()
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    guard_pos = None
    for i, row in enumerate(entries):
        if '^' in row:
            guard_pos = (i, row.index('^'))
            break
    current_dir = next(directions)
    while True:
        r, c = guard_pos
        visited.add((r, c))
        rl, cl = current_dir
        next_r, next_c = r + rl, c + cl
        if not (0 <= next_r < len(entries) and 0 <= next_c < len(entries[0])):
            break
        next_pos = entries[next_r][next_c]
        if next_pos == "#":
            current_dir = next(directions)
        else:
            guard_pos = (next_r, next_c)
    return len(visited)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
