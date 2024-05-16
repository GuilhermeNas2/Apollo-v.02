
import xml.etree.ElementTree as ET
import re
import os
import datetime as dt

from datetime import datetime
from dotenv import load_dotenv

class Utils:

    global path 
    global dir_list     
    load_dotenv()
    
    path = os.getenv("pathXml")
    dir_list = os.listdir(path)          

    def __init__(self):
         self.dir_list = dir_list
         self.path = path

    def getDate():
        todayDate = datetime.now()
        todayDate = todayDate.strftime("%d/%m/%Y %H:%M")          
        return todayDate  
    
    def getDay():
        todayDate = dt.date.today()
        todayDate = todayDate.strftime("%d/%m/%Y")        
        return todayDate

   

    def readXML(file):
        
        try:
            archive = ET.parse(path+file)    
            root = archive.getroot() 
            # print(Utils.findElement(root))
            frase = root[0][0][25][0].text
            cliente = root[0][0][1][2].text

            
            padrao = r'NroCarga:\s*(\d+)\s*-'   
            correspondencia = re.search(padrao, frase)

            if correspondencia:          
                numero = correspondencia.group(1)
                result = {
                    "cliente": cliente,
                    "numero": numero
                }
                return result
            else:
                text ="Número não encontrado na frase."
                Utils.writeLog(text)
        except:   
            text ="Arquivo não encontrado no destino."    
            Utils.writeLog(text) 

    # def findElement(array):  
        
    #     for item in array:      
    #         print(type(item))   
    #         if isinstance(item, ):   
    #             print(1)                
    #             newArray = findElement(item)                
    #             if newArray is not None:
    #                 return newArray
    #         elif isinstance(item, str):                 
    #              if item == 'infCpl':
    #                 return item
    #     return None     


   

    def writeLog(text):
        date = Utils.getDate()
        archiveLog = open('roboLog', 'a')   
        archiveLog.write(date+"  "+text+"\n")     


Utils.readXML('3.xml')