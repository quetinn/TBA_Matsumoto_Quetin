"""
Module représentant la classe Character.

Ce module définit la classe 'Character', qui représente un personnage dans le jeu.
Un personnage peut se déplacer entre différentes salles, interagir avec le joueur
et réagir en fonction de son inventaire.

Classes :
     Character : Représente un personnage avec des messages et des objets spécifiques.
"""
import random

# Description class character

class Character:
    """
    Représente un personnage dans le jeu.

    Attributs :
        name (str) : Le nom du personnage.
        description (str) : Une description du personnage.
        current_room (Room) : La salle où se trouve actuellement le personnage.
        msgs (list[str]) : Une liste de messages que le personnage peut dire.
        item_required (Item) : Un objet requis pour interagir avec le personnage (optionnel).
        item_gift (Item) : Un objet que le personnage peut offrir au joueur (optionnel).
    """
    #Constructeur
    def __init__(self, name, description, room, msgs, item=None, gift=None):
        """
        Initialise un objet Character.

        Args :
            name (str) : Le nom du personnage.
            description (str) : Une description du personnage.
            room (Room) : La salle initiale où se trouve le personnage.
            msgs (list[str]) : Les messages que le personnage peut dire.
            item (Item, optionnel) : L'objet requis pour interagir avec le personnage.
            gift (Item, optionnel) : L'objet offert par le personnage en échange.
        """
        self.name = name
        self.description = description
        self.current_room = room
        self.msgs = msgs
        self.item_required = item
        self.item_gift = gift

    # Representation string
    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du personnage.

        Returns :
            str : Une description formatée du personnage.
        """
        return  f"{self.name} : {self.description}"

    def move(self):
        """
        Déplace le personnage aléatoirement dans une salle adjacente, si possible. 2 chances sur 5 de deplacement

        Le personnage reste dans la salle actuelle ou se déplace vers une salle
        adjacente choisie aléatoirement si des sorties sont disponibles.

        Returns :
            bool : True si le personnage se déplace dans une autre salle, False sinon.
        """
        deplacement = random.choice(["bouge","bouge"])
        sorties = self.current_room.exits
        if not sorties :
            return False
        if deplacement == "bouge":
            direction = random.choice(list(sorties.keys()))
            next_room = self.current_room.exits[direction]
            if type(next_room) == str :
                print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
                return False
            if self.name in self.current_room.characters:
                del self.current_room.characters[self.name]
            self.current_room = next_room
            next_room.characters[self.name]=self
            print(f"{self.name} se trouve maintenant dans {self.current_room.name}\n")
            return True
        print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
        return False

    def get_msg(self, player) :
        """
        Récupère un message du personnage en fonction de l'inventaire du joueur.

        Si le personnage est un "Chomeur" et qu'il nécessite un objet pour interagir,
        la réponse varie en fonction de la possession ou non de l'objet requis.
        Sinon, les messages standards du personnage sont renvoyés de manière cyclique.

        Args :
            player (Player) : Le joueur interagissant avec le personnage.

        Returns :
            str : Le message que le personnage dit.
        """
        if not self.msgs :
            print(f"{self.name} ne veut pas vous parler.")
        if self.name == "Chomeur" :
            if self.item_gift:
                if self.item_required.name not in player.inventory :
                    return ("J'ai tres faim... Je te donnerais un objet "
                            "que j'ai trouve si tu me donnes de quoi manger.")
                return "Je le sens, t'as quelque chose pour moi! On echange?"
            self.msgs.append(self.msgs[0])
            return self.msgs.pop(0)
        self.msgs.append(self.msgs[0])
        return self.msgs.pop(0)
