from lights import Lights
import os
import time
from threading import Thread

from subprocess import call

l = Lights(39)

def fan(arg):
    call(["sudo", "./uhubctl", "-p", "2", "-a", arg])

def lightsPattern():
    for i in range(2):
        if i%2 == 0:
            l.fillEach((100,0,0), 0.05)
        else:
            l.fillEach((0,0,100), 0.05)

def lightsOff():
    l.fillEach((0,0,0), 0.05)


print("Options\n-----------------\n0. Fan Off\n1. Fan on\n2. Lights going\n3. Lights red\n4. Lights Blue\n5. Lights off\n---------------------\n")
while True:
    option = input("Enter option: ")
    if option == '0':
        fan('0')
    elif option == '1':
        fan('1')
    elif option == '2':
        lightsPattern()
    elif option == '3':
        l.fillEach((100,0,0),0.1)
    elif option == '4':
        l.fillEach((0,0,100),0.1)
    elif option == '5':
        lightsOff()
