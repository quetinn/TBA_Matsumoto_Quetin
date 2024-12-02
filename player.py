# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
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
        self.current_room = next_room
        ##self.previous_room = self.current_room
        self.history.append(self.current_room.name)
        print(self.current_room.get_long_description() ,"\n", self.get_history())
        return True

    def get_history(self, game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        history_string = "Vous avez déja visité les endroits suivants :\n"
        for nom in self.history :
            history_string += "\t- " + nom + "\n"
        history_string = history_string.strip(",")
        return history_string

    