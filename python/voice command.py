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

    elif t=="turn left" :

        print("Move to left")

    elif t=="forward" :

        print("Move to forward") 
        
    elif t=="back" :

        print("Move to back")

    else :

        print("Stop")

except sr.UnknownValueError as U:

    print (U)

except sr.RequestError as R:

    print (R)