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
    print '�����Ѿ��ɹ�д�뵽�����ļ�'


#cityname = raw_input("�����ѯ�Ǹ����е�������")  
citycode="101270101"  
      
#try:  
#   citycode =city[cityname]  
#except:  
#   print "not Found"  
if citycode:  
    try:  
      url= "http://www.weather.com.cn/data/cityinfo/"+citycode+".html"#������ַ  
      #url= "http://www.weather.com.cn/data/cityinfo/101270101.html"#������ַ  
      req = urllib2.Request(url)
      response = urllib2.urlopen(req, timeout=120)
      page = response.read()#��ȡ��ҳԴ����
      print "Page"
      print page
      data = json.loads(page,encoding='utf-8')
      print "data"
      print type(data)
      print data
      print "weather"
      #print data["weatherinfo"]
      #text = json.dumps(page,ensure_ascii=True,encoding="utf-8")   
      res = data["weatherinfo"]#��ȡ�ֵ�  
      print "res"
      print res
      #str_temp=("%s :%s~%s")%(res['ptime'],res['temp1'],res['temp2'])#��ʽ���ַ�  
      print res['ptime']
      #print(res['ptime'] + res['temp1'] + res['temp2'])
    except:
      print "Not Found!!"  
