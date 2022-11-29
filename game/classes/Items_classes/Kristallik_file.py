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