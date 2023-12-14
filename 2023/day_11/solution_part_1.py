"""
Solution to Advent of Code 2023 day 11 part 1
Solved by doing some magic
"""
import time
import sys
import pandas as pd


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()

    # Parsing
    df = pd.DataFrame([list(char) for char in entries.strip().splitlines()])
    # get locations of columns that are 'blank'
    dot_columns = df.columns[df.eq('.').all()]
    # get locations of rows that are 'blank'
    dot_rows = df.index[df.eq('.').all(axis=1)]

    # turn locations into tuples.
    positions = [(i, j) for i, row in enumerate(df.values.tolist()) for j, val in enumerate(row) if val == '#']

    sol = 0
    # iter over positions
    for i, pos1 in enumerate(positions, 1):
        for pos2 in positions[i:]:
            # get diff in rows/cols
            d = abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
            # adjust for duplicated galaxy locations along cols and rows
            for col in dot_columns:
                if pos1[1] <= col <= pos2[1] or pos2[1] <= col <= pos1[1]:
                    d += 1
            for row in dot_rows:
                if pos1[0] <= row <= pos2[0] or pos2[0] <= row <= pos1[0]:
                    d += 1
            sol += d
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
