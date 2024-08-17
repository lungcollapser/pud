class Wizard:
    def __init__(self, stats, health, armor_class, weapon, weapon_damage, gold):
        self.stats = stats({"Strength": 10, "Dexterity": 14, "Constitution": 12, "Intelligence": 20, "Wisdom": 16, "Charisma": 18})
        self.health = health(12)
        self.armor_class = armor_class(12)
        self.weapon = weapon("Quarterstaff")
        self.weapon_damage = weapon_damage("1d6")
        self.gold = gold(100)


wizard_sheet = Wizard({"Strength": 10, "Dexterity": 14, "Constitution": 12, "Intelligence": 20, "Wisdom": 16, "Charisma": 18},
                       12, 12, "Quarterstaff", "1d6", 100)


