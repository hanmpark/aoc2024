def is_side(garden, i, j, garden_type):
    return i < 0 or i >= len(garden) or j < 0 or j >= len(garden[0]) or garden[i][j] != garden_type


def is_in_corner_set(corner_set, tmp_corner_set):
    for group in corner_set:
        if len(group.intersection(tmp_corner_set)) >= 2:
            return True
    return False


def count_borders(garden, garden_type, i, j, drct, corner_set):
    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    corners = [directions[(drct + 1) % 4], directions[(drct + 2) % 4]]
    tmp_corner_set = []

    # for l in range(2):
    #     put_in_corner_set = []
    #     put_in_corner_set.append((i, j))
    tmp_corner_set.append((i, j))
    for k in range(2):
        ni = i
        nj = j
        for m in range(k + 1):
            ni += corners[m][0]
            nj += corners[m][1]

        # put_in_corner_set.append((ni, nj))
        tmp_corner_set.append((ni, nj))

    for l in range(len(tmp_corner_set)):
        x, y = tmp_corner_set[l][0]
        x1, y1 = tmp_corner_set[l][1]
        x2, y2 = tmp_corner_set[l][2]
        if not is_side(garden, x1, y1, garden_type) and not is_side(garden, x2, y2, garden_type) and not is_in_corner_set(corner_set, tmp_corner_set[l]):
            print(f" in corner set: {tmp_corner_set[l]}")
            corner_set.add(frozenset(tmp_corner_set[l]))
            count += 1
        elif is_side(garden, x, y, garden_type) and is_side(garden, x2, y2, garden_type) and not frozenset(tmp_corner_set[l]) in corner_set:
            print(f" out corner set: {tmp_corner_set[l]}")
            corner_set.add(frozenset(tmp_corner_set[l]))
            count += 1

    return count


def count_area_price(garden, garden_type, i, j, drct, seen, garden_field, corner_set):
    count = count_occurences = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    if is_side(garden, i, j, garden_type):
        return 0, count_borders(garden, garden_type, i, j, drct, corner_set)
    seen.add((i, j))
    garden_field.add((i, j))
    count_occurences += 1
    for k in range(len(directions)):
        new_i = i + directions[k][0]
        new_j = j + directions[k][1]
        if (new_i, new_j) not in seen:
            new_count = count_area_price(garden, garden_type, new_i, new_j, k, seen, garden_field, corner_set)
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
                corner_set = set()
                garden_done += [count_area_price(garden, garden[i][j], i, j, 0, seen, garden_field, corner_set)]

    print(garden_done)
    return sum(values[0] * values[1] for values in garden_done)


def main():
    with open("input.txt", "r") as file:
        garden = [line.strip() for line in file.readlines()]

    fencing_price = count_fencing_price(garden)
    print(fencing_price)


if __name__ == "__main__":
    main()
