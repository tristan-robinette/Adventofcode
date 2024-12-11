"""
Solution to Advent of Code 2024 day 11 part 1
Solved by doing some magic
"""
import time
import sys
from collections import Counter


def split_stone(stone):
    half = len(str(stone)) // 2
    l, r = divmod(stone, 10 ** half)
    if r % 10 == 0:
        r //= 10
        r *= 10
    return l, r


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = [int(num) for num in file.read().strip().split()]

    stones = Counter(entries)

    for _ in range(25):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_stone(stone)
                new_stones[left] += count
                new_stones[right] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones

    return sum(stones.values())


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
