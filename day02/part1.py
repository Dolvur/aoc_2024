file = open("input.txt", "r")
input = file.read()
file.close()

amount_safe = 0
for line in input.splitlines():
    parts = line.split()
    increasing = True if int(parts[-1]) - int(parts[0]) > 0 else False
    last_digit = int(parts[0])
    dampener_used = False
    for part in parts[1:]:
        digit = int(part)
        diff = digit - last_digit
        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            break
        elif diff < 0 and increasing:
            break
        elif diff > 0 and not increasing:
            break
        last_digit = digit
    else:
        amount_safe += 1

print(amount_safe)
