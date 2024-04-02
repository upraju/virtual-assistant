import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyautogui
import cv2
import random,os
import subprocess




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    global command
    command=""
    
    try:
        with sr.Microphone() as source:
            print('listening .....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pavilion' in command:
                command = command.replace('pavilion','')
                print(command)
               
    except:
        pass
    return command
        


def run_pavilion():
    command = take_command().lower()
    print(command)
    while True:
        if 'play' in command:
            talk('sure Captain')
            song = command.replace('play','')
            talk('playing' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('Current time is' + time)
        elif 'search' in command:
            person = command.replace('search','')
            talk('searching Captain')
            info = wikipedia.summary(person,1)
            talk("According to wikipedia")
            print(info)
            talk(info)
        elif 'is love' in command:
            print("It is 7th sense that destroy all other senses")
            talk("It is 7th sense that destroy all other senses")
        elif 'are you single' in command:
            talk('No,sir I am in a relationship with wifi')
        elif "locate" in command:
            command = command.replace("locate", "")
            location = command
            talk(" locating Captain")
            talk(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        elif 'calculate' in command:
            print('opening calculator')
            talk('opening calculator')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif 'news' in command:
            news = webbrowser.open_new_tab("www.thehindu.com/news/")
            talk('Here are news from the Hindu, Enjoy Captain')

        elif 'screenshot' in command:
            talk('Sure,boss taking screenshot')
            print('taking screenshot')

            im = pyautogui.screenshot()
            im.save("My screenshot.jpg")

            talk('Captain, your screenshot will save as My screenshot' )

        elif "take a pic" in command:
            talk('say cheese! boss')

            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while (result):
                ret, frame = videoCaptureObject.read()
                cv2.imwrite("Pavilion pic.jpg", frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            talk('your pic saved as pavilion pic,Captain')
        elif "nice job" in command or "good job" in command or "awesome" in command:
            print('THANK YOU Captain, MY PLEASURE,its my duty to serve you Captain....')
            talk('THANK YOU Captain, MY PLEASURE,its my duty to serve you Captain')
        elif 'open google' in command:
            print("opening Google chrome")
            talk("opening Google chrome")
            webbrowser.open_new_tab("https://www.google.com")
            talk("Google chrome is open now Captain...")
        elif 'who are you' in command or 'what can you do' in command:
            talk('I am Pavilion, your personal assistant Captain. I am programmed to do minor tasks like'
                'opening youtube, Google Chrome , calculator, playing music  ,predict time, taking photos and screenshots, searching wikipedia,'
                ', get top headline news from the hindu and you can ask me to locate geographical areas too!')
        elif  'songs' in command:
            talk('playing your favorite song Captain')
            n = random.randint(1, 2)
            print(n)
            music_dir = 'C:\\Users\\palra\\Music'
        
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[n]))
        else:
            talk('Please say the command again captain')


while True:
    run_pavilion()





