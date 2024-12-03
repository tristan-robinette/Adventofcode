"""
Solution to Advent of Code 2024 day 3 part 2
Solved by doing some magic
"""
import time
import sys
import re


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read()

	do = True
	mul_pattern = r"mul\((\d+),(\d+)\)"

	entries = entries.strip()
	offset = 0
	runnable_mem = ""
	for i in range(len(entries)):
		curr_mem = entries[offset:i]
		if "do()" in curr_mem:
			do = True
		if curr_mem.endswith("don't()"):
			do = False
			offset = i
		if do:
			runnable_mem += entries[i]
	sol = 0
	for match in re.finditer(mul_pattern, runnable_mem):
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
