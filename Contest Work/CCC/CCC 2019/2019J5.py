subRules = [[],[],[]]

for i in range(3):
	inputString = str(input())
	inStr, outStr = inputString.split()
	subRules[i].append(inStr)
	subRules[i].append(outStr)
	subRules[i].append(len(inStr) < len(outStr)) #Possible Values:(True, False) --> True means that by performing this rule we lengthen the string

print(subRules)


inputString = str(input())

numOfSteps, startingString, endGoal = inputString.split()

numOfSteps = int(numOfSteps)

#Initializes the multidimensional array that will be used to store steps
steps = []
for i in range(numOfSteps):
	steps.append([])

#Check Possible Moves and save as index of sub rules
def getPossibleStartMoves():
	possibleMoves = []
	for i in range(3):
		if(subRules[i][0] in startingString):
			possibleMoves.append(i)
	return possibleMoves

def getPossibleEndMoves():
	possibleEndMoves = []
	for i in range(3):
		if(subRules[i][1] in endGoal):
			possibleEndMoves.append(i)
	return possibleEndMoves

def getShouldLengthenString():
	return len(startingString) < len(endGoal)

possibleMoves = getPossibleStartMoves() #Checks for possible moves to start
endMoves = getPossibleEndMoves() #Returns list of moves that are possible on final step
shouldLengthenString = getShouldLengthenString()#Returns true if the current string is shorter than the goal string

def getOptimalMoves():
	optimalMoves = []
	for i in range(len(possibleMoves)):
		if((subRules[possibleMoves[i]][2] == True and shouldLengthenString == True) or (subRules[possibleMoves[i]][2] == False and shouldLengthenString == False)):
			optimalMoves.append(possibleMoves[i])
	return optimalMoves

print(getOptimalMoves())













