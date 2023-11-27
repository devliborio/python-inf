class Automoveis:
    # Método Construtor:
    def __init__(self, nome, motores, rodas):
        self.nome = nome
        self.motores = motores
        self.rodas = rodas

    def buzinar(self):
        return f"Buzinando: "


class Carro(Automoveis):
    def buzinar(self):
        return f"{super().buzinar()} Biiiii"


class Barco(Automoveis):
    def buzinar(self):
        return f"{super().buzinar()} Fommm!"


class Avião(Automoveis):
    def buzinar(self):
        return f"{super().buzinar()} Tem buzina?"


# Mesa de testes
carro = Carro("BMW", 1, 4)
print("Carro:")
print("Nome:", carro.nome, "Motor(es):", carro.motores, "Rodas:", carro.rodas)
print(carro.buzinar())

aviao = Avião("Boeing", 1, 4)
print("Avião:")
print("Nome:", aviao.nome, "Motor(es):", aviao.motores, "Rodas:", aviao.rodas)
print(aviao.buzinar())

barco = Barco("Mercedes", 1, 4)
print("Barco:")
print("Nome:", barco.nome, "Motor(es):", barco.motores, "Rodas:", barco.rodas)
print(barco.buzinar())
