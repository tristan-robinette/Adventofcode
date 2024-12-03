"""
Solution to Advent of Code 2024 day 3 part 1
Solved by doing some magic
"""
import time
import sys
import re


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	mul_pattern = r"mul\((\d+),(\d+)\)"
	entries = entries.strip()

	sol = 0
	for match in re.finditer(mul_pattern, entries):
		arg1, arg2 = map(int, match.groups())
		sol += arg1 * arg2
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input1.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
