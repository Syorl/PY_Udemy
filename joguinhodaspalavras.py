"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Importa o módulo 'os' para utilizar a função de limpar a tela.
import os

# Define a palavra secreta.
palavra_secreta = 'pneumoultramicroscopicossilicovulcanoconiótico'

# Inicializa a string que vai conter as letras acertadas pelo usuário.
letras_acertadas = ''

# Inicializa o contador de tentativas.
numero_tentativas = 0

# Inicia um loop infinito.
while True:
    # Solicita ao usuário que digite uma letra.
    letra_digitada = input('Digite uma letra: ')
    
    # Incrementa o contador de tentativas.
    numero_tentativas += 1

    # Verifica se o usuário digitou mais de uma letra.
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # Verifica se a letra digitada está na palavra secreta.
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Constrói a palavra formada até o momento.
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    # Exibe a palavra formada até o momento.
    print('Palavra formada:', palavra_formada)

    # Verifica se o usuário adivinhou a palavra secreta.
    if palavra_formada == palavra_secreta:
        # Limpa a tela (depende do sistema operacional).
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        
        # Reseta as variáveis para um novo jogo.
        letras_acertadas = ''
        numero_tentativas = 0
