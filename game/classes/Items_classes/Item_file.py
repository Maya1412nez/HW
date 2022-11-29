class Item:
    def __init__(self, hill_points=0, damage_points=0) -> None:
        self.hillpoints = hill_points
        self.damage_points = damage_points
        self.skills = []

    def get_params(self):
        return [self.hillpoints, self.damage_points, self.skills]
