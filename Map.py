import os
import sys
import requests
import xml.etree.ElementTree as ET
import folium
import time
from selenium import webdriver


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

def GetMap(coord=[35.213145, 129.1076011]):
    map_osm = folium.Map(location=[float(coord[0]), float(coord[1])], zoom_start=15)
    # 마커 지정
    folium.Marker([float(coord[0]), float(coord[1])], popup='Mt. Hood Meadows').add_to(map_osm)
    #html 파일로 저장\
    delay = 5
    fn = 'testmap.html'
    map_osm.save(fn)
    tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=fn)

    browser = webdriver.Chrome('C://Users/sejin/PycharmProjects/untitled1/chromedriver.exe')
    browser.get(tmpurl)
    # Give the map tiles some time to load
    time.sleep(delay)
    browser.save_screenshot('SearchMap.png')
    #browser.quit()