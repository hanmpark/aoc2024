def main():
	def get_strings(content, i, j):
		string1, string2 = "", ""

		for k in range(3):
			string1 += content[i + k][j + k]
		for k in range(3):
			string2 += content[i + 2 - k][j + k]
		return string1, string2

	count = 0

	with open("input.txt", "r") as file:
		content = file.readlines()
		rows, cols = len(content), len(content[0])

		for i in range(1, rows - 1):
			for j in range(1, cols - 1):
				if content[i][j] != "A":
					continue
				string1, string2 = get_strings(content, i - 1, j - 1)
				count += (string1 == "MAS" or string1 == "SAM") and (string2 == "MAS" or string2 == "SAM")

		print(count)

if __name__ == "__main__":
	main()
