#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Notebook,Frame,Button

global isStart
class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("互动窗口")
        self.init_window_name.geometry('300x300+10+10')
        self.button1 = tkinter.Button(self.init_window_name, text='开始？', command=self.startInteraction)
        #self.button1.grid(row=2, column = 11)
        self.button1.pack()
        self.button2 = tkinter.Button(self.init_window_name, text='第一个问题', command=self.chooseFlower)
        self.button2.pack()
        #self.button2.grid(row=2, column = 12)
        self.button3 = tkinter.Button(self.init_window_name, text='第二个问题', command=self.likeMe)
        self.button3.pack()

    def startInteraction(self):
        isStart = messagebox.askyesno(title = "开始咯", message = "准备好了吗？")
        while isStart == False:
            messagebox.showinfo(title = "开始", message = "看来您还没准备好呢，再想想哦？")
            isStart = messagebox.askyesno(title = "开始咯", message = "准备好了吗？")
        messagebox.showinfo(title = "开始", message = "开始！")
    
    def chooseFlower(self):
        flowers = ['玫瑰', '百合', '郁金香', '康乃馨','菊花']
        isCorrect = False
        for flower in flowers:
            isCorrect = messagebox.askyesno(title = "选花界面", message = "你喜欢" + flower + "?")
            if isCorrect == True:
                messagebox.showinfo(title = "选花结果", message = "看来我有点懂你呢！")
                break
        if isCorrect == False:
            messagebox.showinfo(title = "选花结果", message = "好吧，我选择放弃！")
    
    def likeMe(self):
        isLike = messagebox.askyesno(title = "问答界面", message = "你喜欢我吗？")
        while isLike == False:
            isLike = messagebox.showerror(title = "回答结果", message = "回答错误，重来")
            isLike = messagebox.askyesno(title = "问答界面", message = "你喜欢我吗？")
        if isLike == True:
            messagebox.showinfo(title = "回答结果", message = "回答正确！")

def gui_start():
    init_window = tkinter.Tk()
    WINDOW = MY_GUI(init_window)
    WINDOW.set_init_window()
    init_window.mainloop()

if __name__ == '__main__':
    gui_start()