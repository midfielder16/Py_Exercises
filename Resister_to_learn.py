import tkinter

class registration(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        #name
        self.labelVariable = tkinter.StringVar()
        self.labelVariable.set(u"Name")
        label1 = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label1.grid(column=0,row=0,columnspan=2, sticky='EW')
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=1, sticky='EW')
        
        #address
        self.labelVariable = tkinter.StringVar()
        self.labelVariable.set(u"Address")
        label2 = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="black")
        label2.grid(column=0,row=2,columnspan=2, sticky='EW')
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=3, sticky='EW')
        
        #phone
        self.labelVariable = tkinter.StringVar()
        self.labelVariable.set(u"Phone number")
        label3 = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="red",bg="green")
        label3.grid(column=0,row=4,columnspan=2, sticky='EW')
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=5, sticky='EW')
        #email
        self.labelVariable = tkinter.StringVar()
        self.labelVariable.set(u"Email address")
        label4 = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="yellow",bg="white")
        label4.grid(column=0,row=6,columnspan=2, sticky='EW')
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=7, sticky='EW')
        #chose_program_language
        label5 = tkinter.Label(self, text="Chose program language you want to learn : ")
        label5.grid(columnspan = 2)
        var1 = tkinter.IntVar()
        self.chose_program_language1 = tkinter.Checkbutton(self,
        	                                              text = "Python",
        	                                              variable = var1).grid(column=0, row=9)
        var2 = tkinter.IntVar()
        self.chose_program_language2 = tkinter.Checkbutton(self,
        	                                              text = "Java",
        	                                              variable = var2).grid(column=0, row=10)
        var3 = tkinter.IntVar()
        self.chose_program_language3 = tkinter.Checkbutton(self,
        	                                              text = "PHP",
        	                                              variable = var3).grid(column=0, row=11)
        var4 = tkinter.IntVar()
        self.chose_program_language4 = tkinter.Checkbutton(self,
        	                                              text = "Perl",
        	                                              variable = var4).grid(column=0, row=12)
        var5 = tkinter.IntVar()
        self.chose_program_language5 = tkinter.Checkbutton(self,
        	                                              text = "C++",
        	                                              variable = var5).grid(column=0, row=13)
        
        #button
        button = tkinter.Button(self, text = "Send", command = self.Confirm)
        button.grid(column = 0, row = 14)
        self.grid_columnconfigure(0, weight = 1)
        self.resizable(True, False)
    def Confirm(self):
        confirm = tkinter.Label(self, text = "Thanks you very much !!!" )
        confirm.grid(column = 0, row = 15, sticky = "EW")
        
if __name__ == "__main__":
    app = registration(None)
    app.title("Resister")
    app.mainloop()
