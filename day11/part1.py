def main():
    with open("input.txt", "r") as file:
        data = file.read().strip().split(" ")

    def blink(data):
        new_data = []
        for i in range(len(data)):
            if int(data[i]) == 0:
                new_data += ["1"]
            elif len(data[i]) % 2 == 0:
                splitted_number = [str(int(data[i][:len(data[i])//2])), str(int(data[i][len(data[i])//2:]))]
                new_data += splitted_number
            else:
                new_data += [str(int(data[i]) * 2024)]
        return new_data

    for i in range(25):
        data = blink(data)

    print(len(data))

if __name__ == "__main__":
    main()
