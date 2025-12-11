"""
Solution to Advent of Code 2025 day 11 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	entries = [row.split(":") for row in entries.splitlines()]
	connections = {device: outputs.split() for (device, outputs) in entries}
	# Solving
	sol = 0
	starting_device, ending_device = "you", "out"
	queue = [starting_device]
	while queue:
		for output in connections[queue.pop()]:
			sol += output == ending_device
			if output != ending_device:
				queue.append(output)
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
