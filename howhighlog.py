import sys
import time
import datetime

import Adafruit_BMP.BMP085 as BMP085

FREQUENCY_SECONDS     = 15

bmp = BMP085.BMP085_ULTRAHIGHRES()

while True:

    f=open('highlog.txt','a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    temp = bmp.read_temperature()
    pressure = bmp.read_pressure()
    altitude = bmp.read_altitude()
    temper = "Temperature:"
    press = "Pressure:"
    alt = "Altitude"
    brk = "-------------"
    print datetime.datetime.now()
    print 'Temperature: {0:0.1F} C'.format(temp)
    print 'Pressure:    {0:0.1F} Pa'.format(pressure)
    print 'Altitude:    {0:0.1F} m'.format(altitude)
    f.write (str(timestamp)+'\n')
    f.write (temper)
    f.write (str(temp)+"C"+'\n')
    f.write (press)
    f.write (str(pressure)+"Pa"+'\n')
    f.write (alt)
    f.write (str(altitude)+"m"+'\n')
    f.write (str(brk)+'\n')
    f.close()

    time.sleep(FREQUENCY_SECONDS)
