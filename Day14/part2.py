from PIL import Image
import numpy as np

ROBOT_BOUND_X = 101
ROBOT_BOUND_Y = 103

def clean_print(robot_list, seconds):
    floor_plan = [[0 for _ in range(ROBOT_BOUND_X)] for _ in range(ROBOT_BOUND_Y)]

    for robot in robot_list:
        x, y, _, _ = robot
        if floor_plan[y][x] == ".":
            floor_plan[y][x] = 1
        else:
            floor_plan[y][x] += 1

    grid = np.array(floor_plan)
    normalized_grid = (grid - grid.min()) / (grid.max() - grid.min()) * 255
    normalized_grid = normalized_grid.astype(np.uint8)

    img = Image.fromarray(normalized_grid)
    img.save(f"images/{seconds}.png")


def parse_input():
    robot_list = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            position, vel = line.split(" ")
            x, y = position[2:].split(",")
            x, y = int(x), int(y)
            dx, dy = vel[2:].split(",")
            dx, dy = int(dx), int(dy)

            robot_list.append((x, y, dx, dy))

    return robot_list

def simulate(robot_list):
    new_robot_list = []
    for x, y, dx, dy in robot_list:
        x += dx
        y += dy

        x %= ROBOT_BOUND_X
        y %= ROBOT_BOUND_Y

        new_robot_list.append((x, y, dx, dy))

    return new_robot_list

robot_list = parse_input()

i = 1
while i < 15_000:
    robot_list = simulate(robot_list)
    clean_print(robot_list, i)
    i += 1