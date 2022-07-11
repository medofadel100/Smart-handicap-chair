#library
import sys
import smbus2 as smbus#,smbus2
import time
# Slave Addresses
I2C_SLAVE_ADDRESS = 11 #0x0b ou 11
I2Cbus = smbus.SMBus(0)
def ConvertStringsToBytes(src):
  converted = []
  for b in src:
    converted.append(ord(b))
  return converted


from gtts import gTTS from playsound import playsound

import speech_recognition as sr
r=sr.Recognizer()

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
        print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(r) + " command.")
        print(BytesToSend )
        I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)

    elif t=="turn left" :

        print("Move to left")
        
        BytesToSend = ConvertStringsToBytes(f)
        print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(f) + " command.")
        print(BytesToSend )
        I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)

    elif t=="forward" :

        print("Move to forward")
        
        BytesToSend = ConvertStringsToBytes(f)
        print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(f) + " command.")
        print(BytesToSend )
        I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)
 
        
    elif t=="back" :

        print("Move to back")
        BytesToSend = ConvertStringsToBytes(b)
        print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(b) + " command.")
        print(BytesToSend )
        I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)
 

    else :

        print("Stop")
        BytesToSend = ConvertStringsToBytes(s)
        print("Sent " + str(I2C_SLAVE_ADDRESS) + " the " + str(s) + " command.")
        print(BytesToSend )
        I2Cbus.write_i2c_block_data(I2C_SLAVE_ADDRESS, 0x00, BytesToSend)
 

except sr.UnknownValueError as U:

    print (U)

except sr.RequestError as R:

    print (R)