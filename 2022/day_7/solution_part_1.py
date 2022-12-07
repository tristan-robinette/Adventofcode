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


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
