notas = []

for i in range(3):
    codigo_aluno = input("Digite seu RM: ")
    nota = float(input("Digite sua nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print(" Quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM: ", codigo_aluno, "Tirou a nota: ", nota)



