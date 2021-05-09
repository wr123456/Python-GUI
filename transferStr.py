#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import hashlib
import time
from PIL import Image, ImageTk

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=2)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        # self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        # self.str_trans_to_md5_button.grid(row=1, column=11)
        #清空按钮
        self.delete_input_window = Button(self.init_window_name, text="清空输入", bg="lightblue", width=10, command=self.delete_input_window)
        self.delete_input_window.grid(row=2, column=11)
        self.change_background = Button(self.init_window_name, text="更换背景", bg="lightblue", width=10, command=self.change_background)
        self.change_background.grid(row=3, column=11)
        #更换背景
        color = StringVar()
        self.background = ttk.Combobox(self.init_window_name, width=12, textvariable=color)
        self.background['values'] = ('pink', 'blue','red','green')
        self.background.grid(row=4, column=11)
        self.background.current(0)  #设置初始显示值，值为元组['values']的下标
        self.background.config(state='write')  #设为只读模式
        #大小写转换
        self.toUpper = Button(self.init_window_name, text="转换大小写", bg="lightblue", width=10, command=self.toUpper)
        self.toUpper.grid(row=1, column=11)
        #加载图片
        # img = Image.open('D:\Project.png')
        # photo = ImageTk.PhotoImage(img)
        # self.imgLable = Label(self.init_window_name, image = photo)
        # self.imgLable.grid(row = 10, column = 11)
    #清空输入框
    def delete_input_window(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n","").encode()
        if src:
            self.init_data_Text.delete(1.0, END)
            self.result_data_Text.delete(1.0, END)
            self.write_log_to_Text("INFO:clear input successful")
        else:
            self.write_log_to_Text("INFO:input is already empty")
    #更换背景
    def change_background(self):
        background_color = self.background.get()
        if background_color:
            self.init_window_name["bg"] = background_color
        else:
            self.write_log_to_Text("INFO: Please select a color")
    #功能函数
    # def str_trans_to_md5(self):
    #     src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
    #     #print("src =",src)
    #     if src:
    #         try:
    #             myMd5 = hashlib.md5()
    #             myMd5.update(src)
    #             myMd5_Digest = myMd5.hexdigest()
    #             #print(myMd5_Digest)
    #             #输出到界面
    #             self.result_data_Text.delete(1.0,END)
    #             self.result_data_Text.insert(1.0,myMd5_Digest)
    #             self.write_log_to_Text("INFO:str_trans_to_md5 success")
    #         except:
    #             self.result_data_Text.delete(1.0,END)
    #             self.result_data_Text.insert(1.0,"字符串转MD5失败")
    #     else:
    #         self.write_log_to_Text("ERROR:str_trans_to_md5 failed")
    #小写转换为大写
    def toUpper(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n","").encode()
        if src:
            try:
                myUpper = src.upper()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myUpper)
                self.write_log_to_Text("INFO:transfer to upper chars success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"大小写转换失败")
        else:
            self.write_log_to_Text("Error: transfer to upper chars failed")

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示




gui_start()