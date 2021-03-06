import tkinter as tk #Accessing tkinter module and use tk to call it
import os

class Display:

	def __init__(self):

		#Initialize all variables
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		self.rise = 0
		self.run = 0
		self.outputText = "Default"


		#Setup GUI
		print("Running Constructor")
		self.root = tk.Tk()

		#Step 1: Create an instance of the widget
		self.labelx1 =  tk.Label(self.root, text = "x1")
		self.entryx1 = tk.Entry(self.root)
		self.labely1 =  tk.Label(self.root, text = "y1")
		self.entryy1 = tk.Entry(self.root)
		self.labelx2 =  tk.Label(self.root, text = "x2")
		self.entryx2 = tk.Entry(self.root)
		self.labely2 =  tk.Label(self.root, text = "y2")
		self.entryy2 = tk.Entry(self.root)
		self.buttonCompute = tk.Button(self.root, text = "Compute", command = self.buttonComputeClicked)
		self.outputBox = tk.Text(self.root, width = 50, height = 14)
		self.outputBox.config(state = "disable")

		#Step 2: Pack the widget
		self.labelx1.pack()
		self.entryx1.pack()
		self.labely1.pack()
		self.entryy1.pack()
		self.labelx2.pack()
		self.entryx2.pack()
		self.labely2.pack()
		self.entryy2.pack()
		self.buttonCompute.pack()
		self.outputBox.pack()

		self.root.mainloop()
		print("DONE")

	def buttonComputeClicked(self):
		self.storeInput()
		self.calculateRiseRun()
		self.simplifyFraction(self.rise, self.run)
		self.compileRiseRunString()
		self.outputToTextBox()

	def outputToTextBox(self):
		print("outputToTextBox run")
		print("outputText:", self.outputText)
		self.outputBox.config(state = "normal")
		self.outputBox.delete('1.0', '100.0')
		self.outputBox.insert('1.0', self.outputText)
		self.outputBox.config(state = "disable")

		#Say the text in output box
		os.system("say " + self.outputText)

	def compileRiseRunString(self):
		print("compileRiseRunString run")
		if(self.run == 0 and self.rise != 0):
			self.outputText = "Slope: Completely verticle"
		elif((self.run == 1)):
			self.outputText = ("Slope: " + str(self.rise))
		elif(self.run == -1 and self.rise > 0):
			self.outputText = ("Slope: " + str(-1 * self.rise))
		elif(self.run != 0 and self.rise == 0):
			self.outputText = "Slope: Completely horizontal"
		elif(self.run < 0 and self.rise < 0):
			self.outputText = ("Slope: "+ str(self.rise) + "/" + str(self.run))
		elif(self.run == 0 and self.rise == 0):
			self.outputText = ("Please enter different points to calculate slope")
		else:
			self.outputText = ("Slope: "+ str(self.rise) + "/" + str(self.run))

		if(self.rise % 1 == 0 and self.run %1 == 0):
			self.outputText = self.outputText.replace(".0","")
		if(self.rise < 0 and self.run < 0):
			self.outputText = self.outputText.replace("-","")
		elif((self.run < 0 and self.rise > 0) and (self.run != -1)):
			self.outputText = self.outputText.replace("-", "")
			self.outputText = self.outputText.replace("Slope: ","Slope: -")
			 

	def simplifyFraction(self, num, denom):
		print("simplifyFraction run")
		
		cycle = "true"
		while(cycle == "true"):	
			divider = 1
			if(denom == 0 or num == 0):
				cycle = "false"
			elif(num % 13 == 0 and denom % 13 == 0 ):
				divider = 13
			elif(num % 11 == 0 and denom % 11 == 0):
				divider = 11
			elif(num % 7 == 0 and denom % 7 == 0):
				divider = 7
			elif(num % 5 == 0 and denom % 5 == 0):
				divider = 5
			elif(num % 3 == 0 and denom % 3 == 0):
				divider = 3
			elif(num % 2 == 0 and denom % 2 == 0):
				divider = 2
			else:
				cycle = "false"

			num = num / divider
			denom = denom / divider
		self.rise = num
		self.run = denom


	def calculateRiseRun(self):
		print("calculateRiseRun run")
		self.rise = self.y2 - self.y1
		self.run = self.x2 - self.x1

	def storeInput(self):
		print("storInput run")
		self.x1 = float(self.entryx1.get())
		self.y1 = float(self.entryy1.get())
		self.x2 = float(self.entryx2.get())
		self.y2 = float(self.entryy2.get())


d = Display() #Constructs a display object