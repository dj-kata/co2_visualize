#!/usr/bin/python3
import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
os.environ[ 'HOME' ] = '/home/matplotlib/tmp'

def gen_graph():
    dat = pd.read_csv('./co2.log')
    dat.columns = ['ts','co2','temp']
    dat['ts'] = pd.to_datetime(dat['ts'])

    #plt.figure()
    fig,ax = plt.subplots()
    fig.subplots_adjust(bottom=0.3)
    day = dat[-7200:] # 直近2日

    ax.grid(which='major',axis='x', linestyle='--', linewidth=1)
    ax.grid(which='major',axis='y', linestyle='-', linewidth=1)
    plt.plot(day['ts'], day['co2'])
    plt.xticks(rotation=90,size=25)
    plt.yticks(size=25)
    plt.title('co2[ppm]', size=22)
    plt.savefig('tmp/co2.png')
    plt.cla()

    ax.grid(which='major',axis='x', linestyle='--', linewidth=1)
    ax.grid(which='major',axis='y', linestyle='-', linewidth=1)
    plt.plot(day['ts'], day['temp'], color='red')
    plt.xticks(rotation=90,size=25)
    plt.yticks(size=25)
    plt.title('temperature[C]', size=22)
    plt.savefig('tmp/temp.png')
    plt.close('all')

print("Content-Type: text/html")
print("")
print("<!DOCTYPE html>")
print("<head>")
print("<title>living_info</title>")
print("<style>img{max-width: 100%;height: auto;}</style>")
print("</head>")
print("<body><h1>")
sys.stdout.flush()
gen_graph()
print('<img src="../temp.png"><br>')
print('<img src="../co2.png"><br>')
print("</h1><body></html>")