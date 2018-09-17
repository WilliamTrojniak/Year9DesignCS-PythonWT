print("Slope Calculator")

#Input
#Point 1
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
#Point 2
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

#Process
#Calculate slope
rise = (y2 - y1) 
run = (x2 - x1)
m = rise/run
#Output
#Print the slope
print("The slope of your line is: ", rise, "/", run)
print("Or: ", m)
