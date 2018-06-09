import requests
import xml.etree.ElementTree as ET

client_id = "R5BQZkZ9ytJLn2NoTIkg"
client_secret = "okRFeguF9J"
dataFromAPI = None  # dataFromApi - 인터넷으로 부터 받은 자료를 저장하는 변수
dataList = []  # dataList - dataFromApi 에서 xml형태로 변환한 리스트를 저장하는 변수

def ConnectServer(jobNumber="&occupation=01",regionNumber="&region=00000",schoolNumber="&education=00"):
    global dataFromAPI, dataList
    url = "http://openapi.work.go.kr/opi/internInfo/internApi.do?authKey=WNJH5RKZB4YTLPAUVRN8G2VR1HM&returnType=XML&startPage=1&display=10"  # 주소 뒷부분
    url = url + jobNumber
    url = url + regionNumber
    url = url + schoolNumber

    req = requests.get(url)

    if (req.status_code == 200):
        tree = ET.fromstring(req.text)
        company = tree.getiterator("companyNm")
        region = tree.getiterator("regionNm")
        minschool = tree.getiterator("minEdubg")
        index =0
        index2 = 0
        for data in company:
            dataList.append( data.text)
        for data in region:
            dataList[index]+= "  " + data.text
            index += 1
        for data in minschool:
            dataList[index2] += "  " + data.text
            index2+= 1
