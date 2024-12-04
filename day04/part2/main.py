def main():
	def get_strings(content, i, j):
		string1, string2 = "", ""

		print(f"i: {i}, j: {j}")
		print(f"content[i][j]: {content[i][j]}")
		for k in range(3):
			string1 += content[i + k][j + k]
		for k in range(3):
			string2 += content[i + 2 - k][j + k]
		if i == 138 and j == 0:
			print(f"String 1: {string1}")
			print(f"String 2: {string2}")
		return string1, string2

	count = 0

	with open("input.txt", "r") as file:
		content = file.readlines()
		rows, cols = len(content), len(content[0])

		for i in range(1, rows - 1):
			for j in range(1, cols - 1):
				string1, string2 = get_strings(content, i - 1, j - 1)
				count += (string1 == "MAS" or string1 == "SAM") and (string2 == "MAS" or string2 == "SAM")

		print(count)

if __name__ == "__main__":
	main()
