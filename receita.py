# codigo sem função

fluxo_caixa = []

print("---------------")
print("@ Fluxo Caixa")
print("---------------")
print("1- Adicionar Receita")
print("2-Adicionar Despesa")
print("\n# Digite outro numero para encerrar \n#")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("Digite o valor: "))
    fluxo_caixa.append({
        'nome': nome,
        'valor': valor
    })

while True:

    opcao = int(input ("Digite a opção: "))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break


# Nota Fiscal

total = 0

for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", valor R$", fc['valor'])
    total = total + fc['valor']

print("O Seu saldo atual é: ", total)