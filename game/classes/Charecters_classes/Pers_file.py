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