import pyttsx3 
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  


def speak(audio):
   
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning boss!")
    elif 12 <= hour < 18:
        speak("Good Afternoon boss!")
    else:
        speak("Good Evening boss!")

    speak("I am jarvis sir. Please tell me how may I help you.")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
   
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')  
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry my friend vishal. I am not able to send this email.")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I could not find anything on Wikipedia.")
            except Exception as e:
                print(e)
                speak("Something went wrong while searching Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\singh\\Music"
            try:
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))
            except IndexError:
                speak("There are not enough songs in the directory.")
            except FileNotFoundError:
                speak("The music directory was not found.")
            except Exception as e:
                print(e)
                speak("Something went wrong while trying to play music.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\singh\\Downloads"
            try:
                os.startfile(codePath)
            except Exception as e:
                print(e)
                speak("I could not open Visual Studio Code.")

        elif 'email to vishal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                if content != "None":
                    to = " singhvishal1969@gmail.com"
                    sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry my friend vishal. I am not able to send this email.")
