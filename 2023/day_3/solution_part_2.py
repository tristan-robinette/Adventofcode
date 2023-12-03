"""
Solution to Advent of Code 2023 day 3 part 2
Solved by doing some magic
"""

import itertools
import time
import sys
from collections import defaultdict


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()

    entries = entries.strip()

    # Parsing
    entries = entries.splitlines()
    gears = defaultdict(list)
    for i, line in enumerate(entries):
        current_number = ""
        # symbols are tuple of (symbol, x, y)
        adjacent_symbols = set()

        for idx, char in enumerate(line):
            if char.isdigit():
                current_number += char
                # same eval as p1
                for x, y in itertools.product(
		                range(max(0, i - 1), min(len(entries), i + 2)),
		                range(max(0, idx - 1), min(len(line), idx + 2))
                ):
                    if x == i and y == idx:
                        continue
                    if entries[x][y] != "." and not entries[x][y].isdigit():
                        # track position
                        adjacent_symbols.add((entries[x][y], x, y))

            elif len(adjacent_symbols) != 0 and current_number != "":
                for symbol, x, y in adjacent_symbols:
                    if symbol == "*":
                        gears[(x, y)].append(int(current_number))
                adjacent_symbols = set()
                current_number = ""
            else:
                adjacent_symbols = set()
                current_number = ""
        if len(adjacent_symbols) != 0 and current_number != "":
            for symbol, x, y in adjacent_symbols:
                if symbol == "*":
                    gears[(x, y)].append(int(current_number))
    # Sum only if 2 exact parts
    return sum(
        values[0] * values[1] for values in gears.values() if len(values) == 2
    )


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
