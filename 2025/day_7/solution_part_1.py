"""
Solution to Advent of Code 2025 day 7 part 1
Solved by doing some magic
"""
import time
import sys

splitter = "^"

def walk_grid(from_position: tuple[int, int], grid: list[str], seen: set[tuple[int, int]]):
    row, col = from_position
    beams = []
    while grid[row][col] != splitter and row + 1 < len(grid):
        row, col = row + 1, col
        if grid[row][col] == splitter:
            for direction in (1, -1):
                new_pos = (row, col + direction)
                if new_pos not in seen:
                    beams.append(new_pos)
            return beams
    return beams

def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()
    entries = entries.strip()
    starting_pos = None
    starting_char = 'S'
    grid = []
    for i, row in enumerate(entries.splitlines()):
        vals = list(row)
        grid.append(vals)
        if starting_char in vals:
            starting_pos = (i, vals.index(starting_char))
    sol = 0
    seen = set()

    beams = [starting_pos]
    while beams:
        new_beams = walk_grid(beams.pop(), grid, seen)
        seen.update(new_beams)
        beams += new_beams
        sol += len(new_beams) > 0
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
