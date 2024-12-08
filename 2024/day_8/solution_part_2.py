"""
Solution to Advent of Code 2024 day 8 part 2
Solved by doing some magic
"""
import itertools
import time
import sys
from collections import defaultdict


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    entries = [list(e) for e in entries.splitlines()]
    num_rows, num_cols = len(entries), len(entries[0])
    locations = set()

    frequency_to_locations = defaultdict(list)

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if entries[row_index][col_index] != ".":
                frequency = entries[row_index][col_index]
                frequency_to_locations[frequency].append((col_index, row_index))

    def is_inbounds(row, col) -> bool:
        return (0 <= row < num_rows) and (0 <= col < num_cols)

    for freq, positions in frequency_to_locations.items():
        for (col1, row1), (col2, row2) in itertools.combinations(positions, 2):
            delta_row, delta_col = row2 - row1, col2 - col1

            # Traverse in the forward direction
            current_row, current_col = row2, col2

            while is_inbounds(current_row, current_col):
                locations.add((current_row, current_col))
                current_row += delta_row
                current_col += delta_col

            # Traverse in the backward direction
            current_row, current_col = row1, col1
            while is_inbounds(current_row, current_col):
                locations.add((current_row, current_col))
                current_row -= delta_row
                current_col -= delta_col
    return len(locations)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
