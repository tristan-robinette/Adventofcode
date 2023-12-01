"""
Solution to Advent of Code 2023 day 1 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	result = 0
	entries = entries.splitlines()
	for line in entries:
		numbers_in_line = [char for char in line if not char.isalpha()]
		result += int(f"{numbers_in_line[0]}{numbers_in_line[-1]}")
	return result



if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
