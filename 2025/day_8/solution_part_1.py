"""
Solution to Advent of Code 2025 day 8 part 1
Solved by doing some magic
"""
import time
import sys
import numpy as np
import networkx as nx
from math import prod

def solution(input_file):
    with open(input_file,'r') as file:
        entries = file.read()
    entries = entries.strip().splitlines()

    points = np.array([tuple(map(int, box.split(","))) for box in entries])
    diff = points[:, None, :] - points[None, :, :]
    # used internet for this... im not smart. gets the Euclidian distance for each point.
    dist_matrix = np.linalg.norm(diff, axis=2)
    np.fill_diagonal(dist_matrix, np.inf)

    # build graph of edges for each node.
    G = nx.Graph()

    for _ in range(1000):
        i, j = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
        G.add_edge(i, j)
        # mask to not pick that combination in future.
        dist_matrix[i, j] = np.inf
        dist_matrix[j, i] = np.inf

    return prod(sorted([len(c) for c in nx.connected_components(G)], reverse=True)[: 3])


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solution(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
