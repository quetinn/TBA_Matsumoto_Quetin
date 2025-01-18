# Define the Room class.
"""
Module de gestion des pièces.

Il définit la classe Room, qui permet de représenter des pièces interconnectées
contenant des objets, des personnages,
des sorties et des missions. Il inclut des méthodes pour obtenir des descriptions
des pièces, gérer les sorties, et lister les éléments présents dans chaque pièce.

Classes:
    Room: Représente une pièce avec des attributs tels que nom, description,
    sorties, inventaire et personnages.
"""
class Room:
    """
    Représente une pièce dans notre jeu. Chaque pièce peut contenir des objets, des personnages,
    des sorties vers d'autres pièces, ainsi que des conditions d'accès.

    Attributs:
        name (str): Le nom de la pièce.
        description (str): La description de la pièce.
        exits (dict): Un dictionnaire des sorties disponibles,
                    avec les directions comme clés et les pièces comme valeurs.
        inventory (set): Un ensemble contenant les objets présents dans la pièce.
        characters (dict): Un dictionnaire des personnages présents, avec leurs noms comme clés.
        item_required (object, optional): L'objet requis pour entrer ou interagir avec la pièce.
    """

    def __init__(self, name, description, item=None):
        """
        Initialise une nouvelle instance de la classe Room.

        Args:
            name (str): Le nom de la pièce.
            description (str): Une description textuelle de la pièce.
            item (object, optional): Un objet requis pour accéder ou interagir avec la pièce.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = {}
        self.item_required = item

    def get_exit(self, direction):
        """
        Retourne la pièce accessible dans une direction donnée.

        Args:
            direction (str): La direction dans laquelle chercher une sortie.

        Returns:
            Room or None: La pièce correspondante si elle existe, sinon None.
        """
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exit_string(self):
        """
        Retourne une description textuelle des sorties disponibles depuis cette pièce.

        Returns:
            str: Une chaîne indiquant les directions des sorties disponibles.
        """
        exit_string = "Sorties : "
        for direction in self.exits:
            if self.exits.get(direction) is not None:
                exit_string += direction + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_inventory(self):
        if not self.inventory and not self.characters :
            return "Il n'y a rien ici.\n"
        else :
            inventory_string = "On voit :\n"
            for objet in self.inventory :
                inventory_string += "\t- " + str(objet) + "\n"
            for personnage in self.characters.values() :
                inventory_string += "\t- " + str(personnage) + "\n"
            inventory_string = inventory_string.strip(",")
            return inventory_string

    def get_long_description(self):
        """
        Retourne une description complète de la pièce, incluant les sorties disponibles.

        Returns:
            str: Une chaîne décrivant la pièce en détail.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
