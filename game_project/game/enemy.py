class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def taunt(self):
        return f"{self.name} taunts the player!"
    