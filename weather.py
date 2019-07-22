#!/usr/local/bin/python3
#coding=utf-8

'''
Created on 2011-2-25
@author: http://www.cnblogs.com/txw1958/
'''

#http://www.weather.com.cn/data/sk/101010100.html         ʵʱ
#http://www.weather.com.cn/data/cityinfo/101010100.html   ȫ��
#http://m.weather.com.cn/data/101010100.html     ����

##http://www.google.com/ig/api?weather=Beijing Ӣ��
##http://www.google.com/ig/api?weather=TOKYO
##http://www.google.com/ig/api?weather=Beijing&hl=zh-cn ����

import os, io, sys, re, time, base64, json
import webbrowser, urllib.request

#���Ϲ���
cityList_bsgs = [
    {'code':"101010100", 'name':"����"},
    {'code':"101020100", 'name':"�Ϻ�"},
    {'code':"101280101", 'name':"����"},
    {'code':"101280601", 'name':"����"}
]

cityList_main = [   #ȫ����Ҫ����
    #����
    {'code':"101010100", 'name':"����"},
    {'code':"101030100", 'name':"���"},
    {'code':"101090101", 'name':"ʯ��ׯ"},
    {'code':"101100101", 'name':"̫ԭ"},
    {'code':"101080101", 'name':"���ͺ���"},
    {'code':"101090201", 'name':"����"},
    {'code':"101100201", 'name':"��ͬ"},
    {'code':"101080201", 'name':"��ͷ"},
    {'code':"101090402", 'name':"�е���"},
    {'code':"101100401", 'name':"����"},
    {'code':"101080501", 'name':"ͨ��"},
    {'code':"101091101", 'name':"�ػʵ�"},
    #����
    {'code':"101050101", 'name':"������"},
    {'code':"101060101", 'name':"����"},
    {'code':"101070101", 'name':"����"},
    {'code':"101050201", 'name':"�������"},
    {'code':"101060201", 'name':"����"},
    {'code':"101070201", 'name':"����"},
    {'code':"101050301", 'name':"ĵ����"},
    {'code':"101060301", 'name':"�Ӽ�"},
    {'code':"101070301", 'name':"��ɽ"},
    {'code':"101050501", 'name':"�绯"},
    {'code':"101060601", 'name':"�׳�"},
    {'code':"101071401", 'name':"��«��"},
    #����
    {'code':"101280101", 'name':"����"},
    {'code':"101300101", 'name':"����"},
    {'code':"101310101", 'name':"����"},
    {'code':"101320101", 'name':"���"},
    {'code':"101330101", 'name':"����"},
    {'code':"101280601", 'name':"����"},
    {'code':"101300501", 'name':"����"},
    {'code':"101310201", 'name':"����"},
    {'code':"101280701", 'name':"�麣"},
    {'code':"101281701", 'name':"��ɽ"},
    {'code':"101301001", 'name':"��ɫ"},
    {'code':"101310215", 'name':"����"},
    #����
    {'code':"101110101", 'name':"����"},
    {'code':"101160101", 'name':"����"},
    {'code':"101150101", 'name':"����"},
    {'code':"101170101", 'name':"����"},
    {'code':"101130101", 'name':"��³ľ��"},
    {'code':"101110300", 'name':"�Ӱ�"},
    {'code':"101110901", 'name':"����"},
    {'code':"101160901", 'name':"��ˮ"},
    {'code':"101170301", 'name':"����"},
    {'code':"101130501", 'name':"��³��"},
    {'code':"101160801", 'name':"��Ȫ"},
    {'code':"101170401", 'name':"��ԭ"},
    #����
    {'code':"101040100", 'name':"����"},
    {'code':"101270101", 'name':"�ɶ�"},
    {'code':"101260101", 'name':"����"},
    {'code':"101290101", 'name':"����"},
    {'code':"101140101", 'name':"����"},
    {'code':"101270401", 'name':"����"},
    {'code':"101260201", 'name':"����"},
    {'code':"101290201", 'name':"����"},
    {'code':"101271401", 'name':"��ɽ"},
    {'code':"101260801", 'name':"����ˮ"},
    {'code':"101291401", 'name':"����"},
    #����
    {'code':"101020100", 'name':"�Ϻ�"},
    {'code':"101230101", 'name':"����"},
    {'code':"101220101", 'name':"�Ϸ�"},
    {'code':"101240101", 'name':"�ϲ�"},
    {'code':"101120101", 'name':"����"},
    {'code':"101210301", 'name':"����"},
    {'code':"101190101", 'name':"�Ͼ�"},
    {'code':"101210401", 'name':"����"},
    {'code':"101210101", 'name':"����"},
    {'code':"101190401", 'name':"����"},
    {'code':"101120201", 'name':"�ൺ"},
    {'code':"101230201", 'name':"����"},
    {'code':"101340101", 'name':"̨����"},
    #����
    {'code':"101180101", 'name':"֣��"},
    {'code':"101200101", 'name':"�人"},
    {'code':"101250101", 'name':"��ɳ"},
    {'code':"101180201", 'name':"����"},
    {'code':"101200201", 'name':"����"},
    {'code':"101250201", 'name':"��̶"},
    {'code':"101250301", 'name':"����"},
    {'code':"101180401", 'name':"���"},
    {'code':"101250601", 'name':"����"},
    {'code':"101251101", 'name':"�żҽ�"},
    {'code':"101200401", 'name':"Т��"},
    {'code':"101201401", 'name':"����"}
]

