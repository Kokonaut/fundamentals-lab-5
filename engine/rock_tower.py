import pyglet

from lab import selector_rock

from engine.tower import TowerSprite
from engine.util import get_files_in_path


class RockTower(TowerSprite):

    def get_selector_func(self):
        return selector_rock

    def run_attack(self, monsters_in_range):
        self.attack_func(monsters_in_range, self, 'rock')

    def get_attack_cooldown(self):
        return 4

    def get_attack_radius(self):
        return 200

    def get_attack_damage(self):
        return 80

    def get_tower_base(self):
        image = pyglet.image.load('assets/tower_3/tower.png')
        image.anchor_x = image.width // 2
        image.anchor_y = int(image.height * (5/8))
        sprite = pyglet.sprite.Sprite(
            image, x=self.x, y=self.y, batch=self.batch, group=self.layer_4
        )
        sprite.scale = 0.33
        return sprite

    def get_attack_sprite(self):
        attack_frames = [pyglet.resource.image('assets/tower_3/attack_effect/' + f)
                         for f in get_files_in_path('assets/tower_3/attack_effect/')]
        self.attack_ani = pyglet.image.Animation.from_image_sequence(
            attack_frames,
            duration=0.02,
            loop=False
        )
        sprite = pyglet.sprite.Sprite(
            self.attack_ani, x=self.x, y=self.y, batch=self.batch, group=self.layer_4)
        sprite.scale = 0.1
        sprite.visible = False
        return sprite

    def get_spark_sprite(self):
        image = pyglet.image.load('assets/tower_3/rock.png')
        image.anchor_x = image.width // 2
        adjusted_y = self.y + self.tower_base.height * self.tower_base.scale * 0.01
        sprite = pyglet.sprite.Sprite(
            image,
            x=self.x,
            y=adjusted_y,
            batch=self.batch,
            group=self.layer_3
        )
        sprite.scale = 0.03
        sprite.visible = False
        return sprite

    def update(self, dt, monsters):
        super().update(dt, monsters)
        # Hide the attack sprite after done animating
        ani_time = self.get_attack_cooldown() - self.attack_cooldown
        if ani_time > 0.6:
            self.attack_sprite.visible = False
