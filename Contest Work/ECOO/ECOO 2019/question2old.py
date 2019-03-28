with open("DATA22.txt", "r") as file:
	content = file.read().splitlines()

currentDataSet = []
currentRuleSet = []
currentString = ""
output = []

cntr = 0


def ibrahimSucks(inString, ruleArray):
	global cntr
	outputStr = ""
	for i in range(len(inString)):
		for n in range(len(ruleArray)):
			if inString[i] == ruleArray[n][0]:
				outputStr += ruleArray[n][1]

	cntr += 1
	return outputStr


for i in range(len(content)):
	content[i] = content[i].split()


for i in range(len(content)):
	currentDataSet = []

	if(content[i][0].isdigit()):
		for x in range(int(content[i][0])+1):
			currentDataSet.append(content[i+x])
		currentRuleSet = currentDataSet[1:len(currentDataSet)]
		currentString = currentDataSet[0][2]
		for x in range(int(currentDataSet[0][1])):
			currentString = ibrahimSucks(currentString, currentRuleSet)
		print(currentString[0]+currentString[-1], len(currentString))
		
		





