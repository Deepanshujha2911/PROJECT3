import pyautogui
import time

print("Press Ctrl+C to stop")
time.sleep(2)

while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end="\r")  # updates in same line
    time.sleep(0.1)