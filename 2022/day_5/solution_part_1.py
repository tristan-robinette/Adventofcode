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
		if len(items) < number_cols:
			for _ in range(number_cols - len(items)):
				items += [""]
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


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
