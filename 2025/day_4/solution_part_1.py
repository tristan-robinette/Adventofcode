"""
Solution to Advent of Code 2025 day 4 part 1
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
	# Solving
	sol = 0
	directions = [
		(0, 1),  # Right
		(0, -1),  # Left
		(1, 0),  # Down
		(-1, 0),  # Up
		(1, 1),  # Down-right diagonal
		(-1, -1),  # Up-left diagonal
		(1, -1),  # Down-left diagonal
		(-1, 1),  # Up-right diagonal
	]
	max_paper_in_area = 4
	roll_char = "@"
	for row in range(len(entries)):
		for col in range(len(entries[row])):
			candidate = entries[row][col]
			count = 0
			if candidate != roll_char: continue
			for dr, dc in directions:
				nr, nc = row + dr, col + dc
				if 0 <= nr < len(entries) and 0 <= nc < len(entries[nr]):
					count += entries[nr][nc] == roll_char
			sol += count < max_paper_in_area
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
