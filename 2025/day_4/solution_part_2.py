"""
Solution to Advent of Code 2025 day 4 part 2
Solved by doing some magic
"""
import time
import sys

def remove_from_grid(grid: list[str]):
	directions = [
		(0, 1),  # Right
		(0, -1),  # Left
		(1, 0),  # Down
		(-1, 0),  # Up
		(1, 1),  # Down-right diagonal
		(-1, -1),  # Up-left diagonal
		(1, -1),  # Down-left diagonal
		(-1, 1),  # Up-right diagonal
	]
	roll_char = "@"
	max_paper_in_area = 4
	new_grid = grid.copy()
	removed_count = 0
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			candidate = grid[row][col]
			count = 0
			if candidate != roll_char: continue
			for dr, dc in directions:
				nr, nc = row + dr, col + dc
				if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
					surrounding_candidate = grid[nr][nc]
					count += surrounding_candidate == roll_char
			can_remove = count < max_paper_in_area
			if can_remove:
				new_grid[row] = new_grid[row][:col] + '.' + new_grid[row][col + 1:]
				removed_count += 1
	return new_grid, removed_count


def solution(input_file):
	with open(input_file,'r') as file:
		entries = file.read()
	entries = entries.strip()

	# Parsing
	entries = entries.splitlines()
	# Solving
	sol = 0
	can_continue = True
	while can_continue:
		entries, removed = remove_from_grid(entries)
		sol += removed
		can_continue = removed > 0
	return sol


if __name__ == "__main__":
	input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
	start = time.time()
	answer = solution(input_file)
	solution_time = time.time() - start
	print(f"- **Answer**: {answer}")
	print(f"- **Timing**: {solution_time}")
