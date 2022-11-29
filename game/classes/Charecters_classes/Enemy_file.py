from Pers_file import Pers

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