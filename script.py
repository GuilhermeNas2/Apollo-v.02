# import xml.etree.ElementTree as ET

# def find_in_xml(element, target):
#     stack = [(element, 0)]  # Inicializa a pilha com o elemento raiz e o contador

#     while stack:
#         current_element, count = stack.pop()

#         # Se o contador atingir o número de filhos, continuamos para o próximo item na pilha
#         if count == len(list(current_element)):
#             continue

#         # Pega o filho atual
#         child = list(current_element)[count]

#         # Se encontramos o alvo, retornamos
#         if child.tag == target or child.text == target:
#             return True

#         # Empilhamos o estado atual (elemento atual e contador incrementado)
#         stack.append((current_element, count + 1))

#         # Empilhamos o novo elemento filho e começamos do índice 0
#         stack.append((child, 0))

#     return False  # Se a pilha estiver vazia e não encontramos o alvo, retornamos False

# # Exemplo de uso:
# xml_data = '''
# <root>
#     <element1>value1</element1>
#     <element2>
#         <subelement1>value2</subelement1>
#         <subelement2>value3</subelement2>
#     </element2>
#     <element3>value4</element3>
# </root>
# '''

# root = ET.parse("C:\Users\tkdho\Desktop\program\roboLogistica\Excel\3.xml")
# target = "Venda Merc.Adq.Terc."
# found = find_in_xml(root, target)
# print("Encontrado:", found)

from openpyxl import load_workbook

from clienteClass import Cliente
from utilsClass import Utils

# # Carregue o arquivo Excel
# workbook = load_workbook('C:\\Users\\tkdho\\Desktop\\program\\roboLogistica\\Excel\\Fechamento BATE FORTE VARGEM .xlsx')

# sheet = workbook['Dados Viagens']
# # sheet = workbook.active
# sua_palavra = "Notas"
# # Itere sobre as células da planilha
# for row in sheet.iter_rows():
#     for cell in row:
#         # Verifique se a célula contém a palavra desejada
#         if isinstance(cell.value, str) and 'Notas' in cell.value:
#             # Se sim, imprima o endereço da célula
#             print(f'A palavra "{sua_palavra}" está na célula {cell.coordinate}')



# from clienteClass import Cliente
# from utilsClass import Utils
# cliente = input("Qual cliente devo consultar?")
# import imaplib

# # Configurações de conexão
# imap_host = 'imap.gmail.com'
# imap_port = 993
# username = "tkdhouse2@gmail.com"
# password = 'pxij usxg jfyj xpoz'

# # Conectando-se ao servidor IMAP do Gmail
# mail = imaplib.IMAP4_SSL(imap_host, imap_port)
# mail.login(username, password)

# # Selecionando a caixa de entrada (inbox)
# mail.select('inbox')

# # Buscando e exibindo os últimos 5 emails
# status, messages = mail.search(None, 'ALL')
# messages_ids = messages[0].split()
# latest_messages_ids = messages_ids[-5:]  # Pegando os últimos 5 IDs

# for msg_id in latest_messages_ids:
#     status, msg_data = mail.fetch(msg_id, '(RFC822)')
#     raw_email = msg_data[0][1]
#     print(raw_email)  # Aqui você pode processar ou exibir o email conforme necessário

# # Fechando a conexão
# mail.logout()
    
infos = Utils.readXML('4.xml')
info = Cliente.searchCliente(infos)
print(info)
# Cliente.searchCliente(cliente)


