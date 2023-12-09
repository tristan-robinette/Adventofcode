"""
Solution to Advent of Code 2023 day 9 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	rows = [[int(val) for val in e.split()] for e in entries.splitlines()]
	sol = 0
	for row in rows:
		history = [row]
		while set(history[-1]) != {0}:
			# while last row is not all 0 simply grab the latest row history and subtract the next value
			history.append(
				[history[-1][ix + 1] - v for ix, v in enumerate(history[-1]) if ix + 1 < len(history[-1])]
			)
		while len(history) > 1:
			l = history.pop(-1)
			d = l[-1]
			history[-1].append(history[-1][-1] + d)
		sol += history[0][-1]

	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input1.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
