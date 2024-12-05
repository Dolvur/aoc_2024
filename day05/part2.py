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

was_invalid_lines = []
for line in second_chunk.splitlines():
    page_numbers = list(map(int, line.split(",")))
    pns_invalid = page_numbers[:]
    is_right_order = True
    for i_pn, pn in enumerate(page_numbers):
        page_numbers_before = pns_invalid[:i_pn]
        must_be_after = after_dict.get(pn, [])
        for e_i, elem in enumerate(page_numbers_before):
            if elem in must_be_after:
                is_right_order = False
                pns_invalid.pop(i_pn)
                pns_invalid.insert(e_i, pn)
                break

    if not is_right_order:
        was_invalid_lines.append(pns_invalid)

sum = 0
for line in was_invalid_lines:
    middle_index = int(len(line) / 2)
    sum += line[middle_index]

print(sum)
