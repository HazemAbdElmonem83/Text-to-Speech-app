import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root = Tk() 
root.title("SpeakEasy")
root.geometry("1680x900")
root.resizable(False,False)
root.configure(bg="#450011")

eng=pyttsx3.init()
def convert() :
    text=text_plac.get(1.0,END)
    Gender=gender.get()
    Speed=speed.get()
    voices=eng.getProperty('voices')
    def setvoice():
        if(Gender=='Male'):
            eng.setProperty('voice', voices[0].id)
            eng.say(text)
            eng. runAndWait()
        else:
              eng.setProperty('voice', voices[1].id)
              eng.say(text)
              eng. runAndWait()  
    if(text):
        if(Speed=="Fast"):
            eng.setProperty('rate',250)
            setvoice()
        elif(Speed=="Normal"):
                 eng.setProperty('rate', 150)
                 setvoice()
        else:
             eng.setProperty('rate',60)
             setvoice()         
            

def download():
    text=text_plac.get(1.0,END)
    Gender=gender.get()
    Speed=speed.get()
    voices=eng.getProperty('voices')
    def setvoice():
        if(Gender=='Male'):
            eng.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            eng.save_to_file(text,'text.mp3')
            eng. runAndWait()
        else:
              eng.setProperty('voice', voices[1].id)
              eng.setProperty('voice', voices[0].id)
              path=filedialog.askdirectory()
              os.chdir(path)
              eng.save_to_file(text,'text.mp3')
              eng. runAndWait()  
    if(text):
        if(Speed=="Fast"):
            eng.setProperty('rate',250)
            setvoice()
        elif(Speed=="Normal"):
                 eng.setProperty('rate', 150)
                 setvoice()
        else:
             eng.setProperty('rate',60)
             setvoice()


#icon
icon=PhotoImage(file="3.png")
root.iconphoto(False,icon)
#text area
font_tuple = ("Comic Sans MS", 20, "bold")
text_plac=Text(root,font=font_tuple,bg="#e5dcde",relief=GROOVE,wrap=WORD)
text_plac.place(x=50,y=300,width=700,height=400)

#combobox

font_tuple2 = ("Comic Sans MS", 14, "bold")
font_tuple3 = ("Comic Sans MS", 20, "bold")
Label(root,text="Voice",font=font_tuple3,bg="#450011",fg="white").place(x=1000,y=250)
gender=Combobox(root,values=['Male','Famale'],font=font_tuple2,state='r',width=10)
gender.place(x=1000,y=300,width=200)
gender.set('Male')
Label(root,text="Speed",font=font_tuple3,bg="#450011",fg="white").place(x=1300,y=250) 
speed=Combobox(root,values=['Fast','Normal','Slow'],font=font_tuple2,state='r',width=10)
speed.place(x=1300,y=300,width=200)
speed.set('Normal')  
#button
convert_icon=PhotoImage(file="2.png")
convert_btn=Button(root,text="Speak",compound=LEFT,image=convert_icon,width=150,font=font_tuple2,command=convert)
convert_btn.place(x=1000,y=500)





download_icon=PhotoImage(file="5.png")
download=Button(root,text=" download",compound=LEFT,image=download_icon,width=150,font=font_tuple2,command=download)
download.place(x=1300,y=500)






root.mainloop()