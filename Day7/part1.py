from itertools import product

def build_expression(numbers, operators):
    expr = str(numbers[0])

    for i, op in enumerate(operators):
        next_num = str(numbers[i + 1])
        expr = f"({expr}{op}{next_num})"

    return expr

with open("input.txt") as f:
    data = f.readlines()

equations = []
for line in data:
    parts = line.strip().split(": ")
    numbers  = [int(x) for x in parts[1].split(" ")]
    total = int(parts[0])
    equations.append((total, numbers))

operands = ["*", "+"]

total = 0
for i, equation in enumerate(equations):
    possible_ops_list =  list(product(operands, repeat=len(equation[1])-1))

    for op_list in possible_ops_list:
        expression = build_expression(equation[1], op_list)
        running_total = eval(expression)

        if running_total == equation[0]:
            total += running_total
            break

print(total)