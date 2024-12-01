"""
Solution to Advent of Code 2024 day 1 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read()
	entries = entries.strip()
	entries = entries.splitlines()
	counter = {}
	sol = 0
	for entry in entries:
		left, right = entry.split()
		if right not in counter:
			counter[right] = 1
		else:
			counter[right] += 1
	for entry in entries:
		left, right = entry.split()
		sol += counter.get(left, 0) * int(left)

	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input1.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
