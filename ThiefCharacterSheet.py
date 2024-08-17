class Thief:
    def __init__(self, stats, health, armor_class, weapon, weapon_damage, gold):
        self.stats = stats
        self.health = health
        self.armor_class = armor_class
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self.gold = gold


thief_sheet = Thief({"Strength": 10, "Dexterity": 20, "Constitution": 14, "Intelligence": 12, "Wisdom": 16, "Charisma": 18},
                     12, 12, "Dagger", "1d4", 100)
