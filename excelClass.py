from openpyxl import load_workbook
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
     
     if dir_list[0] == 'tempo.xlsx':         
        nomeDoArquivo = path+dir_list[1]   
     else:
        nomeDoArquivo = path+dir_list[1]    

     def searchExcelBF(data):   
            try:     
                itensList = []                    
                count = 0    
                valor_procurado = data
                colunaN = "NOTAS" 
                colunaF = "Total Frete"                
                      
                df = pd.read_excel(nomeDoArquivo, sheet_name='Dados Viagens', engine='openpyxl') 

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
                try:                             
                    if df is None:                        
                        text ="Arquivo Excel não encontrado."    
                        Utils.writeLog(text,1)
                    raise                              
                except:    
                    try:
                        if  item in vars():
                            return
                    except:
                        text ="Valor do frete não encontrado."    
                        Utils.writeLog(text,1)   


     def insertExcelN(title,data, valor):
        coll = 1
        maxColl = 26    
        rowl = None  
        cond = True
        count = 0

        wb = load_workbook(path+'tempo.xlsx')      
        ctePage = wb['CTE']
        
        for row in ctePage.iter_rows(min_col= 1, max_col=26):            
            for cel in row:
                if cel.value == title:                                                         
                    rowl = cel.row + 1 
                    coll = cel.column + 1
        
        if rowl == None:  
            rowl = 48   
            if coll == 1 and ctePage.cell(row=rowl, column=coll).value is not None:
                while count <= 2:   
                    cellTitle = ctePage.cell(row=rowl, column=coll)                
                    if cellTitle.value is None and coll <= maxColl:                    
                        count += 1        
                    elif cellTitle.value is not None and coll <= maxColl:
                        count = 0                
                    if coll <= maxColl:
                        coll += 1    
                    else:    
                        for row in ctePage.iter_rows(min_row=rowl,max_row=rowl,min_col= 1, max_col=26):            
                            for cel in row:
                                if cel.value is not None:                                                                    
                                    coll = 1
                                    rowl +=1
                                    count = 2
                coll -= 1      
            cellTitle = ctePage.cell(row=rowl, column=coll).value = title
            coll += 1           
            cellTitle = ctePage.cell(row=rowl, column=coll).value = "Valor CTE"  
                                
        
        if coll > 1:            
            coll -= 1
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
                                      
        wb.save(path+'tempo.xlsx')  
        # with pd.ExcelWriter(nomeDoArquivo, engine='openpyxl', mode='a',if_sheet_exists='replace') as writer:
        #     writer._book = wb
        #     writer._sheets = {ws.title: ws for ws in wb.worksheets}

        #     # Escrever o DataFrame na planilha específica
        #     df.to_excel(writer, sheet_name='CTE', index=False)            
            
            
        print('foi')        
        return            
                    
                
                    
# Excel.insertExcelN('6','1','1')        
# Excel.insertExcelN('7','1','1')   


