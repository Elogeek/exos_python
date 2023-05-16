from model.player import Player
from model.weapon import Weapon

player1 = Player("Cookies", 20, 3)
#print("Pseudo: ", player1.get_pseudo())
#player1.damage(5)
#print("Il vous reste maintenant", player1.get_health(), "points de vie!")
player2 = Player("Otaku45", 35, 5)

knife = Weapon("canif", 3)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("Bienvenue au joueur", player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque:", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque:", player2.get_attack_value())