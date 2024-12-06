from typing import Dict, Set, Tuple


def populate_map(map, obstacles_set, guard_path_dict):
    obstacles_set.clear()
    guard_path_dict.clear()
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "^":
                guard_path_dict[(x, y)] = directions_rotation[0]
            elif c == "#":
                obstacles_set.add((x, y))


def pos_in_bounds(pos):
    x, y = pos
    return x >= 0 and x < width and y >= 0 and y < height


def walk(guard_path_dict: Dict[Tuple[int, int], str]):
    d_i = 0
    if len(guard_path_dict) != 1:
        raise Exception("Should contain exactly 1 position for the starting position")
    guard_pos = next(iter(guard_path_dict))
    while True:
        direction = directions_rotation[d_i]
        next_guard_pos = (
            guard_pos[0] + relative_pos_step[d_i][0],
            guard_pos[1] + relative_pos_step[d_i][1],
        )
        if not pos_in_bounds(next_guard_pos):
            break
        if next_guard_pos in obstacles_set:
            d_i = (d_i + 1) % 4
            continue

        guard_path_dict[next_guard_pos] = direction
        guard_pos = next_guard_pos


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.read()
    file.close()

    lines = input.splitlines()
    map = [list(line) for line in lines]

    directions_rotation = ["up", "right", "down", "left"]
    relative_pos_step = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    width = len(map[0])
    height = len(map)

    obstacles_set: Set[Tuple[int, int]] = set()
    guard_path_dict: Dict[Tuple[int, int], str] = {}

    populate_map(map, obstacles_set, guard_path_dict)
    walk(guard_path_dict)

    num_distinct_pos = len(guard_path_dict)
    print(num_distinct_pos)
