import pyautogui;
import time
from utilsClass import Utils

class AutoGui:
    
    global util 
    util = Utils() 

    def importArchive(file):         
        try:    
            imgOne = pyautogui.locateCenterOnScreen('C:\\Users\\tkdho\\Desktop\\program\\roboLogistica\\Imagens\\2.png', confidence=0.7)
            if imgOne:      
                pyautogui.click(imgOne.x, imgOne.y)
                time.sleep(2)
                pyautogui.write(util.path)
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.write(file)     
                time.sleep(2)
                pyautogui.press('enter')
                return
            else:
                print('Elemento não encontrado no destino')
        except:
            print('Elemento não encontrado na tela')        