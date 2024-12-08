"""
Solution to Advent of Code 2024 day 8 part 1
Solved by doing some magic
"""
import itertools
import time
import sys
from collections import defaultdict


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	entries = [list(e) for e in entries.splitlines()]
	num_rows, num_cols = len(entries), len(entries[0])
	locations = set()

	# get freq -> locations mapping.
	frequency_to_locations = defaultdict(list)

	for row in range(num_rows):
		for col in range(num_cols):
			if entries[row][col] != ".":
				freq = entries[row][col]
				frequency_to_locations[freq].append((col, row))

	def is_inbounds(row, col) -> bool:
		return (0 <= row < num_rows) and (0 <= col < num_cols)

	# Determine possible antinode locations for each frequency
	for freq, positions in frequency_to_locations.items():
		for (col1, row1), (col2, row2) in itertools.combinations(positions, 2):

			delta_row, delta_col = row2 - row1, col2 - col1
			antinode_row, antinode_col = row2 + delta_row, col2 + delta_col

			if is_inbounds(antinode_row, antinode_col):
				locations.add((antinode_row, antinode_col))
			# Check the second potential antinode location
			antinode_row, antinode_col = row1 - delta_row, col1 - delta_col
			if is_inbounds(antinode_row, antinode_col):
				locations.add((antinode_row, antinode_col))
	return len(locations)


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
