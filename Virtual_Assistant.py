import pyttsx
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib

engine = pyttsx.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak('Good Morning')
        
    elif hour >=12 and hour < 16:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
        
    speak("I am your Assistant")
    print('How can I help you?')
    speak('How can I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said : {query}\n")
        
    except Exception as e:
        print("Say that again please")
        query = None
        
    return query

def main():
    
    wishMe()
    query = takeCommand()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia')
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
        
    elif 'open youtube' in query.lower():
        print('What do you want to search : ')
        speak('What do you want to search : ')
        get = takeCommand()
        search = get.lower()
        url = 'https://www.youtube.com/results?search_query='
        wb.get(chrome_path).open(url + search)
        
    elif 'open google' in query.lower():
        print('What do you want to search : ')
        speak('What do you want to search : ')
        get = takeCommand()
        search = get.lower()
        url = 'https://www.google.com/search?q='
        wb.get(chrome_path).open(url + search)
        
    elif 'open facebook' in query.lower():
        url = 'facebook.com'
        wb.get(chrome_path).open(url)       
        
    elif 'open gmail' in query.lower():
        wb.get(chrome_path).open('gmail.com')
        
    elif 'play music' in query.lower():
        songs_dir = 'E:\\Music'
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
        
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime('%H : %M : %S')
        speak(f"The time is {strTime}")
    
    elif 'stop' in query:
        speak('Thank u. Have a nice day')
    
    else:
        print("sorry. I can't understand")
        speak("sorry. I can't understand")
        print('Do you want to search it in Google ?')
        speak('Do you want to search it in Google ?')
        get = takeCommand()
        if get.lower() == 'yes':
            wb.get(chrome_path).open('https://www.google.com/search?q=' + query)
        else:
            exit()
            
if __name__=="__main__": 
    main()