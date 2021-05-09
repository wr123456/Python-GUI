#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import filedialog, BOTH, HORIZONTAL, ttk, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from tkinter.ttk import Notebook,Frame,Button
import os
import os.path

#image OPENED
global openedImage
#image for CONTOUR
global filter_image

class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("图片处理")
        self.init_window_name.geometry('1068x681+10+10')
        self.button1 = tkinter.Button(self.init_window_name, text='File Open', command=self.openfile).grid(row=1, columnspan = 1, column = 10)
        self.button2 = tkinter.Button(self.init_window_name, text='File Save', command=self.savefile).grid(row=1, columnspan = 1,column = 13)
        choice = tkinter.StringVar()
        self.choice = ttk.Combobox(self.init_window_name, width=12, textvariable=choice)
        self.choice['values'] = ('CONTOUR', 'ROTATE','RESIZE','SHARPEN')
        self.choice.grid(row=1, column=12)
        self.choice.current(0)  #设置初始显示值，值为元组['values']的下标
        self.choice.config(state='write')  #设为只读模式
        self.button3 = tkinter.Button(self.init_window_name, text='File Transfer', command=self.transferFile).grid(row=1, columnspan = 1,column = 11)

    def openfile(self):
        global openedImage
        openedImage = filedialog.askopenfilename(title='打开文件', filetypes=[('Image', '*.png *.bmp *jpg'),('All Files', '*')])
        print(openedImage)
        img = Image.open(openedImage)
        img.thumbnail((200, 200))
        global tk_image
        tk_image = ImageTk.PhotoImage(img)
        self.left = tkinter.Label(self.init_window_name, image = tk_image, bg = 'white').grid(row = 2, columnspan = 1, column = 14)

    def transferFile(self):
        global openedImage
        img = Image.open(openedImage)
        img.thumbnail((200, 200))
        #需要声明为全局变量才能正确加载
        global filter_image, tk_filter_image
        self.transferMethod = self.choice.get()
        #CONTOUR
        if self.transferMethod == "CONTOUR":
            filter_image = img.filter(ImageFilter.CONTOUR)
            tk_filter_image = ImageTk.PhotoImage(filter_image)
            self.right = tkinter.Label(self.init_window_name, image = tk_filter_image, bg = 'white').grid(row = 2, columnspan = 1,column = 15)
        else:
            messagebox.showerror(title = "错误信息", message = "请选择图片处理方式")
        print("done")

    def savefile(self):
        global openedImage
        save_name = os.path.split(openedImage)[-1].split('.')[0] + '_CONTOUR'
        r = filedialog.asksaveasfilename(title='保存文件', filetypes=[('*.png *.bmp *jpg')], initialdir='D:\Download', initialfile= save_name + '.png')
        print(r)

def gui_start():
    init_window = tkinter.Tk()
    WINDOW = MY_GUI(init_window)
    WINDOW.set_init_window()
    init_window.mainloop()

if __name__ == '__main__':
    gui_start()