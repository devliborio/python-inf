class Team:
    def __init__(self, teamName, teamCityGame, teamMascot):
        self.teamName = teamName
        self.teamCityGame = teamCityGame
        self.teamMascot = teamMascot


class Player(Team):
    def __init__(self, playerName, teamName, numberShirt):
        self.playerName = playerName
        self.numberShirt = numberShirt
        self.Team.teamName = teamName


class Technician(Team):
    def __init__(self, technicianName, teamName, preferredTacticalScheme):
        self.technicianName = technicianName
        self.preferredTacticalScheme = preferredTacticalScheme  # Esquema tático tem que ser nesse formato -> 4-3-3
        self.Team.teamName = teamName

    def dar_coletiva(self):
        return "O técnico está dando uma coletiva de imprensa"


class Assistant(Team):
    def __init__(self, assistantName, teamName, preferredTacticalScheme):
        self.assistantName = assistantName
        self.preferredTacticalScheme = preferredTacticalScheme # Esquema tático tem que ser nesse formato -> 4-3-3
        self.Team.teamName = teamName

    def dar_coletiva(self):
        return "O auxiliar está dando uma coletiva de imprensa"


class PersonalTrainer(Team):
    def __init__(self, personalTrainerName, teamName, castPreparation):
        self.personalTrainerName = personalTrainerName
        self.castPreparation = castPreparation  # Jogadores de linha ou Goleiros
        self.Team.teamName = teamName

    def dar_coletiva(self):
        return "O Preparador Físico está dando uma coletiva de imprensa"

    def casPreparation(self, type):
        if type == "Goleiros" or "goleiros":
            return "Preparando Goleiros..."
        elif type == "Jogadores de Linha" or "jogadores de linha":
            return "Preparando Jogadores de Linha..."
        else:
            return "Escolha invalida!"
