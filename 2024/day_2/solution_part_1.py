"""
Solution to Advent of Code 2024 day 2 part 1
Solved by doing some magic
"""
import time
import sys


def safe(line):
    return (
            sorted(line) in [line, line[::-1]] and
            all(1 <= abs(a - b) <= 3 for a, b in zip(line, line[1:]))
    )


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    sol = 0
    entries = entries.splitlines()
    for line in entries:
        line = [int(c) for c in line.split()]
        sol += safe(line)
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input1.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
