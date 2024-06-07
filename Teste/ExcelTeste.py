from excelClass import Excel
from utilsClass import Utils
from clienteClass import Cliente

class ExcelTeste:

    def __init__(self):
        self.excel = Excel()
     
    def excelTeste():
        info = Excel.teste(3407)
        if info == None or info == 'nan':                
            print('ola')  
        else:
            print(info)  

     
    def insertExcelTeste():
        infos = Utils.readXML('5.xml')
        listNumber = list()
        listNumber = [infos['numero']]
        info = Cliente.searchCliente(infos)    

        for i in range(0, len(listNumber),1): 
            count = 0
            while count <= 1:                     
                Excel.insertExcelN(listNumber[i], '54156/5656', info )
                count +=1
       