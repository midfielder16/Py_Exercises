from tkinter import *

root = Tk()

def leftClick(event):
	print("Left")

def middleClick(event):
	print("Mid")

def rightClick(event):
	print("Right")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", rightClick)
frame.bind("<Button-3>", middleClick)
frame.pack()


root.mainloop()