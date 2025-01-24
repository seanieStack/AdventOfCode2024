import re
from sympy import symbols, Eq, solve, Integer

def solve_linear_equation(x1, y1, x2, y2, res_x, res_y):
    n, m = symbols('n m', integer=True, nonnegative=True)

    eq1 = Eq(x1 * n + x2 * m, res_x)
    eq2 = Eq(y1 * n + y2 * m, res_y)

    solutions = solve((eq1, eq2), (n, m), dict=True)

    valid_solutions = []
    for s in solutions:
        is_valid = True
        for val in s.values():
            if not (Integer(val).is_integer and val >= 0):
                is_valid = False
                break
        if is_valid:
            valid_solutions.append(s)

    results = []
    for s in valid_solutions:
        result = {
            'n': s[n],
            'm': s[m],
            'cost': (3 * s[n]) + (s[m] * 1)
        }
        results.append(result)

    min_cost_solution = None
    if len(results) > 0:
        min_cost_solution = min(results, key=lambda x: x['cost'])

    return min_cost_solution


def parse_input():
    parts = []
    with open('input.txt', 'r') as f:
        lines = f.read()
        lines = lines.split("\n\n")
        for line in lines:
            pattern = r'X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)'

            matches = re.findall(pattern, line)

            x1, y1 = map(int, matches[0][:2])
            x2, y2 = map(int, matches[1][:2])
            res_x, res_y = map(int, matches[2][2:])
            parts.append((x1, y1, x2, y2, res_x, res_y))

    return parts