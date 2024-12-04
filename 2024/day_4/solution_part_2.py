"""
Solution to Advent of Code 2024 day 4 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
    with open(input_file, "r") as file:
        entries = file.read().strip().splitlines()

    rows, cols = len(entries), len(entries[0])
    sol = 0

    for r in range(rows - 2):
        for c in range(cols - 2):
            top_left = entries[r][c]
            center = entries[r + 1][c + 1]
            bottom_right = entries[r + 2][c + 2]
            bottom_left = entries[r + 2][c]
            top_right = entries[r][c + 2]

            if (
                (
                    top_left == "M"
                    and center == "A"
                    and bottom_right == "S"
                    and bottom_left == "M"
                    and top_right == "S"
                )
                or (
                    top_left == "M"
                    and center == "A"
                    and bottom_right == "S"
                    and bottom_left == "S"
                    and top_right == "M"
                )
                or (
                    top_left == "S"
                    and center == "A"
                    and bottom_right == "M"
                    and bottom_left == "M"
                    and top_right == "S"
                )
                or (
                    top_left == "S"
                    and center == "A"
                    and bottom_right == "M"
                    and bottom_left == "S"
                    and top_right == "M"
                )
            ):
                sol += 1

    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
