import tkinter as t1
import smtplib
import time
from tkinter import *
from tkinter import ttk
from tkinter import font
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Job
import Map

def jobSerchgui():
    def jobSecch():
        jobselect = job.get()  # 콤보박스에서 얻어옴
        localselect = local.get()
        schoolselect = school.get()
        returnList = []
        # 00 학력무관 01 초졸이하 02 중졸 03 고졸 04 대졸(2~3년) 05 대졸(4년) 06 석사 07 박사
        if jobselect == "경영·사무·금융·보험":
            if localselect == "지역무관":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=00000", "&education=07")  # job.py 에 보냄
            elif localselect == "서울":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=11000", "&education=07")  # job.py 에 보냄
            elif localselect == '인천':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=28000", "&education=07")  # job.py 에 보냄
            elif localselect == '경기':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=41000", "&education=07")  # job.py 에 보냄
            elif localselect == '부산':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=26000", "&education=07")  # job.py 에 보냄
            elif localselect == '제주':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=50000", "&education=07")  # job.py 에 보냄
            elif localselect == '대구':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=01", "&region=27000", "&education=07")  # job.py 에 보냄
        elif jobselect == '연구 및 공학기술':
            if localselect == "지역무관":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=00000", "&education=07")  # job.py 에 보냄
            elif localselect == "서울":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=11000", "&education=07")  # job.py 에 보냄
            elif localselect == '인천':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=28000", "&education=07")  # job.py 에 보냄
            elif localselect == '경기':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=41000", "&education=07")  # job.py 에 보냄
            elif localselect == '부산':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=26000", "&education=07")  # job.py 에 보냄
            elif localselect == '제주':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=50000", "&education=07")  # job.py 에 보냄
            elif localselect == '대구':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=02", "&region=27000", "&education=07")  # job.py 에 보냄
        elif jobselect == '교육·법률·사회복지·경찰·소방 및 군인':
            if localselect == "지역무관":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=00000", "&education=07")  # job.py 에 보냄
            elif localselect == "서울":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=11000", "&education=07")  # job.py 에 보냄
            elif localselect == '인천':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=28000", "&education=07")  # job.py 에 보냄
            elif localselect == '경기':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=41000", "&education=07")  # job.py 에 보냄
            elif localselect == '부산':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=26000", "&education=07")  # job.py 에 보냄
            elif localselect == '제주':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=50000", "&education=07")  # job.py 에 보냄
            elif localselect == '대구':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=03", "&region=27000", "&education=07")  # job.py 에 보냄
        elif jobselect == '보건·의료':
            if localselect == "지역무관":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=00000", "&education=07")  # job.py 에 보냄
            elif localselect == "서울":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=11000", "&education=07")  # job.py 에 보냄
            elif localselect == '인천':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=28000", "&education=07")  # job.py 에 보냄
            elif localselect == '경기':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=41000", "&education=07")  # job.py 에 보냄
            elif localselect == '부산':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=26000", "&education=07")  # job.py 에 보냄
            elif localselect == '제주':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=50000", "&education=07")  # job.py 에 보냄
            elif localselect == '대구':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=04", "&region=27000", "&education=07")  # job.py 에 보냄
        elif jobselect == '예술·디자인·방송·스포츠':
            if localselect == "지역무관":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=00000", "&education=07")  # job.py 에 보냄
            elif localselect == "서울":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=11000", "&education=07")  # job.py 에 보냄
            elif localselect == '인천':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=28000", "&education=07")  # job.py 에 보냄
            elif localselect == '경기':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=41000", "&education=07")  # job.py 에 보냄
            elif localselect == '부산':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=26000", "&education=07")  # job.py 에 보냄
            elif localselect == '제주':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=50000", "&education=07")  # job.py 에 보냄
            elif localselect == '대구':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=05", "&region=27000", "&education=07")  # job.py 에 보냄
        elif jobselect == '영업·판매·운전·운송':
            if localselect == "지역무관":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=00000", "&education=07")  # job.py 에 보냄
            elif localselect == "서울":
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=11000", "&education=07")  # job.py 에 보냄
            elif localselect == '인천':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=28000", "&education=07")  # job.py 에 보냄
            elif localselect == '경기':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=41000", "&education=07")  # job.py 에 보냄
            elif localselect == '부산':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=26000", "&education=07")  # job.py 에 보냄
            elif localselect == '제주':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=50000", "&education=07")  # job.py 에 보냄
            elif localselect == '대구':
                if schoolselect == "학력무관":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=00")  # job.py 에 보냄
                elif schoolselect == "초졸이하":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=01")  # job.py 에 보냄
                elif schoolselect == "중졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=02")  # job.py 에 보냄
                elif schoolselect == "고졸":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=03")  # job.py 에 보냄
                elif schoolselect == "대졸(2~3년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=04")  # job.py 에 보냄
                elif schoolselect == "대졸(4년)":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=05")  # job.py 에 보냄
                elif schoolselect == "석사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=06")  # job.py 에 보냄
                elif schoolselect == "박사":
                    returnList = Job.ConnectServer("&occupation=07", "&region=27000", "&education=07")  # job.py 에 보냄
        for i in range(len(Job.dataList)):
            companyinfoText.insert(INSERT, "[")
            companyinfoText.insert(INSERT, i + 1)
            companyinfoText.insert(INSERT, "]")
            companyinfoText.insert(INSERT, Job.dataList[i])
            companyinfoText.insert(INSERT, '\n\n')

    window = t1.Tk()
    textFont = font.Font(window, size=9, family='맑은 고딕')
    window.geometry("600x700")
    window.title("Intern Serch")
    tabControl = ttk.Notebook(window)

    tab = ttk.Frame(tabControl)
    tabControl.add(tab, text='검색')
    tabControl.pack(expand=1, fill="both")

    Serch = ttk.LabelFrame(tab, text='정보검색')
    Serch.grid(row=0, column=0)

    l1 = Label(Serch, text="직종")
    l2 = Label(Serch, text="지역")
    l3 = Label(Serch, text="학력")
    l1.grid(row=0, column=0)
    l2.grid(row=0, column=2)
    l3.grid(row=0, column=4)

    job = ttk.Combobox(Serch)
    job['values'] = ('경영·사무·금융·보험', '연구 및 공학기술', '교육·법률·사회복지·경찰·소방 및 군인', '보건·의료', '예술·디자인·방송·스포츠',
                     '영업·판매·운전·운송',
                     '미용·여행·숙박·음식·경비·돌봄·청소','건설·채굴','설치·정비·생산-기계·금속·재료','설치·정비·생산-전기·전자·정보통신','설치·정비·생산-화학·환경·섬유·의복·식품가공',
                     '설치·정비·생산-인쇄·목재·공예 및 제조 단순','농림어업직')

    local = ttk.Combobox(Serch)
    local['values'] = ('지역무관', '서울', '인천', '경기', '부산', '제주',
                       '대구', '광주', '대전', '울산', '세종', '강원', '충북', '충남', '전북', '전남', '경북', '경남')
    school = ttk.Combobox(Serch)
    school['values'] = ('학력무관', '초졸이하', '중졸', '고졸', '대졸(2~3년)', '대졸(4년)', '석사', '박사')
    #00 학력무관 01 초졸이하 02 중졸 03 고졸 04 대졸(2~3년) 05 대졸(4년) 06 석사 07 박사

    job.grid(row=0, column=1)
    local.grid(row=0, column=3)
    school.grid(row=0, column=5)

    b1 = Button(Serch, text="검색", command=jobSecch)
    b1.grid(row=1, column=0)

    companyinfo = ttk.LabelFrame(tab, text='회사목록')
    companyinfo.grid(row=5, column=0)
    companyinfof = ttk.LabelFrame(companyinfo)
    companyinfof.grid(row=5, column=0)
    companyinfoText = Text(companyinfof, font=textFont, width=80, height=35)
    companyinfoText.grid(row=0, column=0)
    #companyinfoText.configure(state='disabled')

