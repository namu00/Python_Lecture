from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def displayImage():
    pass

def func_open():
    pass

def func_save():
    pass

def func_exit():
    pass

def func_zoomin():
    pass

def func_zoomout():
    pass

def func_mirror1():
    pass

def func_mirror2():
    pass

def func_rotate():
    pass

def func_bright():
    pass

def func_dark():
    pass

def func_blur():
    pass

def func_embo():
    pass

def func_bw():
    pass

# global variable
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

window = Tk()
window.geometry("250x250")
window.title('mini photoshop')

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=func_open)
fileMenu.add_command(label='Save', command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label='Quit', command=quit)

image1Menu=Menu(mainMenu)
mainMenu.add_cascade(label='Image Op(1)', menu=image1Menu)
image1Menu.add_command(label='Zoom in', command=func_zoomin)
image1Menu.add_command(label='Zoom out', command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label='Mirror (Up/Down)', command=func_mirror1)
image1Menu.add_command(label='Mirror (Left/Right)', command=func_mirror2)
image1Menu.add_command(label='Rotate', command=func_rotate)


image2Menu=Menu(mainMenu)
mainMenu.add_cascade(label='Image Op(2)', menu=image2Menu)
image2Menu.add_command(label='Bright', command=func_bright)
image2Menu.add_command(label='Dark', command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label='Blur', command=func_blur)
image2Menu.add_command(label='Embo', command=func_embo)
image2Menu.add_separator()
image2Menu.add_command(label='Gray', command=func_bw)

window.mainloop()