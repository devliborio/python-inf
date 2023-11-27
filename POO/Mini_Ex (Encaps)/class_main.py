class constasBancarias:
    def __init__(self, correntista, numero):
        self.correntista = correntista
        self.numero = numero
        self.__saldo = 0

    # Getter
    @property
    def movimentar(self):
        return self.__saldo
    
    # Setter
    @movimentar.setter
    def movimentar(self, valor):
        if self.__saldo + valor >= 0:
            self.__saldo += valor
        else:
           print(f"Saldo Insuficiente!")


# Mesa de Teste
guilhermeCC = constasBancarias("Guilherme Libório", 210801 - 8)
print("Saldo atual: ", guilhermeCC.movimentar,"\n")  # 0

guilhermeCC.movimentar = 1000
print("Fundos adicionados!")
print("Saldo atual: ", guilhermeCC.movimentar,"\n")  # 1000

guilhermeCC.movimentar = -400
print("Fundos removidos!")
print("Saldo atual: ", guilhermeCC.movimentar,"\n")  # 600

guilhermeCC.movimentar = -600.01
print("Saldo atual: ", guilhermeCC.movimentar)  # SALDOS INSUFICIENTES!
