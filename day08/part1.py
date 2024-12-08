def get_coordinates_diff(x, y, x1, y1):
	return x - x1, y - y1

def get_possible_antinodes(x, y, x1, y1, lines):
	cx, cy = get_coordinates_diff(x, y, x1, y1)
	px, py = x1 - cx, y1 - cy
	print(f"px: {px} py: {py}")
	if px < 0 or px >= len(lines) or py < 0 or py >= len(lines[0]):
		return None, None
	return px, py

def find_antinodes(lines, seen, x, y):
	print(f"for x: {x} y: {y} and frequency: {lines[x][y]}")
	for x1 in range(len(lines)):
		for y1 in range(len(lines[0])):
			if lines[x1][y1] == lines[x][y] and x1 != x and y1 != y:
				print(f"found lines[{x1}][{y1}] == lines[{x}][{y}] == {lines[x1][y1]}")
				px, py = get_possible_antinodes(x, y, x1, y1, lines)
				if px is not None and (px, py) not in seen:
					seen.add((px, py))
				px, py = get_possible_antinodes(x1, y1, x, y, lines)
				if px is not None and (px, py) not in seen:
					seen.add((px, py))
	print("")

def main():
	with open("input.txt", "r") as file:
		lines = [line.strip() for line in file.readlines()]

	seen = set()

	for x in range(len(lines)):
		for y in range(len(lines[0])):
			if lines[x][y] != '.':
				find_antinodes(lines, seen, x, y)

	print(len(seen))

if __name__ == "__main__":
	main()
