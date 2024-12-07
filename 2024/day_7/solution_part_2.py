"""
Solution to Advent of Code 2024 day 7 part 2
Solved by doing some magic
"""
import itertools
import time
import sys


def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i + 1])
        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
        elif operator == '||':
            result = int(f"{result}{number}")
    return result


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read()
    entries = entries.strip()

    # Parsing
    entries = entries.splitlines()

    sol = 0
    for line in entries:
        test_val, nums = line.split(":")
        nums = nums.split()
        for ops in itertools.product(['+', '*', '||'], repeat=len(nums) - 1):
            # this creates a string like '1 + 3 * 6' where all possible operators are tried
            # to pass into the eval function.
            expression = " ".join(num + " " + op for num, op in zip(nums, ops + ('',)))
            result = evaluate_left_to_right(expression)
            if int(result) == int(test_val):
                sol += int(test_val)
                break
    return sol


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
