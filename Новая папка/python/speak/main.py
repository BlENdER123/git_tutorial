import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

engine = pyttsx3.init()


def talk(words):
    engine.say(words)
    engine.runAndWait()
    
talk('Привет, мир')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Говорите')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    try:
        audio_text = r.recognize_google(audio).lower()
        print('Вы сказали ' + audio_text)
    except sr.UnknownValueError:
        talk('Я вас не понял')
        audio_text = command()

    return audio_text

def makeSomething(task):
    
    if 'open website' in task:
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'stop' in task:
        talk('Ok')
        sys.exit()

while True:
    makeSomething(command())

# def talk(words):
#     print(words)
#     os.system('say ' + words)

# talk('Привет, мир')