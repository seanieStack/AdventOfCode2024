ROBOT_BOUND_X = 101
ROBOT_BOUND_Y = 103

def clean_print(robot_list):
    floor_plan = [["." for _ in range(ROBOT_BOUND_X)] for _ in range(ROBOT_BOUND_Y)]

    for robot in robot_list:
        x, y, _, _ = robot
        if floor_plan[y][x] == ".":
            floor_plan[y][x] = 1
        else:
            floor_plan[y][x] += 1

    for row in floor_plan:
        print("".join(str(x) for x in row))

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

def count_robot_in_quadrant(robot_list):
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0
    for robot in robot_list:
        x, y, _, _ = robot

        if x < ROBOT_BOUND_X // 2 and y < ROBOT_BOUND_Y // 2:
            top_left += 1
        elif x < ROBOT_BOUND_X // 2 and y > ROBOT_BOUND_Y // 2:
            bottom_left += 1
        elif x > ROBOT_BOUND_X // 2 and y < ROBOT_BOUND_Y // 2:
            top_right += 1
        elif x > ROBOT_BOUND_X // 2 and y > ROBOT_BOUND_Y // 2:
            bottom_right += 1

    return top_left, top_right, bottom_left, bottom_right

robot_list = parse_input()
clean_print(robot_list)
for i in range(100):
    robot_list = simulate(robot_list)

print()
print()

clean_print(robot_list)

top_left, top_right, bottom_left, bottom_right = count_robot_in_quadrant(robot_list)

print(top_left, top_right, bottom_left, bottom_right)
print(top_left * top_right * bottom_left * bottom_right)