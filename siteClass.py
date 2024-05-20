import time
import pyautogui
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from clienteClass import Cliente
from utilsClass import Utils
from autoGuiClass import AutoGui
from dotenv import load_dotenv

class Site:

    global driver   
    global runState
    global count

    load_dotenv()
    driver = webdriver.Chrome() 

    def getChrome():        
        driver.get(os.getenv("url"))
        time.sleep(2)        
        driver.maximize_window()
        return driver
        
    def login():
        Site.getChrome()
        try:
            search = driver.find_element(By.XPATH, '//*[@id="login-container"]/form/fieldset/div[1]/div[1]/div/div/input')            
            time.sleep(1)        
            searchSecond = driver.find_element(By.XPATH, '//*[@id="senha"]')
            time.sleep(1)
            btnLogin = driver.find_element(By.XPATH, '//*[@id="btnLogin"]')

            if search is None or searchSecond is None or btnLogin is None:
                text ="Elemento da tela de login não encontrado."    
                Utils.writeLog(text)   
                raise
            try:    
                if search:
                    search.send_keys(os.getenv("user"))                       
                    time.sleep(1)         
                    if searchSecond:
                        searchSecond.send_keys(os.getenv("password"))
                        time.sleep(1)       
                        if btnLogin:
                            time.sleep(1)    
                            btnLogin.click()
                            time.sleep(2)                                                                           
                            Site.fillForm()         
            except:            
                text ='Falha ao inserir dados ou clicar para acessar'    
                Utils.writeLog(text) 
            raise    
        except:  
            time.sleep(5)
            driver.refresh()
            Site.login()
       

    def importFile(file):              
         time.sleep(5)  
         btnCTe = driver.find_element(By.XPATH, '//*[@id="principalMenu"]/li[2]/a/i')
         if btnCTe:       
                try:  
                    btnCTe.click()
                    time.sleep(1)
                    btnImport = driver.find_element(By.XPATH, '//*[@id="modal-opcoes-emissao"]/div/div/div[2]/div/div[1]/button/i') 
                except:                      
                    text ='Não achei o botão de importar'
                    Utils.writeLog(text)

                if btnImport:   
                    try:  
                        time.sleep(1)
                        btnImport.click()
                        time.sleep(1)
                        btnChoosefile = driver.find_element(By.XPATH,'//*[@id="dropzone"]/div')
                    except:                         
                        text ='Não achei o botão de enviar arquivo'   
                        Utils.writeLog(text) 

                    if btnChoosefile:  
                        try:      
                            btnChoosefile.click()
                            time.sleep(1)
                            AutoGui.importArchive(file)
                            time.sleep(1)
                            btnFImport = driver.find_element(By.XPATH,'//*[@id="btnImportarXML"]')
                            time.sleep(5)
                        except:                            
                            text ='Não achei o botão depois de escolher o arquivo'    
                            Utils.writeLog(text)   

                        if btnFImport:       
                            try:                     
                                btnFImport.click()
                                time.sleep(2)
                            except: 
                                text ='Não achei o botão de finalizar import'    
                                Utils.writeLog(text)
                            
    def fillForm():
        util = Utils()        
        for i in range(0,len(util.dir_list)):     
            try:          
                Site.importFile(util.dir_list[i])                
                todayDay = Utils.getDay()

                inputDate = driver.find_element(By.XPATH, '//*[@id="divData"]/div/div/div/input')
                inputDateTwo = driver.find_element(By.XPATH, '//*[@id="dadosTipoCTe"]/div[1]/div/div/div/div[2]/div/div/div/input')
               
              
                span = driver.find_element(By.XPATH, '//*[@id="abaSeguroDiv"]/div/div[1]/h4/span')
               

                if inputDate is None or inputDateTwo is None:
                    text ='Elemento não encontrado na tela do Form'    
                    Utils.writeLog(text) 
                    raise

                try:        
                    if inputDate:                        
                        inputDate.send_keys(Keys.ENTER)
                        time.sleep(1)

                        if inputDateTwo:
                            inputDateTwo.send_keys(todayDay)
                            time.sleep(2)
                            span.click()
                            time.sleep(2)
                            spanball = driver.find_element(By.XPATH, '//*[@id="abaSeguroDiv"]/div/div[2]/div/div/div/div[1]/div/div/label[1]/span')
                            spanball.click()
                            time.sleep(2)
                            span.click()
                            time.sleep(2)
                            inputBall = driver.find_element(By.XPATH,'//*[@id="dadosTipoCTe"]/div[6]/div[2]/div/div/div[1]/div/div/label[2]/span')
                                                       
                        
                            if inputBall:
                                inputBall.click()
                                driver.execute_script("window.scrollTo(0, 2100);")
                                time.sleep(5)
                                inputValue = driver.find_element(By.XPATH, '//*[@id="subtotalPrestacao"]')
                                if inputValue:                                                                 
                                    data = Utils.readXML(util.dir_list[i])                                                                                                          
                                    info = Cliente.searchCliente(data)  
                                    time.sleep(1)                                    
                                    inputValue.send_keys(info)                                      
                                    time.sleep(1)
                                    inputText = driver.find_element(By.XPATH,'//*[@id="odc.observacao"]')                                      
                                    time.sleep(1)   
                                    if inputText: 
                                        time.sleep(1)
                                        nData = "Carga "+data['numero']                                        
                                        inputText.send_keys(nData)                                        
                                        time.sleep(2)
                                        text ='Envio completo '+data['cliente']+" observações " + info    
                                        Utils.writeLog(text) 

                                btnSend = driver.find_element(By.XPATH, '//*[@id="formId"]/div/div/div/button[1]')
                                if btnSend:
                                    # btnSend.click()
                                    time.sleep(10)
                                                                   
                except:
                    text ='Falha ao tentar inserir os dados'    
                    Utils.writeLog(text) 
                    raise
            except:
                time.sleep(2)
                driver.refresh()
        driver.quit()                          
       
            
            
               
            
            

    def scripRobot():        
           Site.login()
           
                  
                      
if __name__ == "__main__":   
    Site.scripRobot()