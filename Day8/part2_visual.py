import os
import time
from collections import defaultdict
from itertools import combinations
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the current state of the map
def print_map(puzzle_map, possible_locations, latest_pos, max_row, max_col):
    clear_console()
    for i in range(max_row + 1):
        row = ""
        for j in range(max_col + 1):
            pos = (i, j)
            char = puzzle_map[pos]
            if pos in possible_locations:
                if pos == latest_pos:
                    row += Fore.GREEN + char + Style.RESET_ALL
                else:
                    row += Fore.RED + char + Style.RESET_ALL
            else:
                row += char
        print(row)
    print("\n")  # Add an extra newline for better readability

# Load the puzzle map from the input file
puzzle_map = defaultdict(lambda: "?")
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(list(line.strip())):
            puzzle_map[(i, j)] = char

max_row = max(key[0] for key in puzzle_map.keys())
max_col = max(key[1] for key in puzzle_map.keys())

# Group coordinates by their values (excluding '.')
grouped_coords = dict()
for pos, value in puzzle_map.items():
    if value != ".":
        if value not in grouped_coords:
            grouped_coords[value] = []
        grouped_coords[value].append(pos)

# Initialize possible_locations as a list to maintain order
possible_locations = []
added_positions = set()  # To ensure uniqueness

# Iterate through each group of antennas
for antenna, cords in grouped_coords.items():
    antenna_pairs = list(combinations(cords, 2))

    for antenna_pair in antenna_pairs:
        ((x1, y1), (x2, y2)) = antenna_pair

        dx = x2 - x1
        dy = y2 - y1

        # Traverse in the positive direction
        pos = (x2, y2)
        while puzzle_map[pos] != "?":
            if puzzle_map[pos] == ".":
                puzzle_map[pos] = "#"

            if puzzle_map[pos] != "?":
                if pos not in added_positions:
                    possible_locations.append(pos)
                    added_positions.add(pos)
                    print_map(puzzle_map, possible_locations, pos, max_row, max_col)
                    time.sleep(0.04)  # Optional: Add delay for visualization

            pos = (pos[0] + dx, pos[1] + dy)

        # Traverse in the negative direction
        pos = (x1, y1)
        while puzzle_map[pos] != "?":
            if puzzle_map[pos] == ".":
                puzzle_map[pos] = "#"

            if puzzle_map[pos] != "?":
                if pos not in added_positions:
                    possible_locations.append(pos)
                    added_positions.add(pos)
                    print_map(puzzle_map, possible_locations, pos, max_row, max_col)
                    time.sleep(0.04)  # Optional: Add delay for visualization

            pos = (pos[0] - dx, pos[1] - dy)

# Final output
print(Fore.GREEN + f"Total number of possible locations: {len(possible_locations)}" + Style.RESET_ALL)
