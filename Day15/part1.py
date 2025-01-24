from collections import defaultdict

warehouse_map = defaultdict(lambda: "?")
robot_position = None
moves = ""

def parse_input():

    global warehouse_map, robot_position, moves

    with open("input.txt") as f:
        data = f.read()
        grid, moves = data.split("\n\n")

        for y, row in enumerate(grid.split("\n")):
            for x, cell in enumerate(row):
                if cell == "#":
                    warehouse_map[(x, y)] = "#"
                elif cell == ".":
                    warehouse_map[(x, y)] = "."
                elif cell == "O":
                    warehouse_map[(x, y)] = "O"
                elif cell == "@":
                    warehouse_map[(x, y)] = "@"
                    robot_position = (x, y)

        moves = moves.strip().replace("\n", "")


def move(current_position, direction):
    global robot_position

    x, y = current_position
    dx, dy = direction
    new_x, new_y = x + dx, y + dy
    new_position = (new_x, new_y)

    if warehouse_map[new_position] == "#":
        return False

    if warehouse_map[new_position] == ".":
        warehouse_map[current_position] = "."
        warehouse_map[new_position] = "@"
        robot_position = new_position
        return True

    if warehouse_map[new_position] == "O":
        chain_positions = []
        check_x, check_y = new_x, new_y

        while warehouse_map[(check_x, check_y)] == "O":
            chain_positions.append((check_x, check_y))
            check_x += dx
            check_y += dy

        next_cell = (check_x, check_y)

        if warehouse_map[next_cell] == ".":
            for bx, by in reversed(chain_positions):
                warehouse_map[(bx + dx, by + dy)] = "O"

            first_box = chain_positions[0]
            warehouse_map[first_box] = "@"
            warehouse_map[current_position] = "."

            robot_position = first_box

            return True
        else:
            return False

    return False


def simulate_move(robot_move):

    direction_map = {
        "v": (0, 1),
        "^": (0, -1),
        ">": (1, 0),
        "<": (-1, 0)
    }

    move(robot_position, direction_map[robot_move])


def clean_print(warehouse_map):
    min_x = min(pos[0] for pos in warehouse_map.keys())
    max_x = max(pos[0] for pos in warehouse_map.keys())
    min_y = min(pos[1] for pos in warehouse_map.keys())
    max_y = max(pos[1] for pos in warehouse_map.keys())

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += warehouse_map[(x, y)]
        print(row)


def main():
    parse_input()

    # clean_print(warehouse_map)

    for robot_move in moves:
        print()
        simulate_move(robot_move)
        print(robot_move)
        # clean_print(warehouse_map)
        print()

    grand_total = 0
    for pos, cell in warehouse_map.items():
        if cell == "O":
            grand_total += 100 * pos[1] + pos[0]

    # clean_print(warehouse_map)

    print(grand_total)

if __name__ == "__main__":
    main()