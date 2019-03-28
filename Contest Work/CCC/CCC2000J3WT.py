q = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

machineState = 0
ctr = 0


while q > 0:
	if(machineState == 0):
		machineState = 1
		q -= 1
		m1 += 1
		if(m1 == 35):
			m1 = 0
			q += 30


	elif(machineState == 1):
		machineState = 2
		q -= 1
		m2 += 1
		if(m2 == 100):
			m2 = 0
			q += 60
	else:
		machineState = 0
		q -= 1
		m3 += 1
		if(m3 == 10):
			m3 = 0
			q += 9
	ctr += 1
print("Martha plays " + str(ctr)+" times before going broke.")
