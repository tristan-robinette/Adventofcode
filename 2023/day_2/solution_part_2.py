"""
Solution to Advent of Code 2023 day 2 part 2
Solved by doing some magic
"""
import time
import sys
from functools import reduce
import math


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read().strip().splitlines()

	result = 0
	for line in entries:
		game, game_sets = line.split(":")
		config = {}
		for gs in game_sets.strip().split(";"):
			for num, color in (r.split() for r in gs.split(",")):
				config[color] = max(config.get(color,0), int(num))
		power = reduce(lambda x, y: x * y, config.values(), 1)
		result += power
	return result


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
