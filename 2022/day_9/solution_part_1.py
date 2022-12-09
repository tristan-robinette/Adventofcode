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


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
