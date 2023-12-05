"""
Solution to Advent of Code 2023 day 5 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	# Parsing
	entries = entries.strip()
	parts = entries.split("\n\n")
	seeds = [int(seed) for seed in parts[0].split(":")[-1].strip().split()]
	mapping = {}

	for m in parts[1:]:
		lines = m.splitlines()
		name = lines[0].strip(":")
		soil_ranges = []
		seed_ranges = []

		for line in lines[1:]:
			destination_range_start, source_range_start, length = map(int, line.split())
			soil_ranges.append((destination_range_start, destination_range_start + length - 1))
			seed_ranges.append((source_range_start, source_range_start + length - 1))
		mapping[name] = {'soil_ranges': soil_ranges, 'seed_ranges': seed_ranges}

	locations = []
	for seed in seeds:
		seed_map = {}
		current_seed_number = seed
		for i, name in enumerate(mapping):
			seed_ranges = mapping[name].get("seed_ranges")
			soil_ranges = mapping[name].get("soil_ranges")
			for seed_range, target_range in zip(seed_ranges, soil_ranges):
				# min, max of range is stored as tuple.
				if seed_range[0] <= current_seed_number <= seed_range[1]:
					current_seed_number += target_range[0] - seed_range[0]
					break
			seed_map[name] = current_seed_number
		locations.append(seed_map["humidity-to-location map"])
	return min(locations)


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
