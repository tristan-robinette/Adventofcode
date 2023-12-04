"""
Solution to Advent of Code 2023 day 4 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	# will store the card number + copies of the card
	mapping = {k+1:1 for k in range(len(entries.splitlines()))}
	for i, card in enumerate(entries.splitlines(), 1):
		# can set the initial instance of the card.
		num_matches = 0
		winning_set, your_set = card.split(":")[-1].strip().split("|")
		# Check if shared values between lists
		if inner := set(winning_set.split()).intersection(set(your_set.split())):
			num_matches = len(inner)
			# for each match add the new instance to mapping
			for ix in range(num_matches):
				mapping[ix + i + 1] = mapping.get(ix + i + 1, 0) + 1
		# for copies of card, clone forwards
		for _ in range(mapping.get(i) - 1):
			for ix in range(num_matches):
				mapping[ix + i + 1] = mapping.get(ix + i + 1, 0) + 1
	return sum(mapping.values())


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
