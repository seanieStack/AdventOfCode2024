from functools import lru_cache

with open("input.txt") as f:
    rocks = [int(x) for x in f.read().strip().split(" ")]

def blink(number):
    if number == 0:
        return [1]
    elif (str_len := len( string_rock := str(number))) % 2 == 0:
        return [int(rock) for rock in [string_rock[:str_len//2], string_rock[str_len//2:]]]
    else:
        return [number * 2024]

@lru_cache(maxsize=None)
def count_even_two_digits(number, iter_count):
    if iter_count == 0:
        return 1
    return sum(count_even_two_digits(n, iter_count - 1) for n in blink(number))

total = 0
for rock in rocks:
    total += count_even_two_digits(rock, 75)

print(total)