#����dict����: twitter = {'image': imgPath, 'message': content}
def getCityWeather_RealTime(cityID):
    url = "http://www.weather.com.cn/data/sk/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')

        jsonDatas = json.loads(weatherInfomation)

        city        = jsonDatas["weatherinfo"]["city"]
        temp        = jsonDatas["weatherinfo"]["temp"]
        fx          = jsonDatas["weatherinfo"]["WD"]        #����
        fl          = jsonDatas["weatherinfo"]["WS"]        #����
        sd          = jsonDatas["weatherinfo"]["SD"]        #���ʪ��
        tm          = jsonDatas["weatherinfo"]["time"]

        content = "#" + city + "#" + " " + temp + "�� " + fx + fl + " " + "���ʪ��" + sd + " "  + "����ʱ��:" + tm
        twitter = {'image': "", 'message': content}

    except (SyntaxError) as err:
        print(">>>>>> SyntaxError: " + err.args)
    except:
        print(">>>>>> OtherError: ")
    else:
        return twitter
    finally:
        None

#����dict����: twitter = {'image': imgPath, 'message': content}
def getCityWeatherDetail_SixDay(cityID):
    url = "http://m.weather.com.cn/data/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')
        jsonDatas = json.loads(weatherInfomation)

        city        = jsonDatas["weatherinfo"]["city"]
        tempF1      = jsonDatas["weatherinfo"]["tempF1"]
        weather     = jsonDatas["weatherinfo"]["img_title1"]
        img         = jsonDatas["weatherinfo"]["img1"]
        fx          = jsonDatas["weatherinfo"]["fx1"]       #����
        cy            = jsonDatas["weatherinfo"]["index"]        #ů        #����ָ��
        zw            = jsonDatas["weatherinfo"]["index_uv"]        #����   #������ָ��
        xc            = jsonDatas["weatherinfo"]["index_xc"]        #����     #ϴ��
        tr            = jsonDatas["weatherinfo"]["index_tr"]        #������    #����
        co            = jsonDatas["weatherinfo"]["index_co"]        #����     #���ʶ�
        cl            = jsonDatas["weatherinfo"]["index_cl"]        #������  #����ָ��
        ls            = jsonDatas["weatherinfo"]["index_ls"]        #��̫����  #��ɹָ��
        ag            = jsonDatas["weatherinfo"]["index_ag"]        #���׷�"    #����
        temp1       = jsonDatas["weatherinfo"]["temp1"]
        temp2       = jsonDatas["weatherinfo"]["temp2"]
        temp3       = jsonDatas["weatherinfo"]["temp3"]
        temp4       = jsonDatas["weatherinfo"]["temp4"]
        temp5       = jsonDatas["weatherinfo"]["temp5"]
        temp6       = jsonDatas["weatherinfo"]["temp6"]
        weather1    = jsonDatas["weatherinfo"]["weather1"]
        weather2    = jsonDatas["weatherinfo"]["weather2"]
        weather3    = jsonDatas["weatherinfo"]["weather3"]
        weather4    = jsonDatas["weatherinfo"]["weather4"]
        weather5    = jsonDatas["weatherinfo"]["weather5"]
        weather6    = jsonDatas["weatherinfo"]["weather6"]

        if int(img) < 10:
            imgPath = "icon\d" + "0" + str(img) + ".gif"
        else:
            imgPath = "icon\d"       + str(img) + ".gif"

        content = "#" + city + "#" + "\n<ָ��> " + "����:" + cy + " ������:" + zw + " ϴ��:" + xc \
                + " ����:" + tr + " ���ʶ�:" + co + " ����:" + cl + " ��ɹ:" + ls + " ����:" + ag + "\n" \
                + "<����>" + " 1��:" + temp1 + " " + weather1 + " 2��:" + temp2 + " " + weather2  + " 3��:" + temp3 + " " + weather3\
                + " 4��:" + temp4 + " " + weather4 + " 5��:" + temp5 + " " + weather5  + " 6��:" + temp6 + " " + weather6

        twitter = {'image': imgPath, 'message': content}

    except (SyntaxError) as err:
        print(">>>>>> SyntaxError: " + err.args)
    except:
        print(">>>>>> OtherError: ")
    else:
        return twitter
    finally:
        None

#����dict����: twitter = {'image': imgPath, 'message': content}
def getCityWeather_AllDay(cityID):
    url = "http://www.weather.com.cn/data/cityinfo/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')
        jsonDatas = json.loads(weatherInfomation)

        city        = jsonDatas["weatherinfo"]["city"]
        temp1       = jsonDatas["weatherinfo"]["temp1"]
        temp2       = jsonDatas["weatherinfo"]["temp2"]
        weather     = jsonDatas["weatherinfo"]["weather"]
        img1        = jsonDatas["weatherinfo"]["img1"]
        img2        = jsonDatas["weatherinfo"]["img2"]
        ptime        = jsonDatas["weatherinfo"]["ptime"]

        content = city + "," + weather + ",�������:" + temp1 + ",�������:"  + temp2 + ",����ʱ��:" + ptime
        twitter = {'image': "icon\d" + img1, 'message': content}

    except (SyntaxError) as err:
        print(">>>>>> SyntaxError: " + err.args)
    except:
        print(">>>>>> OtherError: ")
    else:
        return twitter
    finally:
        None

def main():
    "main function"
    for city in cityList_bsgs:
        title_small = "��ʵʱ��"
        twitter = getCityWeather_RealTime(city['code'])
        print(title_small + twitter['message'])

    for city in cityList_bsgs:
        title_small = "��ȫ�졿"
        twitter = getCityWeather_AllDay(city['code'])
        print(title_small + twitter["message"])

    title_small = "�����졿"
    twitter = getCityWeatherDetail_SixDay(cityList_bsgs[3]['code'])
    print(title_small + twitter["message"])

if __name__ == '__main__':
    main()
