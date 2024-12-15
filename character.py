import random

# Description class character

class Character:

    #Constructeur
    def __init__(self, name, description, room, msgs):
        self.name = name
        self.description = description
        self.current_room = room
        self.msgs = msgs

    # Representation string
    def __str__(self):
        return  f"{self.name} : {self.description}"
    
    def move(self):
        deplacement = random.choice(["bouge","reste"])
        sorties = self.current_room.exits
        direction = random.choice(list(sorties.keys()))
        if deplacement == "bouge":
            if not sorties :
                return False
            next_room = self.current_room.exits[direction]
            self.current_room = next_room
            print(f"{self.name} se trouve maintenant dans {self.current_room.name}\n")
            return True
        else :
            print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
        return False 
    
    def get_msg(self) :
        if not self.msgs :
            print(f"{self.name} ne veut pas vous parler.")
        self.msgs.append(self.msgs[0])
        return self.msgs.pop(0)
    