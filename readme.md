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

#### Jump to solution

[![2022 Day 1 Badge](https://img.shields.io/badge/2022%20Day%201-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-1)
[![2022 Day 2 Badge](https://img.shields.io/badge/2022%20Day%202-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-2)
[![2022 Day 3 Badge](https://img.shields.io/badge/2022%20Day%203-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-3)
[![2022 Day 4 Badge](https://img.shields.io/badge/2022%20Day%204-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-4)
[![2022 Day 5 Badge](https://img.shields.io/badge/2022%20Day%205-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-5)
[![2022 Day 6 Badge](https://img.shields.io/badge/2022%20Day%206-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-6)
[![2022 Day 7 Badge](https://img.shields.io/badge/2022%20Day%207-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-7)
[![2022 Day 8 Badge](https://img.shields.io/badge/2022%20Day%208-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-8)
[![2022 Day 9 Badge](https://img.shields.io/badge/2022%20Day%209-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-9)
[![2022 Day 10 Badge](https://img.shields.io/badge/2022%20Day%2010-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-10)
[![2022 Day 11 Badge](https://img.shields.io/badge/2022%20Day%2011-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-11)

[![2023 Day 1 Badge](https://img.shields.io/badge/2023%20Day%201-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-1-1)
[![2023 Day 2 Badge](https://img.shields.io/badge/2023%20Day%202-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-2-1)
[![2023 Day 3 Badge](https://img.shields.io/badge/2023%20Day%203-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-3-1)
[![2023 Day 4 Badge](https://img.shields.io/badge/2023%20Day%204-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-4-1)
[![2023 Day 5 Badge](https://img.shields.io/badge/2023%20Day%205-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-5-1)
[![2023 Day 6 Badge](https://img.shields.io/badge/2023%20Day%206-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-6-1)
[![2023 Day 7 Badge](https://img.shields.io/badge/2023%20Day%207-none?logo=python&logoColor=f43f5e&color=065f46&labelColor=white&)](#-day-7-1)

<hr>

### Year 2022

### 🎅 Day 1

#### Day 1 Solution Part 1

- **Answer**: 68292
- **Timing**: 0.001828908920288086


<details>
<summary>View code</summary>

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

</details>

#### Day 1 Solution Part 2

- **Answer**: 203203
- **Timing**: 0.001619100570678711


<details>
<summary>View code</summary>

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

</details>

<hr>

### 🍾 Day 2

#### Day 2 Solution Part 1

- **Answer**: 14531
- **Timing**: 0.0012822151184082031


<details>
<summary>View code</summary>

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

</details>

#### Day 2 Solution Part 2

- **Answer**: 11258
- **Timing**: 0.0012898445129394531


<details>
<summary>View code</summary>

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

</details>

<hr>

### ❄️ Day 3

#### Day 3 Solution Part 1

- **Answer**: 7917
- **Timing**: 0.000698089599609375


<details>
<summary>View code</summary>

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

</details>

#### Day 3 Solution Part 2

- **Answer**: 2585
- **Timing**: 0.0006871223449707031


<details>
<summary>View code</summary>

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

</details>

<hr>

### ✨ Day 4

#### Day 4 Solution Part 1

- **Answer**: 518
- **Timing**: 0.00406193733215332


<details>
<summary>View code</summary>

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

</details>

#### Day 4 Solution Part 2

- **Answer**: 909
- **Timing**: 0.0044710636138916016


<details>
<summary>View code</summary>

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

</details>

<hr>

### 🦌 Day 5

#### Day 5 Solution Part 1

- **Answer**: TBVFVDZPN
- **Timing**: 0.005964994430541992


<details>
<summary>View code</summary>

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

</details>

#### Day 5 Solution Part 2

- **Answer**: VLCWHTDSZ
- **Timing**: 0.0019769668579101562


<details>
<summary>View code</summary>

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

</details>

<hr>

### 🎁 Day 6

#### Day 6 Solution Part 1

- **Answer**: 1142
- **Timing**: 0.0006389617919921875


<details>
<summary>View code</summary>

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

</details>

#### Day 6 Solution Part 2

- **Answer**: 2803
- **Timing**: 0.001898050308227539


<details>
<summary>View code</summary>

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

</details>

<hr>

### 🤶 Day 7

#### Day 7 Solution Part 1

- **Answer**: 1306611
- **Timing**: 0.0024399757385253906


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 7 part 1
Solved by doing some magic
"""
import time
import sys
from string import digits


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().strip().splitlines()
	dir_sizes = {}
	checked_f = {}
	crnt_dir = []

	for line in entries:
		ln = line.strip()
		if ln.startswith('$ cd'):
			if not crnt_dir:
				crnt_dir.append('/')
			elif ln.split(' ')[2] == '/':
				crnt_dir = crnt_dir[0]
			elif ln.split(' ')[2] == '..':
				crnt_dir = crnt_dir[:-1]
			else:
				crnt_dir.append(ln.split(' ')[2])

		elif ln[0] in digits:
			dir_str = '\\'.join(crnt_dir)
			if dir_str not in checked_f.keys():
				checked_f[dir_str] = []
			if ln.split(' ')[1] not in checked_f[dir_str]:
				checked_f[dir_str].append(ln.split(' ')[1])
				for f in range(len(crnt_dir)+1):
					if '\\'.join(crnt_dir[:f]) not in dir_sizes.keys():
						if '\\'.join(crnt_dir[:f]).strip() == '':
							continue
						dir_sizes['\\'.join(crnt_dir[:f])] = 0
					dir_sizes['\\'.join(crnt_dir[:f])] += int(line.split(' ')[0])
	return sum(n for n in dir_sizes.values() if n < 100000)
```

</details>

#### Day 7 Solution Part 2

- **Answer**: 13210366
- **Timing**: 0.002366304397583008


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 7 part 2
Solved by doing some magic
"""
import time
import sys
from string import digits


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().strip().splitlines()
	dir_sizes = {}
	checked_f = {}
	crnt_dir = []

	for line in entries:
		ln = line.strip()
		if ln.startswith('$ cd'):
			if not crnt_dir:
				crnt_dir.append('/')
			elif ln.split(' ')[2] == '/':
				crnt_dir = crnt_dir[0]
			elif ln.split(' ')[2] == '..':
				crnt_dir = crnt_dir[:-1]
			else:
				crnt_dir.append(ln.split(' ')[2])

		elif ln[0] in digits:
			dir_str = '\\'.join(crnt_dir)
			if dir_str not in checked_f.keys():
				checked_f[dir_str] = []
			if ln.split(' ')[1] not in checked_f[dir_str]:
				checked_f[dir_str].append(ln.split(' ')[1])
				for f in range(len(crnt_dir)+1):
					if '\\'.join(crnt_dir[:f]) not in dir_sizes.keys():
						if '\\'.join(crnt_dir[:f]).strip() == '':
							continue
						dir_sizes['\\'.join(crnt_dir[:f])] = 0
					dir_sizes['\\'.join(crnt_dir[:f])] += int(line.split(' ')[0])
	sort_vals = sorted(dir_sizes.values())
	space_needed = 30000000-(70000000-sort_vals[-1])
	for n in sort_vals:
		if n >= space_needed:
			return n
```

</details>

<hr>

### 🤍 Day 8

#### Day 8 Solution Part 1

- **Answer**: 1801
- **Timing**: 0.21929192543029785


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 8 part 1
Solved by doing some magic
"""
import time
import sys
import numpy as np


def is_visible(row_ix, column_ix, grid):
	if row_ix in [0, len(grid) - 1]:
		return True
	if column_ix in [0, len(grid[row_ix]) - 1]:
		return True

	value = grid[row_ix][column_ix]
	row = grid[row_ix]
	column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

	left = all(x < value for x in row[:column_ix])
	right = all(x < value for x in row[column_ix + 1:])
	top = all(x < value for x in column[:row_ix])
	bottom = all(x < value for x in column[row_ix + 1:])

	return left or right or top or bottom


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().splitlines()
	grid = np.array([list(row.strip()) for row in entries]).astype('int')
	vis = 0
	for row_num, row in enumerate(grid):
		for col_num, col in enumerate(row):
			if is_visible(row_num, col_num, grid):
				vis += 1
	return vis
```

</details>

#### Day 8 Solution Part 2

- **Answer**: 209880
- **Timing**: 0.20448684692382812


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 8 part 2
Solved by doing some magic
"""
import time
import sys
import numpy as np


def get_score(row_ix, column_ix, grid):
    value = grid[row_ix][column_ix]
    row = grid[row_ix]
    column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

    left, right, top, bottom = 0, 0, 0, 0

    # Check left
    for x in reversed(row[:column_ix]):
        left += 1
        if x >= value:
            break

    # Check right
    for x in row[column_ix + 1:]:
        right += 1
        if x >= value:
            break

    # Check top
    for x in reversed(column[:row_ix]):
        top += 1
        if x >= value:
            break

    # Check bottom
    for x in column[row_ix + 1:]:
        bottom += 1
        if x >= value:
            break

    return left * right * top * bottom


def solution(input_file):
    with open(input_file, 'r') as file:
        entries = file.read().splitlines()
    grid = np.array([list(row.strip()) for row in entries]).astype('int')
    score = []
    for row_num, row in enumerate(grid):
        score.extend(get_score(row_num, col_num, grid) for col_num, col in enumerate(row))
    return max(score)
```

</details>

<hr>

### 🎄 Day 9

#### Day 9 Solution Part 1

- **Answer**: 6023
- **Timing**: 0.018189668655395508


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 9 part 1
Solved by doing some magic
"""
import time
import sys


class Coordinates:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.direction_mapping = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L': (-1, 0)}

	def move_with_direction(self, direction):
		x_shift, y_shift = self.direction_mapping[direction]
		self.x += x_shift
		self.y += y_shift

	def move_to_become_neighbor(self, other_knot):
		if abs(self.x - other_knot.x) == 2 and abs(self.y - other_knot.y) == 2:
			self.x = self.x + int((other_knot.x - self.x) / 2)
			self.y = self.y + int((other_knot.y - self.y) / 2)
		elif abs(self.x - other_knot.x) == 2:
			self.x = self.x + int((other_knot.x - self.x) / 2)
			self.y = other_knot.y
		elif abs(self.y - other_knot.y) == 2:
			self.x = other_knot.x
			self.y = self.y + int((other_knot.y - self.y) / 2)

	@property
	def as_tuple(self):
		return self.x, self.y

	def __repr__(self):
		return f"[{self.x}, {self.y}]"


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read().strip().splitlines()

	number_knots = 2
	knots = [Coordinates() for _ in range(number_knots)]
	tail_coordinates_set = set()
	for direction, number in [row.split() for row in entries]:
		for _ in range(int(number)):
			# this is our parent knot, rest are tail
			knots[0].move_with_direction(direction)
			# offset parent knot and move children to be all fuzzy wuzzy with the parent
			for index, knot in enumerate(knots[1:number_knots], 1):
				knot.move_to_become_neighbor(knots[index - 1])
			# add tail knot to unique set
			tail_coordinates_set.add(knots[number_knots - 1].as_tuple)
	return len(tail_coordinates_set)
```

</details>

#### Day 9 Solution Part 2

- **Answer**: 2533
- **Timing**: 0.0621490478515625


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 9 part 2
Solved by doing some magic
"""
import time
import sys


class Coordinates:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction_mapping = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L': (-1, 0)}

    def move_with_direction(self, direction):
        x_shift, y_shift = self.direction_mapping[direction]
        self.x += x_shift
        self.y += y_shift

    def move_to_become_neighbor(self, other_knot):
        if abs(self.x - other_knot.x) == 2 and abs(self.y - other_knot.y) == 2:
            self.x = self.x + int((other_knot.x - self.x) / 2)
            self.y = self.y + int((other_knot.y - self.y) / 2)
        elif abs(self.x - other_knot.x) == 2:
            self.x = self.x + int((other_knot.x - self.x) / 2)
            self.y = other_knot.y
        elif abs(self.y - other_knot.y) == 2:
            self.x = other_knot.x
            self.y = self.y + int((other_knot.y - self.y) / 2)

    @property
    def as_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return f"[{self.x}, {self.y}]"


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read().strip().splitlines()

    number_knots = 10
    knots = [Coordinates() for _ in range(number_knots)]
    tail_coordinates_set = set()
    for direction, number in [row.split() for row in entries]:
        for _ in range(int(number)):
            # this is our parent knot, rest are tail
            knots[0].move_with_direction(direction)
            # offset parent knot and move children to be all fuzzy wuzzy with the parent
            for index, knot in enumerate(knots[1:number_knots], 1):
                knot.move_to_become_neighbor(knots[index - 1])
            # add tail knot to unique set
            tail_coordinates_set.add(knots[number_knots - 1].as_tuple)
    return len(tail_coordinates_set)
```

</details>

<hr>

### 🏂 Day 10

#### Day 10 Solution Part 1

- **Answer**: 10760
- **Timing**: 0.00040793418884277344


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 10 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	sol = 0
	register_x = 1
	inst = []
	entries = entries.strip().splitlines()
	# add buffer tick if not 'noop'
	for entry in entries:
		splitln = entry.split()
		inst.extend((['noop', 0], [splitln[0], int(splitln[1])])) if len(splitln) > 1 else inst.append([splitln[0], 0])

	for cycle, (instruction, value) in enumerate(inst, 1):
		if (cycle + 20) % 40 == 0:
			sol += register_x * cycle
		register_x += value

	return sol
```

</details>

#### Day 10 Solution Part 2

- **Answer**: FPGPHFGH
- **Timing**: 0.00026917457580566406


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 10 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	register_x = 1
	inst = []
	entries = entries.strip().splitlines()
	screen = [['.']*40 for _ in range(6)]
	# add buffer tick if not 'noop'
	for entry in entries:
		splitln = entry.split()
		inst.extend((['noop', 0], [splitln[0], int(splitln[1])])) if len(splitln) > 1 else inst.append([splitln[0], 0])

	for cycle, (instruction, value) in enumerate(inst, 1):
		rx, cx = divmod(cycle-1, 40)
		if register_x - 1 <= cx <= register_x + 1:
			screen[rx][cx] = '#'
		register_x += value

	print('The result for solution 2 is:')
	for row in screen:
		for ele in row:
			print(ele, end=' ')
		print()

	return 'FPGPHFGH'
```

</details>

<hr>

### 🌿 Day 11

#### Day 11 Solution Part 1

- **Answer**: 119715
- **Timing**: 0.011977910995483398


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 11 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = [line.strip() for line in file.readlines()]

	monkeys = {}
	num_rounds = 20
	monk_count = 0
	for line in entries:
		if not line.strip():
			monk_count += 1
			continue
		if line.startswith("Monkey"):
			monkeys[f"monkey__{monk_count}"] = {
				"starting_items": [],
				"operation": "",
				"test": None, "true": "",
				"false": "",
				"monkeys_inspected": 0
			}
		if line.startswith("Starting"):
			monkeys[f"monkey__{monk_count}"]['starting_items'] = [int(num) for num in line.split(":")[-1].strip().split(",")]
		if line.startswith("Operation"):
			monkeys[f"monkey__{monk_count}"]['operation'] = line.split(":")[-1].split()
		if line.startswith("Test"):
			monkeys[f"monkey__{monk_count}"]['test'] = line.split(":")[-1].strip().split()[-1]
		if line.startswith("If true"):
			monkeys[f"monkey__{monk_count}"]['true'] = line.split(":")[-1].strip()
		if line.startswith("If false"):
			monkeys[f"monkey__{monk_count}"]['false'] = line.split(":")[-1].strip()

	for _ in range(num_rounds):
		for monkey, values in monkeys.items():
			for _ in range(len(values["starting_items"])):
				item = values["starting_items"].pop(0)
				monkeys[monkey]["monkeys_inspected"] += 1
				multiplier = int(values["operation"][-1]) if values["operation"][-1] != "old" else item
				worry = eval(f"{item} {values['operation'][-2]} {multiplier}") // 3
				passes_test = values["true"] if worry % int(values["test"]) == 0 else values["false"]
				monkeys[f"monkey__{int(passes_test.split()[-1])}"]['starting_items'].append(worry)
	monkey1, monkey2 = sorted([monkey["monkeys_inspected"] for monkey in monkeys.values()], reverse=True)[:2]
	return monkey1 * monkey2
```

</details>

#### Day 11 Solution Part 2

- **Answer**: 18085004878
- **Timing**: 5.46789288520813


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2022 day 11 part 2
Solved by doing some magic
"""
import time
import sys
import numpy as np


def solution(input_file):
	with open(input_file,'r') as file:
		entries = [line.strip() for line in file.readlines()]

	monkeys = {}
	num_rounds = 10000
	monk_count = 0
	for line in entries:
		if not line.strip():
			monk_count += 1
			continue
		if line.startswith("Monkey"):
			monkeys[f"monkey__{monk_count}"] = {
				"starting_items": [],
				"operation": "",
				"test": None, "true": "",
				"false": "",
				"monkeys_inspected": 0
			}
		if line.startswith("Starting"):
			monkeys[f"monkey__{monk_count}"]['starting_items'] = [int(num) for num in line.split(":")[-1].strip().split(",")]
		if line.startswith("Operation"):
			monkeys[f"monkey__{monk_count}"]['operation'] = line.split(":")[-1].split()
		if line.startswith("Test"):
			monkeys[f"monkey__{monk_count}"]['test'] = line.split(":")[-1].strip().split()[-1]
		if line.startswith("If true"):
			monkeys[f"monkey__{monk_count}"]['true'] = line.split(":")[-1].strip()
		if line.startswith("If false"):
			monkeys[f"monkey__{monk_count}"]['false'] = line.split(":")[-1].strip()

	worry_divisor = np.prod(
		[int(test['test']) for test in monkeys.values()]
	)

	for _ in range(num_rounds):
		for monkey, values in monkeys.items():
			for _ in range(len(values["starting_items"])):
				item = values["starting_items"].pop(0)
				monkeys[monkey]["monkeys_inspected"] += 1
				multiplier = int(values["operation"][-1]) if values["operation"][-1] != "old" else item
				worry = eval(f"{item} {values['operation'][-2]} {multiplier}")
				worry = int(worry % worry_divisor)
				passes_test = values["true"] if worry % int(values["test"]) == 0 else values["false"]
				monkeys[f"monkey__{int(passes_test.split()[-1])}"]['starting_items'].append(worry)
	monkey1, monkey2 = sorted([monkey["monkeys_inspected"] for monkey in monkeys.values()], reverse=True)[:2]
	return monkey1 * monkey2
```

</details>

<hr>

### Year 2023

### ⛄ Day 1

#### Day 1 Solution Part 1

- **Answer**: 54644
- **Timing**: 0.0014107227325439453


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 1 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	result = 0
	entries = entries.splitlines()
	for line in entries:
		numbers_in_line = [char for char in line if not char.isalpha()]
		result += int(f"{numbers_in_line[0]}{numbers_in_line[-1]}")
	return result
```

</details>


#### Day 1 Solution Part 2

- **Answer**: 53348
- **Timing**: 0.013229846954345703


<details>
<summary>View code</summary>

```python
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
```

</details>


<hr>

### 🎁 Day 2

#### Day 2 Solution Part 1

- **Answer**: 2061
- **Timing**: 0.0006868839263916016


<details>
<summary>View code</summary>

```python
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
```

</details>


#### Day 2 Solution Part 2

- **Answer**: 72596
- **Timing**: 0.0009760856628417969


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 2 part 2
Solved by doing some magic
"""
import time
import sys
from functools import reduce
import math


def solution(input_file):
	with open(input_file, 'r') as file:
		entries = file.read().strip().splitlines()

	result = 0
	for line in entries:
		game, game_sets = line.split(":")
		config = {}
		for gs in game_sets.strip().split(";"):
			for num, color in (r.split() for r in gs.split(",")):
				config[color] = max(config.get(color,0), int(num))
		power = reduce(lambda x, y: x * y, config.values(), 1)
		result += power
	return result
```

</details>


<hr>

### 🦌 Day 3

#### Day 3 Solution Part 1

- **Answer**: 535078
- **Timing**: 0.013290166854858398


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 3 part 1
Solved by doing some magic
"""

import itertools
import time
import sys


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()

    result = 0
    entries = entries.strip()

    # Parsing
    entries = entries.splitlines()

    for i, line in enumerate(entries):
        current_number = ""
        add_number = False

        for idx, char in enumerate(line):
            if char.isdigit():
                current_number += char
                # for each character in the 3x3 grid around the digit
                for x, y in itertools.product(
                        range(max(0, i - 1), min(len(entries), i + 2)),
                        range(max(0, idx - 1), min(len(line), idx + 2))
                ):
                    # exclude the digit itself
                    if x == i and y == idx:
                        continue
                    # if the character is not a digit and not a dot its a symbol
                    if entries[x][y] != "." and not entries[x][y].isdigit():
                        add_number = True
            elif add_number and current_number != "":
                result += int(current_number)
                add_number = False
                current_number = ""
            else:
                add_number = False
                current_number = ""
        if add_number and current_number != "":
            result += int(current_number)
    return result
```

</details>


#### Day 3 Solution Part 2

- **Answer**: 75312571
- **Timing**: 0.019262075424194336


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 3 part 2
Solved by doing some magic
"""

import itertools
import time
import sys
from collections import defaultdict


def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()

    entries = entries.strip()

    # Parsing
    entries = entries.splitlines()
    gears = defaultdict(list)
    for i, line in enumerate(entries):
        current_number = ""
        # symbols are tuple of (symbol, x, y)
        adjacent_symbols = set()

        for idx, char in enumerate(line):
            if char.isdigit():
                current_number += char
                # same eval as p1
                for x, y in itertools.product(
		                range(max(0, i - 1), min(len(entries), i + 2)),
		                range(max(0, idx - 1), min(len(line), idx + 2))
                ):
                    if x == i and y == idx:
                        continue
                    if entries[x][y] != "." and not entries[x][y].isdigit():
                        # track position
                        adjacent_symbols.add((entries[x][y], x, y))

            elif len(adjacent_symbols) != 0 and current_number != "":
                for symbol, x, y in adjacent_symbols:
                    if symbol == "*":
                        gears[(x, y)].append(int(current_number))
                adjacent_symbols = set()
                current_number = ""
            else:
                adjacent_symbols = set()
                current_number = ""
        if len(adjacent_symbols) != 0 and current_number != "":
            for symbol, x, y in adjacent_symbols:
                if symbol == "*":
                    gears[(x, y)].append(int(current_number))
    # Sum only if 2 exact parts
    return sum(
        values[0] * values[1] for values in gears.values() if len(values) == 2
    )
```

</details>


<hr>

### 🎄 Day 4

#### Day 4 Solution Part 1

- **Answer**: 23847
- **Timing**: 0.0009360313415527344


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 4 part 1
Solved by doing some magic
"""
import time
import sys
from functools import reduce


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	sol = 0
	for card in entries.splitlines():
		winning_set, your_set = card.split(":")[-1].strip().split("|")
		# Check if shared values between lists
		if inner := set(winning_set.split()).intersection(set(your_set.split())):
			sol += reduce(lambda x, y: x * 2, list(inner)[:-1], 1)
	return sol
```

</details>


#### Day 4 Solution Part 2

- **Answer**: 8570000
- **Timing**: 1.7587859630584717


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 4 part 2
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()
	# will store the card number + copies of the card
	mapping = {k+1:1 for k in range(len(entries.splitlines()))}
	for i, card in enumerate(entries.splitlines(), 1):
		# can set the initial instance of the card.
		num_matches = 0
		winning_set, your_set = card.split(":")[-1].strip().split("|")
		# Check if shared values between lists
		if inner := set(winning_set.split()).intersection(set(your_set.split())):
			num_matches = len(inner)
			# for each match add the new instance to mapping
			for ix in range(num_matches):
				mapping[ix + i + 1] = mapping.get(ix + i + 1, 0) + 1
		# for copies of card, clone forwards
		for _ in range(mapping.get(i) - 1):
			for ix in range(num_matches):
				mapping[ix + i + 1] = mapping.get(ix + i + 1, 0) + 1
	return sum(mapping.values())
```

</details>


<hr>

### 🤶 Day 5

#### Day 5 Solution Part 1

- **Answer**: 199602917
- **Timing**: 0.0005702972412109375


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 5 part 1
Solved by doing some magic
"""
import time
import sys


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()

	# Parsing
	entries = entries.strip()
	parts = entries.split("\n\n")
	seeds = [int(seed) for seed in parts[0].split(":")[-1].strip().split()]
	mapping = {}

	for m in parts[1:]:
		lines = m.splitlines()
		name = lines[0].strip(":")
		soil_ranges = []
		seed_ranges = []

		for line in lines[1:]:
			destination_range_start, source_range_start, length = map(int, line.split())
			soil_ranges.append((destination_range_start, destination_range_start + length - 1))
			seed_ranges.append((source_range_start, source_range_start + length - 1))
		mapping[name] = {'soil_ranges': soil_ranges, 'seed_ranges': seed_ranges}

	locations = []
	for seed in seeds:
		seed_map = {}
		current_seed_number = seed
		for i, name in enumerate(mapping):
			seed_ranges = mapping[name].get("seed_ranges")
			soil_ranges = mapping[name].get("soil_ranges")
			for seed_range, target_range in zip(seed_ranges, soil_ranges):
				# min, max of range is stored as tuple.
				if seed_range[0] <= current_seed_number <= seed_range[1]:
					current_seed_number += target_range[0] - seed_range[0]
					break
			seed_map[name] = current_seed_number
		locations.append(seed_map["humidity-to-location map"])
	return min(locations)
```

</details>


#### Day 5 Solution Part 2

- **Answer**: 2254686
- **Timing**: 14.684205055236816


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 5 part 2
Solved by doing some magic
"""
import time
import sys


def parse_map(conversion_map_raw):
    map_lst = conversion_map_raw.splitlines()
    conversion_rules = []
    for row in map_lst[1:]:
        dest, source, range_length = [int(num) for num in row.split()]
        conversion_rules.append((dest, source, range_length))
    return conversion_rules

def find_location(seed, maps):
    current = seed
    for rule in maps:
        for dest, source, range_length in rule:
            if source <= current < source + range_length:
                current = current - source + dest
                break
    return current

def solution(input_file):
    with open(input_file,'r') as file:
        seeds_raw, *conversion_maps_raw = file.read().split("\n\n")
    seeds = [int(num) for num in seeds_raw.split()[1:]]
    maps = list(map(parse_map, conversion_maps_raw))

    seeds_ranges = [
        (seeds[i - 1], seeds[i - 1] + seed)
        for i, seed in enumerate(seeds)
        if i % 2 == 1
    ]
    maps = [[(end, s, seed_range) for s, end, seed_range in rule] for rule in maps][::-1]
    location = 0
    while True:
        seed = find_location(location, maps)
        if any(s <= seed < end for s, end in seeds_ranges):
            return location
        location += 1
```

</details>


<hr>

### 🎅 Day 6

#### Day 6 Solution Part 1

- **Answer**: 3316275
- **Timing**: 0.00021004676818847656


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 6 part 1
Solved by doing some magic
"""
import time
import sys
from functools import reduce


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	# Parsing
	entries = entries.strip().splitlines()
	simulations = []

	time_entries = [int(e) for e in entries[0].split(":")[-1].strip().split()]
	distance_entries = [int(e) for e in entries[1].split(":")[-1].strip().split()]
	for i, (time_entry, record_distance) in enumerate(zip(time_entries, distance_entries)):
		for time_held in range(time_entry):
			if (time_held * (time_entry - time_held)) > record_distance:
				if len(simulations) < len(time_entries):
					simulations.append(0)
				simulations[i] += 1
	return reduce(lambda x, y: x * y, simulations, 1)
```

</details>


#### Day 6 Solution Part 2

- **Answer**: 27102791
- **Timing**: 3.1184029579162598


<details>
<summary>View code</summary>

```python
"""
Solution to Advent of Code 2023 day 6 part 2
Solved by doing some magic
"""
import time
import sys
from functools import reduce


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	# Parsing
	entries = entries.strip().splitlines()
	time_entry = int("".join(entries[0].split(":")[-1].strip().split()))
	record_distance = int("".join(entries[1].split(":")[-1].strip().split()))
	return sum(
		time_held * (time_entry - time_held) > record_distance
		for time_held in range(time_entry)
	)
```

</details>


<hr>


### ❄️ Day 7

#### Day 7 Solution Part 1

- **Answer**: 251106089
- **Timing**: 0.003312826156616211


<details>
<summary>View code</summary>

```python
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
```

</details>


#### Day 7 Solution Part 2

- **Answer**: 249620106
- **Timing**: 0.004178762435913086


<details>
<summary>View code</summary>

```python
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
```

</details>


<hr>