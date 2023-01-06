import datetime
import pyttsx3
import speech_recognition as sr
import subprocess
import random as rnd

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said=r.recognize_google(audio)
        except Exception as e:
            print('Exception: '+ str(e))
    return said.lower()

text = get_audio()
if 'bye' in text:
    speak("you're going back too early. hope to have you again")

def note(text):
    date = datetime.datetime.now()
    file_name=str(date).replace(':', '-') + '-note.txt'
    with open(file_name, 'w') as f:
        f.write(text)
        subprocess.Popen(['notepad.exe', file_name])

def getstatescapitals():
    statescapitals = {'mississippi': 'jackson', 'arizona': 'phoenix', 'iowa': 'desmoines',
'massachuettes': 'boston', 'michigan': 'lansing', 'virginia': 'richmond',
'oregon': 'salem', 'hawaii': 'honolulu', 'nebraska': 'lincoln',
'indiana': 'indianapolis', 'ohio': 'columbus', 'illnois': 'springfield'}
    return statescapitals


def game():
    print("states capitals Quiz\n")
    statescapitals = getstatescapitals()
    numberofcorrectanswers = 0
    while True:
        states = list(statescapitals.keys())
        state = rnd.choice(states)
        capital = statescapitals[state]
        # del statescapitals[state]
        # if len(statescapitals) == 0:
        #   break
        # else:
        #   continue
        #  del function if as an comment: name of states may repeat
        #  if not as an comment, name of states won't repeat but the code will end with an error:
        # IndexError: Cannot choose from an empty sequence
        answer = input("what is the capital of "+state+"?")
        if answer.lower() == capital.lower():
            print("correct!")
            numberofcorrectanswers += 1

        else:
            print("incorrect")
            break
        print("\nGame over! you got ", numberofcorrectanswers, "right")


wake = 'hello clock'
while True:
    print('Listening....')
    text= get_audio()
    if text.count(wake) > 0:
        speak('Hi, how can i help you?')
        text = get_audio()
        NOTE_STRS =['hi', 'hai']
        for phrase in NOTE_STRS:
            if phrase in text:
                speak('Yes, what do you want me to note?')
                note_text = get_audio()
                note(note_text)
                speak('Noted!')
        GAME_STRS=['game', 'play']
        for ph in GAME_STRS:
            if ph in text:
                game()