#=======================================================================================================================================

def sendmain():
    def SendMail():
        # me == 보내는 사람의 이메일 주소
        # you == 받는 사람의 이메일 주소
        me = mailIDEntry.get()
        # dhtpws0170@gmail.com
        you = mailSendEntry.get()
        # dhtpwls0170@naver.com
        password = mailPasswordEntry.get()
        # bzeuxvyxdnxxeexf

        message = MIMEMultipart()
        message['Subject'] = 'Your Search Commpany Info!'  # 이메일 제목
        message['From'] = me
        message['To'] = you

        msg = MIMEText('회사 검색 결과\n' +
                        "=================================\n" +
                         Job.dataList[0] + '\n' +
                         Job.dataList[1] + '\n' +
                         Job.dataList[2] + '\n' +
                         Job.dataList[3] + '\n' +
                         Job.dataList[4] + '\n' +
                         Job.dataList[5] + '\n' +
                         Job.dataList[6] + '\n' +
                         Job.dataList[7] + '\n' +
                         Job.dataList[8] + '\n' +
                         Job.dataList[9] + '\n' +
                        "=================================\n")

        message.attach(msg)
        # 로컬 SMTP 서버가 없을 경우 계정이 있는 다른 서버를 사용하면 된다.
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(me, password)
        s.sendmail(me, you, message.as_string())
        s.quit()

    window1 = t1.Tk()
    window1.geometry("230x250")
    window1.title("Intern Serch")
    tabControl = ttk.Notebook(window1)

    tab = ttk.Frame(tabControl)
    tabControl.add(tab, text='메일')
    tabControl.pack(expand=1, fill="both")
    buttonFont = font.Font(window1, size=10, weight='bold', family='맑은 고딕')

    EmailTable = ttk.LabelFrame(tab, text='메일')
    EmailTable.grid(column=0, row=0)

    mailIDLabel = Label(EmailTable, text="ID")
    mailIDLabel.grid(column=0, row=1, pady=2)
    mailIDEntry = Entry(EmailTable, width=30)
    mailIDEntry.grid(column=0, row=2)

    mailPasswordLabel = Label(EmailTable, text="PASSWORD")
    mailPasswordLabel.grid(column=0, row=3, pady=3)
    mailPasswordEntry = Entry(EmailTable, width=30)
    mailPasswordEntry.grid(column=0, row=4)

    LabelSpace = Label(EmailTable, text=" ")
    LabelSpace.grid(column=0, row=5, pady=10)

    mailLabel = Label(EmailTable, text="보내는 주소")
    mailLabel.grid(column=0, row=8)
    mailSendEntry = Entry(EmailTable, bg="yellow", fg="black", width=30)
    mailSendEntry.grid(column=0, row=9)
    mailButton = Button(EmailTable, font=buttonFont, text="전송!", command=SendMail)
    mailButton.grid(column=0, row=10)

