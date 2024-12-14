import re


def parse_lines(lines):
    data = []
    for line in lines:
        data_in_line = list(map(int, re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0]))
        data.append([[data_in_line[0], data_in_line[1]], [data_in_line[2], data_in_line[3]]])

    return data


def count_robots(data, x, y):
    return sum([1 if robot[0] == [x, y] else 0 for robot in data])


def compute(data):
    max_x = max([robot[0][0] for robot in data]) + 1
    max_y = max([robot[0][1] for robot in data]) + 1

    for _ in range(100):
        for robot in data:
            robot[0][0] = (robot[0][0] + robot[1][0]) % max_x
            robot[0][1] = (robot[0][1] + robot[1][1]) % max_y

    # m = "\n".join(["".join(["#" if [x, y] in [robot[0] for robot in data] else "." for x in range(max_x)]) for y in range(max_y)])

    # print(m, end="\n\n")

    # qm1 = "\n".join(["".join(["#" if [x, y] in [robot[0] for robot in data] else "." for x in range(max_x) if x < max_x // 2]) for y in range(max_y) if y < max_y // 2])
    # qm2 = "\n".join(["".join(["#" if [x, y] in [robot[0] for robot in data] else "." for x in range(max_x) if x > max_x // 2]) for y in range(max_y) if y < max_y // 2])
    # qm3 = "\n".join(["".join(["#" if [x, y] in [robot[0] for robot in data] else "." for x in range(max_x) if x < max_x // 2]) for y in range(max_y) if y > max_y // 2])
    # qm4 = "\n".join(["".join(["#" if [x, y] in [robot[0] for robot in data] else "." for x in range(max_x) if x > max_x // 2]) for y in range(max_y) if y > max_y // 2])
    # print(f"Quadrant 1:\n{qm1}")
    # print(f"Quadrant 2:\n{qm2}")
    # print(f"Quadrant 3:\n{qm3}")
    # print(f"Quadrant 4:\n{qm4}")
    quadrant1 = sum([count_robots(data, x, y) for x in range(max_x) for y in range(max_y) if y < max_y // 2 and x < max_x // 2])
    quadrant2 = sum([count_robots(data, x, y) for x in range(max_x) for y in range(max_y) if y < max_y // 2 and x > max_x // 2])
    quadrant3 = sum([count_robots(data, x, y) for x in range(max_x) for y in range(max_y) if y > max_y // 2 and x < max_x // 2])
    quadrant4 = sum([count_robots(data, x, y) for x in range(max_x) for y in range(max_y) if y > max_y // 2 and x > max_x // 2])

    print(f"Quadrant 1: {quadrant1}")
    print(f"Quadrant 2: {quadrant2}")
    print(f"Quadrant 3: {quadrant3}")
    print(f"Quadrant 4: {quadrant4}")

    return quadrant1 * quadrant2 * quadrant3 * quadrant4


def main():
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    data = parse_lines(lines)
    print(compute(data))


if __name__ == "__main__":
    main()
