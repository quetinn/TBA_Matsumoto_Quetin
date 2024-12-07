# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
            
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties : " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    
    # return a string describing items in the room
    #def add_item(self,game):
        for objet in game.items :
            self.inventory.add(objet.name)

    def get_inventory(self):
        if not self.inventory :
            return "Il n'y a rien ici.\n"
        else :
            inventory_string = "La pièce contient :\n"
            for objet in self.inventory :
                inventory_string += "\t- " + print(objet) + "\n"
            inventory_string = inventory_string.strip(",")
            return inventory_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
