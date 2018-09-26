import tkinter as tk
import math

class CylinderCalc:

	def __init__(self):#Acts as a start() function

		self.root = tk.Tk()
		self.root.title("Cylinder Calculator")

		self.labR = tk.Label(self.root, text = "radius")
		self.labR.pack();

		self.entR = tk.Entry(self.root)
		self.entR.pack()

		self.labH = tk.Label(self.root, text = "height")
		self.labH.pack()

		self.entH = tk.Entry(self.root)
		self.entH.pack()

		self.btn = tk.Button(self.root, text = "Calculate", command=self.calculateVolume)
		self.btn.pack()

		self.output = tk.Text(self.root, height = 10, width = 50, borderwidth = 3, relief=tk.GROOVE)
		self.output.config(state="disabled")
		self.output.pack()

		self.root.mainloop()

	def calculateVolume(self):

		#INPUT
		r = float(self.entR.get())
		h = float(self.entH.get())

		v = math.pi*r*r*h
		v = round(v,3)
		print(v)

		outputValue = ("Given\nradius: " + str(r) + " units\nheight: " + str(h)+" units\nVolume: " + str(v) + " units cubed."

		self.output.config(state = "normal")
		self.output.insert(tk.INSERT, outputValue)
		self.output.config(state = "disabled")


cylinderCalc = CylinderCalc()