from tkinter import *

root = Tk()

v = IntVar()

Label(root, text = "Choose a pro language",
	  padx = 20).pack()
Radiobutton(root,
	        text="Python",
	        variable=v,
	        value=1).pack(anchor=W)
Radiobutton(root,
	        text="C",
	        variable=v,
	        value=2).pack(anchor=W)

root.mainloop()