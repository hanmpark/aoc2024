def main():
	try:
		with open("input.txt", "r") as file:
			left_list = []
			right_list = []

			for line in file:
				left, right = line.split()
				left_list.append(int(left))
				right_list.append(int(right))

			left_list.sort()
			right_list.sort()

			differences = [abs(left - right) for left, right in zip(left_list, right_list)]
			sum_differences = sum(differences)
			print(sum_differences)

	except FileNotFoundError:
		print("The file was not found.")
	except IOError:
		print("An error occurred while reading the file.")

if __name__ == "__main__":
	main()
