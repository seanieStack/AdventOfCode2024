import re

with open("input.txt", "r") as f:
    data = f.read()

pattern = r"mul\(\d+,\d+\)|do\(+\)|don\'t\(+\)"
instructions = re.findall(pattern, data)

total_sum = 0
flag = True
for s in instructions:
    if s == "don't()":
        flag = False
    elif s == "do()":
        flag = True
    elif flag:
        nums = s[4:-1].split(",")
        total_sum += int(nums[0]) * int(nums[1])

print(total_sum)