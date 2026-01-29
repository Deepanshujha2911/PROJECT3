🎤 Jarvis – Voice-Controlled Desktop Assistant

Jarvis is a Python-based voice assistant that listens for a wake word and performs commands through speech. It automates web browsing, media control, and music playback using voice interactions and keyboard simulation.

✅ Core Features

Wake Word Activation
Listens for the word “Jarvis” to begin processing commands.

Voice Commands for Browsing
Supports:
• “Open Google”
• “Open Facebook”
• “Open YouTube”

Music Playback via Custom Library
Uses a mymusic module containing a dictionary of songs and links.
Command: play <song_name>

Media Controls (YouTube/Browser)
• “Pause” – Toggles play/pause
• “Next” – Skips to the next video using Shift + N
• “Volume” – Increases volume
• “Volume down” – Decreases volume
• “Mute” – Toggles sound

Voice Feedback
Responds using pyttsx3 for a more interactive experience.

🛠 Technologies Used

speech_recognition

pyttsx3

webbrowser

pyautogui

time

Custom module: mymusic

🚀 Purpose

Jarvis aims to provide a hands-free experience for everyday tasks like opening websites, controlling YouTube playback, and playing music with simple speech commands. It serves as a beginner-friendly personal assistant project built with Python.
