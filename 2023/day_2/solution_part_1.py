"""
Solution to Advent of Code 2023 day 2 part 1
Solved by doing some magic
"""
import time
import sys

def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read().strip().splitlines()

    # Setup limits
    config = {"green": 13, "blue": 14, "red": 12}
    invalid_games = set()
    result = 0
    for line in entries:
        game, game_sets = line.split(":")
        game_id = int(game.split()[-1])
        for gs in game_sets.strip().split(";"):
            # Check if any cube is over config limit and track that gameID as invalid
            if any(config[color] < int(num) for num, color in (r.split() for r in gs.split(","))):
                invalid_games.add(game_id)
                break
        # Remaining games are valid
        if game_id not in invalid_games:
            result += game_id

    return result


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
