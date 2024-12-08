def get_coordinates_diff(x, y, x1, y1):
	return x - x1, y - y1

def get_possible_antinodes(x, y, x1, y1, lines):
	cx, cy = get_coordinates_diff(x, y, x1, y1)
	px, py = x1 - cx, y1 - cy
	if px < 0 or px >= len(lines) or py < 0 or py >= len(lines[0]):
		return None, None
	return px, py

def continue_to_find_antinodes(test, lines, seen, x, y, x1, y1):
	while True:
		px, py = get_possible_antinodes(x, y, x1, y1, lines)
		if px is None:
			break
		if test[px][py] == '.':
			test[px] = test[px][:py] + '#' + test[px][py + 1:]
		if not (px, py) in seen:
			seen.add((px, py))
		x, y = x1, y1
		x1, y1 = px, py

def find_antinodes(test, lines, seen, x, y):
	for x1 in range(len(lines)):
		for y1 in range(len(lines[0])):
			if lines[x1][y1] == lines[x][y] and x1 != x and y1 != y:
				seen.add((x1, y1))
				continue_to_find_antinodes(test, lines, seen, x, y, x1, y1)
				continue_to_find_antinodes(test, lines, seen, x1, y1, x, y)

def main():
	with open("input.txt", "r") as file:
		lines = [line.strip() for line in file.readlines()]

	test = lines.copy()
	seen = set()

	for x in range(len(lines)):
		for y in range(len(lines[0])):
			if lines[x][y] != '.':
				find_antinodes(test, lines, seen, x, y)

	print(len(seen))

if __name__ == "__main__":
	main()
