"""
Module contenant la classe Game.

La classe Game représente le moteur principal du jeu d'aventure textuel.
Elle configure les éléments du jeu, traite les commandes des joueurs
et gère la boucle principale de jeu.
"""
# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:
    """
    Classe principale pour gérer le jeu.

    Attributs:
        finished (bool): Indique si le jeu est terminé.
        rooms (list[Room]): Liste des salles disponibles dans le jeu.
        commands (dict): Dictionnaire des commandes disponibles.
        player (Player): Instance représentant le joueur.
        items (list[Item]): Liste des objets du jeu.
        characters (list[Character]): Liste des personnages non-joueurs.
    """
    # Constructor
    def __init__(self):
        """
        Initialise les attributs de la classe Game.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = []
        self.characters = []

    # Setup the game
    def setup(self):
        """
        Configure les éléments nécessaires au jeu, tels que :
        - Les commandes disponibles.
        - Les objets présents dans les salles.
        - Les salles et leurs sorties.
        - Les personnages non-joueurs.
        - L'état initial du joueur.
        """
        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction"
                     "(en utilisant les lignes de metro ou rer)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir en arriere", Actions.back, 0)
        self.commands["back"] = back
        history = Command("history",
                           " : affiche l'historique des lieux visites", Actions.history, 0)
        self.commands["history"] = history
        check = Command("check", " : affiche l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : recherche les objets dans la station/lieu", Actions.look,0)
        self.commands["look"] = look
        take = Command("take", " <objet> : prendre un objet", Actions.take,1)
        self.commands["take"] = take
        drop = Command("drop", " <objet> : reposer un objet", Actions.drop,1)
        self.commands["drop"] = drop
        talk = Command("talk", " <PNJ> : parler avec le PNJ", Actions.talk,1)
        self.commands["talk"] = talk
        exchange = Command("exchange", " <PNJ> : echanger avec le PNJ", Actions.exchange,1)
        self.commands["exchange"] = exchange

        # Setup items non associes a un Room
        passe = Item("Passe", "un passe Navigo qui donne acces aux trains", 1)
        self.items.append(passe)
        monnaie = Item("Monnaie", "7€ de monnaie", 0.1)
        self.items.append(monnaie)

        # Setup rooms
        champs = Room("Champs Elysees", "aux Champs-Elysees, vous aperecevez l'Arc de Triomphe.")
        self.rooms.append(champs)
        clemenceau = Room("Champs Elysees Clemenceau", "dans la station Champs-Elysees Clemenceau.")
        self.rooms.append(clemenceau)
        lazare = Room("Gare de Saint-Lazare", "dans la gare de Saint Lazare.", passe)
        self.rooms.append(lazare)
        cdg = Room("Charles de Gaulle - étoile  ", "dans la station Charles de Gaulle.", passe)
        self.rooms.append(cdg)
        chatelet = Room("Châtelet", "dans la station de Chatelet.", passe)
        self.rooms.append(chatelet)
        paris_nord = Room("Paris Gare du Nord", "dans la Gare du Nord.", passe)
        self.rooms.append(paris_nord)
        st_michel= Room("Saint-Michel", "dans la station Saint Michel Notre-Dame.", passe)
        self.rooms.append(st_michel)
        catacombes = Room("Les Catacombes de Paris", "dans les catacombes de Paris.")
        self.rooms.append(catacombes)
        surface = Room("Surface", "à la surface.")
        self.rooms.append(surface)
        aeroport = Room("Aéroport Charles de Gaulle",
                         "dans l'aeroport. Felicitations !", None, None)
        self.rooms.append(aeroport)

        # Create exits for rooms
        champs.exits = {"descendre" : clemenceau}
        clemenceau.exits = {"13" : lazare, "1-V" : chatelet,
                             "1-D" : cdg, "C" : st_michel, "remonter" : champs}
        lazare.exits = {"13" : clemenceau, "14" : chatelet, "E" : paris_nord}
        chatelet.exits = {"1-D" : clemenceau, "A" : cdg, "B" : aeroport, "14" : lazare}
        cdg.exits = {"1-V" : clemenceau, "A" : chatelet}
        st_michel.exits = {"C" : clemenceau, "B" : aeroport, "descendre" : catacombes}
        paris_nord.exits = {"E" : lazare, "B" : aeroport, "sortir" : surface}
        surface.exits = {"redescendre" : paris_nord}
        catacombes.exits = {"remonter" : st_michel}
        aeroport.exits = {"B-N" : paris_nord, "B-C" : chatelet, "B-M" : st_michel}

        # Setup items in rooms
        sword = Item("Sword", "une épée au fil tranchant comme un rasoir", 3)
        self.items.append(sword)
        chatelet.inventory.add(sword)
        caca = Item("Caca", "un caca", 2)
        self.items.append(caca)
        cdg.inventory.add(caca)
        sandwich = Item("Sandwich", "un delicieux sandwich", 0.5)
        self.items.append(sandwich)
        clemenceau.inventory.add(sandwich)
        billet = Item("Billet", "un billet de 20€", 0.1)
        self.items.append(billet)
        cdg.inventory.add(billet)
        paris_nord.inventory.add(billet)
        billet_avion = Item("Billet_avion", "un billet d'avion pour Singapour", 1)
        self.items.append(billet_avion)

        # Setup characters in rooms
        chomeur = Character("Chomeur", "un chomeur affamé", clemenceau,
                             ["Merci encore pour le sandwich, vous me sauvez.",
                              "Ravi d'avoir fait affaire avec vous"], sandwich, passe)
        self.characters.append(chomeur)
        clemenceau.characters[chomeur.name]=chomeur
        policier = Character("Policier", "un policier francais a votre recherche", lazare,
                              ["VOUS ETES EN ETAT D'ARRESTATION !!!","HAUT LES MAINS!"])
        self.characters.append(policier)
        lazare.characters[policier.name]=policier
        boulanger = Character("Boulanger", "un boulanger sympathique", champs,
                               ["Voulez-vous acheter un sandwich ? Ca sera 7 euros svp","Merci"],
                                 monnaie, sandwich)
        self.characters.append(boulanger)
        champs.characters[boulanger.name]=boulanger
        billettiste = Character("billettiste", "un vendeur de billet d'avion", aeroport,
                                 ["Voici votre billet.","Bon vol"], billet, billet_avion)
        self.characters.append(billettiste)
        aeroport.characters[billettiste.name]=billettiste


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = champs
        self.player.inventory["Monnaie"] = monnaie
        self.player.inventory["Passe"] = passe

    # Play the game
    def play(self):
        """
        Démarre et gère la boucle principale du jeu.
        Le joueur peut entrer des commandes jusqu'à ce que le jeu soit terminé.
        """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Traite une commande saisie par le joueur.

        Args:
            command_string (str): La commande saisie par le joueur.
        """
        if command_string=='':
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands:
            print(
                f"\nCommande '{command_word}' non reconnue."
                  " Entrez 'help' pour voir la liste des commandes disponibles.\n"
            )
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        """
        Affiche un message de bienvenue et une introduction au jeu.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        print("\nVous etes un espion americain avec des informations confidentielles revelant"
              " la corruption du gouvernement francais. Vous etes poursuivi et vous avez pour" 
              "objectif d'atteindre l'aeroport de Roissy afin de vous echapper. Cependant," 
              "il faut vous faire discret : vous devez vous deplacer dans les lignes parisiennes"
               " (RER ou metro) en sous-terrain. Bonne chance.")
        print(self.player.current_room.get_long_description())


def main():
    """
    Point d'entrée principal pour exécuter le jeu.
    """
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
