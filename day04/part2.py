file = open("input.txt", "r")
input = file.read()
file.close()

lines = input.splitlines()


def char_in_location(x_index, y_index):
    if y_index < 0 or y_index >= len(lines):
        return False
    if x_index < 0 or x_index >= len(lines[0]):
        return False
    return lines[y_index][x_index]


def is_mas(x, y):
    locations = [(x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)]
    last_char = None
    for i, location in enumerate(locations):
        l_x, l_y = location
        char = char_in_location(l_x, l_y)
        if char == last_char:
            return False
        if char != "M" and char != "S":
            return False
        last_char = char
        if i == 1:  # meh
            last_char = None  # start order does not matter for next pair
    return True


word_count = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "A":
            # print(f"found A at ({x},{y})")
            if is_mas(x, y):
                word_count += 1

print(word_count)
