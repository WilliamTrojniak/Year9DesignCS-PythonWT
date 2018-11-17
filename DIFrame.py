import tkinter as tk
root = tk.Tk()

frame = tk.LabelFrame(root, text = "frame 1", padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

entr = tk.Entry(frame)
entr.pack()

root.mainloop()