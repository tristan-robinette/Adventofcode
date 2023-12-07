"""
Solution to Advent of Code 2023 day 7 part 2
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
    num_jokers = hand.count(11)
    hand_without_jokers = tuple(card for card in hand if card != 11)
    trick_strength = list(sorted(Counter(hand_without_jokers).values(), reverse=True))
    if not trick_strength:
        trick_strength = (5,)
    else:
        trick_strength[0] += num_jokers
    trick_strength = tuple(trick_strength)

    new_hand = tuple(1 if card == 11 else card for card in hand)
    return trick_strength, new_hand


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
