numOfLines = int(input())

outLines = []

for i in range(numOfLines):
	cntr = 1
	line = str(input())
	lineLength = len(line)
	if(lineLength == 1):
		outLines.append(str(cntr) + " " + line)
	else:
		lineOut = ""
		for i in range(lineLength-1):
			if(line[i] == line[i+1]):
				cntr += 1
				if(i + 2 == lineLength):
					if(lineOut == ""):
						lineOut += (str(cntr) + " " + line[i])
					else:
						lineOut += (" " + str(cntr) + " " + line[i])
			else:
				if(lineOut == ""):
					lineOut += (str(cntr) + " " + line[i])
				else:
					lineOut += (" " + str(cntr) + " " + line[i])
				cntr = 1

				if(i + 2 == lineLength):
					lineOut += (" 1 " + line[i+1])
		outLines.append(lineOut)


for i in range(len(outLines)):
	print(outLines[i])

