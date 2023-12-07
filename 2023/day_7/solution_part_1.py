"""
Solution to Advent of Code 2023 day 7 part 1
Solved by doing some magic
"""
import time
import sys
from collections import Counter


def get_numerical_card(card):
    if card.isdigit():
        return int(card)
    return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card]


def get_hand_strength(hand):
    trick_strength = tuple(sorted(Counter(hand).values(), reverse=True))
    return trick_strength, hand

def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()
    entries = entries.strip()
    hands = []
    for line in entries.splitlines():
        hand, bid = line.split()
        hands.append((tuple(get_numerical_card(c) for c in hand), int(bid)))
    hands.sort(key=lambda p: get_hand_strength(p[0]))
    return sum(int(pair[1]) * (i + 1) for i, pair in enumerate(hands))


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
