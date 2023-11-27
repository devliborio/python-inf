from classes import (
    Automoveis,
)

print(" ========================== ENTRADA DE DADOS ============================ ")
marca = input("Informe a marca do veiculo: ")
modelo = input("Informe o modelo do veiculo: ")
cor = input("Informe a cor do veiculo: ")
maxima = int(input("Informe a velocidade maxima do veiculo: "))

car = Automoveis(marca, modelo, cor, maxima)
print(" ========================== RETORNO DE DADOS ============================ ")
print("A marca do veiculo é: ", car.marca)
print("O modelo do veiculo é: ", car.modelo)
print("A cor do veiculo é: ", car.cor)
print("A velocidade maxima do veiculo é: ", car.veloMax)

print(" ========================== Teste de Aceleração ============================ ")
car.ligado = True  # Ligando o Chevette...
for a in range(4):
    car.acelerar(50) # Acelerando 200km
print("Acelerando...")
print("A velocidade atual do veiculo é: ", car.veloAtual)

print(" ========================== Teste de Freagem ============================ ")
for f in range(4):
    car.frear(10) # Freando a 40km
print("Freando...")
print("A velocidade atual do veiculo é: ", car.veloAtual)
