"""
Solution to Advent of Code 2025 day 11 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    entries = [row.split(":") for row in entries.splitlines()]
    connections = {device: outputs.split() for (device, outputs) in entries}

    starting_node, ending_node, must_visit = "svr", "out", {"dac", "fft"}

    memo = {}
    def count_paths(node: str, visited: frozenset):
        key = (node, visited)
        if key in memo:
            return memo[key]

        new_visited = visited | ({node} if node in must_visit else set())

        if node == ending_node:
            return 1 if new_visited == must_visit else 0

        total = 0
        for nxt in connections[node]:
            total += count_paths(nxt, new_visited)

        memo[key] = total
        return total

    return count_paths(starting_node, frozenset())


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
