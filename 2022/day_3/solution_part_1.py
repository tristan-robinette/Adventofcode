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
    return sum(
        [alpha_dic[set([char for char in line[:len(line) // 2]]).intersection(
            [char for char in line[len(line) // 2:]]).pop()]
         for line in [line.strip() for line in open(input_file, 'r').readlines()]]
    )


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")