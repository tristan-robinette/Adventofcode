"""
Solution to Advent of Code 2025 day 5 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read().strip().splitlines()

	available_instructions = []
	for line in entries:
		if "-" not in line:
			continue
		available_instructions.append(tuple(map(int, line.split("-"))))

	available_instructions.sort()

	merged = []
	cur_low, cur_high = available_instructions[0]

	for (low, high) in available_instructions[1:]:
		if low <= cur_high + 1:
			cur_high = max(cur_high, high)
		else:
			merged.append((cur_low, cur_high))
			cur_low, cur_high = low, high
	merged.append((cur_low, cur_high))

	return sum(high - low + 1 for low, high in merged)


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
