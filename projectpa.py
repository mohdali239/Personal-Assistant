import tkinter 
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import subprocess
import pyttsx3
import pyaudio
import webbrowser
import datetime
import speech_recognition as sr
from PIL import ImageTk, Image, ImageOps

engine = pyttsx3.init()
engine.setProperty('rate' ,150)

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'C:/chatterbot-corpus-master/chatterbot_corpus/data/english/'

for file in os.listdir(corpus_path):
        trainer.train(corpus_path + file)
engine.say("Hi I am your personal assistant")
engine.runAndWait()
def convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.5)
        #print('Speak Anything:')
        audio = r.listen(source)
        reply = "Got Nothing"
        try:
            spokenText = r.recognize_google(audio) 
            #prevText = label['text'] 
            #reply = "hi"    
            label.config(text = spokenText) 
            if spokenText=="open calculator":
                subprocess.call(['calc'])
                reply="Calculator Application is opened"
            
            elif spokenText=="open Notepad":
                subprocess.call(['notepad.exe'])
                reply="Notepad Application is opened"

            elif spokenText=="open window Media Player":
                subprocess.call(['C:/Program Files (x86)/Windows Media Player/wmplayer.exe'])
                reply="Windows Media Player Application is opened"

            elif spokenText=="open Google Chrome":
                subprocess.call(['C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'])
                reply="Google Chrome Application is opened"

            elif spokenText=="open Excel":
                subprocess.call(['C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'])
                reply="Microsoft Excel Application is opened"

            elif spokenText=="open PowerPoint":
                subprocess.call(['C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE'])
                reply="Microsoft Powerpoint Application is opened"

            elif spokenText=="open Google":
                webbrowser.open('https://www.google.com/')
                reply="Google Application is opened"

            elif spokenText=="open YouTube":
                webbrowser.open('https://www.youtube.com')
                reply="Youtube Website is opened"

            elif spokenText=="open Gmail":
                webbrowser.open('https://www.gmail.com')
                reply="Youtube Website is opened"

            elif spokenText=="open FaceBook":
                webbrowser.open('https://www.fb.com')
                reply="Facebook Website is opened"
            
            elif spokenText=="what is the time":

                now = datetime.datetime.now()
                engine.say(now.strftime("The time is %H:%M"))
                reply="telling you the time"
                engine.runAndWait()

            else:   
                                
                
                reply = bot.get_response(spokenText)
                
                #labelText = prevText + spokenText 
                #print(reply)
                
                
                engine.say(reply)
                engine.runAndWait()
            replyLabel.config(text=reply)
                        
                        #engine.say(reply)
                        #engine.runAndWait()
        except:
            print('Sorry could not recognize your voice.')
            print(reply)
window = tkinter.Tk()
window.title("Personal Assistant")
window.geometry('1600x900')
path="background.gif"
#background



#background

Img = ImageTk.PhotoImage(Image.open(path))
backgroundLabel = tkinter.Label(window,image=Img)
backgroundLabel.place(x=0,y=0,relwidth=1,relheight=1)
label = tkinter.Label(window,text="Click on Speak button for chatting",font=('Comic Sans MS',25),fg="green")
label.pack()
#speakbutton
loadimage = tkinter.PhotoImage(file="speak1.png")
roundedbutton = tkinter.Button(image=loadimage, command=convert)
roundedbutton["bg"] = "black"
roundedbutton["border"] = "20"
roundedbutton.pack(side="right")




#quitbutton
loadimage2 = tkinter.PhotoImage(file="quit1.png")
roundedbutton2 = tkinter.Button(image=loadimage2, command=quit)
roundedbutton2["bg"] = "black"
roundedbutton2["border"] = "20"
roundedbutton2.pack(side="left")


#frame

#tkinter.Label(text="one").pack()

separator = tkinter.Frame(height=2, bd=1)
replyLabel = tkinter.Label(window,text="", font=('Comic Sans MS',22),fg="black")
replyLabel.pack()
#separator.pack(fill=X, padx=5, pady=5)

#tkinter.Label(text="two").pack()

#bottom_frame=tkinter.Frame(window).pack(side="bottom")






#label = tkinter.Label(window,text="Hello World").pack()
window.mainloop()
