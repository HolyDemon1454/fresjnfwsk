import pyaudio
import speech_recognition as sr
import pyttsx3
import webbrowser
from random import randint 

voice = pyttsx3.init()
voice.say("Привет, я голосовой помощник Shadow Fiend! ")
voice.runAndWait()

rec = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    rec.adjust_for_ambient_noise(source, duration=3)
    print("Скажите что-нибудь...")
    audio = rec.listen(source)
text = rec.recognize_google(audio, language="ru_RU").lower()
if text == "привет":
    voice.say("hello")  
    voice.runAndWait()
elif text == "открой yputube":
    webbrowser.open_new("https://www.youtube.com/")
    voice.say("youtube открыт")
    voice.runAndWait() 
    