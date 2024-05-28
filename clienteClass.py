from excelClass import Excel

class Cliente: 
  

    clientes = {
        "ATACADO BF VGP": Excel.teste        
    }    

    def searchCliente(data):      
      clienteAtual = data['cliente']      
      if clienteAtual in Cliente.clientes:
            clientFunc = Cliente.clientes[clienteAtual]
            info = clientFunc(data['numero'])
            return info


