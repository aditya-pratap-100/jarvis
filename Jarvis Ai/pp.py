import pyautogui
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from time import sleep


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
recognizer = sr.Recognizer()


# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to a command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except Exception as e:
        return "some error occured sorry!"


# Function to execute commands
def execute_command(command):
    while True:
        command = listen()

        if "how are you" in command:
            speak("I'm just a computer program, so I don't have feelings, but I'm here to help you.")
        elif "goodbye" in command:
            speak("Goodbye!")
            exit()
        elif "google" in command.lower():
            webbrowser.open("www.google.in")
        elif "instagram" in command.lower():
            webbrowser.open("https://www.instagram.com/aditya_pratapofficial/?hl=en")
        elif "youtube" in command.lower():
            webbrowser.open("www.youtube.in")
        elif "play" in command.lower():
            webbrowser.open("www.youtube.in")
            sleep(3)
            pyautogui.moveTo(624, 176)
            sleep(1)
            pyautogui.click()
            command = command.replace("play", "")
            pyautogui.typewrite(f"{command}")
            sleep(1)
            pyautogui.hotkey("enter")
            sleep(3)
            pyautogui.moveTo(593, 332)
            pyautogui.click()
        elif "prompt" in command.lower():
            pyautogui.hotkey("win", "r")
            pyautogui.hotkey("enter")
        elif "show" in command.lower():
            command = command.replace("type", "")
            if "show all" in command.lower():
                pyautogui.typewrite("netsh wlan show all")
                pyautogui.hotkey("enter")
            elif "show profiles" in command.lower():
                pyautogui.typewrite("netsh wlan show profiles")
                pyautogui.hotkey("enter")
            elif "keyword" in command.lower():
                pyautogui.typewrite("netsh wlan show profiles name="" key=clear")
        elif "to sleep" in command.lower():
            speak("ok master u  can call me anytime")
            break


        elif "" in command.lower():
            speak(" i am sorry master can u please repeat it")


if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    while True:
        print(pyautogui.position())
        command = listen()
        if "wake up" in command.lower() or "get up" in command.lower():
            speak('warm greetings master how can i help you')
            execute_command(command)
