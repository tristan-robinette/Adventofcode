"""
Solution to Advent of Code 2022 day 10 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	sol = 0
	register_x = 1
	inst = []
	entries = entries.strip().splitlines()
	# add buffer tick if not 'noop'
	for entry in entries:
		splitln = entry.split()
		inst.extend((['noop', 0], [splitln[0], int(splitln[1])])) if len(splitln) > 1 else inst.append([splitln[0], 0])

	for cycle, (instruction, value) in enumerate(inst, 1):
		if (cycle + 20) % 40 == 0:
			sol += register_x * cycle
		register_x += value

	return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
