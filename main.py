import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import pyjokes
import pywhatkit
from requests import get
from datetime import date
import pyautogui as pg
import subprocess

questionmark = random.choice(("?", "??", "???", "???"))
# voice selection for iris
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# voices is a list of voices on your computer
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


# speak function will take string input and speak
def there_exists(terms):
    for term in terms:
        if term in query:
            return True


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


def calculator():
    symbol = query.split()[1]
    if symbol == '+':
        speak(int(query.split()[0]) + int(query.split()[2]))
        print(int(query.split()[0]) + int(query.split()[2]))
    elif symbol == '-':
        speak(int(query.split()[0]) - int(query.split()[2]))
        print(int(query.split()[0]) - int(query.split()[2]))
    elif symbol == 'multiply':
        speak(int(query.split()[0]) * int(query.split()[2]))
        print(int(query.split()[0]) * int(query.split()[2]))
    elif symbol == 'divide':
        speak(int(query.split()[0]) / int(query.split()[2]))
        print(int(query.split()[0]) / int(query.split()[2]))
    elif symbol == 'power':
        speak(int(query.split()[0]) ** int(query.split()[2]))
        print(int(query.split()[0]) ** int(query.split()[2]))
    exit()


def game():
    had_fun = "y"
    print("ok which game would you like to play?")
    speak("ok which game would you like to play?")
    print("guess my number,rock paper scissors.")
    speak("guess my number,rock paper scissors.")
    print("that's all i have right now")
    speak("that's all i have right now")

    take_command()

    take_command()
    if "rock" or "stone" or "paper" in query:
        rpsas = "ok lets play"
        rock = "rock"
        paper = "paper"
        sc = "scissors"
        ASgme = "and shoot!"
        print(rpsas)
        speak(rpsas)
        print("==========================================================\n")
        print(rock)
        speak(rock)
        print(paper)
        speak(paper)
        print(sc)
        speak(sc)
        print(ASgme)
        speak(ASgme)
        rpsasr = random.choice(("rock", "paper", "scissors"))
        print(rpsasr)
        speak(rpsasr)


def locate():
    place = query[1]
    speak(f"according to my data base {place} lies here")
    webbrowser.open_new_tab("https://www.google.com/maps/place/" + place)


def get_audio():
    # It tane input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_time_limit = 10
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language='en-in')
        print(f"User said: {said}\n")
    except:
        return "None"
    return said


def screenshot():
    image = pg.screenshot()
    speak("screen shot taken")
    speak("what do you want to save it as?")
    filename = get_audio()
    image.save(filename + ".png")
    speak("do you want me to show it")
    ans = get_audio()
    if "yes" in ans:
        os.startfile(filename + ".png")
    else:
        speak("never mind")


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def repeat_my_speech():
    global reply
    if there_exists(["repeat", "talking tom"]):
        speak("Okay starting to listen")
        speak(f"Okay, please start speaking")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 5
            audio = r.listen(source)

        try:
            said = r.recognize_google(audio, language='en-in')
            print(f"Ok here is ur repetition by me {said}:-\n")
            speak(f"User said:- {said}\n")

            try:
                speak("should i save the file?")
                print("should i save the file?")
                ans = get_audio()
                if "yes" in ans:
                    try:
                        speak("What should i keep the file name")
                        filename = get_audio().lower
                        speak("File saved successfully")
                        try:
                            speak("Do you want me to show it?")
                            reply = get_audio()
                            if "yes" in reply:
                                speak("here it is")

                        except:
                            if "no" or "nope" in reply:
                                speak("Never mind")

                    except:
                        speak("Error in keeping filename")

            except:
                speak("Okay")

        except:
            return "None"
        return said


# wishMe() function will greet you whenever you run this script
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" )

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")

    else:
        speak("Good Evening ")

    speak("I am Iris. How can i help you?")


