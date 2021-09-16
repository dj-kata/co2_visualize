#!/usr/bin/python3
from CO2Meter import *
from datetime import datetime
import time
Meter = CO2Meter("/dev/hidraw2")
while True:
    meas = Meter.get_data()
    meas.update({'timestamp': datetime.now()})
    if 'co2' in meas.keys() and 'temperature' in meas.keys():
        with open('/var/www/cgi-bin/co2.log', 'a') as f:
            ts = meas['timestamp'].strftime("%Y/%m/%d %H:%M:%S")
            # timestamp, co2, temp
            f.write(f"{ts}, {meas['co2']}, {meas['temperature']}\n")
        break