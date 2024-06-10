from excelClass import Excel

class Cliente:   
    #Podem existir 2 ou 3 meios de resolver o problemas dos arquivos Exceis, 1 - Se por acaso a função seja identica para todos os clientes
    #deve ser passado então apenas o arquivo excel do cliente, e a classe deve ser instanciada para que a função passo implicitamente o parametro Self.
    #No segundo jeito o arquivo excel devera ser passado como parametro de todas as funções que mexem com o caminho dele, tanto a search como a insert
    clientes = {
        "Cliente": { 'Formula':Excel.searchExcelBF, 
                            'Excel': 'teste.xlsx',
                            'Emails': ['teste@gmail.com']}       
    }    

    def __init__(self, data):
        self.clienteAtual = data['cliente']
        self.number = data['numero']

    def searchCliente(self):
      excel = Excel()
      if self.clienteAtual in Cliente.clientes:
            excel = excel.initialize(Cliente.clientes[self.clienteAtual]['Excel'])    
            clientFunc = Cliente.clientes[self.clienteAtual]['Formula']            
            info =  clientFunc(self.number)            
            return info

    def searchEmail(self):         
      if  self.clienteAtual in Cliente.clientes:
            clientEmails = Cliente.clientes[ self.clienteAtual]['Emails']   
            return clientEmails