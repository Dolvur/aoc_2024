file = open("input.txt", "r")
input = file.read()
file.close()

lines = input.splitlines()

searched_word = "XMAS"


def char_in_location(char, x_index, y_index):
    if y_index < 0 or y_index >= len(lines):
        return False
    if x_index < 0 or x_index >= len(lines[0]):
        return False
    if lines[y_index][x_index] == char:
        return True
    return False


def words_in_curr_location(
    x_index, y_index, last_letter_index=0, curr_direction="right"
):
    next_letter_index = last_letter_index + 1
    next_char = searched_word[next_letter_index]

    next_x = x_index
    next_y = y_index

    # print(f"before: {x_index},{y_index}")

    match curr_direction:
        case "right":
            next_x += 1
        case "down":
            next_y += 1
        case "left":
            next_x -= 1
        case "up":
            next_y -= 1
        case "down_right":
            next_x += 1
            next_y += 1
        case "up_right":
            next_x += 1
            next_y -= 1
        case "down_left":
            next_x -= 1
            next_y += 1
        case "up_left":
            next_x -= 1
            next_y -= 1

    # print(f"letter:{searched_word[next_letter_index]}, ({next_x},{next_y}), dir:{curr_direction}")

    if char_in_location(next_char, next_x, next_y):
        if next_char == searched_word[-1]:
            # print(f"found word at {next_x},{next_y} with direction:{curr_direction}")
            return 1
        else:
            return words_in_curr_location(next_x, next_y, next_letter_index, curr_direction)
    else:
        return 0



possible_directions = ['right', 'down', 'left', 'up', 'down_right', "up_right", "down_left", "up_left"]
word_count = 0
dir_word_count = {}
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        # print("char here is ", c)
        if c == searched_word[0]:
            # print(f"found x in coord {x},{y}")
            for direction in possible_directions:
                # dir_word_count[direction] = dir_word_count.get(direction,0) + words_in_curr_location(x,y,0,direction) 
                word_count += words_in_curr_location(x,y,0,direction)

print(word_count)
# print(dir_word_count)

