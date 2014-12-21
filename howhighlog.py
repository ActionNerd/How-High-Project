import sys
import time
import datetime

import Adafruit_BMP.BMP085 as BMP085

FREQUENCY_SECONDS     = 30

bmp = BMP085.BMP085()

while True:

    f=open('highlog.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    temp = bmp.read_temperature()
    pressure = bmp.read_pressure()
    altitude = bmp.read_altitude()
    Temper = "Temperature:"
    print datetime.datetime.now()
    print 'Temperature: {0:0.1F} C'.format(temp)
    print 'Pressure:    {0:0.1F} Pa'.format(pressure)
    print 'Altitude:    {0:0.1F} m'.format(altitude)
    f.write (Temper)
    f.write (str(temp)+"C"+'\n')
    f.close()

    time.sleep(FREQUENCY_SECONDS)
