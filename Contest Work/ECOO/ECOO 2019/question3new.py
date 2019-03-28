with open('DATA31.txt', "r") as file:
	content = file.read().splitlines()


currentLevelInfo = []
currentLevelLayout = []

playerPos = []

simulationIsComplete = False




def successfullyCompleteSimulation():
	global simulationIsComplete

	simulationIsComplete = True
	print("CLEAR")

def failSimulation():
	global simulationIsComplete

	simulationIsComplete = True
	print(playerPos[1]+1)

def jump():
	global currentLevelInfo
	global currentLevelLayout
	global playerPos

	hasLanded = False
	for h in range(currentLevelInfo[0]+1):
		
		canLand = True
		#First Check For Vertical Collision
		if(currentLevelLayout[(playerPos[0])-h][playerPos[1]] != "@"):
			# print("No Vertical Collision")
			#Check for horizontal collision
			if(currentLevelLayout[(playerPos[0])-h][(playerPos[1])+1] != "@" and currentLevelLayout[(playerPos[0])-h][(playerPos[1])+2] != "@"):
				# Print("No horizontal collision")
				#Check that path down is clear
				for i in range(h+1):
					if(currentLevelLayout[(playerPos[0])-i][(playerPos[1])+2] == "@"):
						canLand = False
						# print("Path Down is not clear")
			else:
				canLand = False
		else:
			canLand = False
		if(canLand):
			playerPos[1] = playerPos[1]+2
			# print("Player moved to ", playerPos)
			hasLanded = True
	if(hasLanded == False):
		failSimulation()



def simulateLevelPlaythrough():
	global simulationIsComplete
	global playerPos
	global currentLevelInfo
	global currentLevelLayout

	simulationIsComplete = False
	while(simulationIsComplete != True):
		if(currentLevelLayout[playerPos[0]][playerPos[1]] == "G"):
			successfullyCompleteSimulation()
			break
		elif(currentLevelLayout[playerPos[0]][playerPos[1]+1] != "@"):
				playerPos[1] += 1
				# print("Player moved to ", playerPos)
		else:
			jump()


def getPlayerStartPos():
	global playerPos
	for i in range(currentLevelInfo[1]):
		if(currentLevelLayout[(currentLevelInfo[2])-2][i] == "L"):
			playerPos = [(currentLevelInfo[2])-2,i]
			# print(playerPos)



def getLevelLayout(index):
	global currentLevelLayout
	currentLevelLayout = []
	for i in range(currentLevelInfo[2]):
		currentLevelLayout.append(content[index+i+1])
		for t in range(len(currentLevelLayout)):
			currentLevelLayout[t] = list(currentLevelLayout[t])
	# print(currentLevelLayout)




def getLevelInfo(index):
	global currentLevelInfo
	currentLevelInfo = content[index].split()
	for i in range(len(currentLevelInfo)):
		currentLevelInfo[i] = int(currentLevelInfo[i])
	if(currentLevelInfo[0] > currentLevelInfo[2]-2):#Ensures that the player can't jump higher than the game window
		currentLevelInfo[0] = currentLevelInfo[2]-2
	#print(currentLevelInfo)
	getLevelLayout(index)#Gets the level's layout
	getPlayerStartPos()#Gets player's starting position



#Main Loop
cntr = 0
for i in range(len(content)): 
	if(content[i][0].isdigit()):
		cntr += 1
		# print("Now on level", cntr)
		getLevelInfo(i)
		simulateLevelPlaythrough()













