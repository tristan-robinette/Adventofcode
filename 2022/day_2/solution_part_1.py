"""
Solution to Advent of Code 2022 day 2 part 1
Solved by doing some magic
"""
import time
import sys
import numpy as np
from collections import Counter
import re


# easier to think of who wins in if/else block this way, not actually needed
mapping = {"A": "rock", "X": "rock", "B": "paper", "Y": "paper", "C": "scissors", "Z": "scissors"}

points = {"rock": 1, "paper": 2, "scissors": 3}


def solution(input_file):
    with open(input_file, 'r') as file:
        data = file.readlines()
        score = 0
        for line in data:
            # parsing
            line = line.strip().split(" ")
            player1, player2 = line
            player_1_choice, player_2_choice = mapping[player1], mapping[player2]
            if player_1_choice == player_2_choice:
                # draw case
                score += points[player_1_choice] + 3  # can choose any choice since the same
            # lose case
            elif player_1_choice == "rock" and player_2_choice == "scissors":
                score += points[player_2_choice]
            elif player_1_choice == "paper" and player_2_choice == "rock":
                score += points[player_2_choice]
            elif player_1_choice == "scissors" and player_2_choice == "paper":
                score += points[player_2_choice]
            else:
                # we won!
                score += points[player_2_choice] + 6
    return score


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")