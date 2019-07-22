#coding=utf-8

import os, io, sys, re, time, base64, json
import urllib


url= "http://www.weather.com.cn/data/cityinfo/101270101.html"
stdout = urllib.urlopen(url)
weatherInfomation = stdout.read().decode('utf8')
#jsonDatas = json.loads(weatherInfomation)
jsonData = json.dumps(weatherInfomation, ensure_ascii=False) 
print jsonData
        #city        = jsonData["weatherinfo"]["city"]
        #temp1       = jsonData["weatherinfo"]["temp1"]
        #temp2       = jsonData["weatherinfo"]["temp2"]
        #weather     = jsonData["weatherinfo"]["weather"]
        #ptime       = jsonData["weatherinfo"]["ptime"]

        #content = city + "," + weather + ",最高气温:" + temp1 + ",最低气温:"  + temp2 + ",发布时间:" + ptime
        #print(city)
content = "weather"
print(content)

