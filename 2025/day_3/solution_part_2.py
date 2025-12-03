"""
Solution to Advent of Code 2025 day 3 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read().strip().splitlines()

	sol = 0
	batteries_needed = 12
	for bank in entries:
		stack = []
		remaining = len(bank)
		for digit in bank:
			d = int(digit)
			while stack and stack[-1] < d and len(stack) - 1 + remaining >= batteries_needed:
				stack.pop()
			if len(stack) < batteries_needed:
				stack.append(d)
			remaining -= 1
		sol += int("".join(map(str, stack)))
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
