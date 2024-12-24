import random

# Description class character

class Character:

    #Constructeur
    def __init__(self, name, description, room, msgs, item=None, gift=None):
        self.name = name
        self.description = description
        self.current_room = room
        self.msgs = msgs
        self.item_required = item
        self.item_gift = gift

    # Representation string
    def __str__(self):
        return  f"{self.name} : {self.description}"

    def move(self):
        deplacement = random.choice(["bouge","reste"])
        sorties = self.current_room.exits
        if not sorties :
            return False
        if deplacement == "bouge":
            direction = random.choice(list(sorties.keys()))
            next_room = self.current_room.exits[direction]
            if not next_room :
                return False
            if self.name in self.current_room.characters:
                del self.current_room.characters[self.name]
            self.current_room = next_room
            next_room.characters[self.name]=self
            print(f"{self.name} se trouve maintenant dans {self.current_room.name}\n")
            return True
        else :
            print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
        return False

    def get_msg(self, player) :
        if not self.msgs :
            print(f"{self.name} ne veut pas vous parler.")
        if self.name == "Chomeur" :
            if self.item_gift:
                if self.item_required.name not in player.inventory :
                    return "J'ai tres faim... Je te donnerais un objet que j'ai trouve si tu me donnes de quoi manger."
                else :
                    return "Je le sens, t'as quelque chose pour moi! On echange?"
            else :
                self.msgs.append(self.msgs[0])
                return self.msgs.pop(0)
        self.msgs.append(self.msgs[0])
        return self.msgs.pop(0)
