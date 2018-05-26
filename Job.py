import requests
import xml.etree.ElementTree as ET

client_id = "R5BQZkZ9ytJLn2NoTIkg"
client_secret = "okRFeguF9J"
dataFromAPI = None  # dataFromApi - 인터넷으로 부터 받은 자료를 저장하는 변수
dataList = None  # dataList - dataFromApi 에서 xml형태로 변환한 리스트를 저장하는 변수

def ConnectServer(number):
    global dataFromAPI, dataList
    url = "http://openapi.work.go.kr/opi/internInfo/internApi.do?authKey=WNJH5RKZB4YTLPAUVRN8G2VR1HM&returnType=XML&startPage=1&display=10"  # 주소 뒷부분
    req = requests.get(url)

    if(number == 1):
        if (req.status_code == 200):
            tree = ET.fromstring(req.text)
            dataList = tree.getiterator("companyNm")
            LoadData()
        else:
            print("연결 오류")
    if (number == 2):
        if (req.status_code == 200):
            tree = ET.fromstring(req.text)
            dataList = tree.getiterator("collectJobsNm")
            LoadData()
        else:
            print("연결 오류")
    if (number == 3):
        if (req.status_code == 200):
            tree = ET.fromstring(req.text)
            dataList = tree.getiterator("regionNm")
            LoadData()
        else:
            print("연결 오류")
    if (number == 4):
        if (req.status_code == 200):
            tree = ET.fromstring(req.text)
            dataList = tree.getiterator("minEdubg")
            LoadData()
        else:
            print("연결 오류")


def LoadData():
    for data in dataList:
        print(data.text)

