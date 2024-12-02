def check_safe(report_input):
    changes = []
    for i in range(1, len(report_input)):
        changes.append(report_input[i] - report_input[i - 1])

    prev_change = None
    for change in changes:
        if change == 0:
            return False

        if abs(change) > 3:
            return False
        elif prev_change is not None and change * prev_change < 0:
            return False

        prev_change = change

    return True

with open("input.txt", "r") as f:
    lines = f.readlines()

reports = []

for line in lines:
    reports.append([int(i) for i in line.strip().split(" ")])

print(sum(1 if check_safe(i) else 0 for i in reports))