class Player:

    # Constructor
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, "/ Points de vie:", health, "/ Attaque:", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Nooonnn", self.pseudo, "vous venez de subir", damage, "de dégâts!")

    # Attack another player
    def attack_player(self, target_player):
        damage = self.attack

        # si le joueur a une arme
        if self.has_weapon():
            # ajoute les dégats de l'arme au point d'attaque du joueur
            damage += self.weapon.get_damage_amount()

        target_player.damage(damage)

    # méthode pour changer l'arme du joueur
    def set_weapon(self, weapon):
        self.weapon = weapon

        if weapon == "None":
            print(self.pseudo, "n'a plus d'arme équipée !")
        else:
            print(self.pseudo, "est maintenant équipé d'un :", weapon.get_name())

    # méthode pour verifier si le joueur a une arme
    def has_weapon(self):
        return self.weapon is not None


class Shinobi(Player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenue au ninja", pseudo, "/ Points de vie:", health, "/ Attaque:", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
            super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargées")

    def get_armor_point(self):
        return self.armor


ninja = Shinobi("Naruto", 30, 8)
ninja.damage(4)
print("PV:", ninja.get_health(), "armure:", ninja.get_armor_point())

# test que l'héritage se passe bien
if issubclass(Shinobi, Player):
    print("Le ninja est bien une spécialisation de Player")