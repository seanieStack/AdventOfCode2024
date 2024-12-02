from collections import defaultdict
from itertools import combinations

puzzle_map = defaultdict(lambda: "?")
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(list(line.strip())):
            puzzle_map[(i, j)] = char

grouped_coords = dict()
for pos, value in puzzle_map.items():
    if value != ".":
        if value not in grouped_coords:
            grouped_coords[value] = []
        grouped_coords[value].append(pos)

possible_locations = set()
for antenna, cords in grouped_coords.items():
    antenna_pairs = list(combinations(cords, 2))

    for antenna_pair in antenna_pairs:
        ((x1, y1), (x2, y2)) = antenna_pair

        dx = x1 - x2
        dy = y1 - y2

        anti_node1 = ((x2 - dx), (y2 - dy))
        if puzzle_map[anti_node1] != "?":
            possible_locations.add(anti_node1)

        dx = x2 - x1
        dy = y2 - y1

        anti_node2 = ((x1 - dx), (y1 - dy))
        if puzzle_map[anti_node2] != "?":
            possible_locations.add(anti_node2)

print(len(possible_locations))