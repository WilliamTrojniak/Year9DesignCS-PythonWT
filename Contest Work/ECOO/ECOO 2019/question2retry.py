with open("DATA21.txt", "r") as file:
	content = file.read().splitlines()

for i in range(len(content)):
	content[i] = content[i].split()

currentDataSet = []
currentRuleSet = []
currentString = ""
output = []

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
	global charMultFactor
	charMultFactor = [[]]
	for i in range(len(CHARARRAY)):
		charMultFactor.append([])
		for t in range(len(CHARARRAY)):
			charMultFactor[i].append(0)
	print(len(charMultFactor))

	for i in range(len(CHARARRAY)):
		for t in range(len(currentRuleSet)):
			if(CHARARRAY[i] == currentRuleSet[t][0]):
				#Find mutliplication factors of each letter
				for j in range(len(currentRuleSet[t][1])):
					for g in range(len(CHARARRAY)):
						if(CHARARRAY[g] == currentRuleSet[t][1][j]):
							charMultFactor[i][g] += 1
	# print(charMultFactor)






# def alterString():
# 	print()

def nextIteration():
	for i in range(len(charCountArr)):
		charCountArr[i]






for i in range(3): #len(content)
	currentDataSet = []
	if(content[i][0].isdigit()):
		for x in range(int(content[i][0])+1):
			currentDataSet.append(content[i+x])
		currentRuleSet = currentDataSet[1:len(currentDataSet)]
		currentString = currentDataSet[0][2]
		countInitStrChars()
		getMultFactors()




