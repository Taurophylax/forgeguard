class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.wisdom = 1
        self.charisma = 10
        self.inventory = []
        self.position = (0, 0)  # Starting at (0, 0) on the map
    
    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")
        print(f"Inventory: {self.inventory}")
