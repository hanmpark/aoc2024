def main():
	def find_guard(the_map):
		# Find the guard position
		for y, line in enumerate(the_map):
			if "^" in line:
				return line.index("^"), y

	def move_guard(the_map, x, y):
		# Move the guard and puts X in its path
		direction = {
			"^": [0, -1],
			"v": [0, 1],
			">": [1, 0],
			"<": [-1, 0]
		}

		turn_right = {
			"^": ">",
			">": "v",
			"v": "<",
			"<": "^"
		}

		def has_left(the_map, x, y, moveX, moveY):
			if moveX < 0 or moveY < 0 or moveX >= len(the_map[0]) or moveY >= len(the_map):
				return 1
			if the_map[moveY][moveX] == "#":
				the_map[y] = the_map[y][:x] + turn_right[the_map[y][x]] + the_map[y][x + 1:]
				return 2
			return 0

		has_left_district = 0

		while has_left_district != 1:
			moveX, moveY = x + direction[the_map[y][x]][0], y + direction[the_map[y][x]][1]
			has_left_district = has_left(the_map, x, y, moveX, moveY)

			if has_left_district == 2:
				continue

			keep_going = the_map[y][x] # ">"
			the_map[y] = the_map[y][:x] + "X" + the_map[y][x + 1:] # "X"

			if has_left_district == 0:
				x = moveX
				y = moveY
				the_map[y] = the_map[y][:x] + keep_going + the_map[y][x + 1:] # "." -> keep_going "^"

		count = 0
		for line in the_map:
			count += line.count("X")
		print(count)

	with open("input.txt", "r") as file:
		the_map = file.readlines()
		x, y = find_guard(the_map)
		move_guard(the_map, x, y)

if __name__ == "__main__":
	main()
