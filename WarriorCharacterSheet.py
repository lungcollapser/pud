class Warrior:
    def __init__(self, stats, health, armor_class, weapon, weapon_damage, gold):
        self.stats = stats
        self.health = health
        self.armor_class = armor_class
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self.gold = gold


warrior_sheet = Warrior({"Strength": 20, "Dexterity": 16, "Constitution": 18, "Intelligence": 10, "Wisdom": 12, "Charisma": 14},
                       14, 13, "Axe", "1d8", 120)
