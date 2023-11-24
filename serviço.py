print("Digite 1 para ver Pratos de Entrada: ")
print("Digite 2 para ver Pratos Principais: ")
print("Digite 3 para ver as Sobremesas: ")

cliente = int(input("Digite o número para verificar quais lista de prato deseja buscar: "))
preço_total_global = 0  # Variável global para acumular o preço total

def calcular_preco_total(pratos):
    # Função para calcular o preço total de uma lista de pratos
    total = sum(prato['preço'] for prato in pratos)
    return total


def Servico(cliente):

    global preço_total_global

    preço_total = 0  # Variável local para o preço total do pedido atual
    escolhas_cliente = []  # Lista para armazenar os pratos escolhidos pelo cliente

    pratosDeEntrada = [
        {'prato': 'Bruschetta de Tomate e Albahaca', 'descrição': 'Pan tostado com tomates frescos, ajo, albahaca, azeite de oliva e uma pizca de sal.', 'preço': 35},
        {'prato': 'Carpaccio de Res con Parmesano', 'descrição': 'Finas láminas de carne de res cruda, aderezadas com azeite de oliva, limão, alcaparras e queso parmesano', 'preço': 42},
        {'prato': 'Ensalada Caprese', 'descrição': 'Rodajas de tomate maduro, mussarela fresca, hojas de albahaca, aderezo balsâmico e azeite de oliva.', 'preço': 46},
        {'prato': 'Calamares a la Romana', 'descrição': 'Anillos de calamar rebozados y fritos, acompanhados de salsa de alioli para sumergir.', 'preço': 38},
        {'prato': 'Ceviche de Pescado', 'descrição': 'Trozos de pescado frescos marinados em suco de limão, coentro, cebolla morada e pimenta, servidos com aguacate e nachos.', 'preço': 47}
    ]
    pratosPrincipais = [
        {'prato': 'Filete Mignon com Salsa de Champiñones', 'descrição': 'Jugoso filete mignon à la parrilla, acompanhado de uma rica salsa de champiñones, purê de papas e espargos.', 'preço': 65},
        {'prato': 'Risoto de Mariscos', 'descrição': 'Arroz cremoso cozido lentamente com uma mistura de mariscos como camarones, calamares e mejillones, sazonado com hierbas frescas.', 'preço': 62},
        {'prato': 'Pollo Marsala', 'descrição': 'Pechuga de pollo em uma deliciosa salsa Marsala com champiñones, servida com macarrão ou purê de papas e verduras ao vapor.', 'preço': 76},
        {'prato': 'Salmão à Parrilla com Salsa de Mostaza e Miel', 'descrição': 'Salmão fresco à parrilla com molho glaseado de mostaza e mel, acompanhado de quinoa e espargos.', 'preço': 78},
        {'prato': 'Lasanha de Vegetais', 'descrição': 'Capas de macarrão intercaladas com uma mistura de vegetais assados, ricota e molho de tomate, gratinadas com queijo mussarela.', 'preço': 69}
    ]
    sobremesas = [
        {'prato': 'Tiramisú', 'descrição': 'Capas de bizcocho de café empapadas com licor, alternadas com uma mistura de mascarpone e espolvoreadas com cacau em pó.', 'preço': 45},
        {'prato': 'Coulant de Chocolate', 'descrição': 'Um pastel de chocolate quente com um centro fundido, acompanhado de helado de baunilha e salsa de frutos vermelhos.', 'preço': 48},
        {'prato': 'Cremoso de Manga com Coulis de Frutas Exóticas', 'descrição': 'Um postre suave e cremoso de manga, adornado com um coulis de frutas exóticas e trozos de frutas frescas.', 'preço': 39},
        {'prato': 'Cheesecake de Frambuesa', 'descrição': 'Pastel de queso cremoso com base de galleta, cubierto com capa de salsa de frambuesa e decorado com frutas frescas.', 'preço': 42},
        {'prato': 'Profiteroles com Helado e Chocolate Quente', 'descrição': 'Pequeñas bolas de massa rellenas de helado, bañadas em uma generosa cantidad de chocolate quente.', 'preço': 37}
    ]

    if cliente == 1:
     for i in range(len(pratosDeEntrada)):
        print(f"\n Prato {i + 1}: {pratosDeEntrada[i]['prato']}, descrição: {pratosDeEntrada[i]['descrição']} - Preço: R${pratosDeEntrada[i]['preço']},00")
        escolha = input(f"Deseja adicionar {pratosDeEntrada[i]['prato']} ao seu pedido? (S/N): ")
        
        if escolha.upper() == 'S':
            try:
                quantosPedidos = int(input("Quantos pedidos deseja fazer desse prato: "))
                if quantosPedidos > 0:
                    for _ in range(quantosPedidos):
                        escolhas_cliente.append(pratosDeEntrada[i])
                        preço_total += pratosDeEntrada[i]['preço']
                else:
                    print("Por favor, digite um número positivo maior que zero.")
            except ValueError:
                print("Você não digitou um número inteiro.")
    elif cliente == 2:
     for i in range(len(pratosPrincipais)):
        print(f"\n Prato {i + 1}: {pratosPrincipais[i]['prato']}, descrição: {pratosPrincipais[i]['descrição']} - Preço: R${pratosPrincipais[i]['preço']},00")
        escolha = input(f"Deseja adicionar {pratosPrincipais[i]['prato']} ao seu pedido? (S/N): ")
        
        if escolha.upper() == 'S':
            try:
                quantosPedidos = int(input("Quantos pedidos deseja fazer desse prato: "))
                if quantosPedidos > 0:
                    for _ in range(quantosPedidos):
                        escolhas_cliente.append(pratosPrincipais[i])
                        preço_total += pratosPrincipais[i]['preço']
                else:
                    print("Por favor, digite um número positivo maior que zero.")
            except ValueError:
                print("Você não digitou um número inteiro.")
    elif cliente == 3:
     for i in range(len(sobremesas)):
        print(f"\n Prato {i + 1}: {sobremesas[i]['prato']}, descrição: {sobremesas[i]['descrição']} - Preço: R${sobremesas[i]['preço']},00")
        escolha = input(f"Deseja adicionar {sobremesas[i]['prato']} ao seu pedido? (S/N): ")
        
        if escolha.upper() == 'S':
            try:
                quantosPedidos = int(input("Quantos pedidos deseja fazer desse prato: "))
                if quantosPedidos > 0:
                    for _ in range(quantosPedidos):
                        escolhas_cliente.append(sobremesas[i])
                        preço_total += sobremesas[i]['preço']
                else:
                    print("Por favor, digite um número positivo maior que zero.")
            except ValueError:
                print("Você não digitou um número inteiro.")
    else:
        print("Você não escolheu nenhuma opção")

    # Exibir o pedido do cliente e o preço total

    if escolhas_cliente:
     print("\n*** Seu Pedido ***")
    
    # Dicionário para rastrear a quantidade de cada prato no pedido
    quantidades_pratos = {}
    
    for i, escolha in enumerate(escolhas_cliente, start=1):
        print(f"{i}. {escolha['prato']} - R${escolha['preço']},00")

        # Atualizar o dicionário de quantidades
        quantidades_pratos[escolha['prato']] = quantidades_pratos.get(escolha['prato'], 0) + 1

    print(f"\nPreço Total: R${preço_total},00")

    # Adicionar detalhes de quantidade e valor total para cada prato no pedido
    for prato, quantidade in quantidades_pratos.items():
        valor_total_prato = quantidade * pratosDeEntrada[0]['preço']  # Assumindo que todos os pratos têm o mesmo preço
        print(f"{prato} - {quantidade}x - Valor Total: R${valor_total_prato},00")



    # Calcular o preço total do pedido atual
    preço_total_inicial = calcular_preco_total(escolhas_cliente)

    # Perguntar ao cliente se deseja continuar ou encerrar o serviço
    continuar = input("\nDeseja continuar pedindo? (S/N): ")

    if continuar.upper() == 'S':
        # Perguntar ao cliente qual lista deseja ver
        print("\nDigite 1 para ver Pratos de Entrada")
        print("Digite 2 para ver Pratos Principais")
        print("Digite 3 para ver as Sobremesas")

        # Utilizar a variável cliente passada como argumento
        novoPedido = int(input("Digite o número para verificar quais lista de prato deseja buscar: "))

        # Reinicia a função com a nova escolha do cliente
        preço_total_novo_pedido = Servico(novoPedido)

        # Adicionar o preço total do primeiro pedido ao total global apenas se o cliente optar por continuar
        preço_total_global += preço_total_inicial
    else:
        preço_total_novo_pedido = 0

        # Adicionar o preço total do primeiro pedido ao total global
        preço_total_global += preço_total_inicial

    # Retorna o preço total do pedido atual
    return preço_total_inicial + preço_total_novo_pedido

# Chamar a função com a escolha inicial do cliente
preço_total_inicial = Servico(cliente)

# Exibir o total acumulado ao final de todas as chamadas
print(f"\nMuito Obrigado! Volte Sempre. Total gasto: R${preço_total_global},00")