"""
Solution to Advent of Code 2022 day 8 part 2
Solved by doing some magic
"""
import time
import sys
import numpy as np


def get_score(row_ix, column_ix, grid):
    value = grid[row_ix][column_ix]
    row = grid[row_ix]
    column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

    left, right, top, bottom = 0, 0, 0, 0

    # Check left
    for x in reversed(row[:column_ix]):
        left += 1
        if x >= value:
            break

    # Check right
    for x in row[column_ix + 1:]:
        right += 1
        if x >= value:
            break

    # Check top
    for x in reversed(column[:row_ix]):
        top += 1
        if x >= value:
            break

    # Check bottom
    for x in column[row_ix + 1:]:
        bottom += 1
        if x >= value:
            break

    return left * right * top * bottom


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read().splitlines()
    grid = np.array([list(row.strip()) for row in entries]).astype('int')
    score = []
    for row_num, row in enumerate(grid):
        score.extend(get_score(row_num, col_num, grid) for col_num, col in enumerate(row))
    return max(score)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
