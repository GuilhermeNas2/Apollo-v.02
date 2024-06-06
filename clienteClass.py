from excelClass import Excel

class Cliente:   

    clientes = {
        "ATACADO BF VGP": { 'Formula':Excel.searchExcelBF, 
                            'Emails': ['faturamento.vgp@bateforte.com.br','transporte9.vgp@bateforte.com.br','paulosantos@bfmail.com.br']}       
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