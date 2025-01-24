from collections import defaultdict

topo_map = defaultdict(lambda: "?")
starting_locations = []
trailhead = {}

with open("input.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            topo_map[(i, j)] = char
            if char == "0":
                starting_locations.append((i, j))

def walk_map(starting_location, origin_trailhead):
    current_height = int(topo_map[starting_location])
    if current_height == 9:
        if origin_trailhead not in trailhead:
            trailhead[origin_trailhead] = set()
        trailhead[origin_trailhead].add(starting_location)
        return

    next_height = current_height + 1
    neighbors = [
        (starting_location[0] - 1, starting_location[1]),
        (starting_location[0] + 1, starting_location[1]),
        (starting_location[0], starting_location[1] - 1),
        (starting_location[0], starting_location[1] + 1),
    ]


    for n in neighbors:
        if topo_map[n] == str(next_height):
            walk_map(n, origin_trailhead)

for starting_location in starting_locations:
    walk_map(starting_location, starting_location)

grand_total = 0
for values in trailhead.values():
    grand_total += len(values)

print(grand_total)