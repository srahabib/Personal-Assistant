import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import time
import re
import random
#import pyjokes

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !")

    assistantName =("shizo")
    speak("I am your Assistant")
    speak(assistantName)

def username():
    speak("what should I call you")
    userName =takeCommand()
    speak("welcome Mister")
    speak(userName)    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        #my query
        query = r.recognize_google(audio,language ='en')
        print(f"user : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"
    return query

if __name__ == '__main__':
   
   
   wishMe()
   #username()

   

while True:

    query = takeCommand().lower()

    if 'wikipedia' in query:
       speak('Searching Wikipedia...')
       query = query.replace("wikipedia", "")
       results = wikipedia.summary(query, sentences = 2)
       speak("According to Wikipedia")
       print(results)
       speak(results)

       #use re to search the word after open
    
    elif'open' in query:
       speak("opening now")
       getAfterOpen=query
       print(query)
       getAfterOpen=getAfterOpen.split("open",1)[1]
       print(getAfterOpen)
       getWebName=getAfterOpen.split(None,1)[0]
       print(getWebName)
       url = getWebName+".com"
       print(url)
       chrome_path ="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
       webbrowser.get(chrome_path).open(url)       


    elif 'the time' in query:
       strTime = datetime.datetime.now().strftime("%I:%M") 
       speak(f"the time is {strTime}")

    #elif assistantName in query: #query==assname / assname in query
       #wishMe()
       #speak('Im in your service")

    elif "change my name to" in query:
       query = query.replace("change my name to", "")
       userName = query

    elif "change your name" in query:
       speak("What would you like to call me, Sir ")
       assistantName = takeCommand()
       speak("Thanks for naming me")

    elif "what is your name " in query:
       speak("my name is ")
        #speak(assistantName)

    elif "my name " in query:
       speak("your name is ")
       speak(userName)

               
                  
