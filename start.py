from Tkinter  import *
import tkMessageBox
import test.TestWindow



def is_programm_ready(is_ready):
	program_is_ready="program is not ready"
	if is_ready:
		program_is_ready="program is ready"
	L2 = Label(top, text=program_is_ready)
	L2.pack( side = RIGHT)

def startTesting():
	test.TestWindow.TestWindow(None)



top = Tk()

L1 = Label(top, text="Print User Name")
L1.pack( side = LEFT)


E1 = Entry(top, bd =5)
# E2 = Entry(top, bd =10)

E1.pack(side = LEFT)
# E2.pack(side = LEFT)

def helloCallBack():
   tkMessageBox.showinfo( "Start testing programm", "Here will move to testing part")

def about():
   tkMessageBox.showinfo( "About", "version 0.0.0")

B = Button(top, text ="Start testing", command = startTesting)
B2 = Button(top, text ="About", command = about)
B3 = Button(top, text ="Reda", command = about)
B.pack()
B2.pack(side = BOTTOM)
top.mainloop()

