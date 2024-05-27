
import xml.etree.ElementTree as ET
import re
import os
import datetime as dt

from datetime import datetime
from dotenv import load_dotenv
from plyer import notification

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

    def buscar_tag(elemento, tag_procurada, ):    

        if elemento.tag == tag_procurada:            
            return elemento.text       
       
        for filho in elemento:
            data = Utils.buscar_tag(filho, tag_procurada)
            if data:
                return data
        return False    
   

    def readXML(file):       
        
        try:
            
            archive = ET.parse(path+file)            
            root = archive.getroot() 
            
            tag_procurada = "{http://www.portalfiscal.inf.br/nfe}xFant"
            cliente = Utils.buscar_tag(root, tag_procurada)    
            
            tag_procurada = "{http://www.portalfiscal.inf.br/nfe}infCpl"
            frase = Utils.buscar_tag(root, tag_procurada)   
            
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
                text ="Número não encontrado na frase ou Nome da empresa não encontrado."
                Utils.writeLog(text,1)
        except:   
            try:
                if archive in vars():                    
                    return                    
            except:
                text ="Arquivo XML não encontrado no destino."    
                Utils.writeLog(text,1)
   

    def writeLog(text, mode):

        date = Utils.getDate()

        if mode == 1:
            archiveLog = open('roboLog', 'a')   
        
        if mode == 2:
            archiveLog = open('succesLog', 'a') 

        archiveLog.write(date+"  "+text+"\n")     


    def changePath(file):  
        newPath = os.getenv("pathConcluidos")
        os.rename(path+file, newPath+file )


    def notify(title,message):
     notification.notify(
          title=title,
          message=message,
          app_name='Alerta do windows',
          timeout=10
     )

    def msg():
      Utils.notify('Apollo', 'O processo foi finalizado')

