from collections import Counter

with open("input.txt", "r") as f:
    lines = f.readlines()

left, right = [], []

for line in lines:
    left.append(int(line.split("   ")[0].strip()))
    right.append(int(line.split("   ")[1].strip()))

counter = Counter(right)

print(sum([i * counter[i] for i in left]))
