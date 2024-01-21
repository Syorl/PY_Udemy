# Definindo a função para realizar as operações
def calcular(num1, num2, operador):
    """
    Função para calcular uma operação aritmética com base nos dois números e no operador fornecidos.

    Args:
        num1 (float): O primeiro número.
        num2 (float): O segundo número.
        operador (str): O operador aritmético (+, -, *, /).

    Returns:
        float or str: O resultado da operação ou uma mensagem de erro se a operação for inválida.
    """
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"

# Loop principal que permite a execução contínua
while True:
    try:
        # Solicita ao usuário para inserir dois números e um operador
        numero_1 = float(input('Digite o primeiro número: '))
        numero_2 = float(input('Digite o segundo número: '))
        operador = input('Digite o operador (+, -, *, /) ou "s" para sair: ')

        # Verifica se o usuário deseja sair
        if operador == 's':
            break

        # Verifica se o operador é válido
        if operador not in '+-*/':
            print('Operador inválido.')
            continue

        # Chama a função para calcular o resultado
        resultado = calcular(numero_1, numero_2, operador)
        print(f'O resultado é: {resultado}')

        # Pede ao usuário para confirmar se deseja sair
        sair = input('Digite "s" para sair ou pressione Enter para continuar: ')

        # Verifica se o usuário deseja sair após ver o resultado
        if sair == 's':
            break

    # Trata exceção de entrada inválida
    except ValueError:
        print('Entrada inválida. Por favor, insira um número válido.')

# Mensagem de encerramento do programa
print('Programa encerrado.')
