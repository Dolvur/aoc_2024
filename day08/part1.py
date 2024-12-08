from typing import Callable, Dict, List, Set, Tuple


def pos_in_map(pos: Tuple[int, int], width: int, height: int):
    x, y = pos
    return x >= 0 and x < width and y >= 0 and y < height


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.read()
    file.close()

    lines = input.splitlines()
    map = [[c for c in line] for line in lines]
    antennas_dict: Dict[str, List[Tuple[int, int]]] = {}
    width = len(map[0])
    height = len(map)
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c != ".":
                antennas_dict[c] = antennas_dict.get(c, []) + [(x, y)]

    antinodes_set: Set[Tuple[int, int]] = set()
    for _, letter_antennas in antennas_dict.items():
        for pos in letter_antennas:
            x, y = pos
            for second_pos in letter_antennas:
                s_x, s_y = second_pos
                if pos == second_pos:
                    continue
                p_x, p_y = (x - s_x, y - s_y)
                antinode_pos = (x + p_x, y + p_y)
                if pos_in_map(antinode_pos, width, height):
                    antinodes_set.add(antinode_pos)

    print(len(antinodes_set))
