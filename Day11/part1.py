with open("input.txt") as f:
    rocks = [int(x) for x in f.read().strip().split(" ")]

def apply_rule(rock):
    if rock == 0:
        return 1
    elif len(str(rock)) % 2 == 0:
        new_rock = str(rock)
        firstpart, secondpart = new_rock[:len(new_rock) // 2], new_rock[len(new_rock) // 2:]
        return int(firstpart), int(secondpart)
    else:
        return rock * 2024

def update_rocks(rock_list):
    rocks_after_update = []

    for rock in rock_list:
        updated_rock = apply_rule(rock)
        if isinstance(updated_rock, tuple):
            rocks_after_update.extend(updated_rock)
        else:
            rocks_after_update.append(updated_rock)

    return rocks_after_update

for i in range(75):
    print(i, len(rocks))
    rocks = update_rocks(rocks)

print(len(rocks))