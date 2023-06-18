import speech_recognition as sr
import os
import subprocess
import datetime
import win32com.client
import webbrowser
import ai

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry! Some error occured."

if __name__ == '__main__':
    print('Pycharm')
    say("Hello I'am Rex A I")
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Sure! Opening {site[0]}")

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir, the time is {strfTime}")

        if "open vscode".lower() in query.lower():
            say("Opening VS Code")
            try:
                subprocess.Popen(["C:\\Users\\ideapadGAMING\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
            except FileNotFoundError:
                say("Sorry, I couldn't find VS Code on your system.")


        # say(query)
