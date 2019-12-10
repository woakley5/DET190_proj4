from lights import Lights
import os
import time

from subprocess import call
call(["sudo", "./uhubctl", "-p", "2", "-a", "1"])

while True:
    call(["sudo", "./uhubctl", "-p", "2", "-a", "1"])
    print("Fan on!")
    time.sleep(10)
    call(["sudo", "./uhubctl", "-p", "2", "-a", "0"])
    print("Fan off!")
    time.sleep(10)
