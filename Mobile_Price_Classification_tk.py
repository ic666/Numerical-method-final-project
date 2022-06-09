#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import csv
from tkhtmlview import HTMLLabel


# In[137]:


root= tk.Tk()
root.title('Mobile Price Classification')
root.geometry('550x500')

def ssss(): 
    root = tk.Tk()
    with open("C:/Users/user/OneDrive/桌面/期末專題_E94076144_陳彥安/ssss.csv", newline = "") as file:
        reader = list(csv.reader(file))
        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tk.Label(root, width = 20, height = 5, text = row, relief = tk.RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1
    root.wm_title("難道阿扁錯了嗎")
    root.mainloop()

def ssss_h():
    root = tk.Tk()
    with open("C:/Users/user/OneDrive/桌面/期末專題_E94076144_陳彥安/ssss_h.csv", newline = "") as file:
        read = csv.reader(file)
        r = 0
        for col in read:
            c = 0
            for row in col:
                label = tk.Label(root, width = 20, height = 5, text = row, relief = tk.RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1
    root.wm_title("我看你是很勇喔")
    root.mainloop()
    
def info():
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.pack(fill=BOTH, expand=1)
            load = Image.open("C:/Users/user/OneDrive/桌面/期末專題_E94076144_陳彥安/圖片1.png")
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=0)

    root = Toplevel() 
    app = Window(root)
    root.wm_title("好了啦特哥椅子哥")
    root.geometry("425x600")
    root.mainloop()
    
def report():    
    root = Tk()
    root.geometry("200x100")
    my_label = HTMLLabel(root, html="""<a href='C:/Users/user/OneDrive/桌面/期末專題_E94076144_陳彥安/training_report.html'>JUST CLICK!</a>""")
    my_label.pack(pady=40, padx=40)
    root.wm_title("放顆西瓜也會贏")
    root.mainloop()
    
title = "Mobile Price Classification"
a = "Context"
b = "Bob has started his own mobile company and wanna to give fight to big companies like Apple :o"
c = "He wants to find out some relation between features of a mobile phone and its selling price 0.0 " 

Label(root,text= title ,font=("Arial", 20)).place(x=80,y=10)  
Label(root,text= a ,font=("Arial", 16)).place(x=190,y=50)  
Label(root,text= b ,font=('Calibri',10)).place(x=10,y=80)  
Label(root,text= c ,font=('Calibri',10)).place(x=10,y=100)  

Label(root,text= "DATA EDA",font=("Arial", 16)).place(x=175,y=150)  

Label(root,text= "Get an overview of the data we have,\n in order to do more complicated and thorough analysis to it :)",font=('Calibri',10)).place(x=40,y=190)

Button(root,text='train info',activebackground="black",command=info,activeforeground="white").place(x=140,y=250)
Button(root,text='train report',activebackground="black",command=report,activeforeground="white").place(x=240,y=250)

Label(root,text= "MODELS",font=("Arial", 16)).place(x=185,y=290)

Label(root,text="Training the model with a set of data \n so that the model can use to reason about the data and learn from it :)",font=('Calibri',10)).place(x=40,y=330)

Button(root,text='all 21 features',activebackground="black",command=ssss,activeforeground="white").place(x=120,y=390)
Button(root,text='high corr. features',activebackground="black",command=ssss_h,activeforeground="white").place(x=220,y=390)

d = "Thank you to the handsome Professor You and the friendly teaching assistants!"

Label(root,text= d ,font=('Script',16)).place(x=50,y=450) 

root.mainloop()


# In[ ]:




