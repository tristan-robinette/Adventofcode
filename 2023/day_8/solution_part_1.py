"""
Solution to Advent of Code 2023 day 8 part 1
Solved by doing some magic
"""
import itertools
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	rl_set, nodes = entries.split("\n\n")

	mapping = {}
	nodes = nodes.splitlines()
	for node in nodes:
		ele, maps_set = node.split("=")
		ele = ele.strip()
		# build a map of the graph with Left/Right options.
		# Ex: QRX = (XNN,TCJ) -> {'QRX': {'L': 'XNN', 'R': 'TCJ'}}
		maps_set = maps_set.strip().strip("(").strip(")").split(",")
		ele_mapping = {char: maps_set[ix].strip() for ix, char in enumerate(["L","R"])}
		mapping[ele] = ele_mapping

	# @Tristan next time read the question properly.
	current_key = "AAA"
	target_key = "ZZZ"
	# cycle through instructions and map until solution is found.
	for sol, p in enumerate(itertools.cycle(rl_set)):
		if current_key == target_key:
			return sol
		current_key = mapping[current_key][p]


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
