import speech_recognition as sr
import webbrowser
import pyttsx3 
import time
import mymusic  # Ensure this file exists with a 'music' dict; handle import errors if needed
import pyautogui

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
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
    elif "pause" in c_lower:
        print("Toggling play/pause...")  # Debugging output
        # Adjust these coordinates to your Chrome icon position on screen
        chrome_x, chrome_y = 1439, 1033
        pyautogui.click(chrome_x, chrome_y)
        pyautogui.press("space")
        speak("Toggling play/pause.")
    elif "volume" in c_lower and "down" not in c_lower:  # Volume up only if not "down"
        print("Increasing volume...")
        # Adjust these coordinates to your Chrome icon position on screen
        chrome_x, chrome_y = 1439, 1033
        pyautogui.click(chrome_x, chrome_y)
        pyautogui.press("up")
        pyautogui.press("up")
        speak("Increasing volume.")
    elif "next" in c_lower:
        play_next()
    elif "mute" in c_lower:
        mute()
    elif "volume down" in c_lower:
        volume_down()
    elif "exit" in c_lower or "quit" in c_lower:
        speak("Goodbye!")
        exit()  # Gracefully exit the program
    else:
        speak("I don't understand that command. Try saying 'open google' or 'play songname'.")

def play_next():
    print("Playing next song...")  # Debugging output
    chrome_x, chrome_y = 1363, 1043  # Chrome icon coordinates
    
    # Click on Chrome to ensure focus
    pyautogui.click(chrome_x, chrome_y)
    time.sleep(1)
    
    # Press Shift + N for next video
    pyautogui.keyDown('shift')
    pyautogui.press('n')
    pyautogui.keyUp('shift')
    
    print("Next song command sent.")
    speak("Playing next song.")

    

def mute():
    print("Toggling mute...")  # Debugging output
    pyautogui.press("m")  # Assumes YouTube or similar player is focused
    speak("Toggling mute.")

def volume_down():
    print("Decreasing volume...")  # Debugging output
    pyautogui.press("down")  # Assumes YouTube or similar player is focused
    speak("Decreasing volume.")

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
