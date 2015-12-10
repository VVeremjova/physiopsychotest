from Tkinter  import *
import tkMessageBox
import test.TestWindow
import admin.AdminVisual

from admin.saveInDB import SaveInDB

import ConfigParser

class Start(Tk):
    def is_programm_ready(self,start_program): 
        program_is_ready="program is not ready"
        if start_program:
            program_is_ready="program is ready"
        L2 = Label(self, text=program_is_ready)
        L2.pack( side = RIGHT)

    def startTesting(self):
        test.TestWindow.TestWindow(None)

    def helloCallBack(self):
       tkMessageBox.showinfo( "Start testing programm", "Here will move to testing part")

    def about(self):
       tkMessageBox.showinfo( "About", "version 0.0.0")

    def startTestingDemo(self):
       tkMessageBox.showinfo( "Demo", "Will show how use this program")

    def updateUserInDB(self):
        db = SaveInDB(self.db_name)

        name_field = self.user_name
        new_name = name_field.get()
        if db.searchClient(new_name)==None :
            tkMessageBox.showinfo( "Error", "User not found")
        else:
            tkMessageBox.showinfo( "Ok", "User found")
        db.close()

    def goToAdmin(self):
        name_field = self.user_name
        new_name = name_field.get()

        admin.AdminVisual.AdminVisualPart(None,new_name)
      

    def __init__(self, parent,is_programm_ready, db):
        Tk.__init__(self,parent)
        self.parent = parent 

        self.db_name= db   
        self.is_programm_ready(is_programm_ready)
        lbl_user_name = Label(self, text="User Name")
        lbl_user_name.pack( side = LEFT)
        self.user_name = Entry(self, bd =5)
        self.user_name.pack(side = LEFT)
        B = Button(self, text ="Start testing", command = self.startTesting)
        B0 = Button(self, text ="Update user", command = self.updateUserInDB)
        B1 = Button(self, text ="Demo", command = self.startTestingDemo)
        B2 = Button(self, text ="About", command = self.about)
        B3 = Button(self, text ="Add new user", command = self.goToAdmin)

        B.pack()
        B0.pack()
        B1.pack(side = BOTTOM)
        B2.pack(side = BOTTOM)
        B3.pack(side = BOTTOM)
        self.mainloop()

