"""
Solution to Advent of Code 2024 day 6 part 2
Solved by doing some magic
"""
import time
import sys
from itertools import cycle


def solution(input_file):

    with open(input_file, 'r') as file:
        entries = file.read()

    entries = entries.strip().splitlines()
    visited = set()
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    guard_pos = None
    initial_guard_pos = None

    for i, row in enumerate(entries):
        if '^' in row:
            guard_pos = (i, row.index('^'))
            initial_guard_pos = guard_pos
            break

    current_dir = next(directions)
    while True:
        r, c = guard_pos
        visited.add((r, c))
        rl, cl = current_dir
        next_r, next_c = r + rl, c + cl

        if not (0 <= next_r < len(entries) and 0 <= next_c < len(entries[0])):
            break

        next_pos = entries[next_r][next_c]
        if next_pos == "#":
            current_dir = next(directions)
        else:
            guard_pos = (next_r, next_c)

    def is_guard_fked(grid, init_pos):
        dirs = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
        gp = init_pos
        cd = next(dirs)

        unique_paths = set()
        rows, cols = len(grid), len(grid[0])

        while True:
            r, c = gp
            rl, cl = cd
            next_r, next_c = r + rl, c + cl

            if not (0 <= next_r < rows and 0 <= next_c < cols):
                return False

            next_pos = grid[next_r][next_c]

            if (r, c, cd) in unique_paths:
                return True

            if next_pos == "#":
                cd = next(dirs)
            else:
                unique_paths.add((r, c, cd))
                gp = (next_r, next_c)

    sol = 0
    for loc in visited:
        if loc == initial_guard_pos:
            continue
        g = entries.copy()
        r, c = loc
        row_as_list = list(g[r])
        row_as_list[c] = "#"
        g[r] = ''.join(row_as_list)
        is_fked = is_guard_fked(g, initial_guard_pos)
        sol += is_fked
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
