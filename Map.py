import os
import requests
import xml.etree.ElementTree as ET
import time
import folium #pip install folium 추가
from selenium import webdriver #pip install selenium 추가
#Selenium은 웹 브라우져를 컨트롤하여 웹 UI 를 Automation 하는 도구 중의 하나이다.

#GetCoordinate함수에서 장소를 가져와 어드레스 부분에 맞는 위도와경도는 받아 coord에 추가한다
def GetCoordinate(address="판교"):
    global client_id, client_secret
    url = "https://maps.googleapis.com/maps/api/geocode/xml?address="+address+"&key=AIzaSyBYOPieArSXEiwExB00FPNU6e-WMbIYyUg" # json 결과
    req = requests.get(url)
    tree = ET.fromstring(req.text)
    coord=[]
    for item in tree.getiterator("location"):
        coord.append(item.find("lat").text)
        coord.append(item.find("lng").text)
    return coord

#가져온 위도와 경도를 통해 그해당부분에 마커를 찍고 5초뒤에 보고있는 부분을 지도로 찍어 보여주고 브라우져는 계속 켜져있는 상태로 있는다.
def GetMap(coord=[35.213145, 129.1076011]):
    map_osm = folium.Map(location=[float(coord[0]), float(coord[1])], zoom_start=15)
    # 마커 지정
    folium.Marker([float(coord[0]), float(coord[1])], popup='Mt. Hood Meadows').add_to(map_osm)
    #html 파일로 저장\
    delay = 5
    fn = 'testmap.html'
    map_osm.save(fn)
    tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=fn)

    #다른 컴퓨터에서 실행할때 경로를 바꿔야 오류가 발생하지 않는다.
    browser = webdriver.Chrome('C://Users/sejin/PycharmProjects/untitled1/chromedriver.exe')
    browser.get(tmpurl)
    # Give the map tiles some time to load
    time.sleep(delay)
    browser.save_screenshot('SearchMap.png')
    #browser.quit()
