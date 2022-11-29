
from classes.Charecters_classes.Hero_file import Hero
from classes.Items_classes.Item_file import Item
from classes.Items_classes.Kristallik_file import Kristallik
from classes.Charecters_classes.Enemy_file import Enemy

racky = Hero()
racky.take_damage(10)
print(racky.get_states())

kris = Kristallik()
coins = kris.get_coins()
print(coins)
racky.take_treasure(coins)

monsty = Enemy('IWantSleep')
argg = monsty.get_states()
racky.attack('IWantSleep', argg)

apple = Item()
print(racky.take_item(apple))
print(racky.review_item(apple))
print(racky.review_items())
