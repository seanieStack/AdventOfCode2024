from collections import defaultdict

topo_map = defaultdict(lambda: "?")
starting_locations = []
ending_locations = {}

with open("input.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            topo_map[(i, j)] = char

            if char == "0":
                starting_locations.append((i, j))

def walk_map(starting_location):
    current_height = int(topo_map[starting_location])
    if current_height == 9:
        if starting_location in ending_locations:
            ending_locations[starting_location] += 1
        else:
            ending_locations[starting_location] = 1

    next_height = current_height + 1
    neighbors = [
        (starting_location[0] - 1, starting_location[1]),
        (starting_location[0] + 1, starting_location[1]),
        (starting_location[0], starting_location[1] - 1),
        (starting_location[0], starting_location[1] + 1),
    ]

    for n in neighbors:
        if topo_map[n] == str(next_height):
            walk_map(n)

for starting_location in starting_locations:
    walk_map(starting_location)

grand_total = sum(ending_locations.values())
print(grand_total)
