def generate_block(disk_map):
	id = 0
	block = []

	for i in range(len(disk_map)):
		if i % 2 == 0:
			block += [[id] * int(disk_map[i])]
			id += 1
		else:
			block[id - 1] += [None] * int(disk_map[i])

	return block

def count_size(block):
	tmp = block[0]
	count = 0

	for i in range(len(block)):
		if block[i] != tmp:
			break
		count += 1

	return count

def move_block(block):
	i = len(block) - 1

	while i > 0:
		size = count_size(block[i])
		for j in range(i): # from the beginning
			size_none = block[j].count(None)
			skip = len(block[j]) - size_none
			if size <= size_none:
				for k in range(size):
					block[j] = block[j][:skip+k] + [block[i][k]] + block[j][skip+k+1:]
					block[i] = block[i][:k] + [None] + block[i][k+1:]
				break
		i -= 1
	return block

def count_block(block):
	checksum = 0
	index = 0
	for i in range(len(block)):
		print(block[i])
		for j in range(len(block[i])):
			if block[i][j] != None:
				checksum += index * int(block[i][j])
			index += 1
	return checksum

def main():
	with open("input.txt", "r") as file:
		disk_map = file.read().rstrip()

	block = generate_block(disk_map)
	block = move_block(block)
	checksum = count_block(block)
	print(checksum)

if __name__ == "__main__":

	main()
