import threading
import pyautogui
import speech_recognition as sr
import webbrowser
import pyttsx3 
import time
import mymusic  # Ensure this file exists with a 'music' dict; handle import errors if needed
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text) 
    engine.runAndWait()

def processcommand(c):
    print(f"Processing command: {c}")  # Debugging output
    
    # Handle empty or None commands to avoid crashes
    if not c or c.strip() == "":
        speak("I didn't catch that. Please try again.")
        return
    
    c_lower = c.lower()
    
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif c_lower.startswith("play"):
        try:
            song = c_lower.split(" ")[1]
            if song in mymusic.music:
                link = mymusic.music[song]
                webbrowser.open(link)
                speak(f"Playing {song}.")
            else:
                speak("Sorry, I could not find that song.")
        except IndexError:
            speak("Please specify a song to play, like 'play songname'.")
   # --- Media Controls (Hands-Free / No Coordinates) ---
    elif "pause" in c_lower or "play" in c_lower and "google" not in c_lower:
        # Toggles play/pause for whatever is currently playing
        pyautogui.press('playpause')
        speak("Toggling media.")

    elif "next" in c_lower:
        # Sends a system signal to skip to the next track/video
        pyautogui.press('nexttrack')
        speak("Playing next.")

    elif "previous" in c_lower:
        pyautogui.press('prevtrack')
        speak("Playing previous.")

    elif "volume up" in c_lower:
        # Increases system volume directly
        for _ in range(5): # Increases by 10% (2% per press)
            pyautogui.press('volumeup')
        speak("Volume increased.")

    elif "volume down" in c_lower:
        for _ in range(5):
            pyautogui.press('volumedown')
        speak("Volume decreased.")

    elif "mute" in c_lower:
        pyautogui.press('volumemute')
        speak("Muting audio.")

    # --- Exit ---
    elif "exit" in c_lower or "quit" in c_lower:
        speak("Goodbye Deepanshu! Shutting down.")
        exit()
        
    else:
        speak("I heard you, but I don't have a function for that yet.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                word = recognizer.recognize_google(audio)  
                print(f"Recognized: {word}")           
                if word.lower() == "jarvis":
                    speak("Yes?")
                    print("Jarvis activated....")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")  # Added for debugging
                    
                    # Process the command (now inside the if block)
                    processcommand(command)
        except Exception as e:
            print(f"Error: {e}")  # More informative error output
