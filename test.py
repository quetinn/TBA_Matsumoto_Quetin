#test

from item import Item
from game import Game
from player import Player
sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
l="SDLFDSEKG"
print(l.capitalize())
from character import Character
chomeur = Character("Chomeur", "un chomeur affamé", ["J'ai tres faim... Si tu m'apportes a manger, je t'echange ce que tu rapportes","Merci."])
print(Character.get_msg(chomeur))
print(Character.get_msg(chomeur))
print(Character.get_msg(chomeur))
print(chomeur.current_room)
