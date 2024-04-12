import sys
from socket import timeout
import cv2
import pyaudio
import pyttsx3
from requests import get
import speech_recognition as sr
import datetime 
import os
import webbrowser
import pywhatkit as kit
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvisui import Ui_MainWindow
import smtplib
import wikipedia
import pyjokes



engine =pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
        hour = int( datetime.datetime.now().hour )

        if hour >= 0 and hour <= 12:
            speak( "good morning" )
        elif hour>12 and hour<18:
            speak( "good afternoon" )
        else:
            speak( "good evening" )
        speak("i am jarvis sir  please tell me how can i help for you")

def sendEmail(to, content):
                server = smtplib.SMTP( "smtp.gmail.com", 587 )
                server.ehlo()
                server.starttls()
                server.login( "ravianimation@gmail.com", "oshjehrypxdhavus" )  # oshjehrypxdhavus
                server.sendmail( "ravianimation@gmail.com", to, content )
                server.close()

class Harry(QThread):
                def __init__(self):
                    super(Harry,self).__init__()
                def run(self):
                    self.TaskExecution()

                # to convert voice to txt

                def takecommand(self):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print( "listening..." )
                        r.pause_thread=1
                        audio=r.listen( source, timeout=10,phrase_time_limit=20 )
                    try:
                        print( "Recognizing..." )
                        query = r.recognize_google( audio, language="en-in" )
                        print( f"user said:{query}" )

                    except Exception as e:
                        speak( "say that again please..." )
                        return "none"
                    return query

                def TaskExecution(self):
                    wish()
            
                    while True:
                        self.query = self.takecommand().lower()
                        if "open notepad" in self.query:
                            npath = "C:\\Windows\\system32\\notepad.exe"
                            os.startfile( npath )
                        elif "open brave" in self.query:
                            npath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                            os.startfile( npath )

                        elif "open vlc" in self.query:
                            npath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
                            os.startfile( npath )

                        elif "open cmd" in self.query:
                            os.system( "start cmd" )
                            

                        elif "open camera" in self.query:
                            cap = cv2.VideoCapture( 0 )
                            while True:
                                ret, img = cap.read()
                                cv2.imshow( "webcam", img )
                                k = cv2.waitKey( 50 )
                                if k == 27:
                                    break
                            cap.release()
                            cv2.destroyAllWindows()

                        elif "play music" in self.query:
                            music_dir = "F:\\Music"
                            songs = os.listdir( music_dir )
                            # rd=random.choice(songs)
                            for song in songs:
                                if song.endswith( ".mp3" ):
                                    os.startfile( os.path.join( music_dir, song ) )

                        elif "ip address" in self.query:
                            ip = get( "https://api.ipify.org" ).text
                            speak( f"your IP address is {ip}" )

                        elif "wikipedia" in self.query:
                            speak( "searching wikipedia......" )
                            self.query = self.takecommand().lower()
                            #self.query = self.query.replace( "wikipedia", "" )
                            results = wikipedia.summary( self.query, sentences=2 )
                            speak( "according to wikipedia")
                            speak( results )
                            print( results )

                        elif "open youtube" in self.query:
                            webbrowser.open( "www.youtube.com" )

                        elif "open facebook" in self.query:
                            webbrowser.open( "www.facebook.com" )

                        elif "open google map" in self.query:
                            webbrowser.open( "www.google.com/maps/" )

                        elif "open google" in self.query:
                            speak( "sir, what should i search on google" )
                            cm = self.takecommand().lower()
                            webbrowser.open( f"{cm}" )

                        elif "send message" in self.query:
                            kit.sendwhatmsg( "+918758701169", "hello", 19, 44 )  #change time

                        elif "play song on youtube" in self.query:
                            kit.playonyt( "azeri bass" )

                        elif "mail to ravi" in self.query:
                                 try:
                                        speak("what should i say?")
                                        content=self.takecommand().lower()
                                        to="ravianimation@gmail.com"
                                        sendEmail(to,content)
                                        speak("Email has been sent to ravi")
                                 except Exception as e:
                                     print(e)
                                     speak("sorry sir, i am not able to sent this mail")


                        elif "you can sleep now" in self.query:
                            speak("thanks for using me sir, have a good day")
                            sys.exit()


                        elif "close notepad" in self.query:
                            speak( "okay sir , closing notepad" )
                            os.system( "taskkill /f /im notepad.exe" )

                        elif "close brave" in self.query:
                            speak( "okay sir , closing brave" )
                            os.system( "taskkill /f /im brave.exe" )

                        elif "close vlc" in self.query:
                            speak( "okay sir , closing vlc" )
                            os.system( "taskkill /f /im vlc.exe" )

                        elif "set alarm" in self.query:
                            time1 = int( datetime.datetime.now().hour )
                            if time1 == 19:         #change time
                                music_dir = "G:\\ravi data\\music"
                                songs = os.listdir( music_dir )
                                os.startfile( os.path.join( music_dir, songs[0] ) )

                        elif "tell me a joke" in self.query :
                            joke = pyjokes.get_joke()
                            speak( joke )
                        elif "shutdown" in self.query:
                            os.system( "shutdown /s /t 5" )

                        elif "restart" in self.query:
                            os.system( "shutdown /r /t 5" )

                        elif "sleep" in self.query:
                            os.system( "rundll32.exe powrprof.dll,SetSuspendState 0,1,0" )
                        
                        speak("sir, do you have any other work")




                  #to wish
startExecution = Harry()
   # speak("i am jarvis sir  please tell me how can i help for you")
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie( "G:/ravi data/7th SEM/Project 2/jarvis/Jarvis_Loading_Screen.gif" )
        self.ui.label_2.setMovie( self.ui.movie )
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(2000)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText( label_date)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())




