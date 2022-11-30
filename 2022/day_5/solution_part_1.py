"""
Solution to Advent of Code 2022 day 5 part 1
Solved by doing some magic
"""
import time
import sys
import numpy as np
from collections import Counter
from functools import cache
import re


def solution(input_file):
    with open(input_file, 'r') as file:
        pass

    return


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")