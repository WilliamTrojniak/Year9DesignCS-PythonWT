with open("DATA22.txt", "r") as file:
	content = file.read().splitlines()

for i in range(len(content)):
	content[i] = content[i].split()

currentDataSet = []
currentRuleSet = []
currentString = ""
output = []

firstLetter = ""
lastLetter = ""


charCountArr = []
charMultFactor = []
CHARARRAY = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def countInitStrChars():
	global charCountArr
	charCountArr = []
	for i in range(len(CHARARRAY)):
		charCountArr.append(0)

	for i in range(len(currentString)):
		for t in range(len(CHARARRAY)):
			if(currentString[i] == CHARARRAY[t]):
				charCountArr[t] += 1
	# print(charCountArr)

def getMultFactors():
	#Reset the Array
	global charMultFactor
	charMultFactor = []
	for i in range(len(CHARARRAY)):
		charMultFactor.append([])
		for t in range(len(CHARARRAY)):
			charMultFactor[i].append(0)


	#Get conversion rules for letters
	for i in range(len(CHARARRAY)):
		for t in range(len(currentRuleSet)):
			if(CHARARRAY[i] == currentRuleSet[t][0]):
				#Find mutliplication factors of each letter
				for j in range(len(currentRuleSet[t][1])):
					for g in range(len(CHARARRAY)):
						if(CHARARRAY[g] == currentRuleSet[t][1][j]):
							charMultFactor[i][g] += 1


def calcNextIterationLength():
	global charCountArr

	#Setup temporary array
	tempCharCountArr = []
	for i in range(26):
		tempCharCountArr.append(0)


	for i in range(len(charMultFactor)):
		for t in range(len(charMultFactor[i])):
			tempCharCountArr[t] += charMultFactor[i][t] * charCountArr[i]
	charCountArr = tempCharCountArr

def getIterationLength():
	cntr = 0
	for i in range(len(charCountArr)):
		cntr += charCountArr[i]
	return cntr

def nextFirstLetter():
	global firstLetter
	for i in range(len(currentRuleSet)):
		if(firstLetter == currentRuleSet[i][0]):
			firstLetter = currentRuleSet[i][1][0]
			break
	#print(firstLetter)

def nextLastLetter():
	global lastLetter
	for i in range(len(currentRuleSet)):
		if(lastLetter == currentRuleSet[i][0]):
			lastLetter = currentRuleSet[i][1][-1]
			break
	#print(lastLetter)






for i in range(len(content)):
	currentDataSet = []
	if(content[i][0].isdigit()):
		for x in range(int(content[i][0])+1):
			currentDataSet.append(content[i+x])
		currentRuleSet = currentDataSet[1:len(currentDataSet)]
		currentString = currentDataSet[0][2]
		firstLetter = currentString[0]
		lastLetter = currentString[-1]
		countInitStrChars()
		getMultFactors()
		for t in range(int(currentDataSet[0][1])):
			calcNextIterationLength()
			nextFirstLetter()
			nextLastLetter()
		print(firstLetter + lastLetter, getIterationLength())




