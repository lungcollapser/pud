class Wizard:
    def __init__(self, stats, health, armor_class, weapon, weapon_damage):
        self.stats = stats
        self.health = health
        self.armor_class = armor_class
        self.weapon = weapon
        self.weapon_damage = weapon_damage


wizard_sheet = Wizard({"Strength": 10, "Dexterity": 14, "Constitution": 12, "Intelligence": 20, "Wisdom": 16, "Charisma": 18}, 12, 7, "Quarterstaff", "1d6")
