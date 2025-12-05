"""
Solution to Advent of Code 2025 day 5 part 1
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
	available_instructions = []
	ingredients = []
	for line in entries:
		if not line:
			continue
		if "-" in line:
			available_instructions.append(tuple(map(int, line.split("-"))))
		else:
			ingredients.append(int(line))
	sol = 0
	for ingredient in ingredients:
		for (low, high) in available_instructions:
			if low <= ingredient <= high:
				sol += 1
				break
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
