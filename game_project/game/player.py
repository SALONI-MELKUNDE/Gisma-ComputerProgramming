class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return f"{self.name} attacks!"