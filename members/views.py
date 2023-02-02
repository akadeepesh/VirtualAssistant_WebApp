from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

#importing modules/libraries
#---------------------------------------------------------------------------#
from operator import index
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui as pg
import time
import os
import sys
import random
import webbrowser
import math
from AppOpener import run
#---------------------------------------------------------------------------#

# def easy(request):

#     #activating voice
#     #---------------------------------------------------------------------------#
#     def speak(command):
#         engine = pyttsx3.init()
#         engine.say(command)
#         engine.runAndWait()
#     #---------------------------------------------------------------------------#

#     #activating microphone
#     #---------------------------------------------------------------------------#
#     r = sr.Recognizer()
#     m = sr.Microphone()
#     try:
#         speak("A moment of silence, please...")
#         with m as source: r.adjust_for_ambient_noise(source, duration=2)
#         speak("Set minimum energy threshold to {}".format(r.energy_threshold))
#     except KeyboardInterrupt:
#         pass
#     #---------------------------------------------------------------------------#





#     #Take command and store in 'value'
#     #---------------------------------------------------------------------------#
#     def bol():
#         speak("Say something!")
#         with m as source: audio = r.listen(source,timeout=10,phrase_time_limit=10)
        
#         speak("Got it! Now to recognize it...")
#         try:
#             value = r.recognize_google(audio)
#             value = value.lower()
#             ignore = ["that's great", "wow", "amazing", "sad", "nice"]
#             for i in ignore:
#                 if(i in value):
#                     value = value.replace(i, "")
#             if('dipesh' in value):
#                 value.replace('dipesh','deepesh')
#         except sr.UnknownValueError:
#             speak("Oops! Didn't catch that")
#         except sr.RequestError as e:
#             speak("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
#         context = {
#             'value' : value,
#         }
#         return render(request, "/", context)
#     #---------------------------------------------------------------------------#


# #---------------------------------------------------------------------------#
# def typewrite():
#     speak("Tell me what you want to write here")
#     value = bol()
#     pg.typewrite(value)
#     pg.press("enter")
#     a = ["quit", "exit", "bye", "leave me alone"]
#     for i in a:
#         if(i in value):
#             return value
# #---------------------------------------------------------------------------#


# #---------------------------------------------------------------------------#
# def calculator():
#     value = bol()
#     while("into" in value):
#         b = 1
#         a = value.split()
#         c = a.index("into")
#         d = str(float(a[c-1])*float(a[c+1]))
#         a.pop(c-1)
#         a.pop(c-1)
#         a.pop(c-1)
#         a.insert(c-1,d)
#         value = ' '.join(a)
#     while("by" in value):
#         b = 1
#         a = value.split()
#         c = a.index("by")
#         d = str(float(a[c-1])/float(a[c+1]))
#         a.pop(c-1)
#         a.pop(c-1)
#         a.pop(c-1)
#         a.insert(c-1,d)
#         value = ' '.join(a)
#     while("+" in value):
#         b = 1
#         a = value.split()
#         c = a.index("plus")
#         d = str(float(a[c-1])+float(a[c+1]))
#         a.pop(c-1)
#         a.pop(c-1)
#         a.pop(c-1)
#         a.insert(c-1,d)
#         value = ' '.join(a)
#     while("+" in value):
#         b = 1
#         a = value.split()
#         c = a.index("minus")
#         d = str(float(a[c-1])-float(a[c+1]))
#         a.pop(c-1)
#         a.pop(c-1)
#         a.pop(c-1)
#         a.insert(c-1,d)
#         value = ' '.join(a)
#     flt = float(value)
#     value = round(flt, 3)
#     speak(value)
#     speak(value)
# #---------------------------------------------------------------------------#

# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
    
# #---------------------------------------------------------------------------#
# def calcci():
#     value = bol()
#     a = value.split()
#     while("log" in a):
#         ind = a.index("log")
#         num = math.log(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
    
#     while("sin" in value):
#         ind = a.index("sin")
#         num = math.sin(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
#     while("cos" in value):
#         ind = a.index("cos")
#         num = math.cos(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
#     while("tan" in value):
#         ind = a.index("tan")
#         num = math.tan(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
#     while("sec" in value):
#         ind = a.index("sec")
#         num = math.sec(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
#     while("cosec" in value):
#         ind = a.index("cosec")
#         num = math.cosec(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
#     while("cot" in value):
#         ind = a.index("cot")
#         num = math.cot(float(a[ind+1]))
#         a.pop(ind)
#         a.pop(ind)
#         num = str(num)
#         a.insert(ind,num)
#         value = ' '.join(a)
#     while("ki" in a and "power" in a):
#         ind = a.index("ki")
#         num = str(math.pow(float(a[ind-1]),float(a[ind+2])))
#         for i in range(0,4):
#             a.pop(ind-1)
#         a.insert(ind,num)
#         value = ' '.join(a)
# #---------------------------------------------------------------------------#

# def whatsapp():
#     a = value.rfind("to")
#     message = value[3:a].strip()
#     person = value[a+2: ].strip()
    
