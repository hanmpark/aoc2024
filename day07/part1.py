def is_calibration(test_value, equations):
	operators = ["+" for i in range(len(equations) - 1)]
	for i in range(2 ** len(operators)):
		for j in range(len(operators)):
			if i & (1 << j):
				operators[j] = "+"
			else:
				operators[j] = "*"
		result = equations[0]
		for j in range(1, len(equations)):
			if operators[j - 1] == "+":
				result += equations[j]
			else:
				result *= equations[j]
		if result == test_value:
			return True
	return False

def main():
	count = 0

	with open("input.txt", "r") as file:
		lines = [line.strip() for line in file.readlines()]
		lines = [line.split(": ") for line in lines]
		equations = {int(line[0]): list(map(int, line[1].split(" "))) for line in lines}
		for key in equations:
			if is_calibration(key, equations[key]):
				count += key

		print(count)

if __name__ == "__main__":
	main()
