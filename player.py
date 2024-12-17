# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = dict()
        self.max_weight = 3

    # Define the move method.
    def move(self, direction, player):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        if next_room == "interdit":
            print("\nPassage interdit !\n")
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
        print(f"{self.current_room.get_long_description()}\n{self.get_history()}")
        return True

    def get_history(self):
        history_string = "Vous avez déja visité les endroits suivants :\n"
        for station in self.history :
            history_string += "\t- " + station.name + "\n"
        history_string = history_string.strip(",")
        return history_string

    def back(self):
        if len(self.history) <= 1 :
            print("\nVous etes revenu au point de depart.")
            try :
                self.current_room = self.history.pop()
            except IndexError :
                print("\nVous ne pouvez plus revenir en arriere !")
            print(self.current_room.get_long_description())
            return True
        else :
            self.current_room = self.history.pop()
            print("\nVous etes revenu en arriere.")
            print(f"{self.current_room.get_long_description()}\n{self.get_history()}")
            return True

    def get_inventory(self):
        if not self.inventory :
            return "Votre inventaire est vide.\n"
        else :
            inventory_string = "Vous disposez des items suivants :\n"
            for objet in self.inventory.values() :
                inventory_string += "\t- " + str(objet) + "\n"
            inventory_string = inventory_string.strip(",")
            return inventory_string
