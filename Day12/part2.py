from collections import defaultdict

from Day12.helper import print_map

garden_map = defaultdict(lambda: "?")

with open("input.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            garden_map[(i, j)] = char

print_map(garden_map)

def get_sides(crop, locations):
    corner_count = 0
    for location in locations:
        neighbours = [
            (location[0] + 1, location[1]),
            (location[0] - 1, location[1]),
            (location[0], location[1] + 1),
            (location[0], location[1] - 1),
        ]
        exterior = []
        for n in neighbours:
            if garden_map[n] != crop:
                exterior.append(n)

        if len(exterior) == 4:
            corner_count += 4
        elif len(exterior) == 3:
            corner_count += 2
        elif len(exterior) == 2:
            if abs(exterior[0][0] - exterior[1][0]) == 1 and abs(exterior[0][1] - exterior[1][1]) == 1:
                corner_count += 1

        for diagonal in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            horizontal = (location[0] + diagonal[0], location[1])
            vertical = (location[0], location[1] + diagonal[1])
            diagonal = (location[0] + diagonal[0], location[1] + diagonal[1])

            if garden_map[horizontal] == crop and garden_map[vertical] == crop and garden_map[diagonal] != crop:
                corner_count += 1

    return corner_count

accounted_for_cords = set()
grand_total = 0
for cord, crop in list(garden_map.items()):
    if cord in accounted_for_cords:
        continue

    if crop == "?":
        continue

    connected_cords = set()
    connected_cords.add(cord)
    stack = [cord]
    while stack:
        current_cord = stack.pop()
        neighbors = [
            (current_cord[0] - 1, current_cord[1]),
            (current_cord[0] + 1, current_cord[1]),
            (current_cord[0], current_cord[1] - 1),
            (current_cord[0], current_cord[1] + 1),
        ]
        for n in neighbors:
            if garden_map[n] == crop and n not in connected_cords:
                connected_cords.add(n)
                accounted_for_cords.add(n)
                stack.append(n)

    sides = get_sides(crop, connected_cords)
    grand_total += len(connected_cords) * sides

    print(f"Region {crop} with  {len(connected_cords)} x {sides} = {len(connected_cords) * sides}")

    accounted_for_cords.add(cord)



print(grand_total)
