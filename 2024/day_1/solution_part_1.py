"""
Solution to Advent of Code 2024 day 1 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	entries = entries.splitlines()
	left_side = []
	right_side = []
	for entry in entries:
		left, right = entry.split()
		left_side.append(int(left))
		right_side.append(int(right))
	left_side.sort()
	right_side.sort()
	return sum(r - l if r > l else l - r for (r, l) in zip(right_side, left_side))


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
