class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self):
        return f"Using {self.name} which has the effect: {self.effect}!"
