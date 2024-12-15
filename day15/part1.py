def find_robot(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "@":
                return y, x
    return None


def is_safe_move(m, y, x):
    return 0 <= y < len(m) and 0 <= x < len(m[0]) and m[y][x] != "#" and m[y][x] != "O"


def move_boxes(m, y, x, direction):
    next_pos = (y + direction[0], x + direction[1])
    if not is_safe_move(m, next_pos[0], next_pos[1]) and m[next_pos[0]][next_pos[1]] != "O":
        return False
    if m[next_pos[0]][next_pos[1]] == "O":
        move_boxes(m, next_pos[0], next_pos[1], direction)
    if m[next_pos[0]][next_pos[1]] == ".":
        m[next_pos[0]] = m[next_pos[0]][:next_pos[1]] + "O" + m[next_pos[0]][next_pos[1] + 1:]
        m[y] = m[y][:x] + "." + m[y][x + 1:]
        return True
    return False


def count_to_top(m, y, x):
    count = 0
    while 0 < y:
        count += 1
        y -= 1
    return count


def count_to_left(m, y, x):
    count = 0
    while 0 < x:
        count += 1
        x -= 1
    return count


def count_boxes_coordinates(m):
    coordinates = []

    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "O":
                coordinates.append(100 * count_to_top(m, y, x) + count_to_left(m, y, x))

    return sum(coordinates)


def move_robot(m, moves):
    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    y, x = find_robot(m)

    for c in moves:
        # print(f"move is {c}")
        next_pos = (y + directions[c][0], x + directions[c][1])
        if is_safe_move(m, next_pos[0], next_pos[1]):
            m[y] = m[y][:x] + "." + m[y][x + 1:]
            y += directions[c][0]
            x += directions[c][1]
            m[y] = m[y][:x] + "@" + m[y][x + 1:]
        elif m[next_pos[0]][next_pos[1]] == "O":
            if move_boxes(m, next_pos[0], next_pos[1], directions[c]):
                m[y] = m[y][:x] + "." + m[y][x + 1:]
                y += directions[c][0]
                x += directions[c][1]
                m[y] = m[y][:x] + "@" + m[y][x + 1:]
        # print("\n".join(m), end="\n\n")


def main():
    with open("input.txt", "r") as file:
        data_not_parsed = [data.strip() for data in file.read().split("\n\n")]

    m = [line.strip() for line in data_not_parsed[0].split("\n")]
    moves = "".join(line.strip() for line in data_not_parsed[1].split("\n"))

    move_robot(m, moves)
    print(count_boxes_coordinates(m))


if __name__ == "__main__":
    main()
