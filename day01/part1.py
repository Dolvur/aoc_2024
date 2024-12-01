file = open("input.txt", "r")
input = file.read()
file.close()

row_one = []
row_two = []
for line in input.splitlines():
    parts = line.split()
    row_one.append(int(parts[0]))
    row_two.append(int(parts[1]))

row_one.sort()
row_two.sort()

if (len(row_one) != len(row_two)):
    raise Exception("Not same length")

sum = 0
for i in range(0,len(row_one)):
    sum += abs(row_one[i] - row_two[i])

print(sum)
