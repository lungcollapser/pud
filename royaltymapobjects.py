class Door:
    def __init__(self, description, health):
        self.description = description
        self.health = health


door = Door("A sleek door with no visible handle. A glossy button catches your eye to the right.", 100)


class StorageContainer:
    def __init__(self, description, health, items_inside):
        self.description = description
        self.health = health
        self.items_inside = items_inside


storage_container = StorageContainer("A ornately built circle hovers above the ground. A screen at what you assume to be the top shows a list of items.", 100,
                                     "Weapon of choice, Jingo juice, 3x metal plates")


class Bed:
    def __init__(self, description, health):
        self.description = description
        self.health = health


bed = Bed("The table glistens with a sweaty imprint that you left. The metal clamps that were once around your arms and legs are now open, and you sudden pressure in your joints.", 100)

