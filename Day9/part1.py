import re

def is_sorted(s):
    period_index = s.find('.')

    if period_index == -1:
        return s.isdigit()

    periods_part = s[period_index:]

    if not all(ch == '.' for ch in periods_part):
        return False

    return True

def swap_substrings(original, start1, end1, start2, end2):
    if start1 > start2:
        # Ensure that start1 is before start2
        start1, end1, start2, end2 = start2, end2, start1, end1
    part1 = original[:start1]
    sub1 = original[start1:end1]
    part2 = original[end1:start2]
    sub2 = original[start2:end2]
    part3 = original[end2:]
    return part1 + sub2 + part2 + sub1 + part3

with open("input.txt") as f:
    data = f.read().strip()

blocks = [x for x in data]

blocks2 = []
j = 0
for i, block in enumerate(blocks):
    if i % 2 == 0:
        blocks2.append(("_" + str(j) + "_") * int(block))
        j += 1
    else:
        blocks2.append("." * int(block))

final_block = "".join(blocks2)

pattern = re.compile(r'(_\d+_)')

while not is_sorted(final_block):
    # print(final_block)

    # Use finditer to get an iterator of match objects
    matches = list(pattern.finditer(final_block))

    if matches:
        last_match = matches[-1]

        value_number = last_match.group(1)
        start_index = last_match.start(1)
        end_index = last_match.end(1)
        length = end_index - start_index

        period_index = final_block.find('.')

        final_block = swap_substrings(final_block, start_index, end_index, period_index, period_index + 1)


x = final_block.replace("__", "_").split('.')[0].split("_")[1:-1]

x = [int(i) for i in x]

grand_total = 0
for i, id in enumerate(x):
     grand_total += id * i

print(grand_total)




