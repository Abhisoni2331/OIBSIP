import pyttsx3
import datetime
import win32com.client
import datetime
import webbrowser
import os
import pywhatkit
import speech_recognition as spr
import wikipedia
import pyjokes

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("ROMA:", text)
    speaker.Speak(text)

def take_command():

    recognizer = spr.Recognizer()

    with spr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

    try:

            command = recognizer.recognize_google(audio)
            print("You:", command)

            return command.lower().strip()
        
    except Exception as e:
            print("Error", e)
            return ""
   
    
speak("Hi Abhi, Roma here")   

while True:

    command = take_command()

    if command == "":
        continue

    if "hello" in command:
        speak("Hi Abhi, How are you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}" )

    elif "chatgpt" in command:
        speak("opening chatgpt")
        webbrowser.open("https://chatgpt.com/")  

    elif "google" in command:
        speak("opening google")
        webbrowser.open("https://www.google.com/?hl=en-US&authuser=1")     

    elif "search" in command:
        query = command.replace("search", "").strip()

        if query:
            speak(f"searcing {query} on google")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        else:
            speak("What would you like me to search?")    

    elif "calculator" in command:
        speak("opening calculator")
        os.system("calc")

    elif "notepad" in command:
        speak("opening notepad")
        os.system("notepad")    
            
    elif "youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

            url = f"https://www.youtube.com/results?search_query={song}"

        else:
            speak("Which song would you like me to play?")    

    elif "cmd" in command:
        speak("opening command prompt")
        os.system("start cmd")

    elif "visual studio" in command:
        speak("Opening Visual studio code")
        os.system("code")

    elif "gmail" in command:
        speak("opening gmail")
        webbrowser.open("https://mail.google.com")    
    
    elif "who is" in command:
        
        try:

            person = command.replace('who is',"").strip()
            speak(f"Searching for {person}")

            result = wikipedia.summary(person, sentences = 3)

            print(result)
            speak(result)

        except wikipedia.exceptions.DisambiguationError:
            speak("Multiple information found, Please be specific")

        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find that person")

        except Exception as e:
            print(e)
            speak("Something went wrong")           
    
    elif "remember that" in command:
        note = command.replace("remember that","").strip()

        with open("memory.txt", "w") as file:
            file.write(note)
        speak("I have saved it")       

    elif "what do you remember" in command:
        try:

            with open("memory.txt", "r") as file:
                note = file.read()

            speak(note)

        except:
            speak("I do not remember")        

    elif "tell me a joke" in command:
        joke = pyjokes.get_joke()

        print (joke)

        speak(joke)

    elif any(word in command for word in ["exit", "escape", "bye", "goodbye"]):
        speak("Bye Abhi!!")
        break

    else:
        speak("Sorry Abhi, I couldn't Understand")


