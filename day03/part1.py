import re

def main():
	pattern = r"mul\((\d+),(\d+)\)"
	result = 0
	with open("input.txt") as file:
		content = file.read()
		matches = re.findall(pattern, content)
		for match in matches:
			x, y = match
			result += int(x) * int(y)

	print(result)

if __name__ == "__main__":
	main()
