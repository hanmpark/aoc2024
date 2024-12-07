def is_calibration(test_value, equation):
	operators = ["+" for i in range(len(equation) - 1)]
	operator_types = ["+", "*", "||"]

	for op_mask in range(3 ** (len(equation) - 1)):  # 3^(n-1) combinations
		tmp_equation = equation.copy()
		tmp_mask = op_mask

		for i in range(len(equation) - 1):
			operators[i] = operator_types[tmp_mask % 3]
			tmp_mask //= 3

		result = tmp_equation[0]
		for j in range(1, len(tmp_equation)):
			if operators[j - 1] == "+":
				result += tmp_equation[j]
			elif operators[j - 1] == "*":
				result *= tmp_equation[j]
			else:
				result = int(str(result) + str(tmp_equation[j]))
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
		# is_calibration(key, equations[key])
		# break

	print(count)


if __name__ == "__main__":
	main()
