"""
Module actions

Ce module contient les actions exécutables dans le cadre du jeu. Chaque action correspond
à une méthode statique de la classe `Actions`, appelée lorsqu'une commande spécifique est
saisie par le joueur.

Chaque méthode d'action prend les paramètres suivants :
- 'game': L'objet représentant l'état actuel du jeu.
- 'list_of_words': La liste des mots constituant la commande saisie.
- 'number_of_parameters': Le nombre de paramètres attendu pour la commande.

Les méthodes vérifient si le nombre de paramètres est correct et effectuent une action
appropriée dans le jeu (par exemple, déplacer le joueur, prendre un objet, ou quitter le jeu).

Messages d'erreur :
- Les messages pour les erreurs de paramètres sont stockés dans les constantes 'MSG0' et 'MSG1'.

Classes :
- 'Actions': Contient toutes les méthodes statiques pour exécuter les commandes du joueur.

Constantes :
- 'MSG0': Message d'erreur pour les commandes ne prenant pas de paramètres.
- 'MSG1': Message d'erreur pour les commandes prenant exactement un paramètre.
"""

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    Classe contenant les méthodes statiques qui définissent les actions réalisables
    dans le jeu en fonction des commandes saisies par le joueur.
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
         Déplace le joueur dans la direction spécifiée par la commande.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.

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
        characters = game.characters
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Dictionnaire des ecritures possibles pour les directions
        ecriture = {
            "a":"A","rera":"A","lignea":"A",
            "b":"B", "rerb":"B","ligneb":"B",
            "bn":"B-N", "rerbn":"B-N","b-n":"B-N",
            "bc":"B-C", "rerbc":"B-C", "b-c":"B-C",
            "bm":"B-M", "rerbm":"B-M", "b-m":"B-M",
            "c":"C", "rerc":"C","lignec":"C",
            "e":"E", "rere":"E", "lignee":"E",
            "13":"13", "treize":"13", 'metro13':"13", "métro13":"13","m13":"13","ligne13":"13",
            "14":"14", "quatorze":"14", "metro14":"14", "métro14":"14","m14":"14","ligne14":"14",
            "1d":"1-D", "uned":"1-D", "und":"1-D", 
            "metro1d":"1-D", "métro1d":"1-D", "1-d":"1-D","m1-d":"1-D", 
            "1v":"1-V", "unev":"1-V", "unv":"1-V", "metro1v":"1-V", 
            "métro1v":"1-V", "1-v":"1-V", "m1-v":"1-V", 
            "descendre":"descendre","sortir":"sortir", 
            "remonter":"remonter","redescendre":"redescendre", 
            "d":"descendre","s":"sortir"
        }

        # Get the direction from the list of words.
        direction = list_of_words[1].lower()
        direction = ecriture.get(direction,"key error")

        # Move the player in the direction specified by the parameter.
        try:
            if player.move(direction,player):
                for pnj in characters:
                    if pnj.name == "Policier":
                        pnj.move()
        except KeyError:
            print("\n Direction inconnue. \n")
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des déplacements du joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(f"\n{game.player.get_history()}")
        return True
    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la pièce précédente.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            None
        """
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player.back()
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quitte le jeu.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.

        Exemples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "descendre"], 0)
        False
        >>> quit(game, ["quit", "descendre", "1-V"], 0)
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

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Affiche la liste des commandes disponibles.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "descendre"], 0)
        False
        >>> help(game, ["help", "descendre", "1-V"], 0)
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

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Vérifie l'inventaire du joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(f"\n{game.player.get_inventory()}")
        return True
    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Affiche les objets et personnages dans la pièce actuelle.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print("\n",game.player.current_room.get_inventory())
        return True
    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        name_item = list_of_words[1].capitalize()
        total_weight = 0

        for poids in player.inventory.values() :
            total_weight += poids.weight

        for item in player.current_room.inventory :
            if name_item == item.name :

                total_weight += item.weight
                if total_weight > player.max_weight :
                    print(
                        "\nLimite d'objet atteinte, il faut deposer un objet "
                        "avant d'en prendre un nouveau.\n"
                    )
                    return True

                player.inventory[item.name]=item
                player.current_room.inventory.remove(item)
                print(f"\nVous avez pris l'objet : '{item.name}'.\n")
                return True
        if name_item in player.inventory:
            print(f"\nL'objet '{name_item}' se trouve deja dans votre inventaire.\n")
        else :
            print(f"\nL'objet '{name_item}' n'est pas dans cet endroit.\n")
        return True

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un objet dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        name_item = list_of_words[1].capitalize()

        if name_item in player.inventory :
            item = player.inventory.pop(name_item)
            player.current_room.inventory.add(item)
            print(f"\nVous avez déposé l'objet : '{item.name}'.\n")
        else :
            print(f"\nVous ne possedez pas cet objet : '{name_item}'.\n")
        return True

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un personnage dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        characters = game.player.current_room.characters.values()
        player = game.player
        #character correspond aux pnj presents dans la meme room que le joueur
        nom_pnj = list_of_words[1].capitalize()
        for pnj in characters:
            if nom_pnj == pnj.name :
                print(f"\n- {pnj.name} : {pnj.get_msg(player)}\n")
            else :
                print(f"\nIl n'y a personne avec le nom : {nom_pnj} dans cet endroit.\n")
            return True

    @staticmethod
    def exchange(game, list_of_words, number_of_parameters):
        """
        Permet au joueur d'échanger un objet avec un personnage.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        nom_pnj = list_of_words[1].capitalize()
        characters = game.player.current_room.characters.values()
        player = game.player
        for pnj in characters:
            if nom_pnj == pnj.name:
                if pnj.item_gift :
                    if pnj.item_required.name in player.inventory:
                        print(
                            f"\n- {pnj.name} : {pnj.item_required.name} !"
                              " Je vous remercie. Voici un objet en échange.\n"
                        )
                        # Donner un objet au joueur
                        player.inventory[pnj.item_gift.name] = pnj.item_gift
                        # Retirer l'objet donné
                        player.inventory.pop(pnj.item_required.name)
                        print(f"Vous avez recu l'objet: '{pnj.item_gift.name}'\n")
                        pnj.item_gift = None
                    else:
                        print(f"\n- {pnj.name} : Tu n'as pas ce que je veux ... Apporte le moi.\n")
                    return True
                else :
                    print("\nJe n'ai rien a echanger.\n")
                    return True
            else :
                print("\nVous ne pouvez pas echanger.\n")
                return True
        return False
