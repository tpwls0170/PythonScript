import tkinter as t1
from tkinter import *
from tkinter import ttk
window = t1.Tk()

window.geometry("1000x700")
window.title("Intern Serch")
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='검색')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='메일')
tabControl.pack(expand=1, fill="both")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='위치')
tabControl.pack(expand=1, fill="both")

Serch = ttk.LabelFrame(tab1,text='정보검색')
Serch.grid(row=1,column=0)

l1 = Label(Serch, text="직종")
l2 = Label(Serch, text="지역")
l3 = Label(Serch, text="학력")
l1.grid(row=0, column=0)
l2.grid(row=0, column=2)
l3.grid(row=0, column=4)

e1 = Entry(Serch)
e2 = Entry(Serch)
e3 = Entry(Serch)
e1.grid(row=0, column=1)
e2.grid(row=0, column=3)
e3.grid(row=0, column=5)

b1 = Button(Serch, text="검색")
b1.grid(row=1, column=0)

SerchInfo = ttk.LabelFrame(tab1,text='회사목록')
SerchInfo.grid(row=2,column=0)
l1 = Label(SerchInfo, text="직종")
l2 = Label(SerchInfo, text="지역")
l3 = Label(SerchInfo, text="학력")
l1.grid(row=0, column=0)
l2.grid(row=0, column=2)
l3.grid(row=0, column=4)
window.mainloop()
