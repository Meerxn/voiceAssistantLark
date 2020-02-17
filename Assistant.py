# -*- coding: utf-8 -*-
# Name: Lark
# Speech assistant beta: Fardeen Meeran
# email: fardeenfmeeran@gmail.com

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
    
      
    except LookupError: # speech is unintelligible
        print("Could not understand audio")
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
     larkSpeaks('goodbye and have a good day')
     sys.exit()
larkSpeaks('Hello welcome to the Lark experience.')

while True:
    lark(myCommand())
