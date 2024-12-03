def is_valid(levels):
	if not(levels == sorted(levels) or levels == sorted(levels, reverse=True)):
		return False

	for i in range(len(levels) - 1):
		if abs(levels[i] - levels[i + 1]) > 3 or levels[i] == levels[i + 1]:
			return False

	return True

def check_validity(levels):
	if is_valid(levels):
		return True
	else:
		for i in range(len(levels)):
			modified_levels = levels[:i] + levels[i + 1:]
			if is_valid(modified_levels):
				return True
	return False
def main():
	with open("input.txt", "r") as file:
		count = 0
		for line in file:
			levels = [int(level) for level in line.split()]
			count += check_validity(levels)
		print(count)

if __name__ == "__main__":
	main()
