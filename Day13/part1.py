from Day13.helper import parse_input, solve_linear_equation

inputs = parse_input()

grand_total = 0
for input in inputs:
    opt_equation = solve_linear_equation(input[0], input[1], input[2], input[3], input[4], input[5])
    if opt_equation:
        grand_total += opt_equation['cost']

print(grand_total)
