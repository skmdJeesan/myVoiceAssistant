import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit
#import user_config
#import openai_request as ai

engine = pyttsx3.init()               
engine.setProperty('rate',175)     # setting up new voice rate
engine.setProperty('volume',1)     # setting up volume of voice

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # setting up the new voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Helps in noisy environments
        try:
            audio = r.listen(source, timeout=5)  # Adds timeout to avoid infinite wait
            content = r.recognize_google(audio, language='en-IN')
            print("Your command: " + content)
            return content.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return ""
        except sr.RequestError:
            print("Speech recognition service is down. Check your internet connection.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

def main_process() :
    while True :
        request = command().lower()
        if 'james' in request:
            speak("Hello sir! how can I help you")

        elif 'what is time' in request:
            time_now = datetime.datetime.now().strftime("%H:%M")
            speak("current time is " + str(time_now))
        elif 'what is date' in request:
            date_now = datetime.datetime.now().strftime("%d:%m")
            speak("current date is " + str(date_now))

        elif 'play talha anjum' in request:
            speak('playing talha anjum')
            webbrowser.open("https://www.youtube.com/watch?v=pJPnooVS7Ls&pp=ygUaZGVwYXJ0dXJlIGxhbmUgdGFsaGEgYW5qdW0%3D")
        elif 'play xxxtentacion' in request :
            speak("playing xxxtentacion")
            webbrowser.open("https://www.youtube.com/watch?v=58xKTGxmeHI&pp=ygUMeHh4dGVudGFjaW9u")

        elif 'open youtube' in request :
            webbrowser.open("https://youtube.com/")
        elif 'open instagram' in request :
            webbrowser.open("https://www.instagram.com/")
        elif 'open linkedIn' in request :
            webbrowser.open("https://www.linkedin.com/in/sk-md-jeesan-646b88292/")
        elif 'open lead code problem' in request :
            webbrowser.open("https://leetcode.com/problemset/")

        elif 'add task' in request :
            task = request.replace("add task","")
            task = task.strip()
            if task != "" :
                speak("Adding task" + task)
                with open("c:\\Users\\JEESAN\\Desktop\\Coding\\python\\myVoiceAssistant\\todo.txt","a") as f :
                    f.write(task + "\n")
        elif 'speak task' in request : 
            with open("c:\\Users\\JEESAN\\Desktop\\Coding\\python\\myVoiceAssistant\\todo.txt","r") as f :
                speak("Today's tasks is " + f.read())
        elif 'so tas' in request : # show task
            with open("c:\\Users\\JEESAN\\Desktop\\Coding\\python\\myVoiceAssistant\\todo.txt","r") as f :
                tasks = f.read()
                notification.notify(
                title = "Todo list",
                message = tasks
            )
        elif 'remove task' in request:
            task = request.replace("remove task", "").strip()  # Remove "remove task" and strip extra spaces
            if task != "":
                speak("Removing task: " + task)
                try:
                    # Read all tasks from the file
                    with open("c:\\Users\\JEESAN\\Desktop\\Coding\\python\\myVoiceAssistant\\todo.txt", "r") as f:
                        tasks = f.readlines()

                    # Remove the task if it exists
                    tasks = [t.strip() for t in tasks if t.strip() != task]

                    # Write the updated tasks back to the file
                    with open("c:\\Users\\JEESAN\\Desktop\\Coding\\python\\myVoiceAssistant\\todo.txt", "w") as f:
                        f.write("\n".join(tasks) + "\n")

                    speak("Task removed successfully.")
                except FileNotFoundError:
                    speak("The to-do file was not found.")
                except Exception as e:
                    speak(f"An error occurred: {e}")
            else:
                speak("Please specify the task to remove.")

        elif 'open' in request :
            query = request.replace('open','')
            if query != "":
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")

        elif 'wikipedia' in request :
            request = request.replace('search wikipedia','')
            print(request)
            result = wikipedia.summary(request,sentences = 2)
            print(result)
            speak(result)

        elif 'google' in request :
            request = request.replace('search google','')
            webbrowser.open(f'https://www.google.com/search?q={request}')

        elif 'whatsapp' in request :
            pywhatkit.sendwhatmsg("+917074847517", "Hi", 23, 25, 30)
            speak('message sent')
        
        # elif 'email' in request :
        #     try:
        #         pywhatkit.send_mail(
        #             'jeesanskmd@gmail.com',  # Sender email
        #             user_config.password,  # App password from Google
        #             'bakchodi bss',  # Email subject
        #             'Aur bhai kya haal chal?',  # Email content
        #             'skmdjeesan@gmail.com'  # Receiver email
        #         )
        #         print('Email sent successfully.')
        #     except Exception as e:
        #         print(f"An error occurred: {e}")

        # elif 'ask ai' in request :
        #     request = request.replace('ask ai','')
        #     print(request)
        #     response = ai.send_request(request)
        #     print(response)
        #     speak(response)

        elif 'stop' in request :
            speak("jo hukum mere Aaka")
            return


main_process()

#speak("hello, how are you")