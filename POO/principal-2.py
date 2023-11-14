from classes import (
    Automoveis,
)

print(" ========================== ENTRADA DE DADOS ============================ ")
marca = input("Informe a marca do veiculo: ")
modelo = input("Informe o modelo do veiculo: ")
cor = input("Informe a cor do veiculo: ")
maxima = int(input("Informe a velocidade maxima do veiculo: "))

chevette = Automoveis(marca, modelo, cor, maxima)

print(" ========================== RETORNO DE DADOS ============================ ")
print("A marca do veiculo é: ", chevette.marca)
print("O modelo do veiculo é: ", chevette.modelo)
print("A cor do veiculo é: ", chevette.cor)
print("A velocidade maxima do veiculo é: ", chevette.veloMax)
chevette.ligado = True  # Ligando o Chevette...
for a in range(4):
    chevette.acelerar(50)
print("Velocidade Atual: ", chevette.veloAtual)  # VeloMax
