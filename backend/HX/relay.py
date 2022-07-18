import RPi.GPIO as GPIO
import time, sys
import csv
import os
import glob
import datetime
import random

os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
filename1 = 'relay.csv'
tset = float(sys.argv[1])

def csvWrite(val, fn):
    csvfile = open(fn, 'w', newline='')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(val)
    csvfile.close()

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, False)

def startProcs(fn):
    while True:
        filename = "/sys/bus/w1/devices/" + sensor + "/w1_slave"
        tempfile = open(filename) 
        temptext = tempfile.read()
        tempfile.close()
        tempcelsius=temptext.split("\n")[1].split(" ")[9]
        temper = float(tempcelsius[2:])
        temperature = temper/1000
        print(temperature)
        if temperature < tset:
            GPIO.output(21, True)
        else :
            GPIO.output(21, False)
        # temperature = [random.random()]
        csvWrite(temperature, fn)
        time.sleep(5)

startProcs(filename1)
