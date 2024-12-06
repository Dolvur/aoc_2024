file = open("input.txt", "r")
input = file.read()
file.close()

lines = input.splitlines()

obstacles_dict = {}
guard_pos = (0, 0)
width = len(lines[0])
height = len(lines)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            guard_pos = (x, y)
        elif c == "#":
            obstacles_dict[(x, y)] = True

directions_rotation = ["up", "right", "down", "left"]
relative_pos_step = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction_index = 0
guard_in_bounds = True
in_guard_path_dict = {guard_pos: True}


def pos_in_bounds(pos):
    x, y = pos
    return x >= 0 and x < width and y >= 0 and y < height


while guard_in_bounds:
    direction = directions_rotation[direction_index]
    next_guard_pos = (
        guard_pos[0] + relative_pos_step[direction_index][0],
        guard_pos[1] + relative_pos_step[direction_index][1],
    )
    if not pos_in_bounds(next_guard_pos):
        break
    if obstacles_dict.get(next_guard_pos, False):
        direction_index = (direction_index + 1) % 4
        continue

    in_guard_path_dict[next_guard_pos] = True
    guard_pos = next_guard_pos

num_distinct_pos = len(in_guard_path_dict)
print(num_distinct_pos)
