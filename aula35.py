"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
while True:  # Adicionei um loop infinito para que o código continue a pedir nomes até que a condição seja satisfeita.
    nome = input('Qual o seu nome (digite "sair" para encerrar): ')
    
    if nome == 'sair':
        break  # Encerra o loop se o usuário digitar "sair".
    
    print(f'Seu nome é {nome}')
else:
    print('Acabou') #O bloco else não parece ser necessário neste caso.
