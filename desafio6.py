# Pede o tempo em segundos e converte para número inteiro
segundos = int(input("Digite o tempo em segundos: "))

# Calcula quantas horas cabem no total de segundos
horas = segundos // 3600  # 1 hora = 3600 segundos

# Calcula o restante que sobrou depois das horas
resto = segundos % 3600

# Calcula os minutos a partir do resto
minutos = resto // 60  # 1 minuto = 60 segundos

# Calcula os segundos restantes
segundos_restantes = resto % 60

# Mostra o resultado formatado
print(f"{horas}h {minutos}min {segundos_restantes}s")
