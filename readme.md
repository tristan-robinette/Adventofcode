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

### 🥛 Day 1 

##### Day 1 Solution Part 1 

- Answer: 68292 
- Timing: 0.0012252330780029297 


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
- Timing: 0.0010440349578857422 


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

### 🕯 Day 2 

##### Day 10 Solution Part 1 

- Answer: 10760 
- Timing: 0.0002760887145996094 


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
##### Day 10 Solution Part 2 

- Answer: FPGPHFGH 
- Timing: 0.00016617774963378906 


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
<hr>

### 🤍 Day 3 

##### Day 11 Solution Part 1 

- Answer: 119715 
- Timing: 0.0063822269439697266 


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
##### Day 11 Solution Part 2 

- Answer: 18085004878 
- Timing: 2.73844313621521 


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
<hr>



