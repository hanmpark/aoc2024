def main():
	def check_position(page_ordering, update, i, j):
		# iterate through the update list after the current page
		# to check that the next page is in the correct order
		for k in range(len(update)):
			if update[k] == page_ordering[j][1] and k < i:
				return False
		return True

	def check_order(page_ordering, update):
		# check if the order of the update list is correct
		for i in range(len(update)):
			for j in range(len(page_ordering)):
				# look into the page_ordering list
				if update[i] == page_ordering[j][0]:
					if check_position(page_ordering, update, i, j) == False:
						return 0
		return update[len(update) // 2]

	result = 0

	with open("input.txt", "r") as file:
		data = file.read().split("\n-\n")
		page_ordering = [list(map(int, line.split('|'))) for line in data[0].splitlines()]
		updates = [list(map(int, update.split(','))) for update in data[1].splitlines()]

		for i in range(len(updates)):
			result += check_order(page_ordering, updates[i])

		print(result)

if __name__ == "__main__":
	main()
