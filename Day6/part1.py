from collections import defaultdict

puzzle_map = defaultdict(lambda: "-1")

guard_pos = None

with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(list(line)):
            if char == "^":
                guard_pos = (i, j)

            puzzle_map[(i, j)] = char

direction = (-1, 0)
total = 0
while True:
    if puzzle_map[(guard_pos[0], guard_pos[1])] != "x":
        total += 1

    projected_next_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])

    if puzzle_map[(projected_next_pos[0], projected_next_pos[1])] == "-1":
        break
    elif puzzle_map[(projected_next_pos[0], projected_next_pos[1])] == '#':
        direction = (direction[1], -direction[0])

    puzzle_map[(guard_pos[0], guard_pos[1])] = "x"
    guard_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])


print(total)