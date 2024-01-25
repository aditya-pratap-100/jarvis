import sys
import win32com.client

speaker = win32com.client.Dispatch("SAPI.Spvoice")
import os
import speech_recognition
import webbrowser
import datetime

import pyttsx3
import numpy as np
from time import sleep
import pyautogui




def say(text):
    os.system(f"say {text}")





def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said :{query}")
            return query
        except Exception as e:
            return "some error occured sorry!"




def taskexecution():
    while True:
        print("listening")
        speaker.Speak("processing master")
        query = takecommand()
        if "search" in query.lower():
            pyautogui.moveTo(708, 504, 1)
            sleep(3)
            pyautogui.click()
            sleep(1)

            query = query.replace("now", '')
            query = query.replace("Google", '')
            query = query.replace("and", '')
            query = query.replace("search", '')

            pyautogui.typewrite(f"{query}")
            pyautogui.hotkey("enter")

        elif "google" in query.lower():
            webbrowser.open("www.google.in")

        elif "are you" in query.lower():
            speaker.Speak("i am fine master and what about u")
        elif "play" in query.lower():
            webbrowser.open("www.youtube.in")
            pyautogui.moveTo(560, 129, 1)
            sleep(3)
            pyautogui.click()
            sleep(1)
            query = query.replace("open ", '')
            query = query.replace("video", '')
            query = query.replace("jarvis ", '')
            query = query.replace("play", '')

            pyautogui.typewrite(f"{query}")
            pyautogui.hotkey("enter")

            pyautogui.moveTo(361, 386, 1)
            sleep(3)
            pyautogui.click()
        elif "change" in query.lower():
            pyautogui.moveTo(1184, 135, 1)
            sleep(2)
            pyautogui.click()
            sleep(1)
            pyautogui.moveTo(1179, 135, 1)
            pyautogui.click()
            query = query.replace("change", "")
            query = query.replace("and", "")
            pyautogui.typewrite(f"{query}")
            pyautogui.hotkey("enter")
            pyautogui.moveTo(466, 366, 1)
            sleep(2)
            pyautogui.click()

        elif "whatsapp" in query.lower():
            webbrowser.open("web.whatsapp.com")

        elif "instagram" in query.lower():
            webbrowser.open("https://www.instagram.com/aditya_pratapofficial/?next=%2F&hl=en")

        elif "yourself" in query.lower():
            speaker.Speak(
                "Best AI Assistant Powered by GPT, Jarvis, AI Copilot, seamlessly integrates with your web browser and OS (MacOS, Windows, iOS, Android) to boost productivity with a rich features set included AI chat, suggestions, translation, rewriting, explanations, and more.")



        elif "close it" in query.lower():
            pyautogui.hotkey("alt", "F4")
        elif "close" in query.lower():

            from app import closeappweb
            closeappweb(query)


        elif "minimise " in query:
            pyautogui.hotkey("win", "m")
        elif "sleep" in query.lower():
            speaker.Speak("ok master ,you can call me anytime")
            speaker.Speak("pave the way for team tech")
            break

        elif "command prompt" in query.lower():
            pyautogui.hotkey("win", "r")
            sleep(1)
            pyautogui.hotkey("enter")
            sleep(3)
            pyautogui.typewrite("cd/")
            sleep(1)
            pyautogui.hotkey("enter")
            sleep(0.6)
            pyautogui.typewrite("cd\Windows\System32")
            pyautogui.hotkey("enter")
        elif "type" in query.lower():
            if "dance" in query:
                pyautogui.typewrite("rick")
                sleep(1)
                pyautogui.hotkey("enter")
            elif "forest" in query:
                pyautogui.typewrite("forrest")
                sleep(1)
                pyautogui.hotkey("enter")
            elif "network sharing" in query:
                pyautogui.typewrite("netsh wlan show profiles name="" key=clear")
            elif "star wars" in query.lower():
                pyautogui.typewrite("telnet towel.blinkenlights.nl")
                sleep(1)
                pyautogui.hotkey("enter")
            elif "sky" in query.lower():
                pyautogui.typewrite(f'curl ascii.live/')
            elif "show" in query.lower():
                query = query.replace("type", '')
                pyautogui.typewrite(f"netsh wlan{query}")
                sleep(1)
                pyautogui.hotkey("enter")
            elif "system info" in query.lower():
                pyautogui.typewrite("systeminfo")
                sleep(1)
                pyautogui.hotkey("enter")
        elif "open" in query:
            from app import openappweb
            openappweb(query)
        elif "generate" in query.lower():
            webbrowser.open("https://firefly.adobe.com/inspire/images")
            pyautogui.moveTo(229, 940)
            sleep(10)
            pyautogui.click()
            query = query.replace("generate", "")
            pyautogui.typewrite(f"{query}")
            pyautogui.hotkey("enter")

        else:
            speaker.Speak("sorry master can u repeat it")


if __name__  == "_main_":

    while True:

        permission = takecommand()
        if "wake up" in permission.lower():
            time = datetime.datetime.now().strftime("%H  hours %M minutes and %S seconds")
            speaker.Speak(f"greetings master,how can i help you, it is{time}")
            taskexecution()

        elif "goodbye" in permission.lower():
            speaker.Speak("finally exiting master")
            sys.exit()
        elif "get up" in permission.lower():
            speaker.Speak("master we are again on track")
            taskexecution()