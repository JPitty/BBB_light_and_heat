#!/usr/bin/env python

import Adafruit_BBIO.ADC as ADC
import httplib, urllib
import time
import readtemp

sensor_pin='P9_40'
ADC.setup()
AvgV=0.0
AvgVold=0.0
count = 0
diffmag = 0.01

def sendit(V,T):
	V = round(V,4)
	params = urllib.urlencode({'field1':V, 'field2':T[0], 'field3':T[1], 'key':'62O6Z40PY42II6FB'})
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print V
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection failed"

print('Reading\t\tVolts')
while True:
	reading = ADC.read(sensor_pin)
	volts = reading * 1.8
	AvgV = AvgV*0.91+volts*0.09
	print('%f\t%f\t%f' % (reading, volts, AvgV))
	time.sleep(1.)
	count+=1
	diff=abs(AvgV-AvgVold)
	#if count==30:
	if (diff>diffmag and  count>20) or (count==60):
	#if diff>diffmag:
		count=0
		AvgVold=AvgV
                T = readtemp.main()
		sendit(AvgV,T)
