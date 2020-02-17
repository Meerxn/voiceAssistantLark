# -*- coding: utf-8 -*-
# Speech assistant beta: Fardeen Meeran
# email: fardeenfmeeran@gmail.com
# Spyder IDE

import os # User os system import
import sys 
import speech_recognition as listener # Listener import
def myCommand():
   
    r = listener.Recognizer()
    with listener.Microphone() as source:
        print('Listening') # Telling user that they are being heard
        r.pause_threshold= 0.8 # Duration for pausing 
        r.adjust_for_ambient_noise(source, duration=1) 
        userSpeech = r.listen(source)
    try: 
         
        command = r.recognize_google(userSpeech).lower()
    
      
    except listener.UnknownValueError:
        print(' Please try speaking again')
        command = myCommand();
    return command
def larkSpeaks(userSpeech):
    for line in userSpeech.splitlines():
        os.system("say " + userSpeech)
def lark(command):
    
    if 'hello' in command:
        
            larkSpeaks('Hello how are you doing today:?')
    elif ' I am good ' in command:
             lark('that is great ')
          
        
    elif 'goodbye' in command:
     larkSpeaks(' see ya broski')
     sys.exit()
larkSpeaks('Hello welcome to the Lark experience.')

while True:
    lark(myCommand())
