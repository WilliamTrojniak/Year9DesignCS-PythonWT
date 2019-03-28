import tkinter as tk
root = tk.Tk()

x = "male"

rBttnM = tk.Radiobutton(root, text = "Male", variable = x, value = "male")
rBttnF = tk.Radiobutton(root, text = "Female", variable = x, value = "female")

rBttnM.pack()
rBttnF.pack()



root.mainloop()