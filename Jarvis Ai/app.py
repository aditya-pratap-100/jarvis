import os
import pyttsx3
import webbrowser
import pyautogui
from time import sleep
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",200)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
dictapp={"command prompt":"cmd","Notepad":"notepad","Paint":"paint","Word":"winword","Excel":"excel","chrome":"chrome","vs code":"code","PowerPoint":"powerpnt","path":"path"}
def openappweb(query):
    speak("launching sir")
    if".com"in query or ".co.in"in query or ".org" in query:
        query=query.replace("open",'')
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"{dictapp[app]}")
                break
def closeappweb(query):
    speak("closing sir")
    if "one tab"in query or "1 tab "in query:
        pyautogui.hotkey("ctrl","w")
        speak("one tab closed")
    elif "two tabs"in query or "2 tabs"in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("2 tabs closed")
    elif "three tabs" in query or "3 tabs"in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("3 tabs closed")
    elif "four tabs" in query or "4 tabs "in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("4 tabs closed")
    elif "five tabs" in query or "5 tabs"in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed")
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")