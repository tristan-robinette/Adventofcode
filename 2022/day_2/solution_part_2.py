"""
Solution to Advent of Code 2022 day 2 part 2
Solved by doing some magic
"""
import time
import sys

# easier to think of who wins in if/else block this way, not actually needed
mapping = {"A": "rock", "B": "paper", "C": "scissors"}

# key is the choice. Value is array of outcomes based on desired scenario.
# First choice is win, second is loss, third is draw
grid = {
    "rock": ["paper", "scissors", "rock"],
    "paper": ["scissors", "rock", "paper"],
    "scissors": ["rock", "paper", "scissors"],
}

points = {"rock": 1, "paper": 2, "scissors": 3}


def solution(input_file):
    with open(input_file, 'r') as file:
        data = [line.strip().split(" ") for line in file.readlines()]
        score = 0
        for line in data:
            # parsing
            player1, player2 = line
            player_1_choice = mapping[player1]
            if player2 == "X":
                # we lose!
                player_2_choice = grid[player_1_choice][1]
                score += points[player_2_choice]
            elif player2 == "Y":
                # we draw!
                score += points[player_1_choice] + 3  # can choose any choice since the same
            else:
                # we win!
                player_2_choice = grid[player_1_choice][0]
                score += points[player_2_choice] + 6
    return score


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")