

import sys
import time
import datetime

import Adafruit_BMP.BMP085 as BMP085

FREQUENCY_SECONDS     = 30

bmp = BMP085.BMP.BMP085()

while True:



    f=open('highlog.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    temp = bmp.read_temperature()
    pressure = bmp.read_pressure()
    altitude = bmp.read_altitude()
    print 'Timestamp:'(timestamp)
    print 'Temperature: {0:0.1F} C'.format(temp)
    print 'Pressure:    {0:0.1F} Pa'.format(pressure)
    print 'Altitude:    {0:0.1F} m'.format(altitude)
    f.write(timestamp)
    f.write(temp)
    f.write(pressure)
    f.write(altitude)
    f.close()

    #if above doesn't work
    #f=open('highlog.txt','a')
    #temp = bmp.read_temperature()
    #pressure = bmp.read_pressure()
    #altitude = bmp.read_altitude()
    #print 'Timestamp:'(datetime.datetime.now())
    #print 'Temperature: {0:0.1F} C'.format(temp)
    #print 'Pressure:    {0:0.1F} Pa'.format(pressure)
    #print 'Altitude:    {0:0.1F} m'.format(altitude)
    #f.write((datetime.datetime.now(), temp, pressure, altitude))
    #f.close()
    
    print 'Logged Bitch!'

    time.sleep(FREQUENCY_SECONDS)
