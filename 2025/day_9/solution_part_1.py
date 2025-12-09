"""
Solution to Advent of Code 2025 day 9 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    entries = entries.splitlines()

    # Solving
    sol = 0

    for i in range(len(entries)):
        col1, row1 = map(int, entries[i].split(","))
        for j in range(len(entries)):
            col2, row2 = map(int, entries[j].split(","))
            if (col1, row1) == (col2, row2):
                continue
            #     omggggg offbyone got me for soooooo long. grrrrrrr
            sol = max((col2 - col1 + 1) * (row2 - row1 + 1), sol)
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
