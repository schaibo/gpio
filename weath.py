# -*- coding: utf-8 -*-
import urllib2  
from city import city  
import json  
import gzip
import StringIO
      
      
def parseTOUTF8(data):
    data = json.loads(data)
    content = data['weatherinfo']
    return content

def writeToLocal(filepath,filename,data):
    file = os.open(path+filename,'wb')
    file.write(data)
    file.close()
    print '数据已经成功写入到本地文件'


#cityname = raw_input("你想查询那个城市的天气？")  
citycode="101270101"  
      
#try:  
#   citycode =city[cityname]  
#except:  
#   print "not Found"  
if citycode:  
    try:  
      url= "http://www.weather.com.cn/data/cityinfo/"+citycode+".html"#构造网址  
      #url= "http://www.weather.com.cn/data/cityinfo/101270101.html"#构造网址  
      req = urllib2.Request(url)
      response = urllib2.urlopen(req, timeout=120)
      page = response.read()#读取网页源代码
      print "Page"
      print page
      data = json.loads(page,encoding='utf-8')
      print "data"
      print type(data)
      print data
      print "weather"
      #print data["weatherinfo"]
      #text = json.dumps(page,ensure_ascii=True,encoding="utf-8")   
      res = data["weatherinfo"]#获取字典  
      print "res"
      print res
      #str_temp=("%s :%s~%s")%(res['ptime'],res['temp1'],res['temp2'])#格式化字符  
      print res['ptime']
      #print(res['ptime'] + res['temp1'] + res['temp2'])
    except:
      print "Not Found!!"  
