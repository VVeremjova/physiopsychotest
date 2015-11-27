from TestManager import TestManager
from TestingWay import TestingWay
import Tkinter
import tkMessageBox

class TestWindow(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.showAll()
        starttest = TestingWay() 
        # starttest.StartTesting()

    def getNewValues(self,first=0,second=0):
        self.first = first
        self.second = second
        self.label1.config(text=self.first)
        self.label2.config(text=self.second)

    def showAll(self):
        self.label1 = Tkinter.Label(self,
                              anchor="w",fg="white",bg="red", text = 5)
        self.label1.grid(column=0,row=1)

        self.label2 = Tkinter.Label(self,
                              anchor="w",fg="white",bg="blue", text = 3)
        self.label2.grid(column=0,row=2)


        self.entry1 = Tkinter.Entry(self)
        self.entry1.grid(column=1,row=1,columnspan=1)
        self.entry2 = Tkinter.Entry(self)
        self.entry2.grid(column=1,row=2,columnspan=1)
        self.entry1.bind("<Return>", self.ChangeFocus)
        self.entry2.bind("<Return>", self.OnPressEnter)




    def ChangeFocus(self,event):
        pass

    def OnPressEnter(self,event):
        "Call methods from testingManager and testingWay"
        value1 = self.entry1.get()
        value2 = self.entry2.get()
        print value1
        print value2

        # self.starttest.GetTopInputValue(value1)
        # self.starttest.GetBotInputValue(value2)

        self.getNewValues(value1,value2)
        print "You pressed enter !"
        
    def TimeFinished(self):
        tkMessageBox.showinfo( "End", "Time of testing is finished.")