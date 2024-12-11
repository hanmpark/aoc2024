def main():
    with open("input.txt", "r") as file:
        data = file.read().strip().split(" ")

    def blink(data):
        for num in data:
            value = int(num)
            if value == 0:
                yield "1"
            elif len(num) % 2 == 0:
                half_len = len(num) // 2
                yield str(int(num[:half_len]))
                yield str(int(num[half_len:]))
            else:
                yield str(value * 2024)

    for _ in range(25):
        data = blink(data)

    print(sum(1 for _ in data))

if __name__ == "__main__":
    main()
