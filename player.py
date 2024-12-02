# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.previous_room = None
        self.history = []
        ##self.previous_room = None
    
    # Define the move method.
    def move(self, direction):
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

        # Set the current room to the next room.
        self.history.append(self.current_room.name)
        self.previous_room = self.current_room
        self.current_room = next_room
        print(self.current_room.get_long_description(),"\n",self.get_history())
        return True

    def get_history(self):
        history_string = "Vous avez déja visité les endroits suivants :\n"
        for nom in self.history :
            history_string += "\t- " + nom + "\n"
        history_string = history_string.strip(",")
        return history_string
    
    def back(self):
        if len(self.history) <= 1 :
            return False
        else :
            print(self.history.pop())
            self.current_room = self.previous_room
            return True

    