file = open("input.txt", "r")
input = file.read()
file.close()

right_dict = {}
for line in input.splitlines():
    parts = line.split()
    right_num = int(parts[1])
    right_dict[right_num] = right_dict.get(right_num, 0) + 1

sum = 0
for line in input.splitlines():
    parts = line.split()
    left_num = int(parts[0])
    sum += left_num * right_dict.get(left_num, 0)


print(sum)
