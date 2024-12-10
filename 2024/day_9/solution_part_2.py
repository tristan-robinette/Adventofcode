"""
Solution to Advent of Code 2024 day 9 part 2
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
	gaps = []
	blocks = []
	is_block = True
	for i in range(len(entries)):
		if is_block:
			blocks.append((len(strip), block_id, entries[i]))
			strip.extend([block_id] * entries[i])
			block_id += 1
		else:
			gaps.append((entries[i], len(strip)))
			strip.extend([None] * entries[i])

		is_block = not is_block

	for block in reversed(blocks):
		position, b_id, length = block
		for itx, (gap_length, gap_position) in enumerate(gaps):
			if gap_position > position:
				break

			if gap_length >= length:
				for l in range(length):
					strip[position + l] = None
					strip[gap_position + l] = b_id

				diff = gap_length - length
				if diff > 0:
					gaps[itx] = (diff, gap_position + length)
				else:
					gaps.pop(itx)
				break
	return sum(val * itx for (itx, val) in enumerate(strip) if val is not None)


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
