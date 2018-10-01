#Loops run sections of code multiple times

#Two broad categories
#Conditional: Loops while something is true
#Counted: Loops set number of times

print("Manual")
print("1")
print("2")
print("3")
print("4")
print("5")
print("*********************")

print("Counted Loop")
#Counted loop
for i in range(0, 5, 1):
	print(i+1)

print("*********************")

print("Conditional Loop")
#Conditional Loop
t = 0
while(t < 5):
	print(t+1)
	t = t+1
