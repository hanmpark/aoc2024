def is_valid(levels):
	if not(levels == sorted(levels) or levels == sorted(levels, reverse=True)):
		return False
	for i in range(len(levels) - 1):
		if abs(levels[i] - levels[i + 1]) > 3 or levels[i] == levels[i + 1]:
			return False
	return True

def main():
	with open("input.txt", "r") as file:
		count = 0
		for line in file:
			levels = line.split()
			count += is_valid([int(level) for level in levels])
		print(count)

if __name__ == "__main__":
	main()
