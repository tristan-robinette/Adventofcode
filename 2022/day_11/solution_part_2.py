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


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
