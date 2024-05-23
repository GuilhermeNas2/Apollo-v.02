import pyautogui;
import os
import time

from utilsClass import Utils
from dotenv import load_dotenv

class AutoGui:
    
    global util 
    load_dotenv()
    util = Utils() 

    def importArchive(file):         
        try:    
                time.sleep(2)
                pyautogui.write(util.path)
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.write(file)     
                time.sleep(2)
                pyautogui.press('enter')
                return            
        except Exception as e:
            print(f'{e}')      

       