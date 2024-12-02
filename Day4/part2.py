from Day4.helper import process_input_file

padding_rec = 1
puzzle = process_input_file("input.txt", padding_rec)

total_sum = 0
for i in range(padding_rec, len(puzzle) - padding_rec):
    for j in range(padding_rec, len(puzzle[i]) - padding_rec):
        if puzzle[i][j] == "A":

            '''
            M . S
            . A .
            M . S
            '''
            if (puzzle[i - 1][j - 1] == 'M' and
                    puzzle[i - 1][j + 1] == 'S' and
                    puzzle[i + 1][j - 1] == 'M' and
                    puzzle[i + 1][j + 1] == 'S'):
                total_sum += 1

            '''
            M . M
            . A .
            S . S
            '''
            if (puzzle[i - 1][j - 1] == 'M' and
                    puzzle[i - 1][j + 1] == 'M' and
                    puzzle[i + 1][j - 1] == 'S' and
                    puzzle[i + 1][j + 1] == 'S'):
                total_sum += 1

            '''
            S . M
            . A .
            S . M
            '''
            if (puzzle[i - 1][j - 1] == 'S' and
                    puzzle[i - 1][j + 1] == 'M' and
                    puzzle[i + 1][j - 1] == 'S' and
                    puzzle[i + 1][j + 1] == 'M'):
                total_sum += 1

            '''
            S . S
            . A .
            M . M
            '''
            if (puzzle[i - 1][j - 1] == 'S' and
                    puzzle[i - 1][j + 1] == 'S' and
                    puzzle[i + 1][j - 1] == 'M' and
                    puzzle[i + 1][j + 1] == 'M'):
                total_sum += 1

print(total_sum)



