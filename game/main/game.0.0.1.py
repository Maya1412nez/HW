from Pers_file import Pers
from Hero_file import Hero
from Kristallik_file import Kristallik
from Enemy_file import Enemy

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
