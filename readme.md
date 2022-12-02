### AdventofCode
Solutions to the Advent of Code puzzles with some incredibly overkill generative scripts. It's the holidays, have fun with it.

https://adventofcode.com

While in root directory run the following command to automatically:
1. Create a new directory with todays day nested under the current year
2. Create an input.txt file to quickly copy/paste the advent data
3. Create 2 solution.py files (1 for each part) with starter code to read in the txt file and start smashing away at a solution

If you know your a baller and going to complete EVERY challenge you can add the '--all' flag to create a new directory for every day of te month instead of just todays date.

Finally, if you want to overwrite a directory add '--overwrite' and all files will be replaced.

Non baller way of creating new directory

``
python create_new_day.py
``

Baller way of creating a directory for every day of month

``
python create_new_day.py --all
``

Now it's time to update the readme with all your solutions. Because if displayed code isnt pretty than I don't know what is.
Anyways, doing this is easy, define a 'readmetemplate.md' in the root folder and run the following script:

``python update_readme_stats.py``

This will automatically run your solutions, time it and display each solution for each day in the readme.

Bonkers.

<hr>



# Solutions 

### Year 2022

### ❄️ Day 1 

##### Day 1 Solution Part 1 

- Answer: 68292 
- Timing: 0.0011060237884521484 


```python
"""
Solution to Advent of Code 2022 day 1 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
    elf_calories = {}
    with open(input_file, 'r') as file:
        data = file.read().split("\n")
        current_elf = 1
        for line in data:
            if len(line) == 0:
                current_elf += 1
                continue
            elf_calories[str(current_elf)] = elf_calories.get(str(current_elf), 0) + int(line)
    return max(elf_calories.values())



```
##### Day 1 Solution Part 2 

- Answer: 203203 
- Timing: 0.0009961128234863281 


```python
"""
Solution to Advent of Code 2022 day 1 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
    elf_calories = {}
    with open(input_file, 'r') as file:
        data = file.read().split("\n")
        current_elf = 1
        for line in data:
            if len(line) == 0:
                current_elf += 1
                continue
            elf_calories[str(current_elf)] = elf_calories.get(str(current_elf), 0) + int(line)
    return sum(sorted(elf_calories.values(), reverse=True)[:3])



```
<hr>

### 👪 Day 2 

##### Day 2 Solution Part 1 

- Answer: 14531 
- Timing: 0.0009050369262695312 


```python
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



```
##### Day 2 Solution Part 2 

- Answer: 11258 
- Timing: 0.001074075698852539 


```python
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



```
<hr>



