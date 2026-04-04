# Pede um número ao usuário e converte para inteiro
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2
if numero % 2 == 0:
    # Se o resto da divisão por 2 for 0, é par
    print(f"{numero} é par.")
else:
    # Caso contrário, é ímpar
    print(f"{numero} é ímpar.")
