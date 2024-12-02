DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def read_map(filename):
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    n_rows = len(lines)
    n_cols = len(lines[0])

    # Initialize the map with '-' for empty spaces
    puzzle_map = [['-' for _ in range(n_cols)] for _ in range(n_rows)]
    guard_pos = None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            puzzle_map[i][j] = char
            if char == '^':
                guard_pos = (i, j)
    return puzzle_map, guard_pos, n_rows, n_cols


def walk(test_map, start_pos, n_rows, n_cols):
    directions = DIRECTIONS
    direction = 0  # starts facing Up
    pos_x, pos_y = start_pos
    visited = set()

    while True:
        state = ((pos_x, pos_y), direction)

        if state in visited:
            return False

        visited.add(state)

        change_x, change_y = directions[direction]
        forward_x = pos_x + change_x
        forward_y = pos_y + change_y

        if forward_x < 0 or forward_x >= n_rows or forward_y < 0 or forward_y >= n_cols:
            return True

        # Check if there's an obstacle ahead
        if test_map[forward_x][forward_y] == '#':
            # Turn right until a free path is found or all directions are blocked
            turned = False
            for _ in range(4):
                direction = (direction + 1) % 4
                change_x, change_y = directions[direction]
                forward_x = pos_x + change_x
                forward_y = pos_y + change_y
                if 0 <= forward_x < n_rows and 0 <= forward_y < n_cols and test_map[forward_x][forward_y] != '#':
                    turned = True
                    break
            if not turned:
                # All directions are blocked; guard is stuck
                return False
        # Move forward
        change_x, change_y = directions[direction]
        pos_x += change_x
        pos_y += change_y


def count_obstruction_positions(puzzle_map, guard_pos, n_rows, n_cols):
    total = 0
    possible_positions = []
    for i in range(n_rows):
        for j in range(n_cols):
            if puzzle_map[i][j] not in ['#', '^']:
                possible_positions.append((i, j))

    total_positions = len(possible_positions)
    print(f"Total possible obstruction positions: {total_positions}")

    for i, j in possible_positions:
        # Place obstruction
        puzzle_map[i][j] = '#'
        # Simulate guard's movement
        if not walk(puzzle_map, guard_pos, n_rows, n_cols):
            total += 1
        # Remove obstruction
        puzzle_map[i][j] = '.'
    return total


puzzle_map, guard_pos, n_rows, n_cols = read_map("input.txt")

total_loops = count_obstruction_positions(puzzle_map, guard_pos, n_rows, n_cols)
print(total_loops)