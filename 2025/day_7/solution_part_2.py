"""
Solution to Advent of Code 2025 day 7 part 2
Solved by doing some magic
"""
import time
import sys
from functools import lru_cache

splitter = "^"
grid = []

@lru_cache
def walk_grid(row: int, col: int) -> int:
    if row >= len(grid):
        return 1

    while row < len(grid) and grid[row][col] != splitter:
        row += 1

    if row >= len(grid):
        return 1

    total = 0
    for direction in (-1, 1):
        new_col = col + direction
        if 0 <= new_col < len(grid[0]):
            total += walk_grid(row + 1, new_col)
    return total


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()
    entries = entries.strip()
    starting_pos = None
    starting_char = 'S'
    for i, row in enumerate(entries.splitlines()):
        vals = list(row)
        grid.append(vals)
        if starting_char in vals:
            starting_pos = (i, vals.index(starting_char))
    return walk_grid(starting_pos[0], starting_pos[1])


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
