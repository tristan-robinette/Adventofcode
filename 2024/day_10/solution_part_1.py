"""
Solution to Advent of Code 2024 day 10 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	entries = entries.splitlines()
	num_rows = len(entries)
	num_cols = len(entries[0])
	trail_heads = []

	def is_inbounds(row, col) -> bool:
		return (0 <= row < num_rows) and (0 <= col < num_cols)

	# first find trailheads to start with.
	for row in range(len(entries)):
		entries[row] = [int(char) for char in entries[row]]
		for col in range(len(entries[row])):
			if entries[row][col] == 0:
				trail_heads.append((row, col))

	def look_around(pos):
		# this finds new positions in the grid that that are valid to continue down, these new positions get added
		# to the queue to explore.
		row, col = pos
		target_height = entries[row][col] + 1
		positions = []
		for d_r, d_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
			new_row, new_col = row + d_r, col + d_c
			if is_inbounds(new_row, new_col) and entries[new_row][new_col] == target_height:
				positions.append((new_row, new_col))
		return positions
	sol = 0
	for trail in trail_heads:
		paths = set()
		coords = [trail]
		while coords:
			pos = coords.pop()
			new_positions = look_around(pos)
			for (x, y) in new_positions:
				coords.append((x, y))
				if entries[x][y] == 9:
					paths.add((x, y))
		sol += len(paths)
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
