import tkinter as tk#tkinter is a module that holds code


#Root is variable holding information
#About the main window.
root = tk.Tk()

textOut = ""


ent = tk.Entry(root)
btn = tk.Button(root, text = "Press Me")
label = tk.Label(root, text = "...")

#Use grid geometry manager to pack widgets more controllably
ent.grid(row = 0, column = 0)
btn.grid(row = 0, column = 1)
label.grid(row = 1, column = 0, columnspan = 2)

#Sets up program in infinate loop waiting for user
#to do something. This is an EVENT DRIVEN PROGRAM
root.mainloop()



def btnClicked():
	textIn = ent.get()
	for i in range(textIn.length-1, -1, -1):
		textOut = textOut + textIn[i]
	label.config(text = textOut)
btn.config(command = btnClicked)



