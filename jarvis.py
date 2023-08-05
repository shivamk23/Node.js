import pyttsx3
import speech_recognition as sr
import time
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2
from googlesearch import search
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# import pickle
# from __future__ import print_function

# SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# Voice function for AI Model as speak()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# WishMe() function works as a Salutation for the main user
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    
    elif hour>=16 and hour<21:
        speak("Good Evening!")

    else:
        speak("Good Night!")
 
         
    speak("I am Jarvis. Please tell me, how may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string ouput.
    r = sr.Recognizer()
    
    # AI Model will listen to the query said by the main / master user
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    # AI Model will calculate and circulate the speech recognized information spoken by the main / master user
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    # If information is not listened / not caught properly by the microphone of the device / problem occurs while exchanging information with the AI Model ->
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query

# sendEmail() function can send emails with the smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_gmail_id', 'your_gmail_password')
    server.sendmail('your_gmail_id', to, content)
    server.close()


if __name__ == "__main__":
    speak("Hello Sir.")
    WishMe()
    
    while True:
    # if 1:
        query = takeCommand().lower()
# call a dataset

        # Logic for executing tasks based on query
        
        # By speaking  your query along with according to wikipedia, query will be searched over wikipedia and your ansers will be well spoken and also printyed on the terminal
        if 'wikipedia' in query:
            print('Searching on Wikipedia...')
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            webbrowser.get('windows-default').open(results)
            print(results)
            speak(results)


        elif 'google' in query:
            try:
                # to search
                print('Searching on Google...')
                speak('Searching on Google...')
                query = query.replace("google", "")
                speak("According to Google")
                for result in search(query, tld="com", num=10, stop=5, pause=2):
                    # print(result)
                    # speak(result)
                    webbrowser.get('windows-default').open(result)
                
            except ImportError as e:
                print(e)
                print("No module named 'google' found")
                speak("No module named 'google' found")
            
            

        
        elif 'thank you' in query:
            print("Your's Welcome sir. Have a nice time sir.")
            speak("Your's Welcome sir. Have a nice time sir.")
            exit()
        

        # It can send any message via email if you provide someone's email address and the message you want to send to that person
        elif 'i want to email' in query:
            try:
                speak("To whom would you like to contact sir?")
                to = takeCommand()

                speak("What should I say sir?")
                content = takeCommand()    
                
                sendEmail(to, content)
                speak("Email has been sent successfully!")

            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")


        # Opens Youtube
        elif 'open youtube' in query:
            webbrowser.get('windows-default').open('https://youtube.com')


        # Opens Gmail
        elif 'open gmail' in query:
            webbrowser.get('windows-default').open('https://gmail.com')


        # Opens TryHackMe
        elif 'open try hack me' in query:
            webbrowser.get('windows-default').open('https://tryhackme.com')


        # Opens Google
        elif 'open google' in query:
            webbrowser.get('windows-default').open('https://google.com')


        # Opens LindenIn
        elif 'open linkedin' in query:
            webbrowser.get('windows-default').open('https://linkedin.com')


        # Opens Brave Browser from system directory as brave is my system default browser and you can change as per your system browser
        elif 'open browser' in query:
            brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(brave)
        
        
        # Plays the Music
        elif 'play music' in query:
            # music_dir -> your music directory path 
            music_dir = 'E:\\Arsh\\Mobile Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[364]))
            os.open()
        

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")


        # Opens Visual Studios Code 
        elif 'open code' in query:
            # codePath -> Opens Visual Studios Code from the system path where the .exe file is stored
            codePath = "C:\\Users\\arshb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        # Recording a Video with Integrated Camera or a Default Camera
        elif 'record a video' in query:
            # Capture the video frame by frame and choosing the camera while changing digits in -> ()
            # cap = cv2.VideoCapture(0)
            cap = cv2.VideoCapture(1)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

            # detection -> detection of any face or any body
            detection = False
            
            detection_stopped_time = None
            timer_started = False

            SECONDS_TO_RECORD_AFTER_DETECTION = 3

            frame_size = (int(cap.get(3)), int(cap.get(4)))
            # fourcc -> 4 Character Code with defining the file format
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            while True:
                _, frame = cap.read()

                # faces & bodies will detect the face or a body if caught will the camera is in turned on mode.
                # gray -> It is used to make any color preference of your choice while detecting any face or a body
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

                # The condition gets true if any type of face or a body will be caught in front of camera
                if len(faces) + len(bodies) > 0:
                    # If nothing detects in front of camera then recording will not start ->
                    if detection:
                        timer_started = False
                    
                    # If something gets detected in front of camera like a face or a body it will start recording the video ->
                    else:
                        detection = True

                        # current_time = current format of date and time -> ("%d-%m-%Y-%H-%M-%S")
                        # out - it is a variable where current time stamp is used with file format to store a file in the current folder where the source code file is stored.
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                        out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
                        
                        print("Started Recording!")
                        speak("Started Recording!")
                
                # If any interuption will be caused will recording the video ->
                elif detection:
                    # If nothing is getting detected by the camera then ->
                    if timer_started:
                        if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                            detection = False
                            timer_started = False
                            out.release()
                            print('Stopped Recording!')
                            speak('Stopped Recording!')
                    
                    # If any face or object get caught in between the SECONDS_TO_RECORD_AFTER_DETECTION then it will continue to record the video -> 
                    else:
                        timer_started = True
                        detection_stopped_time = time.time()

                # If a face or body again get caught in the camera then it will start recording ->
                if detection:
                    out.write(frame)

                for (x, y, width, height) in faces:
                    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

                cv2.imshow("Video", frame)

                # the 'q' button is set as the quitting button you may use any desired button of your choice
                if cv2.waitKey(1) == ord('q'):
                    break

            # After the loop release the cap object
            out.release()
            cap.release()

            # Destroy all the windows
            cv2.destroyAllWindows()



        elif 'take a photo' in query:
            # Capture the photo frame by frame and choosing the camera while changing digits in -> ()
            # pic = cv2.VideoCapture(0)
            pic = cv2.VideoCapture(1)

            # # To set the resolution
            # pic.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            # pic.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            # .read() function reads/gets the data from the camera in the resulting frame
            ret, frame = pic.read()
            if ret:
                # while(True):
                    
            
                # Display the resulting frame
                cv2.imshow('Photo', frame)

                # .imwrite() function saves the picture in the current directory folder
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                cv2.imwrite(f"{current_time}.png", frame)
                
                # the 'q' button is set as the quitting button you may use any desired button of your choice
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
                # After the loop release the cap object
                pic.release()
                
                # Destroy all the windows
                cv2.destroyAllWindows()

                print("Done sir.")
                speak("Done sir.")

            else :
                print("Could not open camera device for a picture")
                speak("Could not open camera device for a picture")
        


        # elif '' in query:
        #     print
        