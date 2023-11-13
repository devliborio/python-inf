# POO (OOP) Programação Orientada a Objetos

# - É um modelo de programação.
# - Formado por Classes


class Automoveis:
    # Método Construtor:
    # Métodos, ações, comportamentos, dos objetos.
    def __init__(self, marca, modelo, cor, maxima, data=None):
        # Atributos, propriedades:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = data
        self.veloMax = maxima
        self.veloAtual = 0
        self.ligado = False


    def acelerar(self, valor):
        if self.ligado: 
            if (self.veloAtual + valor) <= self.veloMax:
                self.veloAtual += valor
        else:
            self.veloAtual = self.veloMax

    # PEP 8 (Normas e Melhores praticas do pyton, geralmente são duas linhas para separar os métodos.)
    def frear(self, valor):
        if self.ligado: # Se o carro estiver ligado, faça.
            if (self.veloAtual - valor) >= 0: # Se a velocidade atual for maior ou igual a 0, freie.
                self.veloAtual = self.veloAtual - valor
            else:
                self.veloAtual = 0