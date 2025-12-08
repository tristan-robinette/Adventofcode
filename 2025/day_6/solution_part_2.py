"""
Solution to Advent of Code 2025 day 6 part 2
Solved by doing some magic
"""
import time
import sys
import pandas as pd
import math

def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	df = pd.DataFrame([list(row) for row in entries.splitlines()]).fillna("")
	# find all columns that are empty and use as ranges as the sep for a given problem.
	breaks = [c for c in df.columns if df[c].str.strip().eq("").all()]
	all_cols = list(df.columns)

	segments = []
	offset = 0
	# build the segments for each problem.
	for b in breaks:
		segments.append(all_cols[offset:b])
		offset = b + 1
	segments.append(all_cols[offset:])

	sol = 0
	problem_operator = {"*": math.prod, "+": sum}
	# iterate over problems, join the column values and use assigned operator.
	for problem in [df.loc[:, seg] for seg in segments]:
		entries = []
		operator = None
		for column in problem.columns:
			series = df.loc[:, column]
			column_string = ''.join(series)
			mask = series.isin(problem_operator)
			if mask.any():
				operator = problem_operator[series[mask].iloc[0]]
				column_string = column_string.replace(series[mask].iloc[0], '', 1)
			entries.append(int(column_string))
		entries.reverse()
		sol += operator(entries)
	return sol

if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
