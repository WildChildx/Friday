import speech_recognition as sr
import wikipedia
import pyttsx3
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(sentence):

    print(sentence)
    engine.say(sentence)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    text = ""
    with sr.Microphone() as source:
        print("Clearing background noise...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        speak("Hello Sir , I'm Listening")
        recordedaudio = recognizer.listen(source)
        speak("Done recording...")
    try:
        print('Printing your message...Please wait')
        text = recognizer.recognize_google(recordedaudio, language='en-US')
        print('Your Message:{}', format(text))
    except Exception as ex:
        print(ex)
    return text


setupReady = False

while True:
    msg = listen()
    if 'stop' in msg.lower():
        speak("Good bye sir! , Have a nice day")
        break
    elif 'initialise' in msg.lower() or 'initialize' in msg.lower():
        speak("Initializing developer setup")
        program = "C:\\Users\shreec\Documents\AutomaticCommands\initilizeDevSetup.bat"
        subprocess.Popen([program])
        continue
    elif 'chrome' in msg.lower():
        speak("Opening google chrome...")
        program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
        continue
    elif 'wikipedia' in msg.lower():
        speak(wikipedia.summary(msg))
        continue
    elif 'kill' in msg.lower():
        speak("Killing all the processes!")
        program = "C:\\Users\shreec\Documents\AutomaticCommands\killDevSetup.bat"
        subprocess.Popen([program])
        continue
