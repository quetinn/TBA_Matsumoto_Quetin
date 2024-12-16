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

    