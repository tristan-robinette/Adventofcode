"""
Solution to Advent of Code 2023 day 6 part 2
Solved by doing some magic
"""
import time
import sys
from functools import reduce


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	# Parsing
	entries = entries.strip().splitlines()
	time_entry = int("".join(entries[0].split(":")[-1].strip().split()))
	record_distance = int("".join(entries[1].split(":")[-1].strip().split()))
	return sum(
		time_held * (time_entry - time_held) > record_distance
		for time_held in range(time_entry)
	)


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
