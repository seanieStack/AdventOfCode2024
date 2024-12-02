import re

with open("input.txt", "r") as f:
    data = f.read()

pattern = r"mul\(\d+,\d+\)"
mults = re.findall(pattern, data)

total_sum = 0
for s in mults:
    nums = s[4:-1].split(",")
    total_sum += int(nums[0]) * int(nums[1])

print(total_sum)
