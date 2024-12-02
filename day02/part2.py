file = open("input.txt", "r")
input = file.read()
file.close()


def remove_index(lst, index):
    return lst[:index] + lst[index + 1 :]


def is_level_safe(level, increasing, dampener_used=False):
    last_digit = int(level[0])
    for i, part in enumerate(level[1:], 1):
        digit = int(part)
        diff = digit - last_digit
        abs_diff = abs(diff)
        if (
            (abs_diff < 1 or abs_diff > 3)
            or (diff < 0 and increasing)
            or (diff > 0 and not increasing)
        ):
            if not dampener_used:
                return is_level_safe(
                    remove_index(level, i - 1), increasing, dampener_used=True
                ) or is_level_safe(
                    remove_index(level, i), increasing, dampener_used=True
                )
            break
        last_digit = digit
    else:
        return True
    return False


amount_safe = 0
for line in input.splitlines():
    parts = line.split()
    increasing = True if int(parts[-1]) - int(parts[0]) > 0 else False
    dampener_used = False
    level_safe = is_level_safe(parts, increasing, dampener_used)
    if level_safe:
        amount_safe += 1

print(amount_safe)
