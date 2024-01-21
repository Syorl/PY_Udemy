# Inicializa as variáveis
codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))
altura = float(input("Digite a altura do cliente (em metros): "))
peso = float(input("Digite o peso do cliente (em kg): "))

# Inicializa variáveis para os clientes mais alto, mais baixo, mais gordo e mais magro
mais_alto = mais_baixo = codigo
altura_alto = altura_baixo = altura
mais_gordo = mais_magro = codigo
peso_gordo = peso_magro = peso

# Inicializa variáveis para a soma das alturas e pesos
soma_alturas = soma_pesos = 0
num_clientes = 0

# Loop para receber os dados dos clientes
while codigo != 0:
    # Atualiza os clientes mais alto, mais baixo, mais gordo e mais magro
    if altura > altura_alto:
        mais_alto = codigo
        altura_alto = altura
    if altura < altura_baixo:
        mais_baixo = codigo
        altura_baixo = altura
    if peso > peso_gordo:
        mais_gordo = codigo
        peso_gordo = peso
    if peso < peso_magro:
        mais_magro = codigo
        peso_magro = peso
    
    # Atualiza a soma das alturas e pesos
    soma_alturas += altura
    soma_pesos += peso
    num_clientes += 1

    # Pede os dados do próximo cliente
    codigo = int(input("Digite o código do cliente (ou 0 para encerrar): "))
    if codigo == 0:
        break
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

# Calcula a média de alturas e pesos
media_alturas = soma_alturas / num_clientes
media_pesos = soma_pesos / num_clientes

# Mostra os resultados
print(f"Código do cliente mais alto: {mais_alto}, Altura: {altura_alto}m")
print(f"Código do cliente mais baixo: {mais_baixo}, Altura: {altura_baixo}m")
print(f"Código do cliente mais gordo: {mais_gordo}, Peso: {peso_gordo}kg")
print(f"Código do cliente mais magro: {mais_magro}, Peso: {peso_magro}kg")
print(f"Média das alturas dos clientes: {media_alturas:.2f}m")
print(f"Média dos pesos dos clientes: {media_pesos:.2f}kg")
