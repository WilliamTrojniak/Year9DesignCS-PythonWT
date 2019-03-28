import tkinter as tk#tkinter is a module that holds code

root = tk.Tk()

x = tk.StringVar(root)
x.set("one")

oMenu = tk.OptionMenu(root,x, "one", "two", "three")

oMenu.pack()

#Sets up program in infinate loop waiting for user
#to do something. This is an EVENT DRIVEN PROGRAM
root.mainloop()
