file = open("input.txt", "r")
input = file.read()
file.close()

chunks = input.strip().split("\n\n")
first_chunk = chunks[0]
second_chunk = chunks[1]

after_dict = {}
for line in first_chunk.splitlines():
    a, b = map(int, line.split("|"))
    after_dict[a] = after_dict.get(a, []) + [b]

correct_lines = []
for line in second_chunk.splitlines():
    page_numbers = list(map(int, line.split(",")))
    is_right_order = True
    for i, p_g in enumerate(page_numbers):
        page_numbers_before = page_numbers[:i]
        page_numbers_after = page_numbers[i + 1 :]
        must_be_after = after_dict.get(p_g, [])
        # print(i, "curr:", p_g, page_numbers_before, page_numbers_after)
        # print("must_be_after: ", must_be_after)
        if any(elem in page_numbers_before for elem in must_be_after):
            is_right_order = False
            break

    if is_right_order:
        correct_lines.append(page_numbers)

# print(correct_lines)

sum = 0
for line in correct_lines:
    middle_index = int(len(line) / 2)
    # print(middle_index, line[middle_index])
    sum += line[middle_index]

print(sum)
