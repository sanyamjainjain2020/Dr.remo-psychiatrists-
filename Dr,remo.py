from tkinter import *
import PIL.Image, PIL.ImageTk

import pyttsx3
import speech_recognition as sr
import datetime
import os
import smtplib
import sys
import wikipedia
import pywhatkit as kit
import webbrowser

from PIL import Image


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',180)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        var.set("good morning!")
        window.update()
        speak("good morning!")
    elif hour>=12 and hour<=18:
        var.set("good afternoon!")
        window.update()
        speak("good afternoon!")
    else:
        var.set("good evening!")
        window.update()
        speak("good evening!")
    speak("this is doctor remo how can i help you")

def takecommand():
    #it take mic input from user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("listning......")
        window.update()
        print("listning......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5)
    # try for print without any error
    try:
        var.set("recoginizition......")
        window.update()
        print("recoginizition......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    # if cant recognize voice
    except Exception as e:
    #    speak("say it again please sir")
        return "none"
    var1.set(query)
    window.update()
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sanyamsanyam2016@gmail.com','*************')
    server.sendmail('sanyamjainjain2020@gmail.com',to, content)
    server.close()
def emaildata():
    str("he is not well")
    print(str)    

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
    #if 1:
    
        query = takecommand().lower()
        if 'exit' in query:
            var.set("Bye and stay home stay safe")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye and stay home stay safe")
            break

        elif"open notepad"in query:
            var.set('opening')
            window.update()
            speak('opening')
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif"i am not good"in query:
            var.set('dont worry sir i am hear')
            window.update()
            speak("dont worry sir i am hear")
            var.set('what is your problem')
            window.update()
            speak("what is your problem")
            takecommand().lower()
            var.set("i am prescribing some medicine. do yoga. and after its not work take aspirin and nalfon")
            window.update()
            speak("i am prescribing some medicine. do yoga. and after its not work take aspirin and nalfon")
            var.set("perasitamol and do yoga")
            window.update()
            print("perasitamol and do yoga")
        

        elif"i want to die"in query:
            try:
                var.set("please dont do this look at your mom and dad. you can tall your problem to me")
                window.update()
                speak("please dont do this look at your mom and dad. you can tall your problem to me")
                npath = "C:\\Users\\hjg\Desktop\\dr remo code\\images\\mom.jpg"
                os.startfile(npath)
                content = str("he is not good call him.I am his doctor")
                #content = takecommand().lower()
                to = "sanyamjainjain2020@gmail.com"
                sendEmail(to, content)
                var.set("i told to your friend alhil")
                window.update()
                speak("i told to your friend akhil")
            except Exception as e:
                print(e)
                var.set("please dont do this i am here")
                window.update()
                speak("please dont do this i am here")
        #---------------------------------------------------whatsapp------------        
        elif"i got fight with my best friend"in query:
            try:
                var.set("talk to him. and say sorry. other wise you lose your friend")
                window.update()
                speak("talk to him. and say sorry. other wise you lose your friend")
                kit.sendwhatmsg("+918770158393","pleas save him",0,1)
                
            except Exception as e:
                print(e)
                speak("talk to him. and say sorry. other wise you lose your friend")
        elif"feeling bad"in query:
            var.set("want meditation or medicine")
            window.update()
            speak("want meditation or medicine")
            query = takecommand().lower()
            if"meditation"in query:
                webbrowser.open("https://www.youtube.com/watch?v=OEhAsM-uEjM")
                var.set("injoy yor meditation")
                window.update()
                speak("injoy yor meditation")
                #sys.exit()
            else:
                var.set("perasitamol and do yoga")
                window.update()
                speak("perasitamol and do yoga")
        elif"i have fever"in query:
            var.set("what is your temperature in centigrade")
            window.update()
            speak("what is your temperature in centigrade")
            query = takecommand()
            if (int(query))<100:
                var.set("you are good dont wory")
                window.update()
                speak("you are good dont wory")
            else:
                var.set("can you feel smale")
                window.update()
                speak("can you feel smale")
                query = takecommand().lower()
                if"no"in query:
                    var.set("do you have cough and cold")
                    window.update()
                    speak("do you have cough and cold")
                    query = takecommand().lower()
                    if"yes"in query:
                        var.set("probably you have corona virus. please go for check up. till then i am prescribing you some medicine")
                        window.update()
                        speak("probably you have corona virus. please go for check up. till then i am prescribing you some medicine")
                        var.set("take peracitamol and cough syrup")
                        window.update()
                        speak("take peracitamol and cough syrup")
        elif"i am feeling as a loser"in query:
            query.replace("mi", "")
            var.set("no sanyam. you are not loser. you made me. and you doveloped laundry wala website for s a t i")
            window.update()
            speak("no sanyam. you are not loser. you made me. and you doveloped laundry wala website for s a t i")

        elif"no thanks"in query:
            var.set("thanks for using me")
            window.update()
            speak("thanks for using me")
            sys.exit()
        elif"thanks"in query:
            var.set("Bye and stay home stay safe")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye and stay home stay safe")
            break
        
        speak("please tell your problem")






def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Dr.remo(Sanyam Jain)SATI')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
