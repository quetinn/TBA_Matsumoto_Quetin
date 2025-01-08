"""
Module command.

Ce module contient la définition de la classe Command, utilisée pour représenter une commande 
dans le jeu. Une commande est composée d'un mot-clé, d'une description, d'une action à exécuter et 
du nombre de paramètres attendus.

Classes :
    - Command : Représente une commande et ses attributs associés.
"""

class Command:
    """
    Cette classe représente une commande. Une commande est composée d'un mot-clé, 
    d'une chaîne d'aide, d'une action à exécuter et d'un nombre de paramètres.

    Attributs :
        command_word (str) : Le mot-clé de la commande.
        help_string (str) : La description de la commande (texte d'aide).
        action (function) : La fonction associée à la commande qui sera exécutée.
        number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

    Méthodes :
        __init__(self, command_word, help_string, action, number_of_parameters) :
            Initialise une commande avec ses attributs.
        __str__(self) : Retourne une représentation sous forme de chaîne de la commande.

    Exemples :
        >>> from actions import go
        >>> command = Command("aller", "Permet de se déplacer dans une direction.", go, 1)
        >>> command.command_word
        'aller'
        >>> command.help_string
        'Permet de se déplacer dans une direction.'
        >>> type(command.action)
        <class 'function'>
        >>> command.number_of_parameters
        1
    """
    # Désactivation de la règle "trop peu de méthodes publiques"
    # pylint: disable=too-few-public-methods

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        """
        Initialise une commande.

        Args :
            command_word (str) : Le mot-clé de la commande.
            help_string (str) : La description de la commande.
            action (function) : La fonction associée à la commande.
            number_of_parameters (int) : Le nombre de paramètres requis.
        """
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    # The string representation of the command.
    def __str__(self):
        """
        Retourne une représentation textuelle de la commande, 
        incluant le mot-clé et sa description.

        Returns :
            str : Une chaîne de caractères décrivant la commande.
        """
        return  self.command_word \
                + self.help_string
