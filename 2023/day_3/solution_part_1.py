"""
Solution to Advent of Code 2023 day 3 part 1
Solved by doing some magic
"""

import itertools
import time
import sys


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()

    result = 0
    entries = entries.strip()

    # Parsing
    entries = entries.splitlines()

    for i, line in enumerate(entries):
        current_number = ""
        add_number = False

        for idx, char in enumerate(line):
            if char.isdigit():
                current_number += char
                # for each character in the 3x3 grid around the digit
                for x, y in itertools.product(
                        range(max(0, i - 1), min(len(entries), i + 2)),
                        range(max(0, idx - 1), min(len(line), idx + 2))
                ):
                    # exclude the digit itself
                    if x == i and y == idx:
                        continue
                    # if the character is not a digit and not a dot its a symbol
                    if entries[x][y] != "." and not entries[x][y].isdigit():
                        add_number = True
            elif add_number and current_number != "":
                result += int(current_number)
                add_number = False
                current_number = ""
            else:
                add_number = False
                current_number = ""
        if add_number and current_number != "":
            result += int(current_number)
    return result


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
