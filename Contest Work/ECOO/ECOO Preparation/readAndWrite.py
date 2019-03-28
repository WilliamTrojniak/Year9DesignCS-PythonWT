stringArray = ["Hello", "bob"]
fileName = "text.txt"

def writeArrayToFile(textToWrite):
	f = open(fileName, "w+")
	for i in range(len(textToWrite)):
		f.write(str(textToWrite[i]) + "\n")
	f.close()

def readFile(file):
	f = open(file, "r")
	content = f.read()
	print(content)
	content = content.splitlines()
	f.close()
	print(content)
	for i in range(len(content)):
		print(str(content[i]))


writeArrayToFile(stringArray)
readFile(fileName)