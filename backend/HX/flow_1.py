# import RPi.GPIO as GPIO
import time, sys
import random, csv
 
FLOW_SENSOR_GPIO = 25 # hot flow rate
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

fields = ['Fhot']
global count
global start_counter
count = 0
filename1 = 'fhot_rate.csv'

# writing to csv file 
with open(filename1, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

def countPulse(channel):
   global count
   if start_counter == 1:
        count = count + 1

def csvWrite(val, fn):
    csvfile = open(fn, 'a', newline='')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(val)
    csvfile.close()

# GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

def startLogs(fn):
    flow = 0
    global start_counter
    while True:
        # start_counter = 1
        # time.sleep(2)
        # start_counter = 0
        # flow = (count / 7.5) 
        # print("The flow is: %.3f Liter/min" % (flow))
        # count = 0
        flow = random.random()

        # print(temperature)
        csvWrite([flow], fn)
        time.sleep(2)

startLogs(filename1)
