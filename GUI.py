import tkinter as t1
import smtplib
from tkinter import *
from tkinter import ttk
from tkinter import font
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import Job

window = t1.Tk()
textFont = font.Font(window, size=9, family = '맑은 고딕')

def jobSecch():
    select = job.get()#콤보박스에서 얻어옴
    select1 = local.get()
    select2 = school.get()
    returnList = []
    if select == "경영·사무·금융·보험":
        if select1 == "지역무관":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=00000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01","&region=00000","&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01","&region=00000","&education=05")  # job.py 에 보냄
        elif select1 == "서울":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=11000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01","&region=11000","&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01","&region=11000","&education=05")  # job.py 에 보냄
        elif select1 == '인천':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=28000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=05")  # job.py 에 보냄
        elif select1 == '경기':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=41000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=05")  # job.py 에 보냄
        elif select1 == '부산':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=26000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=05")  # job.py 에 보냄
        elif select1 == '제주':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=56000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=56000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=56000", "&education=05")  # job.py 에 보냄
        elif select1 == '대구':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=01","&region=27000","&education=00")#job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=05")  # job.py 에 보냄
    elif select == '연구 및 공학기술':
        if select1 == "지역무관":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=05")  # job.py 에 보냄
        elif select1 == "서울":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=05")  # job.py 에 보냄
        elif select1 == '인천':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=05")  # job.py 에 보냄
        elif select1 == '경기':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=05")  # job.py 에 보냄
        elif select1 == '부산':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=05")  # job.py 에 보냄
        elif select1 == '제주':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=56000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=56000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=56000", "&education=05")  # job.py 에 보냄
        elif select1 == '대구':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=05")  # job.py 에 보냄
    elif select == '교육·법률·사회복지·경찰·소방 및 군인':
        if select1 == "지역무관":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=05")  # job.py 에 보냄
        elif select1 == "서울":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=05")  # job.py 에 보냄
        elif select1 == '인천':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=05")  # job.py 에 보냄
        elif select1 == '경기':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=05")  # job.py 에 보냄
        elif select1 == '부산':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=05")  # job.py 에 보냄
        elif select1 == '제주':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=56000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=56000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=56000", "&education=05")  # job.py 에 보냄
        elif select1 == '대구':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=05")  # job.py 에 보냄
    elif select == '보건·의료':
        if select1 == "지역무관":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=05")  # job.py 에 보냄
        elif select1 == "서울":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=05")  # job.py 에 보냄
        elif select1 == '인천':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=05")  # job.py 에 보냄
        elif select1 == '경기':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=05")  # job.py 에 보냄
        elif select1 == '부산':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=05")  # job.py 에 보냄
        elif select1 == '제주':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=56000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=56000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=56000", "&education=05")  # job.py 에 보냄
        elif select1 == '대구':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=05")  # job.py 에 보냄
    elif select == '예술·디자인·방송·스포츠':
        if select1 == "지역무관":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=05")  # job.py 에 보냄
        elif select1 == "서울":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=05")  # job.py 에 보냄
        elif select1 == '인천':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=05")  # job.py 에 보냄
        elif select1 == '경기':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=05")  # job.py 에 보냄
        elif select1 == '부산':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=05")  # job.py 에 보냄
        elif select1 == '제주':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=56000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=56000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=56000", "&education=05")  # job.py 에 보냄
        elif select1 == '대구':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=05")  # job.py 에 보냄
    elif select == '영업·판매·운전·운송':
        if select1 == "지역무관":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=05")  # job.py 에 보냄
        elif select1 == "서울":
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=05")  # job.py 에 보냄
        elif select1 == '인천':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=05")  # job.py 에 보냄
        elif select1 == '경기':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=05")  # job.py 에 보냄
        elif select1 == '부산':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=05")  # job.py 에 보냄
        elif select1 == '제주':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=56000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=56000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=56000", "&education=05")  # job.py 에 보냄
        elif select1 == '대구':
            if select2 == "학력무관":
                returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=00")  # job.py 에 보냄
            elif select2 == "2년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=04")  # job.py 에 보냄
            elif select2 == "4년제":
                returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=05")  # job.py 에 보냄
    for data in Job.dataList:
        companyinfoLabel.insert(INSERT, data)
        companyinfoLabel.insert(INSERT, '\n\n')

window.geometry("600x700")
window.title("Intern Serch")
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='검색')
tabControl.pack(expand=1, fill="both")

Serch = ttk.LabelFrame(tab1,text='정보검색')
Serch.grid(row=0,column=0)

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
local['values'] = ('지역무관', '서울', '인천', '경기', '부산', '제주', '대구')
school =ttk.Combobox(Serch)
school['values'] = ('학력무관', '2년제', '4년체')
#00 04 05
job.grid(row=0, column=1)
local.grid(row=0, column=3)
school.grid(row=0, column=5)

b1 = Button(Serch, text="검색",command = jobSecch)
b1.grid(row=1, column=0)

companyinfo = ttk.LabelFrame(tab1,text='회사목록')
companyinfo.grid(row=5,column=0)
companyinfof = ttk.LabelFrame(companyinfo)
companyinfof.grid(row=5,column=0)
companyinfoLabel = Text(companyinfof , font = textFont,width = 80, height = 35)
companyinfoLabel.grid(row=0,column=0)
#=======================================================================================================================================

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='메일')
tabControl.pack(expand=1, fill="both")
buttonFont = font.Font(window, size=10, weight='bold', family = '맑은 고딕')

def SendMail():
    # me == 보내는 사람의 이메일 주소
    # you == 받는 사람의 이메일 주소
    me = mailIDEntry.get()
    #dhtpws0170@gmail.com
    you = mailSendEntry.get()
    #dhtpwls0170@naver.com
    password = mailPasswordEntry.get()
    #fsoxfmtohvjswgst

    message = MIMEMultipart()
    message['Subject'] = 'Your Search Commpany Info!'  # 이메일 제목
    message['From'] = me
    message['To'] = you

    for data in Job.dataList:
        mag = MIMEText(data)

    # 로컬 SMTP 서버가 없을 경우 계정이 있는 다른 서버를 사용하면 된다.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(me, password)
    s.sendmail(me, you, message.as_string())
    s.quit()

EmailTable = ttk.LabelFrame(tab2, text='메일')
EmailTable.grid(column=0, row=0)

mailIDLabel = Label(EmailTable, text = "ID")
mailIDLabel.grid(column=0, row=1, pady = 2)
mailIDEntry = Entry(EmailTable, width = 30)
mailIDEntry.grid(column=0, row=2)

mailPasswordLabel = Label(EmailTable, text = "PASSWORD")
mailPasswordLabel.grid(column=0, row=3, pady = 3)
mailPasswordEntry = Entry(EmailTable, width = 30)
mailPasswordEntry.grid(column=0, row=4)

LabelSpace2 = Label(EmailTable, text = " ")
LabelSpace2.grid(column=0, row=5, pady = 10)

mailLabel = Label(EmailTable, text = "보내는 주소")
mailLabel.grid(column=0, row=8)
mailSendEntry = Entry(EmailTable,bg="yellow", fg="black", width = 30)
mailSendEntry.grid(column=0, row=9)
mailButton = Button(EmailTable, font = buttonFont, text = "전송!",command=SendMail)
mailButton.grid(column=0, row=10)
#========================================================================================================================================
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='위치')
tabControl.pack(expand=1, fill="both")

window.mainloop()
