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

    seen = set()
    i = 0
    with open("output.txt", "a") as file:
        while True:
            for robot in data:
                robot[0][0] = (robot[0][0] + robot[1][0]) % max_x
                robot[0][1] = (robot[0][1] + robot[1][1]) % max_y

            m = "\n".join(["".join(["#" if [x, y] in [robot[0] for robot in data] else "." for x in range(max_x)]) for y in range(max_y)])

            if m in seen:
                break
            seen.add(m)

            file.write(f"Step {i}:\n{m}\n\n")

            i += 1


def main():
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    data = parse_lines(lines)
    compute(data) # response found at 8049


if __name__ == "__main__":
    main()
