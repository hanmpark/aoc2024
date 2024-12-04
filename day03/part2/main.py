import re

def main():
	pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
	result = 0
	enabled = True
	with open("input.txt") as file:
		content = file.read()
		matches = re.finditer(pattern, content)
		for match in matches:
			if match.group(1) and match.group(2) and enabled:
				x, y = match.group(1), match.group(2)
				result += int(x) * int(y)
			elif "do()" in match.group():
				enabled = True
			elif "don't()" in match.group():
				enabled = False

	print(result)

if __name__ == "__main__":
	main()
