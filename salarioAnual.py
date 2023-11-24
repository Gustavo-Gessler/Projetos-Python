SalarioAnual = []
total_ganho = 0

for i in range(12):
    SalarioMes = int(input("Digite seu salário por mês: "))
    SalarioAnual.append(SalarioMes)
    total_ganho += SalarioMes

for mes, sal in enumerate(SalarioAnual):
    mes += 1
    print("O seu salário no mês", mes, "foi de: ", sal)

print("O total ganho no ano foi de: ", total_ganho)
