def main():
	try:
		with open("input.txt", "r") as file:
			left_list = []
			right_list = []

			for line in file:
				left, right = line.split()
				left_list.append(int(left))
				right_list.append(int(right))

			similarity_score = 0
			for number in left_list:
				similarity_score += number * right_list.count(number)
			print(similarity_score)


	except FileNotFoundError:
		print("The file was not found.")
	except IOError:
		print("An error occurred while reading the file.")

if __name__ == "__main__":
	main()
