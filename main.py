import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from tkinter import scrolledtext

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#GUI
root = tk.Tk()
root.title("My Alex: Virtual Assistant by Sanika")
root.geometry("500x400")
root.configure(bg="#eaf6f6")

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, font=("Arial", 10))
output_text.pack(pady=10)

def talk(text):
    output_text.insert(tk.END, f"Alex: {text}\n\n")
    output_text.see(tk.END)
    engine.say(text)
    engine.runAndWait()

def take_command():
    command =""
    try:
        with sr.Microphone() as source:
            print("Say something!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                    command = command.replace('alex', '')
                    print(command)

    except Exception as e:
        print("Error:", e)
    return command

def run_alex():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is :" + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what is my name' in command:
        talk("Your name is sanika sharma")
    elif 'introduce yourself' in command:
        talk("I am a virtual assistant made by Sanika Sharma. My name is Alex.")
    else:
        talk("I'm Sorry! Please say the command again!")

start_button = tk.Button(root, text="Start Listening", command=run_alex, font=("Arial", 12), bg="#90ee90")
start_button.pack(pady=10)

root.mainloop()

while True:
    run_alex()
