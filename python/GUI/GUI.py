import sys
#import smbus2 as smbus#,smbus2
import time
# Slave Addresses
#I2C_SLAVE_ADDRESS = 11 #0x0b ou 11


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
            BytesToSend = ConvertStringsToBytes(r)
        # print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(r) + " command.")
            print(BytesToSend )
            #I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, r, BytesToSend)

        elif t=="turn left" :

            print("Move to left")
            
            BytesToSend = ConvertStringsToBytes(f)
            #print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(f) + " command.")
            print(BytesToSend )
            #I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)

        elif t=="forward" :

            print("Move to forward")
            
            BytesToSend = ConvertStringsToBytes(f)
        # print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(f) + " command.")
            print(BytesToSend )
            #I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)
    
            
        elif t=="back" :

            print("Move to back")
            BytesToSend = ConvertStringsToBytes(b)
            #print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(b) + " command.")
            print(BytesToSend )
            #I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)
    

        else :

            print("Stop")
            BytesToSend = ConvertStringsToBytes(s)
            #print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(s) + " command.")
            print(BytesToSend )
            #I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)
    

    except sr.UnknownValueError as U:

        print (U)

    except sr.RequestError as R:

        print (R)
    
def Right():
    print("To Right")
    BytesToSend = ConvertStringsToBytes(s)
    #print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(s) + " command.")
    print(BytesToSend )
    #I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, r, BytesToSend)
            
def Left():
    print("To Left")
    
def Back():
    print("To Back")
    
def Forward():
    print("To Forward")
    
        
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