import pyautogui
from time import sleep
import pynput
import random
import keyboard

#패파
KeyBoard_button = pynput.keyboard.Controller()
Keyboard_key=pynput.keyboard.Key

skilla=pyautogui.locateCenterOnScreen('a.png')
skills=pyautogui.locateCenterOnScreen('s.png')
skilld=pyautogui.locateCenterOnScreen('d.png')

skillw=pyautogui.locateCenterOnScreen('w.png')
skillq=pyautogui.locateCenterOnScreen('q.png')
skille=pyautogui.locateCenterOnScreen('e.png')

#skillz=pyautogui.locateCenterOnScreen('q.png')
skillx=pyautogui.locateCenterOnScreen('x.png')
skillc=pyautogui.locateCenterOnScreen('c.png')#텔포 더블점프






#menu = ['skilla','skills','skillc','skillc','skillc','skillc',
 #   'left','right']  더블점프
menu = [
    'skillw','skilla','skills','skilla',
    'skills','skilla','skills','skilla','skills'
    'skills','skilla','skills','skilla','skills']  #텔레포트




tr=1


keep =1
keedi=1
keedi2=1
while True:
   
    sleep(0.5)
    if keyboard.is_pressed('/'):
        exit()  
    
    if keyboard.is_pressed(','):
        print('일시정지')
        while True:
            if keyboard.is_pressed('.'):
                break
            else :
                continue

    keep =keep+1
    keedi=keep
    print(keep)

    



    sleep(1)
    sleep(random.random()/20)
    pyautogui.click(skillc)
    sleep(random.random()/5)
    pyautogui.click(skillc)
    pyautogui.click(skillc)
    sleep(random.random()/10)
    pyautogui.click(skilla)  

    sleep(1)
    sleep(random.random()/20)
    pyautogui.click(skillc)
    sleep(random.random()/5)
    pyautogui.click(skillc)
    pyautogui.click(skillc)
    sleep(random.random()/10)
    pyautogui.click(skilla)    

    sleep(1)
    sleep(random.random()/20)
    pyautogui.click(skillc)
    sleep(random.random()/5)
    pyautogui.click(skillc)
    pyautogui.click(skillc)
    sleep(random.random()/10)
    pyautogui.click(skilla)  

    sleep(1)
    sleep(random.random()/20)
    pyautogui.click(skillc)
    sleep(random.random()/5)
    pyautogui.click(skillc)
    pyautogui.click(skillc)
    sleep(random.random()/10)
    pyautogui.click(skilla) 

    sleep(1)
    sleep(random.random()/20)
    pyautogui.click(skillc)
    sleep(random.random()/5)
    pyautogui.click(skillc)
    pyautogui.click(skillc)
    sleep(random.random()/10)
    pyautogui.click(skilla)  

    sleep(1)
    sleep(random.random()/5)
    pyautogui.click(skills) 
    sleep(random.random()/5)   

    if tr==1:
        sleep(0.1)
        sleep(random.random()/5)
        KeyBoard_button.press(Keyboard_key.right)
        sleep(random.random())
        KeyBoard_button.release(Keyboard_key.right)
        sleep(random.random())
        KeyBoard_button.press(Keyboard_key.right)
        sleep(random.random())
        KeyBoard_button.release(Keyboard_key.right)
        tr=2
        print("왼쪽도착")
        continue

    if tr==2:
        sleep(0.1)
        sleep(random.random()/5)
        KeyBoard_button.press(Keyboard_key.left)
        sleep(random.random())
        KeyBoard_button.release(Keyboard_key.left)
        sleep(random.random())
        KeyBoard_button.press(Keyboard_key.left)
        sleep(random.random())
        KeyBoard_button.release(Keyboard_key.left)
        tr=1
        print("오른쪽도착")
        continue
 



    

    
     
        

