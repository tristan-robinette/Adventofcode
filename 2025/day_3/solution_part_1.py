"""
Solution to Advent of Code 2025 day 3 part 1
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
	sol = 0
	for i, bank in enumerate(entries):
		bank_max = 0
		for j in range(len(str(bank))):
			for ij in range(len(bank[j + 1:])):
				bank_max = max(bank_max, int(f"{bank[j]}{bank[ij + j + 1]}"))
		sol += bank_max
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
