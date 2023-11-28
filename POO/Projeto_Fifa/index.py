from classes import *
from tqdm import tqdm
import time


print(" ========================= BEM VINDO(A) AO FIFA.INC ============================ ", "\n")
def menu():
    print("-" * 20)
    print("Menu do Sistema")
    print("-" * 20)
    print("OPÇÕES: ")
    print("[1] - Cadastro de Time")
    print("[2] - Cadastro de Jogadores")
    print("[3] - Cadastro da Comissão Têcnica")
    print("[4] - Encerrar Programa")


def choices():
    while True:
        menu()
        resp = int(input("Sua escolha: "))
        if resp == 1:
            print(" ========================= CADASTRO DE TIME ============================ ", "\n")

            for i in tqdm(range(10)):
                time.sleep(0.2)
            print("\n")

            global teamName, teamCityGame, teamMascot

            teamName = input("Informe o nome do time: ")
            teamCityGame = input("Informe a cidade onde o time fará os jogos como mandante: ")
            teamMascot = input("Informe o mascote do time: ")

            

            print("\n")
            print("Dados registrados!!")
            print("\n")


        elif resp == 2:
            print(" ========================= CADASTRO DE JOGADORES ============================ ", "\n")

            for i in tqdm(range(10)):
                time.sleep(0.3)
            print("\n")

            global playerName, numberShirt, teamNamePlayer

            playerName = input("Informe o nome do jogador: ")
            teamNamePlayer = input("Informe o nome do time: ")
            numberShirt = int(input("Informe o numero da camisa do jogador: "))

            print("\n")
            print("Dados registrados!!")
            print("\n")


        elif resp == 3:
            print(" ========================= CADASTRO DA COMISSÃO TÉCNICA ============================ ", "\n")

            for i in tqdm(range(10)):
                time.sleep(0.3)
            print("\n")

            global technicianName, teamNameA, preferredTacticalSchemeA

            technicianName = input("Informe o nome do técnico: ")
            teamNameA = input("Informe o nome do time: ")
            preferredTacticalSchemeA = input("Informe o esquema tático do técnico: ")

            print("\n")
            print("Dados registrados!!")
            print("\n")


            print("-" * 20, "\n")

            global assistantName, teamNameB, preferredTacticalSchemeB

            assistantName = input("Informe o nome do auxiliar do técnico: ")
            teamNameB = input("Informe o nome do time: ")
            preferredTacticalSchemeB = input("Informe o esquema tático do técnico: ")

            print("\n")
            print("Dados registrados!!")
            print("\n")

            print("-" * 20, "\n")

            global personalTrainerName, teamNameC, castPreparation

            personalTrainerName = input("Informe o nome do Preparador Físico: ")
            teamNameC = input("Informe o nome do time: ")
            castPreparation = input("Informe se a preparação física sera nos Jogadores de Linha ou Goleiros: ")

            print("\n")
            print("Dados registrados!!")
            print("\n")

        elif resp == 4:
            print(" ========================= ENCERRANDO PROGRAMA ============================ ", "\n")
            break
        else:
            print("Escolha invalida!")
choices()



print(" ========================== TIME CADASTRADO ============================ ")
teamData = Team(teamName, teamCityGame, teamMascot)
print("O time cadastrado foi: ", teamData.teamName)
print("A cidade onde o time vai jogar como mandante é: ", teamData.teamCityGame)
print("O mascote escolhido para o time foi: ", teamData.teamMascot)

print("\n")

print(" ========================== JOGADOR CADASTRADO ============================ ")
playerData = Player(playerName, teamNamePlayer, numberShirt)