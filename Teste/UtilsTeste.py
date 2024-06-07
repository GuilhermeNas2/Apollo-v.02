from utilsClass import Utils
from clienteClass import Cliente

class UtilsTeste:

    def __init__(self):
        self.util = Utils()

    def xmlTeste(self):           
        infos = self.util.readXML('4.xml')    
        client = Cliente(infos)
        info = client.searchCliente()    
        if info == None or info == 'nan':
            print('ola')  
        else:
            print(info)  

    def changePathTeste(self,file):       
        self.util.changePath(file)