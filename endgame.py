


class Endgame:
    def __init__(self):
        self.is_game_over = False
        self.winner = None  # "Player" ou "Enemy"

    def check_game_state(player, game_state):
    # Exemple de condition de victoire
    if "Objet Final" in player.inventory:
        game_state.is_game_over = True
        game_state.winner = "Player"
        print("Félicitations ! Vous avez gagné le jeu !")
        return

    # Exemple de condition de défaite
    if player.health <= 0:
        game_state.is_game_over = True
        game_state.winner = "Enemy"
        print("Vous avez perdu !")
        return

    # Autres conditions possibles
    if player.current_room.name == "Piège Mortel":
        game_state.is_game_over = True
        game_state.winner = "Enemy"
        print("Vous êtes tombé dans un piège et avez perdu.")
        return
