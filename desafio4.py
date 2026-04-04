# Calculadora simples em Python

# Função que soma dois números
def soma(a, b):
	return a + b  # retorna o resultado da soma

# Função que subtrai dois números
def subtrai(a, b):
	return a - b  # retorna o resultado da subtração

# Função que multiplica dois números
def multiplica(a, b):
	return a * b  # retorna o resultado da multiplicação

# Função que divide dois números
def divide(a, b):
	if b == 0:  # verifica se o divisor é zero
		return 'Erro: divisão por zero!'  # evita erro no programa
	return a / b  # retorna o resultado da divisão


# Função principal (onde o programa acontece)
def main():
	# Mostra o menu na tela
	print('Calculadora Simples')
	print('1. Soma')
	print('2. Subtração')
	print('3. Multiplicação')
	print('4. Divisão')

	# Pede ao usuário para escolher uma operação
	escolha = input('Escolha a operação (1/2/3/4): ')

	# Pede dois números e converte para decimal (float)
	a = float(input('Digite o primeiro número: '))
	b = float(input('Digite o segundo número: '))

	# Verifica qual operação o usuário escolheu
	if escolha == '1':
		print('Resultado:', soma(a, b))  # chama a função soma

	elif escolha == '2':
		print('Resultado:', subtrai(a, b))  # chama a função subtração

	elif escolha == '3':
		print('Resultado:', multiplica(a, b))  # chama a função multiplicação

	elif escolha == '4':
		print('Resultado:', divide(a, b))  # chama a função divisão

	else:
		print('Opção inválida!')  # caso o usuário digite algo errado


# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
	main()  # chama a função principal e inicia o programa
