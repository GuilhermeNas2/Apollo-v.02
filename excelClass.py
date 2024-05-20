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
           
            dir_list = os.listdir(path) 
            nomeDoArquivo = path+dir_list[0]
            # nomeDoArquivo = path+"Fechamento BATE FORTE VARGEM .xlsx"
            print(nomeDoArquivo)  
            try:     
                itensList = []     
                count = 0                  
                valor_procurado = data
                colunaN = "NOTAS" 
                colunaF = "Total Frete"  
                 
                
                df = pd.read_excel(nomeDoArquivo, sheet_name='Dados Viagens')  
                # df = pd.read_excel(nomeDoArquivo) 
                while len(itensList) <= 1:
                    for celula in df:                  
                        if df.at[count, celula] == colunaF:
                            itensList.append(celula)
                        if df.at[count, celula] == colunaN:
                            itensList.append(celula)                           
                    count += 1                 
                for index,row in df.iterrows():       
                                 
                    # while len(itensList) <= 1: 
                        #  print(0)                                                                     
                        #  if row.iloc[count] == colunaN:  
                        #   itensList.append(df.iloc[index].loc[df.iloc[index] == colunaN].index[0]) 
                        #   index = 0
                        #   count = 0
                                                     
                        #  if row.iloc[count] == colunaF: 
                        #   itensList.append(df.iloc[index].loc[df.iloc[index] == colunaF].index[0])  
                        #   index = 0
                        #   count = 0
                                                
                        #  count+=1                                       
                    for column,value in row.items():  
                           
                        if str(value) == str(valor_procurado):                                 
                            row1 = row.name
                         
                
                # teste = df.at[row1,'Unnamed: 3']
                
                notas = df.at[row1, itensList[0]]
                frete = df.at[row1, itensList[1]] 
                print(notas)
                print(frete)
                # frete =float('%.2f'%frete)
                # notas = float(notas)
                # item = frete/notas
                # item = float('%.2f'%item) 
                # print(item)               
                # return item
            except:
                text ="Arquivo não encontrado no destino."    
                Utils.writeLog(text) 


# Excel.searchExcelBF(6)