def main():
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

	def find_guard(the_map):
		# Find the guard position
		for y, line in enumerate(the_map):
			if "^" in line:
				return line.index("^"), y

	def has_left(the_map, x, y, moveX, moveY):
		if moveX < 0 or moveY < 0 or moveX >= len(the_map[0]) or moveY >= len(the_map):
			return 1
		if the_map[moveY][moveX] == "#":
			the_map[y] = the_map[y][:x] + "+" + the_map[y][x + 1:]
			return 2
		if the_map[moveY][moveX] == "O":
			return 3
		return 0

	def do_the_loop(the_map, x, y, go_to):
		has_left_district = 0

		while has_left_district != 1:
			moveX, moveY = x + direction[go_to][0], y + direction[go_to][1]
			has_left_district = has_left(the_map, x, y, moveX, moveY)

			if has_left_district == 3:
				return True
			if has_left_district == 2:
				go_to = turn_right[go_to]
				continue

			if has_left_district == 0:
				x = moveX
				y = moveY

		return False

	def has_intersection_in_sight(check_intersection):
		for i in range(len(check_intersection) - 1):
			if check_intersection[i] == '+' and check_intersection[i + 1] == '#':
				return True
			elif check_intersection[i] == '#':
				return False
		return False

	def is_loop(the_map, x, y, moveX, moveY, go_to):
		check_intersection = ''

		if go_to == "<":
			check_intersection = ''.join(the_map[row][x] for row in range(y))
			check_intersection = check_intersection[::-1]
		elif go_to == ">":
			check_intersection = ''.join(the_map[row][x] for row in range(y + 1, len(the_map)))
		elif go_to == "^":
			check_intersection = the_map[y][x + 1:]
		else:
			check_intersection = the_map[y][:x]
			check_intersection = check_intersection[::-1]

		print("HAHA " + " ".join(check_intersection))
		if has_intersection_in_sight(check_intersection):
			tmp_map = the_map[:]
			tmp_map[moveY] = tmp_map[moveY][:moveX] + "O" + tmp_map[moveY][moveX + 1:]
			go_to = turn_right[go_to]
			return do_the_loop(tmp_map, x, y, go_to)

		return False

	def find_loops(the_map, x, y):
		has_left_district = 0 # 0: no left, 1: left, 2: obstacle 3: custom obstacle
		go_to = "^"
		count = 0

		while has_left_district != 1:
			# current position of the guard moving through the district
			moveX, moveY = x + direction[go_to][0], y + direction[go_to][1]
			has_left_district = has_left(the_map, x, y, moveX, moveY)

			if has_left_district == 2:
				go_to = turn_right[go_to]
				continue

			if has_left_district == 0:
				count += is_loop(the_map, x, y, moveX, moveY, go_to)
				x = moveX
				y = moveY

		print("\n".join(the_map))
		print(count)


	with open("input.txt", "r") as file:
		the_map = file.readlines()
		x, y = find_guard(the_map)
		find_loops(the_map, x, y)

if __name__ == "__main__":
	main()
