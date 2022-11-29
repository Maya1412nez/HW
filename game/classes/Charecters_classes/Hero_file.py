from Pers_file import Pers
from Items_classes.Item_file import Item


class Hero(Pers):
    def __init__(self):
        super().__init__()
        self.killed = 0
        self.bag_of_coins = 100
        self.skills_quality = 1  # Quality of different skills. Dep on level
        self.coins = 0
        self.bag = {} # Inventory. Structure: {name}: class_object


    def up_level(self, reason, params):
        self.level += 1
        if reason == 'SKILL':
            # params = [type of skill (attack, protect, hill)]
            if params[0] == 'attack':
                self.damage_points += 3
            elif params[0] == 'protect':
                self.armor_points += 1
            elif params[0] == 'hill':
                self.hill_points += 0.5
        elif reason == 'DAMAGE':
            pass
        self.coins = 0  # coins are spent for upping level,
        self.bag_of_coins += 20  # so bag is growing up

    def hill_myself(self):
        self.health_points += self.hill_points
        # TO DO start cooldown

    def take_treasure(self, args):  # get coins from treasure
        coin, kind = args
        if kind == 'usual':
            pass
        self.coins += coin

    def get_states(self, kind='changing'):
        if kind == 'changing':
            return f'health#{self.health_points}', f'damage#{self.damage_points}', f'protect#{self.armor_points}', \
                   f'hill#{self.hill_points}', f'cooldown#{self.cool_down}'
        elif kind == 'constant':
            return self.level, self.skills_quality
        elif kind == 'all':
            return self.level, self.skills_quality, self.health_points, self.damage_points, self.armor_points, \
                   self.hill_points, self.cool_down

    def attack(self, name, states):
        # enemy_health = states[0].split('#')[1]
        # enemy_damage = states[1].split('#')[1]
        # while self.health_points > 0 and enemy_health > 0:
        #     enemy_health -= self.damage_points
        #     self.health_points -= enemy_damage
        #     time.sleep(self.cool_down)
        ...

    def eat(self, item_object):
        if item_object in self.bag:
            points = item_object.get_params[0]
            self.health_points += points
            

