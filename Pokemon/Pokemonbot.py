from pyautogui import *
import pyautogui

import time
import keyboard
import numpy as np
import random
import win32api, win32con

lor = 10000

num = 10

print("Starting Pokemon Bot by Braha")

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
            #click D
             pyautogui.keyDown('D')
             time.sleep(0.1)
             pyautogui.keyUp('D')
             #wait a bit
             time.sleep(0.2)
             #click A
             pyautogui.keyDown('A')
             time.sleep(0.1)
             pyautogui.keyUp('A')
             if pyautogui.locateOnScreen('Fighting.png', grayscale= True, confidence=0.5) != None:
                time.sleep(1)
                pyautogui.keyDown('1')
                time.sleep(0.5)
                pyautogui.keyUp('1')
                time.sleep(0.2)
                if pyautogui.locateOnScreen('015.png', grayscale= True, confidence=0.9) !=None:
                    time.sleep(1)
                    print("2nd Attack")
                    pyautogui.keyDown('2')      
                    time.sleep(0.5)
                    pyautogui.keyUp('2')
                    time.sleep(0.5)
                else:
                    print("1st attack")
                    pyautogui.keyDown('1')
                    time.sleep(0.5)
                    pyautogui.keyUp('1')
                    time.sleep(0.5)

                    
                

        
        

        
