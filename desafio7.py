# Pede o capital inicial (valor do dinheiro)
capital = float(input("Digite o capital inicial: "))

# Pede a taxa de juros em porcentagem e converte para decimal
taxa = float(input("Digite a taxa de juros (%): ")) / 100

# Pede o tempo (pode ser meses, anos, etc.)
tempo = float(input("Digite o tempo: "))

# Calcula os juros simples
juros = capital * taxa * tempo

# Calcula o montante final (capital + juros)
montante = capital + juros

# Mostra os juros calculados
print(f"Juros: {juros}")

# Mostra o valor total final
print(f"Montante final: {montante}")
