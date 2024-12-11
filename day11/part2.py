def blink(number, n, dictionary):
    if n == 0:
        return 1
    if (number, n) in dictionary:
        return dictionary[(number, n)]
    if number == "0":
        result = blink("1", n - 1, dictionary)
    elif len(number) % 2 == 0:
        half_len = len(number) // 2
        result = 0
        result += blink(str(int(number[:half_len])), n - 1, dictionary)
        result += blink(str(int(number[half_len:])), n - 1, dictionary)
    else:
        result = blink(str(int(number) * 2024), n - 1, dictionary)
    dictionary[(number, n)] = result
    return result


def main():
    with open("input.txt", "r") as file:
        data = file.read().strip().split(" ")

    dictionary = {}
    res = 0

    for num in data:
        res += blink(num, 75, dictionary)

    print(res)

if __name__ == "__main__":
    main()
