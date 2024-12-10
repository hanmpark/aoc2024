from collections import deque

def count_paths_to_9(grid):
	rows, cols = len(grid), len(grid[0])
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
	target_sequence = list(range(10))
	path_count = 0

	def breadth_first_search(start_row, start_col):
		queue = deque([(start_row, start_col, 0)])
		count = 0

		while queue:
			row, col, idx = queue.popleft()

			if idx == len(target_sequence) - 1:
				count += 1
				continue

			# explore all possible directions
			for dr, dc in directions:
				nr, nc = row + dr, col + dc
				if 0 <= nr < rows and 0 <= nc < cols:
					if grid[nr][nc] == target_sequence[idx + 1]:
						queue.append((nr, nc, idx + 1))

		return count

	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == 0:
				path_count += breadth_first_search(r, c)

	return path_count

def main():
	with open("input.txt") as file:
		grid = [list(map(int, line.strip())) for line in file]

	print(count_paths_to_9(grid))

if __name__ == "__main__":
	main()
