from tkinter import *

root = Tk()

lab = Label(root, text="Data dX:", font="Arial 12") #txt
fra_print_dX = Frame(root,width=500,height=100,bg="darkred") #corect delt data

labC = Label(root, text="Control Panel:", font="Arial 12") #txt2
fra_control = Frame(root,width=500,height=150,bg="darkblue")

lab2 = Label(root, text="Data X:", font="Arial 12") #txt2
fra_print_X = Frame(root,width=500,height=100,bg="red") #corect now data


def onClickClearD(event):
    print("onClickClearD() = ")
def onClickT(event):
    print("onClickT() = ")
def onClickF(event):
    print("onClickF() = ")
def onClickHelp(event):
    print("onClickHelp()")
    win = Toplevel(root, relief=SUNKEN, bd=10, bg="lightblue")
    win.title("Help window")
    win.minsize(width=400, height=200)

butClear = Button(fra_control,
          text="this is button for clear data!",
          width=30,height=5,
          bg="white",fg="blue")
butClear["text"] = "Clear"
butClear.bind("<Button-1>", onClickClearD)


butT= Button(fra_control,
          text="this is button for clear data!",
          width=15,height=5,
          bg="darkgreen",fg="blue")
butT["text"] = "True"
butT.bind("<Button-1>", onClickT)

butF= Button(fra_control,
          text="this is button for clear data!",
          width=15,height=5,
          bg="darkred",fg="blue")
butF["text"] = "False"
butF.bind("<Button-1>", onClickF)

butHelp= Button(root,
          text="this is button for clear data!",
          width=13,height=3,
          bg="green",fg="blue")
butF["text"] = "Help"
butF.bind("<Button-1>", onClickHelp)


lab.pack()
fra_print_dX.pack()

labC.pack()

fra_control.pack()
butClear.pack()
butT.pack()
butF.pack()

lab2.pack()
fra_print_X.pack()


def exit_(event):
    root.destroy()
root.bind('<Control-z>',exit_)
root.bind('<space>',onClickClearD)
root.bind('c',onClickT)
root.bind('h',onClickHelp)
root.bind('v',onClickF)
root.mainloop()

#TODO: OOP, integr. leap, .db...
#http://younglinux.info/book/export/html/48