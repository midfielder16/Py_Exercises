from tkinter import *

master = Tk()
msg_ = "hello baby this is an important message"
msg = Message(master, text = msg_)
msg.config(bg = "white", fg = "black", font = ('times', 24, 'italic'))
msg.pack()
master.mainloop()