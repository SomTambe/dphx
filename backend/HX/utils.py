import HX
import subprocess
import csv
import glob
from .models import *

def startRel():
    f = glob.glob('**/relay.py')[0]
    p = subprocess.Popen(['python', f, str(getStpt())])
    return p

def liveSetPt(csvfile):
    with open(csvfile) as file:
        for line in file:
            pass
        print(line)
        return line.split('\n')[0]

def getStpt():
    h = HX.objects.get(id=1)
    tst = h.Tsetpt
    if tst > 70:
        tst = 70
    elif tst < 40:
        tst = 40
    return tst

def stopRel(p):
    p.terminate()

def startFlowReading():
    f1, f2 = glob.glob("**/flow_*.py", recursive=True)
    p1 = subprocess.Popen(['python', f1])
    p2 = subprocess.Popen(['python', f2])
    return p1, p2

def stopFlowReading(p1, p2):
    p1.terminate()
    p2.terminate()

def getLastLine(csvfile):
    with open(csvfile) as file:
        for line in file:
            pass
        print(line)
        return line.split('\n')[0]

def startTempReading():
    f = glob.glob('**/HX.py')[0]
    p = subprocess.Popen(['python', f])
    return p

def writeCurrTempValues(vals):
    """
    vals: comma seperated string
    Currently only store 1 set of values in the database.
    """
    t1, t2, t3, t4 = vals.split(',')
    h = HX.objects.get(id=1)
    h.Tcin = t1
    h.Tcout = t2
    h.Thin = t3
    h.Thout = t4
    h.save()

def writeCurrFlowValues(vals):
    """
    vals: comma seperated string
    Currently only store 1 set of values in the database.
    """
    f1, f2 = vals.split(',')
    h = HX.objects.get(id=1)
    h.Fcold = f2
    h.Fhot = f1
    h.save()

def stopTempReading(p):
    p.terminate()
