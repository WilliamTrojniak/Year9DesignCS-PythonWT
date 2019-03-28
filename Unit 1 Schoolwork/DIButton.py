import tkinter as tk
root = tk.Tk()

def hello():
	print ("hello")

bttn = tk.Button(root, text = "Hello", command = hello)
bttn.pack()

root.mainloop()