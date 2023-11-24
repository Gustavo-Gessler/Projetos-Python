def aposta(jogos):
    acumulado_por_jogo = {'time1': 0, 'empate': 0, 'time2': 0}

    for i in range(len(jogos)):
        print(f"\nJogo {i + 1}: {jogos[i]['time1']} vs {jogos[i]['time2']}")
        print(f"1- {jogos[i]['time1']} - Odd({jogos[i]['odds'][0]}) / 2- Empate - Odd({jogos[i]['odds'][1]}) / 3- {jogos[i]['time2']} - Odd({jogos[i]['odds'][2]})")

        escolha_time = int(input("Digite o número da operação desejada (1/2/3): "))
        
        if escolha_time in (1, 2, 3):
            acumulado_por_jogo['time1'] += jogos[i]['odds'][0] if escolha_time == 1 else 0
            acumulado_por_jogo['empate'] += jogos[i]['odds'][1] if escolha_time == 2 else 0
            acumulado_por_jogo['time2'] += jogos[i]['odds'][2] if escolha_time == 3 else 0
        else:
            print("Opção inválida. Não foi feita nenhuma aposta para este jogo.")

    return acumulado_por_jogo

def total_ganho(acumulado_por_jogo):
    total = sum(acumulado_por_jogo.values())
    print(f"\nOdd Acumulada: {total}")

def multipla():
    jogos = [
        {'time1': 'Palmeiras', 'time2': 'América Mg', 'odds': [2.3, 4.5, 6.3]},
        {'time1': 'Internacional', 'time2': 'Flamengo', 'odds': [4.5, 3.2, 2.1]},
        {'time1': 'Real Madrid', 'time2': 'Bayer de Munique', 'odds': [1.5, 3.2, 3]},
        {'time1': 'Liverpool', 'time2': 'Manchester City', 'odds': [3.2, 2.8, 1.6]},
        {'time1': 'Milan', 'time2': 'Inter de Milão', 'odds': [2.5, 3.3, 2.8]},
        {'time1': 'Cruzeiro', 'time2': 'Coritiba', 'odds': [1.7, 2.6, 3.3]},
        {'time1': 'Denver Nuggets', 'time2': 'Cleveland Cavaliers', 'odds': [2.2, 3.2, 2.7]},
        {'time1': 'São Paulo', 'time2': 'Fluminense', 'odds': [2.5, 2.7, 2.6]},
        {'time1': 'Chicaco Bulls', 'time2': 'Utha Jazz', 'odds': [1.9, 2.4, 3.8]},
        {'time1': 'Borrusia Dortmund', 'time2': 'Leipzig', 'odds': [1.7, 3.1, 3.6]}
        # Adicione mais jogos conforme necessário
    ]

    quantidade_jogos = int(input("Digite a quantidade de jogos que deseja apostar: "))

    if quantidade_jogos > len(jogos):
        print("Você digitou um número maior do que os jogos disponíveis.")
    else:
        jogos_selecionados = jogos[:quantidade_jogos]
        acumulado_por_jogo = aposta(jogos_selecionados)
        total_ganho(acumulado_por_jogo)

        valor_aposta_final = float(input("Digite o valor da sua aposta final: "))
        ganho_potencial_final = valor_aposta_final * sum(acumulado_por_jogo.values())
        print(f"Você ganhou {ganho_potencial_final} se todos os resultados forem a seu favor.")

# Chama a função multipla
multipla()
