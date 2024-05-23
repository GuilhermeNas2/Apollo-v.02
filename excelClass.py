import openpyxl
import pandas as pd
import os
from utilsClass import Utils
from dotenv import load_dotenv

class Excel:
     
     global nomeDoArquivo  
     global path 
    

     load_dotenv()
     path = os.getenv("pathEx")

     dir_list = os.listdir(path) 
     nomeDoArquivo = path+dir_list[0]
    
   

     def searchExcelBF(data):   
            # nomeDoArquivo = path+"Fechamento BATE FORTE VARGEM .xlsx"
            
            try:     
                itensList = []     
                count = 0                  
                valor_procurado = data
                colunaN = "NOTAS" 
                colunaF = "Total Frete" 
                
                df = pd.read_excel(nomeDoArquivo, sheet_name='Dados Viagens')  
                
                while len(itensList) <= 1:
                    for celula in df:                  
                        if df.at[count, celula] == colunaF:
                            itensList.append(celula)
                        if df.at[count, celula] == colunaN:
                            itensList.append(celula)                           
                    count += 1                 
                for index,row in df.iterrows():      
                    for column,value in row.items():  
                           
                        if str(value) == str(valor_procurado):                                 
                            row1 = row.name 

                notas = df.at[row1, itensList[0]]
                frete = df.at[row1, itensList[1]] 

                frete =float('%.2f'%frete)
                notas = float(notas)
                item = frete/notas
                item = float('%.2f'%item) 
                            
                return item
            except:
                text ="Arquivo não encontrado no destino."    
                Utils.writeLog(text,1) 


     def insertExcelN(number):
        count = 0
        lastN = ""
        df = pd.read_excel(nomeDoArquivo, sheet_name='CTE') 
        for celula in df:
            if celula.value == "":
                count += 1

            if count == 2:
                celula.value = number
                lastN = number

            # if celula.value == lastN:
   

     def main(data, valor):
        coll = 1
        rowl = 48       
        cond = True

        book = openpyxl.load_workbook(nomeDoArquivo)
        ctePage = book['CTE']

        
        while cond == True:
            cell = ctePage.cell(row=rowl, column=coll)

            if cell.value is not None:               
               rowl += 1

            if cell.value is None:                
                cell.value = data
                coll+=1
                cellTwo = ctePage.cell(row=rowl, column=coll)
                if cellTwo.value is None:
                   
                    cellTwo.value = valor
                    rowl += 1
                    coll = 1
                    cond = False
                    
                    
                
                    
        book.save(nomeDoArquivo)
Excel.main('teste', "3")