# iris will take your voice command and convert into string
def take_command():
    # it takes microphone input from user and returns string output
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
        print(e)
        print("Say That Again Please...")
        speak("Say That Again Please...")
        return "None"
        pass

    return query


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        global person_name, reply
        if there_exists(['hey','hi','hai','hello']):
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning")

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon ")

            else:
                speak("Good Evening ")
            greetings = ["How can I help you",
                         "What's up? How can I help you"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)
        # 2: name
        if there_exists(["what is your name", "what's your name", "tell me your name"]):
           speak("Myself Iris.")

        # 3: greeting
        if there_exists(["how are you", "how are you doing"]):
            speak("I'm very well, thanks for asking ")

        #  check ip address
        if there_exists(["ip address"]):
            ip = get('http://api.ipify.org').text
            print(f"your ip address is {ip}")
            speak(f"your ip address is {ip}")

        # 7: get stock price
        if there_exists(["price of"]):
            search_term = query.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for " + search_term + " on google")

        # search for amazon.com
        if there_exists(["amazon.com"]):
            search_term = query.split("for")[-1]
            url = "https://www.amazon.in" + search_term
            webbrowser.get().open(url)
            speak("here is what i found for" + search_term + "on amazon.com")

        # # make a note
        #     if there_exists(["make a note"]):
        #         search_term = query.split("for")[-1]
        #         url = "https://keep.google.com/#home"
        #         webbrowser.get().open(url)
        #         speak("Here you can make notes")

        # open instagram
        if there_exists(["open instagram", "have some fun"]):
            search_term = query.split("for")[-1]
            url = "https://www.instagram.com/"
            webbrowser.get().open(url)
            speak("opening instagram")

        # open twitter
        if there_exists(["open twitter"]):
            search_term = query.split("for")[-1]
            url = "https://twitter.com/"
            webbrowser.get().open(url)
            speak("opening twitter")

        # 9 weather
        if there_exists(["weather"]):
            search_term = query.split("for")[-1]
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            speak("Here is what I found for on google")

        # open gmail
        if there_exists(["open my mail", "gmail", "check my email"]):
            search_term = query.split("for")[-1]
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            speak("here you can check your gmail")

        # 10 stone paper scissors
        if there_exists(["play"]):
            if there_exists(["game"]):
                speak("Let's play rock paper scissors")
                speak("choose among rock paper or scissor")
                query = get_audio()
                moves = ["rock", "paper", "scissor"]

                cmove = random.choice(moves)
                pmove = query

                speak("The computer chose " + cmove)
                speak("You chose " + pmove)
                # engine_speak("hi")
                if pmove == cmove:
                    speak("the match is draw")
                elif pmove == "rock" and cmove == "scissor":
                    speak("Player wins")
                elif pmove == "rock" and cmove == "paper":
                    speak("Computer wins")
                elif pmove == "paper" and cmove == "rock":
                    speak("Player wins")
                elif pmove == "paper" and cmove == "scissor":
                    speak("Computer wins")
                elif pmove == "scissor" and cmove == "paper":
                    speak("Player wins")
                elif pmove == "scissor" and cmove == "rock":
                    speak("Computer wins")
                    # search for music
            elif there_exists(["play"]):
                song = query.replace('play', '')
                speak("playing" + song)
                print("playing...")
                pywhatkit.playonyt(song)

        # 11 toss a coin
        if there_exists(["toss", "flip", "coin"]):
            moves = ["head", "tails"]
            cmove = random.choice(moves)
            speak("The computer chose " + cmove)

        # 12 calc
        if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
            opr = query.split()[1]

            if opr == '+':
                speak(int(query.split()[0]) + int(query.split()[2]))
            elif opr == '-':
                speak(int(query.split()[0]) - int(query.split()[2]))
            elif opr == 'multiply':
                speak(int(query.split()[0]) * int(query.split()[2]))
            elif opr == 'divide':
                speak(int(query.split()[0]) / int(query.split()[2]))
            elif opr == 'power':
                speak(int(query.split()[0]) ** int(query.split()[2]))
            else:
                speak("Wrong Operator")

        # 13 screenshot
        if there_exists(["capture", "my screen", "screenshot"]):
            image = pg.screenshot()
            speak("screen shot taken")
            speak("what do you want to save it as?")
            filename = get_audio()
            image.save(filename + ".png")
            speak("do you want me to show it")
            ans = get_audio()
            if "yes" in ans:
                os.startfile(filename + ".png")
            else:
                speak("never mind")

            #  talking Tom
        if there_exists(["repeat", "talking tom"]):
            repeat_my_speech()

        if there_exists(["make a note", "write this down", "remember this"]):
            speak("What would you like me to write down? ")
            write_down = get_audio()
            note(write_down)
            speak("I've made a note of that.")

        if there_exists(["joke", "jokes"]):
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        #    introduction
        if there_exists(["introduce yourself"]):
            speak("Okay,Let me start by The time I was born,,")
            print("Okay,Let me start by The time I was born,,")
            speak("I was a dream of a team dreaming to make a perfect virtual assistant,,")
            print("I was a dream of a team dreaming to make a perfect virtual assistant,,")
            speak("They soon established the project named Iris,")
            print("They soon established the project named Iris,")
            speak("Slowly,I came to life,")
            print("Slowly,I came to life,")
            speak("I started learning various things like searching, opening files, etcetera,")
            print("I started learning various things like searching, opening files, etcetera,")
            speak("hmm...yeah, that's my story")
            print("hmm...yeah, that's my story")

        if there_exists(["locate"]):
            query.split("locate")
            locate()

        if there_exists(["your friends"]):  # You can ask, "Who are your friends"
            speak("Yes, they are Kaven, Pratheep, Jhasim and Samhitha")

        if there_exists(["you watch"]):  # You can ask, "Did you watch <movie name>""
            speak("yeah, that's an average movie")

        if there_exists(["you nostalgic"]):  # You can ask, "What makes you nostalgic?"
            speak("When I hear the name Guido Van Rossum...")

        if there_exists(["tell me a quote"]):
            speak("You must be the change you wish to see in the world, told by Mahatma Gandhi")

        if there_exists(["my homework"]):  # You can ask, "Will you do my homework, please?"
            speak("First I need to figure out how to use a pencil. Then we'll talk about homeworks, lol")

        if there_exists(["tell me a joke on your own"]):
            speak("If we shouldn't eat at night, why do they put a light in the fridge?")

        if there_exists(["value of Pi"]):  # You can ask, "What is the value of pi?"
            speak(
                "3.14159..Also, a pie is a baked dish which is made of...NoNo that was a bad joke forget what I said.")

        if there_exists(["favourite website"]):  # You can ask, "Whats your favourite website?"
            speak("Its www.maharishividyamandirch .com")

        if there_exists(["What's your favorite thing on the internet"]):
            speak("Every programming website!!")

        if there_exists(["your mind"]):
            speak("Nah! I was just wondering what my next task would be...")
            print("Nah! I was just wondering what my next task would be 🤗😄...")

        #   bye
        if there_exists(["exit", "quit", "goodbye", "stop"]):
            speak("we could continue more , but...bye")
            exit()