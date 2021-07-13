from lab import selector_lightning

from engine.tower import TowerSprite


class LightningTower(TowerSprite):

    def run_attack(self, monsters_in_range):
        self.attack_func(monsters_in_range, self, 'lightning')

    def get_selector_func(self):
        return selector_lightning

    def get_attack_cooldown(self):
        return 2

    def get_attack_radius(self):
        return 300

    def get_attack_damage(self):
        return 25
