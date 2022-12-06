"""
Solution to Advent of Code 2022 day 6 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().strip()
	min_char_before_marker = 4

	for i, char in enumerate(entries, 1):
		if i < min_char_before_marker:
			continue
		if len(set(entries[i - min_char_before_marker: i])) == min_char_before_marker:
			return i


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
