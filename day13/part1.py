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
        game_data.append(game_input)

    return game_data


def find_solutions(game_data):
    prices = []

    for game in game_data:
        target_x, target_y = game["prize"]
        a_x, a_y = game["a"]
        b_x, b_y = game["b"]

        best_cost = float("inf")
        found_solution = False

        for a in range(101):
            for b in range(101):
                if (a * a_x + b * b_x == target_x) and (a * a_y + b * b_y == target_y):
                    cost = 3 * a + b
                    if cost < best_cost:
                        best_cost = cost
                        found_solution = True
        if found_solution:
            prices.append(best_cost)

        print()

    return prices


def main():
    with open("input.txt") as file:
        games = file.read().strip().split("\n\n")

    game_data = parse_input(games)
    prices = find_solutions(game_data)

    print(sum(prices))


if __name__ == "__main__":
    main()
