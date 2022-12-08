"""
Solution to Advent of Code 2022 day 8 part 1
Solved by doing some magic
"""
import time
import sys
import numpy as np


def is_visible(row_ix, column_ix, grid):
	if row_ix in [0, len(grid) - 1]:
		return True
	if column_ix in [0, len(grid[row_ix]) - 1]:
		return True

	value = grid[row_ix][column_ix]
	row = grid[row_ix]
	column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

	left = all(x < value for x in row[:column_ix])
	right = all(x < value for x in row[column_ix + 1:])
	top = all(x < value for x in column[:row_ix])
	bottom = all(x < value for x in column[row_ix + 1:])

	return left or right or top or bottom


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().splitlines()
	grid = np.array([list(row.strip()) for row in entries]).astype('int')
	vis = 0
	for row_num, row in enumerate(grid):
		for col_num, col in enumerate(row):
			if is_visible(row_num, col_num, grid):
				vis += 1
	return vis


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
