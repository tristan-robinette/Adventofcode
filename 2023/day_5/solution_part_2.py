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


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
