NsMsDs = []
As = []
cleanShirts = 0
totalShirts = 0
output = []



with open("DATA11.txt", "r") as file:
	content = file.read().splitlines()

for i in range(len(content)):
	if(i%2 == 0):
		NsMsDs.append(content[i].split())
	else:
		As.append(content[i].split())





for i in range(len(NsMsDs)):
	cleanShirts = int(NsMsDs[i][0])
	totalShirts = cleanShirts
	eventCount = int(NsMsDs[i][1])
	days = int(NsMsDs[i][2])
	laundry = 0


	for x in range(days):
		if(cleanShirts <= 0):
			cleanShirts = totalShirts
			laundry += 1
		cleanShirts -= 1
			



		for y in range(len(As[i])):
			if (x+1 == int(As[i][y])):
				cleanShirts += 1
				totalShirts += 1
		
	output.append(laundry)

for i in range(len(output)):
	print(output[i])


