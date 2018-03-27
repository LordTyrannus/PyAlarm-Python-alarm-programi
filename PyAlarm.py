from playsound import playsound
from time import sleep
from datetime import datetime
import ctypes
from os import system
from timing import *
from sys import exit

mesage="""===============================
         PyAlarm : Python alarm programi
      -Kubilay Gezer-26.03.2018 : 23.33
            -1 Sesli alarm kur.
            -2 Sesli ve uygulama kapatmali kur.
            -3 Cikis
===============================
"""

Cikis=0
Ciki=0

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def ControlTime(alar):
   curtime=datetime.now().strftime("%H:%M")
   if str(curtime)==str(alar):
       print("--- "+str(alar)+" vaktine olan alarm caliyor...")
       playsound("alarm1.wav")
       sleep(12)
       exit()

def ControlTimeEndProcess(alar,uygulama):
   curtime=datetime.now().strftime("%H:%M")
   if str(curtime)==str(alar):
       system("TASKKILL /IM "+str(uygulama))
       print(uygulama+" programi kapatildi ve alarm caliyor...")
       playsound("alarm1.wav")
       sleep(12)
       exit()

while not Cikis==1:
   print str(mesage)
   secim=input(">Secim yapin: ")
   if secim==1:
      alar=raw_input(">Saat girin (Sa, Dak, ve aralarinda iki nokta): ")
      Cikiss=True
      Cikis=1
   elif secim==2:
      alar=raw_input(">Saat girin (Sa, Dak, ve aralarinda iki nokta): ")
      uygulama=raw_input(">Alarm ile kapatilacak task: ")
      Cikiss=True
      Cikis=1
      Ciki=1
   elif secim==3:
      print(">Cikiliyor....")
      Cikis=1

while Cikiss==True:
   if Ciki==1:
      ControlTimeEndProcess(alar,uygulama)
      sleep(1)
   if Ciki==0:
      ControlTime(alar)
      sleep(1)
