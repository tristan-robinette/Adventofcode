"""
Solution to Advent of Code 2023 day 4 part 1
Solved by doing some magic
"""
import time
import sys
from functools import reduce


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	sol = 0
	for card in entries.splitlines():
		winning_set, your_set = card.split(":")[-1].strip().split("|")
		# Check if shared values between lists
		if inner := set(winning_set.split()).intersection(set(your_set.split())):
			sol += reduce(lambda x, y: x * 2, list(inner)[:-1], 1)
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
