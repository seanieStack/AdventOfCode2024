colors_dict = {
    'A': '\033[31m',  # Red
    'B': '\033[32m',  # Green
    'C': '\033[33m',  # Yellow
    'D': '\033[34m',  # Blue
    'E': '\033[35m',  # Magenta
    'F': '\033[36m',  # Cyan
    'G': '\033[91m',  # Bright Red
    'H': '\033[92m',  # Bright Green
    'I': '\033[93m',  # Bright Yellow
    'J': '\033[94m',  # Bright Blue
    'K': '\033[95m',  # Bright Magenta
    'L': '\033[96m',  # Bright Cyan
    'M': '\033[37m',  # White
    'N': '\033[90m',  # Gray
    'O': '\033[41m',  # Background Red
    'P': '\033[42m',  # Background Green
    'Q': '\033[43m',  # Background Yellow
    'R': '\033[44m',  # Background Blue
    'S': '\033[45m',  # Background Magenta
    'T': '\033[46m',  # Background Cyan
    'U': '\033[30m',  # Black
    'V': '\033[97m',  # Bright White
    'W': '\033[100m', # Bright Background Black
    'X': '\033[101m', # Bright Background Red
    'Y': '\033[102m', # Bright Background Green
    'Z': '\033[103m', # Bright Background Yellow
    'RESET': '\033[0m' # Reset to default
}

def print_map(puzzle_map):
    max_row = max(key[0] for key in puzzle_map.keys())
    max_col = max(key[1] for key in puzzle_map.keys())

    for i in range(max_row + 1):
        row = ""
        for j in range(max_col + 1):
            pos = (i, j)
            char = puzzle_map[pos]
            row += colors_dict[char] + char + colors_dict['RESET']
        print(row)
    print("\n")