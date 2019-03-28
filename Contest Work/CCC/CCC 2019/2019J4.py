#		  A  B
#nums = 1[1, 2]
#		2[3, 4]


defaultArr = [1, 2, 3, 4]

def hFlip(arr):
	a1 = arr[2]
	b1 = arr[3]
	a2 = arr[0]
	b2 = arr[1]
	tempArr = [a1, b1, a2, b2]
	defaultArr[0] = tempArr[0]
	defaultArr[1] = tempArr[1]
	defaultArr[2] = tempArr[2]
	defaultArr[3] = tempArr[3]

def vFLip(arr):
	a1 = arr[1]
	b1 = arr[0]
	a2 = arr[3]
	b2 = arr[2]
	tempArr = [a1, b1, a2, b2]
	defaultArr[0] = tempArr[0]
	defaultArr[1] = tempArr[1]
	defaultArr[2] = tempArr[2]
	defaultArr[3] = tempArr[3]

stringIn = str(input())

stringInLength = len(stringIn)

for i in range(stringInLength):
	if (stringIn[i] == "H"):
		hFlip(defaultArr)
	elif(stringIn[i] == "V"):
		vFLip(defaultArr)

print(str(defaultArr[0]) + " " + str(defaultArr[1]))
print(str(defaultArr[2]) + " " + str(defaultArr[3]))
