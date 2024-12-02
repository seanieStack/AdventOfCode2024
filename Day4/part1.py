from Day4.helper import process_input_file, clean_print

padding_rec = len("xmas")
puzzle = process_input_file("input.txt", padding_rec)

clean_print(puzzle)

index_pos = []

for i in range(padding_rec, len(puzzle) - padding_rec):
    for j in range(padding_rec, len(puzzle[i]) - padding_rec):
        if puzzle[i][j] == "X":
            # UP
            up = [(i, j)]
            for x in range(1, 4):
                if puzzle[i - x][j] == "XMAS"[x]:
                    up.append((i - x, j))
                else:
                    break
            if len(up) == 4:
                index_pos.append(up)

            # DOWN
            down = [(i, j)]
            for x in range(1, 4):
                if puzzle[i + x][j] == "XMAS"[x]:
                    down.append((i + x, j))
                else:
                    break
            if len(down) == 4:
                index_pos.append(down)

            # LEFT
            left = [(i, j)]
            for y in range(1, 4):
                if puzzle[i][j - y] == "XMAS"[y]:
                    left.append((i, j - y))
                else:
                    break
            if len(left) == 4:
                index_pos.append(left)

            # RIGHT
            right = [(i, j)]
            for y in range(1, 4):
                if puzzle[i][j + y] == "XMAS"[y]:
                    right.append((i, j + y))
                else:
                    break
            if len(right) == 4:
                index_pos.append(right)

            # LEFT UP
            left_up = [(i, j)]
            for k in range(1, 4):
                if puzzle[i - k][j - k] == "XMAS"[k]:
                    left_up.append((i - k, j - k))
                else:
                    break
            if len(left_up) == 4:
                index_pos.append(left_up)

            # RIGHT UP
            right_up = [(i, j)]
            for k in range(1, 4):
                if puzzle[i - k][j + k] == "XMAS"[k]:
                    right_up.append((i - k, j + k))
                else:
                    break
            if len(right_up) == 4:
                index_pos.append(right_up)

            # LEFT DOWN
            left_down = [(i, j)]
            for k in range(1, 4):
                if puzzle[i + k][j - k] == "XMAS"[k]:
                    left_down.append((i + k, j - k))
                else:
                    break
            if len(left_down) == 4:
                index_pos.append(left_down)

            #RIGHT DOWN
            right_down = [(i, j)]
            for k in range(1, 4):
                if puzzle[i + k][j + k] == "XMAS"[k]:
                    right_down.append((i + k, j + k))
                else:
                    break
            if len(right_down) == 4:
                index_pos.append(right_down)

print(len(index_pos))



