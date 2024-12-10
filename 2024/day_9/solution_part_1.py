"""
Solution to Advent of Code 2024 day 9 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read()
	entries = iter(entries.strip())

	entries = [int(num) for num in entries]

	block_id = 0
	strip = []
	is_block = True
	for i in range(len(entries)):
		if is_block:
			strip.extend([block_id] * entries[i])
			block_id += 1
		else:
			strip.extend([None] * entries[i])

		is_block = not is_block

	free_space = strip.index(None)
	for i in reversed(range(0, len(strip))):
		if strip[i] is not None:
			strip[free_space] = strip[i]
			strip[i] = None
			while strip[free_space] is not None:
				free_space += 1
			if i - free_space <= 1:
				break

	return sum(val * itx for (itx, val) in enumerate(strip) if val is not None)



if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
