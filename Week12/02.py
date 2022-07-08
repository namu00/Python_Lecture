from tkinter import *
from tkinter.filedialog import *

def func_open():
    filename = askopenfilename(parent = window,filetypes = (("GIF 파일","*.gif"),
            ("모든 파일","*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def func_exit():
    window.quit()
    window.destroy()
    
window = Tk()
window.geometry("400x400")
window.title("명화 감상")

photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "file Open",command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "quit",command = func_exit)

window.mainloop()