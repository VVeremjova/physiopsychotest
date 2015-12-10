import Tkinter
import tkMessageBox
from admin.saveInDB import SaveInDB

import ConfigParser


class  AdminVisualPart(Tkinter.Tk):
    """docstring for  AdminVisualPart"""
    def __init__(self, parent,user_name):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent

        config = ConfigParser.RawConfigParser()
        config.read('format.ini')
        self.db_name = config.get('Main', 'db_name')
        self.showFields(user_name)

    def showFields(self,user_name=""):

        self.lbl_name = Tkinter.Label(self, text = "User name:")
        self.lbl_name.pack()
        self.entry_name = Tkinter.Entry(self)
        self.entry_name.insert(0,user_name)
        self.entry_name.pack()
      
        self.lbl_id = Tkinter.Label(self, text = "Identifier:")
        self.lbl_id.pack()
        self.entry_id = Tkinter.Entry(self)
        self.entry_id.pack()

        self.lblsex = Tkinter.Label(self, text = "Gender:")
        self.lblsex.pack()
        # self.checkSex = Tkinter.IntVar()
        # R1 = Tkinter.Radiobutton(self, text="Male", variable=self.checkSex, value=1,
        #           command=self.selectedSex)
        # R2 = Tkinter.Radiobutton(self, text="Female", variable=self.checkSex, value=2,
        #           command=self.selectedSex)
        # R1.pack( anchor = Tkinter.W )
        # R2.pack( anchor = Tkinter.W )
        self.entry_sex = Tkinter.Entry(self)
        self.entry_sex.pack()


        self.lbl_birthday = Tkinter.Label(self, text = "Birthday:")
        self.lbl_birthday.pack()
        self.entry_birthday = Tkinter.Entry(self)
        self.entry_birthday.pack()
        self.lbl_occupation = Tkinter.Label(self, text = "Occupation:")
        self.lbl_occupation.pack()

        self.entry_occupation = Tkinter.Entry(self)
        self.entry_occupation.pack()
        # self.entry1.grid(column=1,row=1,columnspan=1)

        self.lbl_expirience = Tkinter.Label(self, text = "Overall experience (years):")
        self.lbl_expirience.pack()

        self.entry_expirience = Tkinter.Entry(self)
        self.entry_expirience.pack()
        self.lbl_lastexp = Tkinter.Label(self, text = "Work experience in the last positions (years):")
        self.lbl_lastexp.pack()

        self.entry_lastexp = Tkinter.Entry(self)
        self.entry_lastexp.pack()

        self.lbl_comment = Tkinter.Label(self, text = "Comments:")
        self.lbl_comment.pack()

        self.entry_comment = Tkinter.Entry(self)
        self.entry_comment.pack()

        BSave = Tkinter.Button(self, text ="Save", command = self.save)
        BSave.pack(side = Tkinter.RIGHT)

        BUpdate = Tkinter.Button(self, text ="Update", command = self.updateFields)
        BUpdate.pack(side = Tkinter.LEFT)

    def save(self):
        # tkMessageBox.showinfo( "Demo", "Will save new user")
        db = SaveInDB(self.db_name)
        name =  self.entry_name.get()
        id_ = self.entry_id.get()

        gender = self.entry_sex.get()
        date_age = self.entry_id.get()
        occupation = self.entry_id.get()
        work_experience = self.entry_id.get()
        last_work_experience = self.entry_id.get()
        comments = self.entry_id.get()
        # db.addNewClient()
      
        db.addNewClient(id_, name, gender, date_age, occupation,work_experience,last_work_experience,comments)
        db.close()

    # def UpdateFields(self,user_name="",id_,gender,date_age,occupation,work_experience,last_work_experience,comments):
    def updateFields(self,user_name,id_,gender,date_age,occupation,work_experience,last_work_experience,comments):
        pass
        # db = SaveInDB(self.db_name)
        # values = db.searchClient(user_name)
        # if values==None :
        #     tkMessageBox.showinfo( "Error", "User not found")
        # else:
        #     print values
        # db.close()

# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
#                   command=sel)
# R1.pack( anchor = W )

# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                   command=sel)
# R2.pack( anchor = W )

# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                   command=sel)
# R3.pack( anchor = W)

# label = Label(root)
# label.pack()