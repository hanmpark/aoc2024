def main():
	def check_position(page_ordering, update, i, j):
		# iterate through the update list after the current page
		# to check that the next page is in the correct order
		for k in range(len(update)):
			if int(update[k]) == int(page_ordering[j][1]) and k < i:
				return False
		return True

	def check_order(page_ordering, update):
		# check if the order of the update list is correct
		for i in range(len(update)):
			for j in range(len(page_ordering)):
				# look into the page_ordering list
				if int(update[i]) == int(page_ordering[j][0]):
					if check_position(page_ordering, update, i, j) == False:
						return 0
		return int(update[len(update) // 2])

	result = 0

	with open("input.txt", "r") as file:
		data = file.read().split("\n-\n")
		page_ordering = data[0].splitlines()
		for i in range(len(page_ordering)):
			page_ordering[i] = page_ordering[i].split('|')
		updates = data[1].splitlines()

		for i in range(len(updates)):
			result += check_order(page_ordering, updates[i].split(','))
		print(result)

if __name__ == "__main__":
	main()
