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

### 🎄 Day 1 

##### Day 1 Solution Part 1 

- Answer: 68292 
- Timing: 0.001188039779663086 


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
- Timing: 0.0010559558868408203 


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

### ☕ Day 2 

##### Day 2 Solution Part 1 

- Answer: 14531 
- Timing: 0.0008630752563476562 


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
- Timing: 0.0011868476867675781 


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

### 🍫 Day 3 

##### Day 3 Solution Part 1 

- Answer: 7917 
- Timing: 0.0005249977111816406 


```python
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
        alpha_dic[
            set(line[: len(line) // 2])
            .intersection(line[len(line) // 2 :])
            .pop()
        ]
        for line in [
            line.strip() for line in open(input_file, 'r').readlines()
        ]
    )



```
##### Day 3 Solution Part 2 

- Answer: 2585 
- Timing: 0.0005071163177490234 


```python
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
    with open(input_file, 'r') as file:
        groups = []
        current_group = []
        # create elf groups
        for line in [line.strip() for line in file.readlines()]:
            current_group.append(set(list(line)))
            if len(current_group) == 3:
                groups.append(current_group)
                current_group = []
    return sum(alpha_dic[set.intersection(*group).pop()] for group in groups)



```
<hr>

### 🥂 Day 4 

##### Day 4 Solution Part 1 

- Answer: 518 
- Timing: 0.002772092819213867 


```python
"""
Solution to Advent of Code 2022 day 4 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	# Parsing
	entries = [line.split(",") for line in entries.strip().splitlines()]
	sol = 0
	for entry in entries:
		# more parsing...
		elf1, elf2 = [list(map(int, e.split("-"))) for e in entry]  # must be better way doing this??
		# create ranges for each section with adding 1 to account for 0 based
		elf1_range = set(range(elf1[0], elf1[1] + 1))
		elf2_range = set(range(elf2[0], elf2[1] + 1))
		# check both cases of full ranges being in either elves sections.
		if set.issubset(elf2_range, elf1_range):
			sol += 1
		elif set.issubset(elf1_range, elf2_range):
			sol += 1
	return sol



```
##### Day 4 Solution Part 2 

- Answer: 909 
- Timing: 0.002775907516479492 


```python
"""
Solution to Advent of Code 2022 day 4 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	# Parsing
	entries = [line.split(",") for line in entries.strip().splitlines()]
	sol = 0
	for entry in entries:
		# more parsing...
		elf1, elf2 = [list(map(int, e.split("-"))) for e in entry]  # must be better way doing this??
		# create ranges for each section with adding 1 to account for 0 based
		elf1_range = set(range(elf1[0], elf1[1] + 1))
		elf2_range = set(range(elf2[0], elf2[1] + 1))
		# check both cases of full ranges being in either elves sections.
		if set.intersection(elf2_range, elf1_range):
			sol += 1
		elif set.intersection(elf1_range, elf2_range):
			sol += 1
	return sol



```
<hr>

### ⛄ Day 5 

##### Day 5 Solution Part 1 

- Answer: TBVFVDZPN 
- Timing: 0.0037679672241210938 


```python
"""
Solution to Advent of Code 2022 day 5 part 1
Solved by doing some magic
"""
import time
import sys
import pandas as pd


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.readlines()
	instructions = [line.strip() for line in entries if 'move' in line]
	above_instructions = [line for line in entries if 'move' not in line]
	number_cols = max(int(num) for num in above_instructions[-2].split())  # get how many cols there are supposed to be
	crates = above_instructions[:-2]  # last items is a newline and numbers row so we remove
	data = []
	for line in crates:
		line = line.replace("    ", "\n").replace("\n", " ").split(" ")  # elf style parsing. dont ask.
		items = line[:-1] if not line[-1] else line  # strips out lines that end in blanks
		data.append(items)
	df = pd.DataFrame(columns=[str(num + 1) for num in range(number_cols)], data=data)
	final_arr = [[val for val in a if val] for a in [df[col].tolist() for col in df.columns]]

	for instruction in instructions:
		action, number_to_move, from_col, from_col_num, to_col, to_col_num = instruction.split()  # <-- lol
		from_col_num = int(from_col_num)
		number_to_move = int(number_to_move)
		to_col_num = int(to_col_num)
		for _ in range(number_to_move):
			# get the value to move
			arr_value_move = final_arr[from_col_num - 1][0]
			# update the array with removed value
			final_arr[from_col_num - 1] = final_arr[from_col_num - 1][1:]
			# update the new array
			final_arr[to_col_num - 1] = [arr_value_move] + final_arr[to_col_num - 1]
	return "".join(arr[0] for arr in final_arr).replace("[","").replace("]","")



```
##### Day 5 Solution Part 2 

- Answer: VLCWHTDSZ 
- Timing: 0.0007109642028808594 


```python
"""
Solution to Advent of Code 2022 day 5 part 2
Solved by doing some magic
"""
import time
import sys
import pandas as pd


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.readlines()
	instructions = [line.strip() for line in entries if 'move' in line]
	above_instructions = [line for line in entries if 'move' not in line]
	number_cols = max(int(num) for num in above_instructions[-2].split())  # get how many cols there are supposed to be
	crates = above_instructions[:-2]  # last items is a newline and numbers row so we remove
	data = []
	for line in crates:
		line = line.replace("    ", "\n").replace("\n", " ").split(" ")  # elf style parsing. dont ask.
		items = line[:-1] if not line[-1] else line  # strips out lines that end in blanks
		data.append(items)
	df = pd.DataFrame(columns=[str(num + 1) for num in range(number_cols)], data=data)
	final_arr = [[val for val in a if val] for a in [df[col].tolist() for col in df.columns]]

	for instruction in instructions:
		# remove loop and grab len(num_to_move) from array instead
		action, number_to_move, from_col, from_col_num, to_col, to_col_num = instruction.split()  # <-- lol
		from_col_num = int(from_col_num)
		number_to_move = int(number_to_move)
		to_col_num = int(to_col_num)
		arr_value_move = final_arr[from_col_num - 1][:int(number_to_move)]
		# update the array with removed value
		final_arr[from_col_num - 1] = final_arr[from_col_num - 1][int(number_to_move):]
		# update the new array
		final_arr[to_col_num - 1] = arr_value_move + final_arr[to_col_num - 1]
	return "".join(arr[0] for arr in final_arr).replace("[","").replace("]","")



```
<hr>

### 🍪 Day 6 

##### Day 6 Solution Part 1 

- Answer: 1142 
- Timing: 0.0004737377166748047 


```python
"""
Solution to Advent of Code 2022 day 6 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().strip()
	min_char_before_marker = 4

	for i, char in enumerate(entries, 1):
		if i < min_char_before_marker:
			continue
		if len(set(entries[i - min_char_before_marker: i])) == min_char_before_marker:
			return i



```
##### Day 6 Solution Part 2 

- Answer: 2803 
- Timing: 0.0013110637664794922 


```python
"""
Solution to Advent of Code 2022 day 6 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().strip()
	min_char_before_marker = 14

	for i, char in enumerate(entries, 1):
		if i < min_char_before_marker:
			continue
		if len(set(entries[i - min_char_before_marker: i])) == min_char_before_marker:
			return i



```
<hr>



