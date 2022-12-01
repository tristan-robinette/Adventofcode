"""
Solution to Advent of Code 2022 day 1 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
    elf_calories = {}
    with open(input_file, 'r') as file:
        data = file.read().split("\n")
        current_elf = 1
        for line in data:
            if len(line) == 0:
                current_elf += 1
                continue
            elf_calories[str(current_elf)] = elf_calories.get(str(current_elf), 0) + int(line)
    return sum(sorted(elf_calories.values(), reverse=True)[:3])


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")