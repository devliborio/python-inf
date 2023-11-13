# POO (OOP) Programação Orientada a Objetos

# - É um modelo de programação.
# - Formado por Classes


class Automoveis:
    # Método Construtor:
    # Métodos, ações, comportamentos, dos objetos.
    def __init__(self, marca, modelo, cor, ano, preco, maxima):
        # Atributos, propriedades:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.veloMax = maxima
        self.veloAtual = 0
        self.ligado = False


    def acelerar(self, valor):
        if self.ligado and (self.veloAtual + valor) <= self.veloMax: # Se o carro estiver ligado e a velocidade atual for menor ou igual a velocidade maxima, acelere.
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