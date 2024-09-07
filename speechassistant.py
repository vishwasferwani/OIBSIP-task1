import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia

now = datetime.datetime.now()
time = now.time().strftime("%H:%M")
date = now.date()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

recognizer = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("listening")
        recognizer.adjust_for_ambient_noise(source=source,duration=0.5)
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            text = text.lower()
            print("You said:", text)

            if "hello" in text:
                print("Hello sir")
                speak("Hello sir")
            elif "how" in text:
                speak("I'm good sir, Ask me anything")
            elif "time" in text:
                print(f"the time is {time}")
                speak(f"the time is {time}")

            elif "date" in text:
                print(f"today's date is {date}")
                speak(f"today's date is {date}")

            elif "exit" in text:
                print("goodbye sir")
                speak("goodbye sir")
                break

            elif 'wikipedia' in text:
                speak('Searching Wikipedia...')
                text = text.replace("wikipedia", "")

                try:
                    results = wikipedia.summary(text, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"There are multiple meanings for '{text}'. Please be more specific.")
                    speak(f"There are multiple meanings for '{text}'. Please be more specific.")
                except wikipedia.exceptions.PageError as e:
                    print(f"'{text}' does not match any Wikipedia page. Please try again.")
                    speak(f"'{text}' does not match any Wikipedia page. Please try again.")


        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            speak("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")

