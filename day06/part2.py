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

	obstacles = set()

	def find_guard(the_map):
		# Find the guard position
		for y, line in enumerate(the_map):
			if "^" in line:
				return line.index("^"), y

	def has_left(the_map, moveX, moveY):
		if moveX < 0 or moveY < 0 or moveX >= len(the_map[0]) or moveY >= len(the_map):
			return 1
		if the_map[moveY][moveX] == "#" or the_map[moveY][moveX] == "O":
			return 2
		return 0

	def do_the_loop(the_map, x, y, go_to):
		has_left_district = 0

		visited = set()

		while has_left_district != 1:
			if (x, y, go_to) in visited:
				return True
			visited.add((x, y, go_to))

			moveX, moveY = x + direction[go_to][0], y + direction[go_to][1]
			has_left_district = has_left(the_map, moveX, moveY)

			if has_left_district == 2:
				go_to = turn_right[go_to]
				continue

			if has_left_district == 0:
				x = moveX
				y = moveY

		return False

	def is_loop(the_map, x, y, moveX, moveY, go_to):
		tmp_map = list(the_map)
		if (moveY, moveX) in obstacles:
			return False
		obstacles.add((moveY, moveX))
		tmp_map[moveY] = tmp_map[moveY][:moveX] + "O" + tmp_map[moveY][moveX + 1:]
		go_to = turn_right[go_to]
		return do_the_loop(tmp_map, x, y, go_to)

	def find_loops(the_map, x, y):
		has_left_district = 0 # 0: no left, 1: left, 2: obstacle 3: custom obstacle
		go_to = "^"
		count = 0

		while has_left_district != 1:
			# current position of the guard moving through the district
			moveX, moveY = x + direction[go_to][0], y + direction[go_to][1]
			has_left_district = has_left(the_map, moveX, moveY)

			if has_left_district == 2:
				go_to = turn_right[go_to]
				continue

			if has_left_district == 0:
				if is_loop(the_map, x, y, moveX, moveY, go_to):
					count += 1
				x = moveX
				y = moveY

		print(count)


	with open("input.txt", "r") as file:
		the_map = [line.strip() for line in file.readlines()]
		x, y = find_guard(the_map)
		find_loops(the_map, x, y)

if __name__ == "__main__":
	main()