#     if (person in 'DC_name'):
#         try:
#             #DC_phone -from dataset
#             pass
#         except:
#             #DC_mail
#             try:
#                 #DC_linkedin
#                 pass
#             except:
#                 #DC_instagram
#                 pass
#             pass
# #---------------------------------------------------------------------------#
# #---------------------------------------------------------------------------#
# def check():
#     global value
#     time.sleep(1)
#     value = bol()
#     if  'hello' in value:
#         speak("Hi, My name is DC...what's your")
#         b = bol()
#         a = ["my name is", "i am", "i'm"]
#         for j in a:
#             if(j in b):
#                 if("dipesh" in b):
#                     speak("Hi Deepesh, nice to meet you")
#                 else:
#                     speak("Hi "+ b.replace(j, "") +", nice to meet you")
#                     speak("Give me command now")
#                 break
#             else:
#                 speak("Hi" + b + "nice to meet you")
#                 speak("Give me command now")
#                 break
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if 'play' in value:
#         song = value.replace('play', '') + "audio"
#         speak("playing"+ song)
#         pywhatkit.playonyt(song)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if 'sing me a song' in value:
#         lis = ["farq hai", "kun faya kun", "bin tere reprise", "tere bin", "swaar loon", "mai bola hey!", "tere liye abdullah quereshi", "lamha lamha", "jiyen kyun", "saajna", "sajni boondh", "sadje", "khush to hai n", "ghar bharat chauhan", "tu hoti toh", "nit nit", "mera mann kehne laga", "O meri Jaan", "ya ali", "o sanam lucky ali"]
#         ran = random.choice(lis)
#         speak("playing",ran)
#         pywhatkit.playonyt(ran)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if("joke" in value):
#         My_joke = pyjokes.get_joke(language="en", category="all")
#         speak(My_joke)
#         speak(My_joke)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if "wikipedia" in value:
#         speak("Searching wikipedia...")
#         query = value.replace("wikipedia", "")
#         results = wikipedia.summary(query, sentences=1)
#         speak(results)
#     spl = value.split()
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if(spl[0]=="search" and spl[len(spl)-2]=="on" and spl[len(spl)-1] == "youtube"):
#         spl.pop(0)
#         spl.pop(len(spl)-2)
#         spl.pop(len(spl)-1)
#         a = (" ".join(spl))
#         url = f"https://www.youtube.com/results?search_query={a}"
#         webbrowser.get().open(url)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if(spl[0:2] == "where is"):
#         spl.pop(0)
#         spl.pop(1)
#         a = (" ".join(spl))
#         url = f"https://google.nl/maps/place/{a}/&amp;"
#         webbrowser.get().open(url)
#         speak(f"Here is the location of {a}.")
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

       
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if(spl[0]=="search" and spl[len(spl)-2]=="on" and spl[len(spl)-1] == "google"):
#         spl.pop(0)
#         spl.pop(len(spl)-2)
#         spl.pop(len(spl)-1)
#         a = (" ".join(spl))
#         url = f"https://www.google.com/search?q={a}"
#         webbrowser.get().open(url)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        
#     if "toss coin" in value:
#         coin_flip_with_random = "Heads" if random.random() > 0.5 else "Tails"
#         speak(f"You got {coin_flip_with_random}!")
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

        
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        
#     if "sleep" in value:
#         os.system('cmd /c "rundll32.exe powrprof.dll, SetSuspendState Sleep"')
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
       
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        
#     if("minimise" in value):
#         pg.click(x=1785, y=25, clicks = 1, button = "left", duration= 1)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        
#     if("close" in value):
#         pg.click(x=1919, y=1, clicks = 1, button = "left", duration= 1)
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
        

# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        
#     if("calculator" in value):
#         speak("Calculator activated")
#         speak("Tell me the equation")
#         calcci()
#         calculator()
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

       
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        
#     if("whatsapp" in value):
#         pass
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if("task manager" in value):
#         pg.hotkey('ctrl', 'shift', 'esc')
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#    
#     if("open" in value or "run" in value):
#         if("browser" in value):
#             run("microsoft edge")
#         elif("chrome" in value):
#             run("GOOGLE CHROME")
#         elif("whatsapp" in value):
#             run("WHATSAPP")
#         elif("word" in value):
#             run("WORD")
#         elif("ppt" in value or "powerpoint" in value):
#             run("POWERPOINT")
#         elif("wordpad" in value):
#             run("WORDPAD")
#         elif("notepad" in value or "note" in value):
#             run("notepad")
#         elif("vs" in value or "visual studio code" in value or "code editor" in value):
#             run("VISUAL STUDIO CODE")
#         elif("tg" in value or "telegram" in value):
#             run("telegram")
#         elif("this pc" in value):
#             run("this pc")
#         elif("settings" in value):
#             run("settings")
#         elif("paint" in value):
#             run("paint")
#         elif("dc" in value or "discord" in value):
#             run("DISCORD")
#         elif("camera" in value):
#             run("camera")
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     if("type here" in value):
#         while True:
#             typewrite()
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     # else:
#     #     file = open("check_these.txt", "a")
#     #     file.append(value,"\n")
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     a = ["quit", "exit", "bye", "leave me alone"]
#     for i in a:
#         if(i in value):
#             sys.exit()
# #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    
# #---------------------------------------------------------------------------#

# #---------------------------------------------------------------------------#  
# while True:
#     check()
# #---------------------------------------------------------------------------#


def Home(request):
      template = loader.get_template('Home.html')
      return HttpResponse(template.render())
# Create your views here.

def Whatsapp(request):
      template = loader.get_template('Whatsapp.html')
      return HttpResponse(template.render())
    
def details(request):
      mymembers = Member.objects.all().values()
      template = loader.get_template('Whatsapp.html')
      context = {      
            'mymembers': mymembers,
      }
      return HttpResponse(template.render(context, request))

# def tri(reuest):
#       pass
#       return render(request, "/", context)

'''
Commands:-
1)hello
	1.1)my name is/ I'm
2)play
3)sing me a song
4)joke
5)wikipedia
6)search ______ on youtube
7)search ______ on google
8)toss coin
9)sleep
10)minimize
11)close
12)calculator
	12.1) equation...like 2+8 or much complex
13)open/run (app name)
14)type here
'''