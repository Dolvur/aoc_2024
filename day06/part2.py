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
in_guard_path_dict = {guard_pos: [directions_rotation[direction_index]]}


def pos_in_bounds(pos):
    x, y = pos
    return x >= 0 and x < width and y >= 0 and y < height


possible_obs_pos_dict = {}
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

    if guard_pos == (4, 6):
        print("wow", direction)
        print("a", in_guard_path_dict[guard_pos])

    # If pretend obstacle makes guard go in path before with same direction
    if directions_rotation[(direction_index + 1) % 4] in in_guard_path_dict.get(
        next_guard_pos, []
    ):
        print("here")
        obs_pos = (
            next_guard_pos[0] + relative_pos_step[direction_index][0],
            next_guard_pos[1] + relative_pos_step[direction_index][1],
        )
        possible_obs_pos_dict[obs_pos] = True

    in_guard_path_dict[next_guard_pos] = in_guard_path_dict.get(next_guard_pos, []) + [
        direction
    ]
    guard_pos = next_guard_pos

num_distinct_pos = len(in_guard_path_dict)
print(num_distinct_pos)

# num_obs_pos = len(possible_obs_pos_dict)
print(possible_obs_pos_dict)
