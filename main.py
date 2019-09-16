import ctypes
import os
import webbrowser
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import download_media
import web

greetings_dict = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
bye_dict = ['exit', 'close', 'goodbye', 'nothing']
download_video = ['download video','download a video','download a youtube video','download a video from youtube',
            'download a video for me']
download_song = ['play song','play a song','play a song','play a song from youtube',
            'play a song for me']
date_dict = ['date','current date','can you tell me the date','todays date']
time_dict = ['time','current time','can you tell me the time','whats the time']
lock_dict=['lock my device','lock','lock this device']
thank_you_dict=['thank you','thank you so much','thanks']

global now
now = datetime.now()

try:
    engine = pyttsx3.init()
except ImportError:
    print("Driver Not Found")
except RuntimeError:
    print("Driver fail")

engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)
engine.setProperty('volume', 1)

speech = sr.Recognizer()


def ail(cmd):
    engine.say(cmd)
    engine.runAndWait()


def command():
    voice_text = ""
    print("listening..")

    with sr.Microphone() as source:
        speech.pause_threshold = 1
        speech.adjust_for_ambient_noise(source, duration=1)
        global audio
        audio = speech.listen(source=source, timeout=7, phrase_time_limit=7)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        ail("Cant understand")
    except sr.RequestError as e:
        ail("Network error")
    return voice_text


if __name__ == "__main__":

    ail("Hey there...! i am your personal voice assistant Ail")

    while True:
        voice_note = command().lower()
        print('cmd : {}'.format(voice_note))

        if voice_note in greetings_dict:
            day_time = int(now.strftime('%H'))
            if day_time < 12:
                ail('Hello Sir. Good morning')
            elif 12 <= day_time < 18:
                ail('Hello Sir. Good afternoon')
            else:
                ail('Hello Sir. Good evening')
            continue
        elif 'Open' in voice_note:
            ail("Okey sir")
            WithOutSpace = voice_note.replace(" ", "").title()
            print(WithOutSpace)
            os.system('explorer C:\\{}'.format(WithOutSpace.replace('Open', '')))
            print('explorer C:\\ {}'.format(WithOutSpace.replace('Open', '')))

        elif 'launch' in voice_note:
            web.launchWeb(voice_note)

        elif "search" in voice_note:
            webbrowser.open("https://www.google.com/search?q={}".format(voice_note.replace("search", "")))

        elif 'tell me about' in voice_note:
            web.wiki(voice_note)

        elif 'news for today' in voice_note:
            web.news()

        elif 'tell me weather in' in voice_note:
            web.weather(voice_note)

        elif voice_note in download_video:
            download_media.initYT_Video()

        elif voice_note in download_song:
            download_media.initYT_Song()

        elif  voice_note in date_dict:

            date = now.strftime("%m/%d/%Y")
            ail("today is {}".format(date))

        elif  voice_note in time_dict:
            time = now.strftime("%I:%M %p")
            ail("it's {} now".format(time))
        elif voice_note in lock_dict :
            ail('Sure sir')
            ctypes.windll.user32.LockWorkStation()
            ail('Your system is locked.')
        elif voice_note in thank_you_dict :
            ail("Glad to help...")
        elif  voice_note in bye_dict :
            ail('okay Bye...have a good day')
            exit()
