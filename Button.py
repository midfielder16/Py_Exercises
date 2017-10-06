from tkinter import *
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.button = Button(frame,
			                 text='QUIT',
			                 fg='red',
			                 command=quit)
		self.button.pack(side=LEFT)
		self.slogan = Button(frame,
			                 text='hello',
			                 command=self.write_slogan)
		self.slogan.pack(side=LEFT)
	def write_slogan(self):
	    print("tkinter is so easy")

root = Tk()
app = App(root)
root.mainloop()	    	