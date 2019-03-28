numOfLines = int(input())

for i in range(numOfLines):
	inputStr = str(input())
	num, char = inputStr.split()
	num = int(num)
	word = ""

	for i in range(num):
		word += char
	print(word)