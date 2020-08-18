import pyautogui
from time import sleep
import pynput
import random
import keyboard
import winsound

KeyBoard_button = pynput.keyboard.Controller()
Keyboard_key=pynput.keyboard.Key

t=0
while True:
    try:
        num1 = pyautogui.locateCenterOnScreen('1.png')
        #pyautogui.moveTo(num1)
        x,y=num1
        t=1
        num2 = pyautogui.locateCenterOnScreen('2.png')
        #pyautogui.moveTo(num2)
        x,y=num2
        t=2
        num3 = pyautogui.locateCenterOnScreen('3.png')
        #pyautogui.moveTo(num3)
        x,y=num3
        t=3
        num4 = pyautogui.locateCenterOnScreen('4.png')
        #pyautogui.moveTo(num4)
        x,y=num4
        t=4
        num5 = pyautogui.locateCenterOnScreen('5.png')
        #pyautogui.moveTo(num5)
        x,y=num5
        t=5
        num6 = pyautogui.locateCenterOnScreen('6.png')
        #pyautogui.moveTo(num6)
        x,y=num6
        t=6
        num7 = pyautogui.locateCenterOnScreen('7.png')
        #pyautogui.moveTo(num7)
        x,y=num7
        t=7
        num8 = pyautogui.locateCenterOnScreen('8.png')
        #pyautogui.moveTo(num8)
        x,y=num8
        t=8
        num9 = pyautogui.locateCenterOnScreen('9.png')
        #pyautogui.moveTo(num9)
        x,y=num9
        t=9
        num10 = pyautogui.locateCenterOnScreen('10.png')
        #pyautogui.moveTo(num10)
        x,y=num10
        t=10
        num11 = pyautogui.locateCenterOnScreen('11.png')
        #pyautogui.moveTo(num11)
        x,y=num11
        t=11
    except:
        print(t)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        sleep(20)
        continue
        

    

