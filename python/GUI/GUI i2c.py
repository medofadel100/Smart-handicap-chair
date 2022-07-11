import sys
import smbus2 as smbus#,smbus2
import time
# Slave Addresses
addr = 0x0b # bus address
from smbus import SMBus
bus = SMBus(1) # indicates /dev/ic2-1

from gtts import gTTS 
from playsound import playsound

import speech_recognition as sr
r=sr.Recognizer()


from cgitb import text
from sqlite3 import Row
import tkinter
from tkinter import font
from tkinter import ttk
form=tkinter.Tk()
form.geometry("800x480")
psinfo= str(form.winfo_screenwidth()) +"x" +str(form.winfo_screenheight())
form.title(psinfo)
form.config(background="navy")
form.resizable(False,False)


    
    
def ConvertStringsToBytes(src):
  converted = []
  for b in src:
    converted.append(ord(b))
  return converted

def Alarm():
    print("Alartm")
    bus.write_byte(addr, 1) # switch it on

def Voice():
    print("Voice Order")
    with sr.Microphone() as src:
        print('say something....') 
        audio=r.listen(src)
        
    try:
        t=r.recognize_google (audio)

        print(t)

        f=open('text.text', 'a')

        f.writelines (t+"\n")

        f.close()

        obj=gTTS(text=t, lang='en', slow=False)

        if t== "turn right" :
            
            print("Move to right")
            bus.write_byte(addr, 2) # switch it on
            time.sleep(1)
            bus.write_byte(addr, 6)

        elif t=="turn left" :

            print("Move to left")
            
            bus.write_byte(addr, 3) # switch it on
            time.sleep(1)
            bus.write_byte(addr, 6)

        elif t=="forward" :

            print("Move to forward")
            
            bus.write_byte(addr, 4) # switch it on
            time.sleep(1)
            bus.write_byte(addr, 6)
            
        elif t=="back" :

            bus.write_byte(addr, 5) # switch it on
            time.sleep(1)
            bus.write_byte(addr, 6)
    

        else :

            print("Stop")
            bus.write_byte(addr, 6) # switch it on
    

    except sr.UnknownValueError as U:

        print (U)

    except sr.RequestError as R:

        print (R)
    
def Right():
    print("To Right")
    bus.write_byte(addr, 2) # switch it on
    time.sleep(1)
    bus.write_byte(addr, 6)
            
def Left():
    print("To Left")
    bus.write_byte(addr, 3) # switch it on
    time.sleep(1)
    bus.write_byte(addr, 6)
    
def Back():
    print("To Back")
    bus.write_byte(addr, 5) # switch it on
    time.sleep(1)
    bus.write_byte(addr, 6)
    
def Forward():
    print("To Forward")
    bus.write_byte(addr, 4) # switch it on
    time.sleep(1)
    bus.write_byte(addr, 6)
    
        
lbl1=ttk.Label(form,text="Smart Stand Up WheelChair")
lbl1.config(background="red",foreground="lightblue",font=("tahoma",21),padding=(20,10))
btns1=ttk.Style()
btns1.configure("TButton",font=("tahoma",25))
btn1=ttk.Button(form,text="Alarm",style="TButton",command = Alarm)
btns2=ttk.Style()
btns2.configure("TButton",font=("tahoma",25))
btn2=ttk.Button(form,text="Voice Order",style="TButton",command = Voice)
btns3=ttk.Style()
btns3.configure("TButton",font=("tahoma",25))
btn3=ttk.Button(form,text="Right",style="TButton",command = Right)
btns4=ttk.Style()
btns4.configure("TButton",font=("tahoma",25))
btn4=ttk.Button(form,text="Left",style="TButton",command = Left)
btns5=ttk.Style()
btns5.configure("TButton",font=("tahoma",25))
btn5=ttk.Button(form,text="Back",style="TButton",command = Back)
btns6=ttk.Style()
btns6.configure("TButton",font=("tahoma",25))
btn6=ttk.Button(form,text="Forward",style="TButton",command = Forward)
lbl1.grid(row=0,column=20)
btn1.grid(row=3,column=5,pady=60)
btn2.grid(row=3,column=35)
btn3.grid(row=9,column=35)
btn4.grid(row=9,column=5)
btn5.grid(row=12,column=20)
btn6.grid(row=6,column=20)


form.mainloop()