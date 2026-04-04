capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa de juros (%): ")) / 100
tempo = float(input("Digite o tempo: "))

juros = capital * taxa * tempo
montante = capital + juros

print(f"Juros: {juros}")
print(f"Montante final: {montante}")
