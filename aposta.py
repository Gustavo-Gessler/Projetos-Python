oddInter = 4.5
empateIntFla = 3.2
oddFla = 2.1

oddPalmeiras = 2.3
oddAmerica = 6.3
empatePalAme = 4.5

def aposta():
    print("Selecione o jogo que vai querer apostar: ")
    print("1- Palmeiras - América Mg")
    print("2- Internacional - Flamengo")

    escolha = input("Digite o número da operação desejada (1/2): ")

    if escolha in ('1', '2'):

     if escolha == '1':
          print("Palmeiras - Odd(2.3) / Empate - Odd(4.5) / America Mg - Odd(6.3)")
          escolhatime = int(input("Digite 1 para Palmeiras / Digite 2 para Empate / Digite 3 para América-Mg: "))
          if escolhatime == 1:
           apostaJogo = float(input("Digite o valor da sua aposta para o palmeiras: "))
           print(f"Você ganhou {oddPalmeiras * apostaJogo}")
          elif escolhatime == 2:
           apostaJogo = float(input("Digite o valor da sua aposta para o Empate: "))
           print(f"Você ganhou {empatePalAme * apostaJogo}") 
          elif escolhatime == 3:
           apostaJogo = float(input("Digite o valor da sua aposta para o América-Mg: "))
           print(f"Você ganhou {oddAmerica * apostaJogo}")
          else:
            print("Você não escolheu nenhum resultado") 
     elif escolha == '2':
          print("Internacional - Odd(4.5) / Empate - Odd(3.2) /  Flamengo - Odd(2.1)")
          escolhatime2 = int(input("Digite 1 para Internacional / Digite 2 para Empate / Digite 3 para Flamengo: "))
          if escolhatime2 == 1:
           apostaJogo = float(input("Digite o valor da sua aposta para o Internacional: "))
           print(f"Você ganhou {oddInter * apostaJogo}")
          elif escolhatime2 == 2:
           apostaJogo = float(input("Digite o valor da sua aposta para o Empate: "))
           print(f"Você ganhou {empateIntFla * apostaJogo}") 
          elif escolhatime2 == 3:
           apostaJogo = float(input("Digite o valor da sua aposta para o Flamengo: "))
           print(f"Você ganhou {oddFla * apostaJogo}")  
          else:
           print("Você não escolheu nenhum resultado")     
     else:
       print("Opção inválida")

# Chama a função aposta
aposta()
