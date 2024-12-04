"""
Solution to Advent of Code 2024 day 4 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	entries = entries.strip().splitlines()
	xmas = "XMAS"
	word_len = len(xmas)
	sol = 0
	directions = [
		(0, 1),  # Right
		(0, -1),  # Left
		(1, 0),  # Down
		(-1, 0),  # Up
		(1, 1),  # Down-right diagonal
		(-1, -1),  # Up-left diagonal
		(1, -1),  # Down-left diagonal
		(-1, 1),  # Up-right diagonal
	]
	for row in range(len(entries)):
		for col in range(len(entries[row])):
			if entries[row][col] == xmas[0]:
				for dr, dc in directions:
					current_word = ""
					for i in range(word_len):
						nr, nc = row + i * dr, col + i * dc
						if 0 <= nr < len(entries) and 0 <= nc < len(entries[nr]):
							current_word += entries[nr][nc]
						else:
							break
					if current_word == xmas:
						sol += 1
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
