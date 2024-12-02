        
# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go

        # Setup rooms
        
        champs = Room("champs", "dans la station Champs-Elysees Clemenceau")
        self.rooms.append(champs)
        lazare = Room("lazare", "dans la gare de Saint Lazare")
        self.rooms.append(lazare)
        cdg = Room("Charles de Gaulle - étoile  ", "dans la station Charles de Gaulle")
        self.rooms.append(cdg)
        chatelet = Room("Châtelet", "dans la station de Chatelet")
        self.rooms.append(chatelet)
        paris_nord = Room("Paris Gare du Nord", "dans la Gare du Nord")
        self.rooms.append(paris_nord)
        st_michel= Room("Saint-Michel", "dans la station Saint Michel Notre-Dame")
        self.rooms.append(st_michel)
        catacombes = Room("Les Catacombes de Paris", "dans les catacombes de Paris")
        self.rooms.append(catacombes)
        surface = Room("Surface", "à la surface")
        self.rooms.append(surface)
        aeroport = Room("Aéroport Charles de Gaulle", "dans l'aeroport. Felicitations !")
        self.rooms.append(aeroport)

        # Create exits for rooms
        champs.exits = {"13" : lazare, "1-V" : chatelet, "1-D" : cdg, "C" : st_michel}
        lazare.exits = {"13" : champs, "14" : chatelet, "E" : paris_nord}
        chatelet.exits = {"1-D" : champs, "A" : cdg, "B" : aeroport}
        cdg.exits = {"1-V" : champs, "A" : chatelet}
        st_michel.exits = {"C" : champs, "B" : aeroport, "descendre" : catacombes}
        paris_nord.exits = {"E" : lazare, "B" : aeroport, "sortir" : surface}
        surface.exits = {"redescendre" : paris_nord}
        catacombes.exits = {"remonter" : st_michel}
        aeroport.exits = {"B-N" : paris_nord, "B-C" : chatelet, "B-M" : st_michel}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = champs
        ##self.player.previous_room = self.player.current_room
        ##retour = self.player.previous_room
        ##surface.exits = {"redescendre" : retour}


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        if command_string=='':
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        print("\nVous etes un espion americain avec des informations confidentielles revelant la corruption du gouvernement francais. Vous etes poursuivi et vous avez pour objectif d'atteindre l'aeroport de Roissy afin de vous echapper. Cependant, il faut vous faire discret : vous devez vous deplacer dans les lignes parisiennes (RER ou metro) en sous-terrain. Bonne chance.")
        print(self.player.current_room.get_long_description())


def main():
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()