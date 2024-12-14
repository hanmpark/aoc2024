import re


def parse_input(games):
    game_data = []

    for game in games:
        game_input = {}
        game = game.split("\n")
        for i, line in enumerate(game):
            if i == 0:
                game_input["a"] = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", line)[0]))
            elif i == 1:
                game_input["b"] = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", line)[0]))
            else:
                game_input["prize"] = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", line)[0]))
                game_input["prize"][0] += 10000000000000
                game_input["prize"][1] += 10000000000000
        game_data.append(game_input)

    return game_data


def is_solution(a, b, target_x, target_y, a_x, a_y, b_x, b_y):
    if a < 0 or b < 0:
        return False
    return a * a_x + b * b_x == target_x and a * a_y + b * b_y == target_y


"""
prize_x = a_x * a + b_x * b
prize_y = a_y * a + b_y * b

equation of b for y:
b = (prize_y - a_y * a) / b_y

now find a for the x equation:
a_x * a + b_x * ((prize_y - a_y * a) / b_y) = prize_x
a_x * a * b_y + b_x * prize_y - b_x * a_y * a = prize_x * b_y
a * (a_x * b_y - b_x * a_y) = prize_x * b_y - b_x * prize_y
a = (prize_x * b_y - b_x * prize_y) / (a_x * b_y - b_x * a_y)
"""

def find_solutions(game_data):
    prices = []

    for game in game_data:
        target_x, target_y = game["prize"]
        a_x, a_y = game["a"]
        b_x, b_y = game["b"]

        i_a = (target_x * b_y - b_x * target_y) // (a_x * b_y - b_x * a_y)
        i_b = (target_y - a_y * i_a) // b_y

        if is_solution(i_a, i_b, target_x, target_y, a_x, a_y, b_x, b_y):
            prices.append(i_a * 3  + i_b)

    return prices


def main():
    with open("input.txt") as file:
        games = file.read().strip().split("\n\n")

    game_data = parse_input(games)
    prices = find_solutions(game_data)

    print(sum(prices))


if __name__ == "__main__":
    main()
