"""
Solution to Advent of Code 2025 day 9 part 2
Solved by doing some magic
"""
import time
import sys

from shapely import box
from shapely.geometry.polygon import Polygon


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    entries = [tuple(map(int, row.split(","))) for row in entries.splitlines()]
    # shoutout joseph brosef for shapely.
    poly = Polygon(entries)
    # Solving
    sol = 0
    for i, (x1, y1) in enumerate(entries):
        for j, (x2, y2) in enumerate(entries):
            if i >= j:
                continue
            if x1 == x2 or y1 == y2:
                continue
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            rect = box(min_x, min_y, max_x, max_y)
            # Check if rectangle is completely inside the polygon
            if poly.contains(rect):
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                sol = max(sol, area)
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
