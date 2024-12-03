import re

file = open("input.txt", "r")
input = file.read()
file.close()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, input)
numbers = [(int(x), int(y)) for x, y in matches]

sum = 0
for number_tuple in numbers:
    sum += number_tuple[0] * number_tuple[1]

print(sum)
