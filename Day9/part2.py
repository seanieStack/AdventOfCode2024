def swap_parts(data):
    attempted_ids = set()
    while True:

        current_part_index = None
        for i in range(len(data) - 1, -1, -1):
            if isinstance(data[i], list) and tuple(data[i]) not in attempted_ids:
                current_part_index = i
                attempted_ids.add(tuple(data[i]))
                break

        if current_part_index is None:
            return data

        current_part = data[current_part_index]

        period_index = None
        for i in range(len(data)):
            if isinstance(data[i], str) and len(data[i]) >= len(current_part):
                period_index = i
                break

        if period_index is None:
            continue

        if period_index > current_part_index:
            continue

        data[period_index] = "." *  (len(data[period_index]) - len(current_part))
        data[current_part_index] = "." * len(current_part)
        data.insert(period_index, current_part)

        i = 0
        while i < len(data) - 1:
            if isinstance(data[i], str) and isinstance(data[i + 1], str):
                combined_length = len(data[i]) + len(data[i + 1])
                data[i] = "." * combined_length
                data.pop(i + 1)
            else:
                i += 1

        for i in range(len(data) - 1):
            try:
                if data[i] == "":
                    data.pop(i)
            except IndexError:
                pass

with open("input.txt") as f:
    data = f.read().strip()

blocks = [x for x in data]

blocks2 = []
j = 0
for i, block in enumerate(blocks):
    if i % 2 == 0:
        blocks2.append("_[" + ((str(j) + ",") * int(block))[:-1] + "]_")
        j += 1
    else:
        blocks2.append("." * int(block))

final_block = "".join(blocks2)

final_block = final_block.split("_")[1:-1]

parts = []

for seg in final_block:
    if len(seg) == 0:
        parts.append("")
    elif seg[0] == "[" and len(seg) > 3:
        parts.append([int(x) for x in seg[1:-1].split(",")])
    elif seg[0] == "[" and len(seg) == 3:
        parts.append([int(seg[1])])
    elif seg[0] == "[" and seg[1] =="]":
        continue
    else:
        parts.append(seg)

new_parts = swap_parts(parts)
print(new_parts)

out = []

for part in new_parts:
        [out.append(x) for x in part]

grand_total = 0
for i, val in enumerate(out):
    if val == ".":
        continue
    grand_total += val * i

print(grand_total)

