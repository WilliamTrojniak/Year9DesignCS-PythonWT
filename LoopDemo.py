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
print("7 to 104, odd numbers inclusive")
for i in range(7, 104, 2):
	print(i)

print("*********************")
print("-22 to 134, even numbers inclusive")
for i in range(-22, 135, 2):
	print(i)

print("*********************")
print("Count down from 100 to 0 by 2")
for i in range(100, -1, -2):
	print(i)

print("*********************")
print("Count down from 101 to 0 inclusive")
for i in range(101, -1, -1):
	print(i)

print("*********************")
s = "Yaba Daba Dooo!"
print("Every character of string")
for i in range((len(s)-1), -1, -1):
	print(s[i])

print("*********************")
s = "Yaba Daba Dooo!"
print("Every other character of string")
for i in range(0, len(s), 2):
	print(s[i])

print("*********************")

print("Conditional Loop")
#Conditional Loop
t = 0
while(t < 5):
	print(t+1)
	t = t+1
