import tkinter as tk #Accessing tkinter module and use tk to call it


class Display:

	def __init__(self):
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
		self.buttonCompute = tk.Button(self.root, text = "Compute", command = self.storeInput)
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

	def outputToTextBox(self, rise, run):
		self.outputBox.config(state = "normal")
		self.outputBox.delete('1.0', '100.0')
		self.outputBox.insert('1.0',"Slope = "+ str(rise)+"/"+str(run)+".")
		self.outputBox.config(state = "disable")


	def calculateRiseRun(self, x1,  y1,  x2,  y2):
		rise = y2 - y1
		run = x2 - x1

		self.outputToTextBox(rise, run)
		

	def storeInput(self):
		print("Calculating Slope")
		x1 = int(self.entryx1.get())
		y1 = int(self.entryy1.get())
		x2 = int(self.entryx2.get())
		y2 = int(self.entryy2.get())

		self.calculateRiseRun(x1, y1, x2, y2)

	

	

d = Display() #Constructs a display object