"""
Solution to Advent of Code 2022 day 10 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	register_x = 1
	inst = []
	entries = entries.strip().splitlines()
	screen = [['.']*40 for _ in range(6)]
	# add buffer tick if not 'noop'
	for entry in entries:
		splitln = entry.split()
		inst.extend((['noop', 0], [splitln[0], int(splitln[1])])) if len(splitln) > 1 else inst.append([splitln[0], 0])

	for cycle, (instruction, value) in enumerate(inst, 1):
		rx, cx = divmod(cycle-1, 40)
		if register_x - 1 <= cx <= register_x + 1:
			screen[rx][cx] = '#'
		register_x += value

	print('The result for solution 2 is:')
	for row in screen:
		for ele in row:
			print(ele, end=' ')
		print()

	return 'FPGPHFGH'


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
