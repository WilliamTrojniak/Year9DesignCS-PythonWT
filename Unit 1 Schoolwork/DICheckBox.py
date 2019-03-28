import tkinter as tk
root = tk.Tk()

x = 0

cBttn = tk.Checkbutton(root, text = "On/Off", variable = x)
cBttn.pack()

root.mainloop()