import os
import time
import pyttsx3

engine = pyttsx3.init()


def noise(fileName):
    os.popen("ffplay " + fileName)



print("Options\n-----------------\n0. Siren\n1. Help is on the way.\n2. Where are you\n3. What happened\n4. How do you feel\n5. On the way\n6. Find help\n7. Ask around\n---------------------\n")
while True:
    option = input("Enter option: ")
    if option == '0':
         noise("siren.mp3")
    elif option == '1':
         noise("hello.mp3")
    elif option == '2':
         noise("do-you.mp3")
    elif option == '3':
         noise("what-happened.mp3")
    elif option == '4':
         noise("describe.mp3")
    elif option == '5':
         noise("first-responders.mp3")
    elif option == '6':
         noise("okay.mp3")
    elif option == '7':
         noise("excuse-me.mp3")
