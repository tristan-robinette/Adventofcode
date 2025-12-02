"""
Solution to Advent of Code 2025 day 2 part 1
Solved by doing some magic
"""
import time
import sys


def is_invalid(s: str):
    l = len(s)
    if l % 2 != 0:
        return False
    half = l // 2
    return s[:half] == s[half:]


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    ranges = [(map(int, part.split("-"))) for part in entries.split(",")]

    sol = 0

    for first, last in ranges:
        for candidate in range(first, last + 1):
            if is_invalid(str(candidate)):
                sol += candidate
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
