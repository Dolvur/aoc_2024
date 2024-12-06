from typing import Dict, List, Set, Tuple
import copy


def populate_map(
    map: List[List[str]],
    obstacles_set: Set[Tuple[int, int]],
    guard_path_dict: Dict[Tuple[int, int], List[str]],
):
    obstacles_set.clear()
    guard_path_dict.clear()
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "^":
                guard_path_dict[(x, y)] = [directions_rotation[0]]
            elif c == "#":
                obstacles_set.add((x, y))


def pos_in_bounds(pos: Tuple[int, int]):
    x, y = pos
    return x >= 0 and x < width and y >= 0 and y < height


def walk_ends(
    custom_guard_path_dict: Dict[Tuple[int, int], List[str]],
    custom_obstacles_set: Set[Tuple[int, int]],
):
    d_i = 0
    if len(custom_guard_path_dict) != 1:
        raise Exception("Should contain exactly 1 position for the starting position")
    guard_pos = next(iter(custom_guard_path_dict))
    num_loops = 0
    while True:
        direction = directions_rotation[d_i]
        next_guard_pos = (
            guard_pos[0] + relative_pos_step[d_i][0],
            guard_pos[1] + relative_pos_step[d_i][1],
        )
        if not pos_in_bounds(next_guard_pos):  # Not a loop
            return True
        if next_guard_pos in custom_obstacles_set:
            d_i = (d_i + 1) % 4
            continue
        last_dirs_on_space = custom_guard_path_dict.get(next_guard_pos, [])
        if (
            len(last_dirs_on_space) >= 1
            and direction in last_dirs_on_space  # last_dirs_on_space[-1] == direction
        ):  # If a loop
            return False

        custom_guard_path_dict[next_guard_pos] = custom_guard_path_dict.get(
            next_guard_pos, []
        ) + [direction]
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
    guard_path_dict: Dict[Tuple[int, int], List[str]] = {}

    populate_map(map, obstacles_set, guard_path_dict)
    if len(guard_path_dict) != 1:
        raise Exception("Should only contain start position")
    start_guard_pos = next(iter(guard_path_dict))

    # Walk once to populate all positions
    walk_ends(guard_path_dict, obstacles_set)

    unique_obs_positions: Set[Tuple[int, int]] = set()
    for coord in guard_path_dict:
        if coord == start_guard_pos:
            continue
        custom_guard_path_set: Dict[Tuple[int, int], List[str]] = {
            start_guard_pos: [directions_rotation[0]]
        }
        custom_obstacles_set = copy.deepcopy(obstacles_set)
        custom_obstacles_set.add(coord)
        # print(len(custom_obstacles_set))
        if coord not in unique_obs_positions and not walk_ends(
            custom_guard_path_set, custom_obstacles_set
        ):
            unique_obs_positions.add(coord)

    print(len(unique_obs_positions))
    # print(unique_obs_positions)

    # num_distinct_pos = len(guard_path_dict)
    # print(num_distinct_pos)
