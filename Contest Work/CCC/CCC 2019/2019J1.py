scores = []


for i in range(6):
	scores.append(int(input()))

scoreA = (scores[0]*3) + (scores[1]*2) + scores[2]
scoreB = (scores[3]*3) + (scores[4]*2) + scores[5]

if(scoreA > scoreB):
	print("A")
elif(scoreA < scoreB):
	print("B")
else:
	print("T")