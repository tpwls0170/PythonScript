import os
import sys
import requests
import xml.etree.ElementTree as ET
import folium
import time
from selenium import webdriver


client_id = "R5BQZkZ9ytJLn2NoTIkg"
client_secret = "okRFeguF9J"
dataFromAPI = None  # dataFromApi - 인터넷으로 부터 받은 자료를 저장하는 변수
dataList = None  # dataList - dataFromApi 에서 xml형태로 변환한 리스트를 저장하는 변수

def ConnectServer():
    global dataFromAPI, dataList
    server = ""  # 메인 주소

    url = "http://openapi.work.go.kr/opi/internInfo/internApi.do?authKey=WNJH5RKZB4YTLPAUVRN8G2VR1HM&returnType=XML&startPage=1&display=10&region=11260"  # 주소 뒷부분
    req = requests.get(url)
    if(req.status_code==200):
        tree = ET.fromstring(req.text)
        dataList = tree.getiterator("collectJobsNm")
    else:
        print("연결 오류")

def LoadData(dataList):
    for data in dataList:
        print(data.text)