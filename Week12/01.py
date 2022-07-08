from tkinter import *
from time import *
import glob

fd = "Week12/gif/" #file directory

fnameList = ["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif","jeju5.gif"
             ,"jeju6.gif","jeju7.gif","jeju8.gif","jeju9.gif"]
photoList = [None]*9
num = 0
file = ''

def clickNext():
    global num
    num +=1
    if num > 8:
        num = 0
    file = fd + fnameList[num]
    photo = PhotoImage(file)
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    file = fd + fnameList[num]
    photo = PhotoImage(file)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
window = Tk()
window.geometry("700x500")
window.title("사진 앨법 보기")

btnPrev = Button(window, text = "<<Prev",command = clickPrev)
btnNext = Button(window, text = "Next>>", command = clickNext)
pLabel = Label(window, text = file)

photo = PhotoImage(file = fd + fnameList[0])
pLabel = Label(window,image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()