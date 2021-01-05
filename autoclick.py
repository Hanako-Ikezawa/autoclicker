import time
import pyautogui
import keyboard

on = True

seconds = float(pyautogui.prompt(
    "Please indicate the interval (seconds) per click. Press 'q' to quit."))


while(on):
    # pyautogui.click()
    pyautogui.alert("Looping")
    time.sleep(seconds)

    if(keyboard.is_pressed("q")):
        pyautogui.alert("Stopped Auto Clicking")
        break
