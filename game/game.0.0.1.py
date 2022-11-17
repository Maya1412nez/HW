import time


class Pers:
    def __init__(self):
        # passive (not using in fighting)
        self.level = 1  # level

        # active (using in fighting)
        self.health_points = 20  # HP. Depends on level, skills
        self.armor_points = 0  # Armor points. Depends on skills, level
        self.damage_points = 5  # Depends on skills, level
        self.hill_points = 2  # Depends on skills, level
        self.cool_down = 0.25  # Depends on skills

    def take_damage(self, damage, skill=None):
        if skill == 'fire':
            damage *= 1.2
        self.health_points -= damage


class Hero(Pers):
    def __init__(self):
        super().__init__()
        self.killed = 0
        self.bag_of_coins = 100
        self.skills_quality = 1  # Quality of different skills. Dep on level
        self.coins = 0

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


class Enemy(Pers):
    def __init__(self, name):
        super().__init__()
        self.coins = 15
        self.name = name

    def get_states(self):
        return f'health#{self.health_points}', f'damage#{self.damage_points}', f'protect#{self.armor_points}', \
               f'hill#{self.hill_points}', f'cooldown#{self.cool_down}'

    def take_damage(self, damage, skill=None):
        ...


class Kristallik:
    def __init__(self, kind='usual'):
        self.coins = 10
        self.level = 1
        self.kind = kind

    def disappear(self):
        self.coins = 0
        self.kind = None

    def get_coins(self):
        return self.coins, self.kind


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
