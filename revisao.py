#**Revisão Geral.**

# ! - 1 As funções em python sempre tem que vir antes da chamada dela.

# Exemplo de Bloco de código e chamada de função.
def funcaoTeste(x,y,z) -> list:
    return [x ** 2, y ** 3, z ** 4]

outputFunc = funcaoTeste(10, 100, 1000)
print(outputFunc)

#################################################################################################

# ! Uso de dicionario no python.

menu = {
    1: ['Adicionar', 'Incluir()', ],
    2: ['Remover', 'Alterar()'],
    3: ['Listar', 'Listar()'],
    4: ['Sair', 'Sair()']
}

for opcao in menu.values():
    print(opcao[0])