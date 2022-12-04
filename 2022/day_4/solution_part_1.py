"""
Solution to Advent of Code 2022 day 4 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	# Parsing
	entries = [line.split(",") for line in entries.strip().splitlines()]
	sol = 0
	for entry in entries:
		# more parsing...
		elf1, elf2 = [list(map(int, e.split("-"))) for e in entry]  # must be better way doing this??
		# create ranges for each section with adding 1 to account for 0 based
		elf1_range = set(range(elf1[0], elf1[1] + 1))
		elf2_range = set(range(elf2[0], elf2[1] + 1))
		# check both cases of full ranges being in either elves sections.
		if set.issubset(elf2_range, elf1_range):
			sol += 1
		elif set.issubset(elf1_range, elf2_range):
			sol += 1
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
