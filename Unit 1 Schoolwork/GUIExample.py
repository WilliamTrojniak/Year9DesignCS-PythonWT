import tkinter as tk

class Display:
	def __init__(self):
		print("running")
		#Step 0: Setup GUI
		self.root = tk.Tk()

		#Step 1: Create an instance of the widgets
		self.titleLabel = tk.Label(self.root, text = "PASSWORD GENERATOR", font = ("Helvetica", 16), background = "yellow", foreground = "blue")
		self.outText = tk.Text(self.root, height = 10, width = 50)
		self.wrd1Label = tk.Label(self.root, text = "Word 1")
		self.wrd2Label = tk.Label(self.root, text = "Word 2")
		self.wrd3Label = tk.Label(self.root, text = "Word 3")
		self.wrd1Entr = tk.Entry(self.root)
		self.wrd2Entr = tk.Entry(self.root)
		self.wrd3Entr = tk.Entry(self.root)
		self.goBttn = tk.Button(self.root, text = "GO!", command = self.bttnClicked)

		#Step 2: Pack/Initialize the widgets
		self.titleLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")
		self.outText.grid(row = 1, column = 0, columnspan = 2)
		self.wrd1Label.grid(row = 2, column = 0)
		self.wrd2Label.grid(row = 3, column = 0)
		self.wrd3Label.grid(row = 4, column = 0)
		self.wrd1Entr.grid(row = 2, column = 1)
		self.wrd2Entr.grid(row = 3, column = 1)
		self.wrd3Entr.grid(row = 4, column = 1)
		self.goBttn.grid(row = 5, column = 1, sticky = "NESW", padx = 50)

		#Step 3: Initialize window
		self.root.mainloop()
	def bttnClicked(self):
		print("Clicked")

d = Display()