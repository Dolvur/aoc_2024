import re

file = open("input.txt", "r")
input = file.read()
file.close()

input_string = "Here are examples: do() don't() mul(12,34), mul(567,89), don't(), do(), and mul(1234,56)."
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))"

matches = re.findall(pattern, input)

sum = 0
do = True
for match in matches:
    if match[2] == "do()":
        do = True
    elif match[2] == "don't()":
        do = False
    elif do:
        sum += int(match[0]) * int(match[1])

print(sum)
