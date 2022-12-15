"""
Solution to Advent of Code 2022 day 12 part 1
Solved by doing some magic
"""
import time
import sys

# tools
import re

import numpy as np
import scipy.ndimage

from collections import Counter
from functools import cache


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	entries = entries.splitlines()
	entries = [int(e) for e in entries]
	#entries = [re.findall(r'(\d+)',e)[0] for e in entries]
	entries = np.array(entries)
	print(entries)

	# Solving
	kern = np.ones((3), dtype=int)
	def conv_func(arr):
		arr = arr.reshape((3))
		return arr[1]
	entries = scipy.ndimage.filters.generic_filter(entries, conv_func, footprint=kern, mode='constant', cval=0)
	
	sol = 0
	for i,n in enumerate(entries):
		sol += 1
		

	return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
