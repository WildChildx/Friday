import speech_recognition as sr
import wikipedia
import pyttsx3
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1])
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing background noise...Please wait")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    print("waiting for your message...")
    recordedaudio = recognizer.listen(source)
    print('Done recording')

try:
    print('Printing your message...Please wait')
    text = recognizer.recognize_google(recordedaudio, language='en-US')
    print('Your Message:{}', format(text))

except Exception as ex:
    print(ex)

if 'setup' in text.lower():
    a = "Hello Sir , Initializing developer setup"
    engine.say(a)
    engine.runAndWait()
    program = "C:\\Users\shreec\Desktop\startFriday.bat"
    subprocess.Popen([program])

if 'chrome' in text.lower():
    a = "Hello Sir , Opening google chrome"
    engine.say(a)
    engine.runAndWait()
    program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([program])


if 'wikipedia' in text.lower():
    wikisearch = wikipedia.summary(text)
    engine.say(wikisearch)
    engine.runAndWait()
    program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([program])
# Input data
