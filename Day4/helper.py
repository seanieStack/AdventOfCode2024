def clean_print(row):
    for line in row:
        print("".join(line))

def create_padding_line(length, padding):
    return list("." * (length + padding * 2))

def add_padding_rows(rows, line_length, padding):
    padding_line = create_padding_line(line_length, padding)
    for _ in range(padding):
        rows.append(padding_line)

def process_input_file(file_path, padding=4):
    with open(file_path, "r") as f:
        data = f.readlines()

    rows = []

    add_padding_rows(rows, len(data[0].strip()), padding)

    for line in data:
        rows.append(list("." * padding + line.strip() + "." * padding))

    add_padding_rows(rows, len(data[0].strip()), padding)

    return rows