#========================================================================================================================================
def mapProcess():
    tag = MapEntry.get()
    coord = Map.GetCoordinate(tag)
    print(coord)
    Map.GetMap(coord)
    photo = PhotoImage(file="SearchMap.png")
    Mapimg.configure(image=photo, width=1000, height=500)
    Mapimg.image = photo

#========================================================================================================================================

def InitTopText():
    TempFont = font.Font(tab1, size=20, weight='bold', family = 'Consolas')
    MainText = Label(tab1, font = TempFont, text="[취업톡톡 인턴검색 App]")
    MainText.pack()
    MainText.place(x=80)


mainBackGround = t1.Tk()
mainBackGround.geometry("500x500")
mainBackGround.title("메인화면")
tabControl = ttk.Notebook(mainBackGround)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='메인')
tabControl.pack(expand=1, fill="both")
mainimage = PhotoImage(file = "mainimg.gif")
mainimage_Label = Label(tab1, image = mainimage)
mainimage_Label.pack()
mainimage_Label.place(x = 0,y = 0)

InitTopText()
TempFont = font.Font(tab1, size=25, weight='bold', family='Consolas')
button = Button(tab1, font = TempFont, text="회사 검색", command = jobSerchgui)
button.place(x=150,y=100)
button = Button(tab1, font = TempFont, text="메일 보내기", command = sendmain)
button.place(x=150,y=300)

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='위치')
tabControl.pack(expand=1, fill="both")

MapTable = ttk.LabelFrame(tab2, text='위치 검색')
MapTable.grid(column=0, row=0)

MapEntry = Entry(MapTable, width=30)
MapEntry.grid(column=0, row=0)

MaploactionSerch = Button(MapTable, text="검색", command=mapProcess)
MaploactionSerch.grid(column=0, row=1)

MapImageTable = ttk.LabelFrame(tab2, text='지도 이미지')
MapImageTable.grid(column=0, row=2)

photo = PhotoImage(file="SearchMap.png")
Mapimg = Label(MapImageTable)
Mapimg.grid(column=0, row=3)
Mapimg.configure(image=photo, width=1000, height=500)
Mapimg.image = photo
mainBackGround.mainloop()
