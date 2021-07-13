from engine.monster import MonsterSprite


FAST_SPEED = 90
FAST_HEALTH = 35

HEAVY_SPEED = 35
HEAVY_HEALTH = 140


class Spawner:

    def __init__(self, config, position_name, path, grid, batch, group=None):
        self.config = config
        self.monster_queue = list()
        self.spawned = list()
        self.interval = self.config[0]['cooldown']
        self.xy = grid.calculate_xy_from_percentage(position_name)
        # self.xy = (self.xy[0] - grid.cell_length, self.xy[1],)
        self.path = path
        self.batch = batch
        self.group = group

        self.monster_index = 0

        self.load_in_monsters()

    def load_in_monsters(self):
        for i in range(len(self.config)):
            spawn = self.config[i]
            monster_id = "monster_" + str(i)
            if spawn['type'] == 'fast':
                self.monster_queue.append(self.load_fast_monster(monster_id))
            elif spawn['type'] == 'heavy':
                self.monster_queue.append(self.load_heavy_monster(monster_id))
            else:
                raise ValueError(
                    'Unsupported Monster Type: ' + spawn['type'])

    def update(self, dt):
        self.run_spawn(dt)
        for sprite in self.spawned:
            sprite.update(dt)

    def run_spawn(self, dt):
        if len(self.monster_queue) == 0:
            return
        if self.interval <= 0:
            sprite = self.monster_queue.pop(0)
            self.spawned.append(sprite)
            print("Spawning monster: {id}".format(id=sprite.id))
            sprite.show()
            self.monster_index += 1
            self.interval = self.get_interval_to_next_spawn()
        else:
            self.interval -= dt

    def get_interval_to_next_spawn(self):
        if len(self.monster_queue) == 0:
            return 999
        next_spawn = self.config[self.monster_index]
        return next_spawn['cooldown']

    def load_fast_monster(self, monster_id):
        sprite = MonsterSprite(
            monster_id,
            'assets/enemy_2/',
            self.xy[0],
            self.xy[1],
            self.path[:],
            FAST_SPEED,
            FAST_HEALTH,
            batch=self.batch,
            group=self.group,
        )
        sprite.hide()
        return sprite

    def load_heavy_monster(self, monster_id):
        sprite = MonsterSprite(
            monster_id,
            'assets/enemy_1/',
            self.xy[0],
            self.xy[1],
            self.path[:],
            HEAVY_SPEED,
            HEAVY_HEALTH,
            batch=self.batch,
            group=self.group,
        )
        sprite.hide()
        return sprite
