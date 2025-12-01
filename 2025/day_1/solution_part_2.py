"""
Solution to Advent of Code 2025 day 1 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# tupes ma goops
	entries = [(line[0], int(line[1:])) for line in entries.splitlines()]
	# Solving
	dial = 50
	sol = 0
	for i, (direction, distance) in enumerate(entries):
		# my sloppy range means p2 is easy. yay.
		for j in range(distance):
			if direction == 'L':
				dial -= 1
				if dial < 0:
					dial = 99
			else:
				dial += 1
				if dial > 99:
					dial = 0
			sol += dial == 0
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
