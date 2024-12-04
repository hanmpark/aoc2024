def main():
	def count_horizontal(content):
		count = 0

		for line in content:
			count += line.count("XMAS") + line.count("SAMX")

		return count

	def count_vertical(content):
		count = 0
		for col in range(len(content[0]) - 1):
			column = ''.join(content[row][col] for row in range(len(content)))
			count += column.count("XMAS") + column.count("SAMX")
			print(f"Column {col}: {column}")

		return count

	def get_diagonal(content):
		diagonals = []
		rows, cols = len(content), len(content[0])

		for start in range(rows + cols - 1):
			diagonal = []
			for i in range(max(0, start - cols + 1), min(rows, start + 1)):
				diagonal.append(content[i][start - i])
			diagonals.append(diagonal)

		for start in range(rows + cols - 1):
			diagonal = []
			for i in range(max(0, start - cols + 1), min(rows, start + 1)):
				diagonal.append(content[i][cols - 1 - (start - i)])
			diagonals.append(diagonal)

		return diagonals

	def count_diagonal(content):
		count = 0

		for diagonal in get_diagonal(content):
			diagonal = ''.join(diagonal)
			count += diagonal.count("XMAS") + diagonal.count("SAMX")

		return count

	count = 0

	with open("input.txt", "r") as file:
		content = file.readlines()
		count += count_horizontal(content) + count_vertical(content) + count_diagonal(content)

	print(count)

if __name__ == "__main__":
	main()
