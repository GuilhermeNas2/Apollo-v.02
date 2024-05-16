import pandas as pd
import os
from utilsClass import Utils
from dotenv import load_dotenv

class Excel:
     
     global nomeDoArquivo  
     global path   

     load_dotenv()
     path = os.getenv("pathEx")

     def searchExcelBF(data):
            print(path)
            nomeDoArquivo = path+"Fechamento BATE FORTE VARGEM .xlsx"

            try:     
                itensList = []     
                count = 0               
                df = pd.read_excel(nomeDoArquivo, sheet_name='Dados Viagens');                
                valor_procurado = data
                colunaN = "NOTAS" 
                colunaF = "Total Frete"  
                
                for index,row in df.iterrows(): 
                    while len(itensList) <= 1:                                                   
                        if row.iloc[count] == colunaN:                                                  
                         itensList.append(df.iloc[0].loc[df.iloc[0] == colunaN].index[0]) 
                                                     
                        if row.iloc[count] == colunaF: 
                         itensList.append(df.iloc[0].loc[df.iloc[0] == colunaF].index[0])  
                                                 
                        count+=1                                       
                    for column, value in row.items():                                       
                        if str(value) == str(valor_procurado):                                                                       
                            row1 = row.name 

                   
                notas = df.at[row1, itensList[0]]
                frete = df.at[row1, itensList[1]] 
                            
                frete =float('%.2f'%frete)
                notas = float(notas)
                item = frete/notas
                item = "R$ "+'%.2f'%item
                
                return item
            except:
                text ="Arquivo não encontrado no destino."    
                Utils.writeLog(text) 


Excel.searchExcelBF(1)                