from game.player import Player
from game.enemy import Enemy
from game.items import Item


player = Player(name="Hero", health=100)
enemy = Enemy(name="Goblin", health=30)
item = Item(name="Health Potion", effect="Restore 20 HP")


print(player.attack())
print(enemy.taunt())
print(item.use())
