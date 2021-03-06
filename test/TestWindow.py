import random

from TestManager import TestManager
from TestingWay import TestingWay
from TestingWay1 import TestingWay1
from TestingWay2 import TestingWay2
import Tkinter
import time
import tkMessageBox

from TestingWay import TestingWay

class TestWindow(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.showAll()
        starttest = TestingWay() 
        # starttest.StartTesting()

    def timer(self):
        now = time.localtime(time.time())
        return now[5]

    def getNewValues(self,first,second):
        self.first = first
        self.second = second
        self.label1.config(text=self.first)
        self.label2.config(text=self.second)

    def showAll(self):
        self.label0 = Tkinter.Label(self,
                                    anchor="w", fg="black", bg="white", text=2)
        self.label0.grid(column = 0,row = 1)
        self.label1 = Tkinter.Label(self,
                              anchor="w",fg="white",bg="red", text=TestingWay.GetRandomNumbers("T"))
        self.label1.grid(column=0,row=2)

        self.label2 = Tkinter.Label(self,
                              anchor="w",fg="white",bg="blue", text=TestingWay.GetRandomNumbers("B"))
        self.label2.grid(column=0,row=3)

        self.entry0 = Tkinter.Entry(self)
        self.entry0.grid(column=1,row=1,columnspan=1)
        self.entry1 = Tkinter.Entry(self)
        self.entry1.grid(column=1,row=2,columnspan=1)
        self.entry2 = Tkinter.Entry(self)
        self.entry2.grid(column=1,row=3,columnspan=1)
        self.entry1.bind("<Return>", self.ChangeFocus)
        self.entry2.bind("<Return>", self.OnPressEnter)



    def OnUpdate(self,event):
        self.label0.config(text=self.timer())

    def ChangeFocus(self,event):
        pass

    def OnPressEnter(self,event):
        "Call methods from testingManager and testingWay"
        value1 = self.entry1.get()
        value2 = self.entry2.get()
        print value1
        print value2
        TestingWay._TOP_VALUE = int(value1)
        TestingWay._BOT_VALUE = int(value2)
        # self.starttest.GetTopInputValue(value1)
        # self.starttest.GetBotInputValue(value2)
        print("Top value : " + TestingWay._TOP_INPUT_VALUE.__str__())
        print ("Bot value : " + TestingWay._BOT_INPUT_VALUE.__str__())
        #print TestingWay2.CorrectOutputValues()
        if(self.entry0.get()=="1"):
            TestingWay1.CorrectInputValues()
        else:
            TestingWay2.CorrectInputValues()
        print TestingWay._CORRECT
        print TestingWay._ERRORS_VAL
        print TestingWay._ERRORS_WAY
        self.getNewValues(TestingWay.GetRandomNumbers("T"),TestingWay.GetRandomNumbers("B"))
        print "You pressed enter !"

        
    def TimeFinished(self):
        tkMessageBox.showinfo( "End", "Time of testing is finished.")