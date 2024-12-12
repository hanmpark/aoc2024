def count_area_price(garden, garden_type, i, j, seen, garden_field):
    count = count_occurences = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    if (i < 0 or i >= len(garden) or j < 0 or j >= len(garden[0])) or garden_type != garden[i][j]:
        return 0, 1
    seen.add((i, j))
    garden_field.add((i, j))
    count_occurences += 1
    for k in range(len(directions)):
        new_i = i + directions[k][0]
        new_j = j + directions[k][1]
        if (new_i, new_j) not in seen:
            new_count = count_area_price(garden, garden_type, new_i, new_j, seen, garden_field)
            count_occurences += new_count[0]
            count += new_count[1]

    return [count_occurences, count]


def count_fencing_price(garden):
    garden_done = []
    garden_field = set()

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) not in garden_field:
                seen = set()
                garden_done += [count_area_price(garden, garden[i][j], i, j, seen, garden_field)]

    return sum(values[0] * values[1] for values in garden_done)


def main():
    with open("input.txt", "r") as file:
        garden = [line.strip() for line in file.readlines()]

    fencing_price = count_fencing_price(garden)
    print(fencing_price)


if __name__ == "__main__":
    main()
