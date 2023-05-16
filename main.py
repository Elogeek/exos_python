from model.player import Player
from model.weapon import Weapon

# Weapons
knife = Weapon("couteau suisse", 3)
katana = Weapon("Katana", 10)

# Players
player1 = Player("Cookies", 50, 3)
player2 = Player("Otaku45", 6, 10)

# Equipped players
player2.set_weapon(katana)
player1.set_weapon(knife)

# Attack player2
print(player2.get_pseudo(), "attaque", player1.get_pseudo())
player2.attack_player(player1)
print(player1.get_pseudo(),"il vous reste maintenant", player1.get_health(),"PV")

# Attack player1
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
player1.attack_player(player2)
print(player2.get_pseudo(), "est maintenant à", player2.get_health(), "PV")

#print("Bienvenue au joueur", player1.get_pseudo(), "PV:", player1.get_health(), "/ Attaque:", player1.get_attack_value(), "/ Equipement:", player1.weapon.get_name())
#print("Bienvenue au joueur", player2.get_pseudo(), "PV:", player2.get_health(), "/ Attaque:", player2.get_attack_value(), "/ Equipement:", player2.weapon.get_name())

# Victory
if player2.get_health() > 0:
    print("{} aie ... Il ne vous reste plus que {} points de vie"
          .format(player2.get_pseudo(), player2.get_health()))
else:
    print("{} est mort ... {} a gagné".format(
        player2.get_pseudo(), player1.get_pseudo()))