"""
Solution to Advent of Code 2024 day 5 part 1
Solved by doing some magic
"""
import time
import sys


def swappy_papi(update, rules):
    changed = True
    while changed:
        changed = False
        for rule in rules:
            r1, r2 = rule
            if r1 in update and r2 in update:
                i1, i2 = update.index(r1), update.index(r2)
                if i1 > i2:
                    update[i1], update[i2] = update[i2], update[i1]
                    changed = True


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read().strip()

    rules, updates = [], []
    for entry in entries.splitlines():
        if "|" in entry:
            rules.append([int(e) for e in entry.split('|')])
        elif entry:
            updates.append([int(e) for e in entry.split(',')])

    sol = 0
    for update in updates:
        original = update.copy()
        swappy_papi(update, rules)
        if update == original:
            mid_index = (len(update) - 1) // 2
            sol += update[mid_index]

    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
