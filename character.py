import random

# Description class character

class Character:

    #Constructeur
    def __init__(self, name, description, msgs):
        self.name = name
        self.description = description
        self.current_room = None
        self.msgs = msgs
        self.inventory = dict()

    # Representation string
    def __str__(self):
        return  f"{self.name} : {self.description}"
    
    def move(self):
        deplacement = random.choice(["bouge","reste"])
        sorties = self.current_room.exits
        direction = random.choice(sorties.keys())
        for pnj in self.inventory.values() :
            if deplacement == "bouge" and pnj.name == "Policier":
                if not sorties :
                    return False
                next_room = pnj.current_room.exits[direction]
                self.current_room = next_room
                print(f"{pnj.name} se trouve maintenant dans {pnj.current_room}")
                return True
            print(f"{pnj.name} se trouve maintenant dans {pnj.current_room}")
            return False 