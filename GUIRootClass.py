import tkinter as tk #Accessing tkinter module and use tk to call it


class Display:

	def __init__(self):

		#Initialize all variables
		x1 = 0
		x2 = 0
		y1 = 0
		y2 = 0
		rise = 0
		run = 0
		outputText = ""


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
		self.simplifyFraction(rise, run)
		self.outputToTextBox()

	def outputToTextBox(self):
		print("outputToTextBox run")
		self.outputBox.config(state = "normal")
		self.outputBox.delete('1.0', '100.0')
		self.outputBox.insert('1.0',outputText)
		self.outputBox.config(state = "disable")

	def compileRiseRunString(self):
		print("compileRiseRunString run")
		outputText = "Slope = "+ str(rise)+"/"+str(run)+"."

	def simplifyFraction(self, num, denom):
		print("simplifyFraction run")
		
		cycle = "true"
		while(cycle == "true"):	
			divider = 1
			if(num % 13 == 0 and denom % 13 == 0 ):
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
		rise = num
		run = denom


	def calculateRiseRun(self):
		print("calculateRiseRun run")
		rise = y2 - y1
		run = x2 - x1


	def storeInput(self):
		print("storInput run")
		x1 = int(self.entryx1.get())
		y1 = int(self.entryy1.get())
		x2 = int(self.entryx2.get())
		y2 = int(self.entryy2.get())


d = Display() #Constructs a display object