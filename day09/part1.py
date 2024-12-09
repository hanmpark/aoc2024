def generate_block(disk_map):
	id = 0
	block = []

	for i in range(len(disk_map)):
		if i % 2 == 0:
			block += [id] * int(disk_map[i])
			id += 1
		else:
			block += [None] * int(disk_map[i])

	return block

def move_block(block):
	i = len(block) - 1
	j = 0
	while j < i:
		if block[i] == None:
			i -= 1
			continue
		for k in range(j, len(block)):
			if block[k] == None:
				block
				block = block[:k] + [block[i]] + block[k+1:]
				block = block[:i] + [None] + block[i+1:]
				j = k + 1
				break
		i -= 1

	return block

def count_block(block):
	checksum = 0
	for i in range(len(block)):
		if block[i] == None:
			break
		checksum += i * int(block[i])
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
