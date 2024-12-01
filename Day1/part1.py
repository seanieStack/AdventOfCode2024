with open("input.txt", "r") as f:
    lines = f.readlines()

left, right = [], []

for line in lines:
    left.append(int(line.split("   ")[0].strip()))
    right.append(int(line.split("   ")[1].strip()))

left.sort()
right.sort()

print(sum([abs(left - right) for left, right in zip(left, right)]))
