from Day13.helper import parse_input, solve_linear_equation

inputs = parse_input()

grand_total = 0
for input in inputs:
    result = solve_linear_equation(input[0], input[1], input[2], input[3], input[4] + 10000000000000, input[5] + 10000000000000)
    if result:
        grand_total += result['cost']

print(grand_total)

