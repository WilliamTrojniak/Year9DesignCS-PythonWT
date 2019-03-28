#print("CCC2018J2")

numOfSpaces = int(input())
parkStr1 = str(input())
parkStr2 = str(input())
ctr = 0
for i in range(numOfSpaces):
	if(parkStr1[i] == 'C' and parkStr1[i] == parkStr2[i]):
		ctr+= 1
print(ctr)