from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

class GUI(Frame):
    def func_open(self):
        pass

    def displayImage(self):
        pass

    def func_save(self):
        pass

    def func_exit(self):
        pass

    def func_zoomin(self):
        pass

    def func_zoomout(self):
        pass

    def func_mirror1(self):
        pass

    def func_mirror2(self):
        pass

    def func_rotate(self):
        pass

    def func_bright(self):
        pass

    def func_dark(self):
        pass

    def func_blur(self):
        pass

    def func_embo(self):
        pass

    def func_bw(self):
        pass

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 250, 250
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)

        self.master = master
        mainMenu = Menu(master)
        master.config(menu=mainMenu)

        fileMenu = Menu(mainMenu)
        mainMenu.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='Open', command=self.func_open)
        fileMenu.add_command(label='Save', command=self.func_save)
        fileMenu.add_separator()
        fileMenu.add_command(label='Quit', command=quit)

        image1Menu = Menu(mainMenu)
        mainMenu.add_cascade(label='Image Op(1)', menu=image1Menu)
        image1Menu.add_command(label='Zoom in', command=self.func_zoomin)
        image1Menu.add_command(label='Zoom out', command=self.func_zoomout)
        image1Menu.add_separator()
        image1Menu.add_command(label='Mirror (Up/Down)', command=self.func_mirror1)
        image1Menu.add_command(label='Mirror (Left/Right)', command=self.func_mirror2)
        image1Menu.add_command(label='Rotate', command=self.func_rotate)

        image2Menu = Menu(mainMenu)
        mainMenu.add_cascade(label='Image Op(2)', menu=image2Menu)
        image2Menu.add_command(label='Bright', command=self.func_bright)
        image2Menu.add_command(label='Dark', command=self.func_dark)
        image2Menu.add_separator()
        image2Menu.add_command(label='Blur', command=self.func_blur)
        image2Menu.add_command(label='Embo', command=self.func_embo)
        image2Menu.add_separator()
        image2Menu.add_command(label='Gray', command=self.func_bw)

root = Tk()
app = GUI(master=root)
app.mainloop()