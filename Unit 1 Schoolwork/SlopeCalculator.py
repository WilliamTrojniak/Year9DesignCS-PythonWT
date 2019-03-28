print("Slope Calculator")

takeInput = "true"

#Input
while(takeInput == "true"):
	#Point 1
	x1 = (input("Enter x1: "))
	y1 = (input("Enter y1: "))
	#Point 2
	x2 = (input("Enter x2: "))
	y2 = (input("Enter y2: "))
	if(type(x1) == "int" and type(x2) == "int" and type(y2) == "int" and type(y2) == "int"):
		takeInput = "false"
	else:
		print("Please reenter all points as valid whole numbers")



#Process
#Calculate slope
rise = (y2 - y1) 
run = (x2 - x1)
m = rise/run
#Output
#Print the slope
print("The slope of your line is: "+ str(rise)+ "/"+ str(run))
print("Or:", m)
