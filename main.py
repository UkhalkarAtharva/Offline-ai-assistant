import eel
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

def start():
    eel.init("frontend") 
    
    play_assistant_sound()

    @eel.expose
    def init():
        eel.hideLoader()
        speak("Welcome to Jarvis")
        speak("Ready for Face Authentication")
        flag = AuthenticateFace()
        if flag == 1:
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak("Welcome to Your Assistant")
            eel.hideStart()
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")

    # Start the frontend
    eel.start("index.html", size=(1000, 600), mode='chrome', host='localhost', port=8000)

if __name__ == "__main__":
    start()
