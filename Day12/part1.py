from collections import defaultdict

garden_map = defaultdict(lambda: "?")

with open("input.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            garden_map[(i, j)] = char

def get_perimeter(crop, locations):
    perimeter = 0

    for location in locations:
        neighbors = [
            (location[0] - 1, location[1]),
            (location[0] + 1, location[1]),
            (location[0], location[1] - 1),
            (location[0], location[1] + 1),
        ]
        for n in neighbors:
            if garden_map[n] != crop:
                perimeter += 1

    return perimeter

accounted_for_cords = set()
grand_total = 0
for cord, crop in list(garden_map.items()):
    if cord in accounted_for_cords:
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

    perimeter = get_perimeter(crop, connected_cords)
    grand_total += len(connected_cords) * perimeter

    accounted_for_cords.add(cord)

print(grand_total)
