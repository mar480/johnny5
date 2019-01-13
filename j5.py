import speech_recognition as sr
from playsound import playsound
import random
import os

def j5():
	with mic as source:
	    r.adjust_for_ambient_noise(source)
	    audio = r.listen(source)
	    try:
	        a = r.recognize_google(audio)
	        print(a)
	        if a.__contains__('number'):
	            playsound(path + 'hey-laserlips.mp3')
	        elif a.__contains__('ok'):
	            playsound(random.choice(howAreYou))
	        elif a.__contains__('where'):
	            playsound(path + 'nova-robotics.mp3')
	        elif a.__contains__('off'):
	            playsound(path + 'no-disassemble-number-five.mp3')
	        elif a.__contains__('sorry'):
	            playsound(path + 'no-shit.mp3')
	        elif a.__contains__('play'):
	            g = random.choice(os.listdir(path))
	            playsound(path+g)
	        else:
	            playsound(random.choice(error))
	    except sr.RequestError:
	        print("Classic Google.... please can you repaeat that?")
	    except sr.UnknownValueError:
	        print("I didn't understand one of those words. Please try again!")

r = sr.Recognizer()
mic = sr.Microphone()

path = 'C:\\Users\\Future Rob\\Desktop\\j5\\audio\\'
pathFiles = os.listdir(path)

hi = path + 'hi.mp3'
hi2 = path + 'hi2.mp3'
hello=[hi, hi2]

fine = path + 'im-fit-as-a-fiddle.mp3'
fine2 = path + 'excelent.mp3'
howAreYou=[fine, fine2]

error1 = path + 'need-input.mp3'
error2 = path + 'try-again.mp3'
error3 = path + 'uh-oh.mp3'
error = [error2, error3]

playsound(error1)
print('I need input! Please talk to me :)')
while (True==True):
    j5()
