"""
Solution to Advent of Code 2023 day 6 part 1
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
	simulations = []

	time_entries = [int(e) for e in entries[0].split(":")[-1].strip().split()]
	distance_entries = [int(e) for e in entries[1].split(":")[-1].strip().split()]
	for i, (time_entry, record_distance) in enumerate(zip(time_entries, distance_entries)):
		for time_held in range(time_entry):
			if (time_held * (time_entry - time_held)) > record_distance:
				if len(simulations) < len(time_entries):
					simulations.append(0)
				simulations[i] += 1
	return reduce(lambda x, y: x * y, simulations, 1)


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
