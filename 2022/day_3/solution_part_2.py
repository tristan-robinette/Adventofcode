"""
Solution to Advent of Code 2022 day 3 part 1
Solved by doing some magic
"""
import time
import sys
import string

alphabet = string.ascii_lowercase
alpha_dic = {char: i for i, char in enumerate(alphabet + alphabet.upper(), 1)}


def solution(input_file):
    with open(input_file, 'r') as file:
        groups = []
        current_group = []
        # create elf groups
        for line in [line.strip() for line in file.readlines()]:
            current_group.append(set(list(line)))
            if len(current_group) == 3:
                groups.append(current_group)
                current_group = []
    return sum(alpha_dic[set.intersection(*group).pop()] for group in groups)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")