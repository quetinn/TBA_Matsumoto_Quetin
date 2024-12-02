# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Listes des ecritures possibles pour les directions
        rerA = ["A", "a", "RERA", "rerA", "rera","ligneA"]
        rerB = ["B", "b", "RERB", "rerB", "rerb","ligneB"]
        rerBN = ["BN", "bn", "RERBN", "rerBN", "rerbn","B-N","b-n"]
        rerBC = ["BC", "bc", "RERBC", "rerBC", "rerbc","B-C","b-c"]
        rerBM = ["BM", "bm", "RERBM", "rerBM", "rerbm", "B-M","b-m"]
        rerC = ["C", "c", "RERC", "rerC", "rerc","ligneC"]
        rerE = ["E", "e", "RERE", "rerE", "rere","ligneE"]
        Mtreize = ["13", "treize", "Treize", "TREIZE", 'metro13', "METRO13", "métro13","M13","ligne13"]
        Mquatorze = ["14", "quatorze", "Quatorze", "QUATORZE", "metro14", "METRO14", "métro14","M14","ligne14"]
        MuneD = ["1D", "uneD", "1D", "unD", "metro1D", "METRO1D", "métro1D", "1-D","M1-D","1d"]
        MuneV = ["1V", "uneV", "1V", "unV", "metro1V", "METRO1V", "métro1V", "1-V", "M1-V","1v"]
        Surface = ["sortir", "Sortir", "SORTIR"]
        red = ["redescendre", "Redescendre", "REDESCNDRE"]
        Catacombes = ["descendre", "DESCENDRE", "Descendre"]
        rem = ["remonter", "Remonter", "REMONTER"]


        # Get the direction from the list of words.
        if list_of_words[1] in rerA:
            direction = "A"
        elif list_of_words[1] in rerB:
            direction = "B"
        elif list_of_words[1] in rerBN:
            direction = "B-N"
        elif list_of_words[1] in rerBC:
            direction = "B-C"
        elif list_of_words[1] in rerBM:
            direction = "B-M"
        elif list_of_words[1] in rerC:
            direction = "C"
        elif list_of_words[1] in rerE:
            direction = "E"
        elif list_of_words[1] in Mtreize:
            direction = "13"
        elif list_of_words[1] in Mquatorze:
            direction = "14"
        elif list_of_words[1] in MuneD:
            direction = "1-D"
        elif list_of_words[1] in MuneV:
            direction = "1-V"
        elif list_of_words[1] in Surface:
            direction = "sortir"
        elif list_of_words[1] in red:
            direction = "redescendre"
        elif list_of_words[1] in Catacombes:
            direction = "descendre"
        elif list_of_words[1] in rem:
            direction = "remonter"

        # Move the player in the direction specified by the parameter.
        try:
            player.move(direction)
        except UnboundLocalError:
            print("\n Direction inconnue. \n")
        except KeyError:
            print("\n Ligne indisponible dans cette station. \n")
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True