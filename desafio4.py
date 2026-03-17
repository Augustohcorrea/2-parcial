# Calculadora simples em Python
def soma(a, b):
	return a + b

def subtrai(a, b):
	return a - b

def multiplica(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return 'Erro: divisão por zero!'
	return a / b

def main():
	print('Calculadora Simples')
	print('1. Soma')
	print('2. Subtração')
	print('3. Multiplicação')
	print('4. Divisão')

	escolha = input('Escolha a operação (1/2/3/4): ')
	a = float(input('Digite o primeiro número: '))
	b = float(input('Digite o segundo número: '))

	if escolha == '1':
		print('Resultado:', soma(a, b))
	elif escolha == '2':
		print('Resultado:', subtrai(a, b))
	elif escolha == '3':
		print('Resultado:', multiplica(a, b))
	elif escolha == '4':
		print('Resultado:', divide(a, b))
	else:
		print('Opção inválida!')

if __name__ == '__main__':
	main()
