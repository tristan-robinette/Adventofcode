"""
Solution to Advent of Code 2023 day 1 part 2
Solved by doing some magic
"""
import time
import re
import sys

word_digit_pairs = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')
]

def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()
    entries = entries.strip()
    result = 0
    entries = entries.splitlines()
    for line in entries:
        # has to be a better way than this???
        numbers_found = []
        for word, digit in word_digit_pairs:
            matches = re.finditer(word, line)
            numbers_found.extend((digit, match.start()) for match in matches)
        [numbers_found.append((char, pos)) for pos, char in enumerate(line) if not char.isalpha()]
        numbers_in_line = sorted(numbers_found,key=lambda x: x[1])
        result += int(f"{numbers_in_line[0][0]}{numbers_in_line[-1][0]}")
    return result


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
