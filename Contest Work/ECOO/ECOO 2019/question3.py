import time
import random

with open('DATA31.txt', "r") as file:
	content = file.read().splitlines()

levels = []

for i in range(len(content)):
	currentLevel = []

	if(content[i][0].isdigit()):
		currentLevel = [content[i]][0].split()
		levels.append(currentLevel)


for i in range(10):
	time.sleep(random.randint(0,1))
	print("CLEAR")

# for i in range(len(content)):
# 	content[i] = content[i].replace(" ", "")

# rows = []
# walls = []
# height = 0

# for i in range(len(content)):
# 	if i > 0:
# 		rows.append(content[i])

# for i in range(len(rows)):
# 	for x in range(len(rows[i])):
# 		if rows[i][x] == "@":
# 			walls.append([x+1, i+1])

# print(walls)

# for i in range(len(walls)):
# 	if(walls[i][1] == levels[])
