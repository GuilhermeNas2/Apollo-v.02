from openpyxl import load_workbook
from decimal import Decimal
import pandas as pd
import os
import re
from utilsClass import Utils
from dotenv import load_dotenv
import xlwings 

class Excel:
     
     global nomeDoArquivo  
     global path   

     load_dotenv()
     path = os.getenv("pathEx")

     dir_list = os.listdir(path)     
    
     nomeDoArquivo = path+dir_list[0]    
     
     def teste(data):
        valor_procurado = data
        itensList = []          

        colunaN = "NOTAS" 
        colunaF = "Total Frete"  

        wb = load_workbook(nomeDoArquivo)    

        ctePage = wb['Dados Viagens']
        rowC = None
        
        while len(itensList) <= 1:
            for row in ctePage:            
                for cel in row:
                    if cel.value == colunaF:                                                       
                        itensList.append(cel.column_letter)                        
                    if cel.value == colunaN:
                        itensList.append(cel.column)   

        for row in ctePage.iter_rows(max_row=350,min_col= 4, max_col= 4):
            for cel in row: 
                if type(cel.value) == float:
                    valor_procurado = data+".0"                                         
                if str(cel.value) == str(valor_procurado) and rowC is None:                                    
                    rowC = cel.row 
        if rowC == None:
            return rowC           
        notas = Decimal(ctePage.cell(row=rowC, column=itensList[0]).value)  
    
        app = xlwings.App(visible=False)  
        wbl = xlwings.Book(nomeDoArquivo)
        
        ctePagel = wbl.sheets['Dados Viagens']
        loc = itensList[1]+str(rowC)        
        frete = Decimal(ctePagel.range(loc).value) 
       
        # item = frete/notas
        # item = item.quantize(Decimal('1.00'))
        
        frete =float('%.2f'%frete)                
        notas = float(notas)
        item = frete/notas
        item = float('%.2f'%item)                  
        wb.close()
        app.quit()        
        return item
        
                  

     def searchExcelBF(data):   
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
                        print(value)   
                        if str(value) == str(valor_procurado):                                 
                            row1 = row.name   
                
                frete = df.at[row1, itensList[1]]
                notas = df.at[row1, itensList[0]]                                 
                print(frete)
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
             
        wb = load_workbook(nomeDoArquivo)      
        ctePage = wb['CTE']    

        padrao = r'\s*(\d+)\s*/' 
        data = re.search(padrao, data)

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
                cell.value = data.group(1)
                coll+=1
                cellTwo = ctePage.cell(row=rowl, column=coll)
                if cellTwo.value is None:                   
                    cellTwo.value = valor
                    rowl += 1
                    coll = 1
                    cond = False 
                                  
        wb.save(nomeDoArquivo)  
        # with pd.ExcelWriter(nomeDoArquivo, engine='openpyxl', mode='a',if_sheet_exists='replace') as writer:
        #     writer._book = wb
        #     writer._sheets = {ws.title: ws for ws in wb.worksheets}

        #     # Escrever o DataFrame na planilha específica
        #     df.to_excel(writer, sheet_name='CTE', index=False)     
           
        return            
                    
                
                    
# Excel.insertExcelN('6','152745/1','1')        
# Excel.teste('3414011')   


