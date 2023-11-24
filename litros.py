volume = float(input("Digite o Volume do seu recipiente em litros: "))
tempo = float(input("Digite o tempo em segundos que ele demora para encher: "))

def vazao():
    Vazao = 3.6 * volume / tempo
    print("Total de litros/hora para encher seu recipiente ficou em: ", Vazao, "m³/h")
    
vazao()
