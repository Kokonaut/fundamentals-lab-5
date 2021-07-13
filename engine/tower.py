import pyglet

from engine.util import get_files_in_path


class TowerSprite:

    ARROW_SPEED = 1

    def __init__(self, x, y, batch, layer=4):
        self.layer_1 = pyglet.graphics.OrderedGroup(layer)
        self.layer_2 = pyglet.graphics.OrderedGroup(layer+1)
        self.layer_3 = pyglet.graphics.OrderedGroup(layer+2)
        self.layer_4 = pyglet.graphics.OrderedGroup(layer+3)
        self.layer_5 = pyglet.graphics.OrderedGroup(layer+4)

        self.x = x
        self.y = y
        self.batch = batch
        self.tower_base = self.get_tower_base()
        self.attack_ani = None
        self.attack_sprite = self.get_attack_sprite()
        self.spark_sprite = self.get_spark_sprite()

        self.attack_dest = None
        self.attack_cooldown = self.get_attack_cooldown()
        self.target = None

        self.selector_func = None

        self.active = True
        # self.character_1 = self.get_char_1()
        # self.character_2 = self.get_char_2()

    def activate(self):
        self.tower_base.visible = True
        self.active = True

    def deactivate(self):
        self.tower_base.visible = False
        self.active = False

    def draw(self):
        self.tower_base.draw()
        self.attack_sprite.draw()
        self.spark_sprite.draw()

    def get_attack_cooldown(self):
        return 2

    def get_attack_radius(self):
        return 500

    def get_attack_damage(self):
        return 10

    def get_tower_base(self):
        image = pyglet.image.load('assets/tower_2/tower.png')
        image.anchor_x = image.width // 2
        image.anchor_y = int(image.height * (5/8))
        sprite = pyglet.sprite.Sprite(
            image, x=self.x, y=self.y, batch=self.batch, group=self.layer_4
        )
        sprite.scale = 0.33
        return sprite

    def get_attack_sprite(self):
        attack_frames = [pyglet.resource.image('assets/tower_2/attack_effect/' + f)
                         for f in get_files_in_path('assets/tower_2/attack_effect/')]
        self.attack_ani = pyglet.image.Animation.from_image_sequence(
            attack_frames,
            duration=0.05,
            loop=False
        )
        sprite = pyglet.sprite.Sprite(
            self.attack_ani, x=self.x, y=self.y, batch=self.batch, group=self.layer_4)
        sprite.scale = 0.15
        sprite.visible = False
        return sprite

    def get_spark_sprite(self):
        image = pyglet.image.load('assets/tower_2/20.png')
        image.anchor_x = image.width // 2
        adjusted_y = self.y + self.tower_base.height * self.tower_base.scale * 0.9
        sprite = pyglet.sprite.Sprite(
            image,
            x=self.x,
            y=adjusted_y,
            batch=self.batch,
            group=self.layer_3
        )
        sprite.scale = 0.25
        sprite.visible = False
        return sprite

    def get_monsters_in_range(self, monsters):
        in_range = list()
        for monster in monsters:
            if self.is_monster_in_range(monster):
                in_range.append(monster)
        return in_range

    def is_monster_in_range(self, monster):
        distance = self.get_distance_from_tower(monster.x, monster.y)
        return distance < self.get_attack_radius()

    def get_distance_from_tower(self, x, y):
        diff_x = abs(self.x - x)
        diff_y = abs(self.y - y)
        return (diff_x ** 2 + diff_y ** 2) ** 0.5

    def get_selector_func(self):
        return self.selector_func

    def set_selector_func(self, func):
        self.selector_func = func

    def select_target(self, monsters):
        return self.get_selector_func()(monsters)

    def update(self, dt, monsters):
        if not self.active:
            return
        monsters_in_range = self.get_monsters_in_range(monsters)
        # What animation time step is the attack currently in
        ani_time = self.get_attack_cooldown() - self.attack_cooldown
        if (ani_time < 0.1) or (ani_time > 0.4 and ani_time < 0.5):
            # Only show the spark if the main attack is occurring
            if self.attack_sprite.visible:
                self.spark_sprite.x -= 0.5
                self.spark_sprite.visible = True
        elif ani_time > 0.2 and ani_time < 0.3:
            if self.attack_sprite.visible:
                self.spark_sprite.x += 1
                self.spark_sprite.visible = True
        else:
            self.spark_sprite.visible = False
        if self.attack_cooldown > 0 and self.attack_cooldown < 0.5:
            self.attack_sprite.visible = False
        if self.attack_cooldown <= 0:
            self.target = self.select_target(monsters_in_range)
            if self.target:
                self.attack_sprite.x = self.target.x - \
                    self.attack_sprite.scale * self.attack_ani.get_max_width() / 2
                self.attack_sprite.y = self.target.y - \
                    self.attack_sprite.scale * self.attack_ani.get_max_height() / 2
                # self._attack(self.target)
                self.run_attack(monsters_in_range)
        else:
            self.attack_cooldown -= dt
        if self.target:
            self.attack_sprite.x = self.target.x - \
                self.attack_sprite.scale * self.attack_ani.get_max_width() / 2
            self.attack_sprite.y = self.target.y - \
                self.attack_sprite.scale * self.attack_ani.get_max_height() / 8

    def _attack(self, target):
        if not self.attack_sprite.visible:
            self.attack_sprite.image = self.attack_ani
            self.attack_sprite.visible = True
            target.damage(self.get_attack_damage())
            self.attack_cooldown = self.get_attack_cooldown()

    def set_attack_func(self, func):
        self.attack_func = func

    def run_attack(self, monsters_in_range):
        raise NotImplementedError

    def attack(self, target, damage):
        if not self.attack_sprite.visible:
            self.target = target
            self.attack_sprite.image = self.attack_ani
            self.attack_sprite.visible = True
            target.damage(damage)
            self.attack_cooldown = self.get_attack_cooldown()
