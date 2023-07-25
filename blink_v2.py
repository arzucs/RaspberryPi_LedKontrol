from tkinter import *
#arayuz olusturmak icin gereken kutuphane,tkinter modulunu tum ogeleri ile birlikte cagirmis oluruz
import tkFont 
from tkinter.font import Font
import RPi.GPIO as GPIO
import time
win = Tk()
#bu komutu kullanarak tkinter icindeki tk adli komutu cagirmis olduk
win.title(">> LED GUI ^.^ <<")#pencere ismi
win.geometry('330x380+450+250')#boyut+konumx+konumy gibi

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)

myFont = tkFont.Font(family = 'Georgia', size = 15, weight = 'bold')
def ledON1(): #led acip kapatma fonksiyonu
    print("LED button pressed")
    if GPIO.input(40):
       GPIO.output(40,GPIO.LOW)
       ledButton1["text"] = "1 LED YAK"
    else:
       GPIO.output(40,GPIO.HIGH)
       ledButton1["text"] = "1 LED KAPAT"
       
def ledON2():
    print("LED button pressed")
    if GPIO.input(38) & GPIO.input(40):
       GPIO.output(38,GPIO.LOW)
       GPIO.output(40,GPIO.LOW)
       ledButton2["text"] = "2 LED YAK"
    else:
       GPIO.output(38,GPIO.HIGH)
       GPIO.output(40,GPIO.HIGH)
       ledButton2["text"] = "2 LED KAPAT"
       
def ledON3():
    print("LED button pressed")
    if GPIO.input(40) & GPIO.input(38) & GPIO.input(36):
       GPIO.output(36,GPIO.LOW)
       GPIO.output(38,GPIO.LOW)
       GPIO.output(40,GPIO.LOW)
       ledButton3["text"] = "Hepsini Yak"
    else:
          GPIO.output(38,GPIO.HIGH)
          time.sleep(1)
          GPIO.output(36,GPIO.HIGH)
          time.sleep(1)
          GPIO.output(40,GPIO.HIGH)
          time.sleep(1)
          ledButton3["text"] = "Hepsini Kapat"
          
def exitProgram():
   print("Exit Button pressed")
   GPIO.cleanup()
   win.quit() #tiklaninca pencereyi kapatmak icin

ledButton1 = Button(win, text = "1 LED YAK",bg="#000066",fg="#00FF66", font = myFont, command = ledON1, height = 1, width =10 )
ledButton1.pack(pady=6)#buton .pack olmazsa gorunmez yani paketlemek gerekli

ledButton2 = Button(win, text = "2 LED YAK",bg="#000066",fg="#00FF66", font = myFont, height = 1,command= ledON2, width =10 )
ledButton2.pack(pady=6)#ledButton1 ve ledButton2 arasina y duzleminde 10 birimlik bosluk
#birakmis olduk padx deseydik x duzleminde bosluk birakirdik

ledButton3 = Button(win, text = "Hepsini Yak",bg="#000066",fg="#00FF66", font = myFont, height = 2,command= ledON3, width =10 )
ledButton3.pack(pady=6)#command ledON3 fonksiyonuna git

exitButton  = Button(win, text = "Exit", font = myFont,bg="#000066",fg="#00FF66", command = exitProgram, height =1 , width = 10)
exitButton.pack(side = BOTTOM)# parantez icine buton konumu side ile belirtilir bottom alta alinmasini saglar

mainloop()
"""Tk() ile olusturulan pencere mainloop() satiri ile bir dongu
olusturularak acilan pencerenin daima ekranda gorunur 
kalmasi saglanir. Eger bu yapi kullanilmazsa pencere 
ekranda gorunup hemen kaybolur. Bu nedenle pencereyi 
biz goremeyiz.""" 
