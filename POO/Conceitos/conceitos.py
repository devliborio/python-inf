# 1 - Polimorfismo 
# 2 - Herança 
# 3 - Abstração
# 4 - Encapsulamento

# 1 = Criar uma função que se transforma, existem diversos tipos da mesma função.
# Ex:
class Superclasse:
    def mostrar_mensagem(self):
        return "Olá eu sou a Superclasse (Classe mãe)"
    
class Subclasse1(Superclasse):
    def mostrar_mensagem(self):
        return super().mostrar_mensagem() # O construtor super sempre faz ref a classe maior, que engloba as classes filhas.
        # return "Olá eu sou a Subclasse1"
    
class Subclasse2(Superclasse):
    def mostrar_mensagem(self):
        return Superclasse.mostrar_mensagem(self)
        # return "Olá eu sou a Subclasse2"

# Mesa de teste:
objSubclasse1 = Subclasse1()
objSubclasse2 = Subclasse2()
# print(objSubclasse1.mostrar_mensagem())

# Usando o método da "Classe mãe Superclasse"
print(objSubclasse1.mostrar_mensagem(),"\n")
print(objSubclasse2.mostrar_mensagem())