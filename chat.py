import os

mensagens = []

nome = input("Nome: ")

while True:

    # Limpando o terminal 
    os.system("cls")
   
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    
    print("___________________")

    # Obtendo o texto
    texto = input("Mensagem: ")
    if texto == 'fim':
        break

    # Adicionando mensagem na lista:
    mensagens.append({
         'nome': nome,
         'texto': texto
     })

