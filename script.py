# Pro FUTURO
# def encontrar_palavra(array_vo, palavra):
#     for item in array_vo:
#         if isinstance(item, list):  # Verifica se é uma lista (array pai)
#             # Se for uma lista, tenta encontrar a palavra nela
#             resultado_pai = encontrar_palavra(item, palavra)
#             if resultado_pai is not None:
#                 return resultado_pai
#         elif isinstance(item, str):  # Verifica se é uma string (array filho)
#             # Se for uma string, verifica se é a palavra desejada
#             if item == palavra:
#                 return item
#     return None  # Retorna None se a palavra não for encontrada

# # Exemplo de array hierárquico
# array_vo = ["pai", ["filho1", "filho2", ["neto1", "neto2"]], "outro_pai"]

# palavra = "neto1"
# resultado = encontrar_palavra(array_vo, palavra)
# if resultado is not None:
#     print(f"A palavra '{palavra}' foi encontrada: {resultado}")
# else:
#     print(f"A palavra '{palavra}' não foi encontrada.")



# while cond:     
#     if row.iloc[count] == coluna:                            
#         cond = False
#     count+=1    

from clienteClass import Cliente
from utilsClass import Utils
# cliente = input("Qual cliente devo consultar?")

infos = Utils.readXML('3.xml')
info = Cliente.searchCliente(infos)
print(info)
# Cliente.searchCliente(cliente)