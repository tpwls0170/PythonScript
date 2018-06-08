import tkinter as t1
from tkinter import *
from tkinter import ttk
from tkinter import font
import Job

window = t1.Tk()
textFont = font.Font(window, size=9, family = '맑은 고딕')

def jobSecch():
    select = job.get()#콤보박스에서 얻어옴
    returnList = []
    if select == "경영·사무·금융·보험":
        returnList = Job.ConnectServer("&occupation=01")#job.py 에 보냄
    elif select == '연구 및 공학기술':
        returnList = Job.ConnectServer("&occupation=02")
    for data in Job.dataList:
        companyinfoLabel.insert(INSERT, data)
        companyinfoLabel.insert(INSERT, '\n\n')

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

job = ttk.Combobox(Serch)
job['values'] = ('경영·사무·금융·보험', '연구 및 공학기술', '교육·법률·사회복지·경찰·소방 및 군인', '보건·의료', '예술·디자인·방송·스포츠',
'영업·판매·운전·운송')

local = ttk.Combobox(Serch)
local['values'] = ('서울', '인천', '강원도', '충청도', '전라도', '경상도',)
school =ttk.Combobox(Serch)
school['values'] = ('무관', '2년제', '4년체')

job.grid(row=0, column=1)
local.grid(row=0, column=3)
school.grid(row=0, column=5)

b1 = Button(Serch, text="검색",command = jobSecch)
b1.grid(row=1, column=0)


companyinfo = ttk.LabelFrame(tab1,text='회사목록')
companyinfo.grid(row=2,column=0)
companyinfof = ttk.LabelFrame(companyinfo)
companyinfof.grid(row=2,column=0)
companyinfoLabel = Text(companyinfof , font = textFont,width = 100, height = 100)
companyinfoLabel.grid(row=0,column=0)
window.mainloop()
