from tkinter import *
root =Tk()

one = Label(root, text = 'One', bg='blue', fg='white')
one.pack()
two = Label(root, text = 'Two', bg='red', fg='black')
two.pack(fill=X)
three = Label(root, text = 'Three', bg='yellow', fg='green')
three.pack(side=LEFT, fill=Y)

root.mainloop()