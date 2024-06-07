from excelClass import Excel

class Cliente:   

    clientes = {
        "ATACADO BF VGP": { 'Formula':Excel.searchExcelBF, 
                            'Emails': ['tkdhouse2@gmail.com']}       
    }    

    def searchCliente(data):      
      clienteAtual = data['cliente']      
      if clienteAtual in Cliente.clientes:
            clientFunc = Cliente.clientes[clienteAtual]['Formula']
            print(clientFunc)
            info = clientFunc(data['numero'])            
            return info

    def searchEmail(data):
      clienteAtual = data['cliente']      
      if clienteAtual in Cliente.clientes:
            clientEmails = Cliente.clientes[clienteAtual]['Emails']   
            return clientEmails