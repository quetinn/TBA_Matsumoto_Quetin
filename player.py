"""
Module représentant la classe Player.

Ce module définit la classe `Player`, qui représente le joueur dans le jeu. 
Le joueur peut se déplacer, suivre son historique de déplacements et gérer 
son inventaire.

Classes :
    - Player : Représente un joueur avec un nom, une position actuelle, un inventaire
               et un historique de déplacements.
"""
class Player():
    """
    Représente un joueur dans le jeu.

    Attributs :
        name (str) : Le nom du joueur.
        current_room (Room) : La salle actuelle où se trouve le joueur.
        history (list[Room]) : L'historique des salles visitées par le joueur.
        inventory (dict) : L'inventaire du joueur, contenant des objets (Item).
        max_weight (float) : Le poids maximum transportable par le joueur.
    """
    # Define the constructor.
    def __init__(self, name):
        """
        Initialise un joueur.

        Args :
            name (str) : Le nom du joueur.
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 500
        self.move_count = 0

    # Define the move method.
    def move(self, direction, player):
        """
        Permet au joueur de se déplacer dans une direction donnée.

        Args :
            direction (str) : La direction dans laquelle le joueur souhaite se déplacer.
            player (Player) : Le joueur effectuant le déplacement.

        Returns :
            bool : True si le déplacement est réussi, False sinon.
        """
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        if next_room == "malaise":
            print("\nMalaise voyageur ! Le traffic est interrompu ici.\n")
            return False

        if next_room == "unique":
            print("\nPassage a sens unique !\n")
            return False
        objet_recquis = next_room.item_required
        if objet_recquis and objet_recquis not in player.inventory.values() :
            print("\nVous avez besoin d'un passe pour acceder aux trains.\n")
            return False
        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        self.move_count += 1
        print(f"{self.current_room.get_long_description()}\n{self.get_history()}")
        print(f"Vous vous etes deplace {self.move_count} fois.\n")
        return True

    def get_history(self):
        """
        Retourne une chaîne décrivant l'historique des lieux visités par le joueur.

        Returns :
            str : Une liste des salles précédemment visitées.
        """
        history_string = "Vous avez déja visité les endroits suivants :\n"
        for station in self.history :
            history_string += "\t- " + station.name + "\n"
        history_string = history_string.strip(",")
        return history_string

    def back(self):
        """
        Permet au joueur de revenir à la salle précédente.

        Returns :
            bool : True si le retour est effectué avec succès, False sinon.
        """
        if len(self.history) <= 1 :
            print("\nVous etes revenu au point de depart.")
            try :
                self.current_room = self.history.pop()
            except IndexError :
                print("\nVous ne pouvez plus revenir en arriere !")
            print(self.current_room.get_long_description())
            return True
        self.current_room = self.history.pop()
        print("\nVous etes revenu en arriere.")
        print(f"{self.current_room.get_long_description()}\n{self.get_history()}")
        return True

    def get_inventory(self):
        """
        Retourne une chaîne décrivant le contenu de l'inventaire du joueur.

        Returns :
            str : Une liste des objets dans l'inventaire, ou un message indiquant que
                  l'inventaire est vide.
        """
        if not self.inventory :
            return "Votre inventaire est vide.\n"
        inventory_string = "Vous disposez des items suivants :\n"
        for objet in self.inventory.values() :
            inventory_string += "\t- " + str(objet) + "\n"
        inventory_string = inventory_string.strip(",")
        return inventory_string
