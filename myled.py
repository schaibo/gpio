# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
# BOARD��ŷ�ʽ�����ڲ������ű��    
GPIO.setmode(GPIO.BOARD)    
# ���ģʽ    
GPIO.setup(16, GPIO.OUT)    

while True:    
     GPIO.output(1, GPIO.HIGH)    
     time.sleep(1)    
     GPIO.output(1, GPIO.LOW)    
     time.sleep(1)   