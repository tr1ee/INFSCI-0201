class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def equip(self, weapon):
        self.weapon = weapon

class Hero(Character):
    pass

class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.equip(weapon)

class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

# Setting up weapons
empty_handed = Weapon(name="Empty Handed", weapon_type="dummy", damage=0, value=0)
healing_staff = Weapon(name="Healing Staff", weapon_type="magic", damage=-3, value=0)

# Setting up characters
protagonist = Hero(name="Hero", health=100)
protagonist.equip(empty_handed)

ally = Enemy(name="Friendly Enemy", health=100, weapon=healing_staff)
