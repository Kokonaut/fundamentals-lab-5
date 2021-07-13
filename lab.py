def get_distance_to_goal(monster):
    diff_x = abs(monster.x - monster.dest_x)
    diff_y = abs(monster.y - monster.dest_y)
    return (diff_x ** 2 + diff_y ** 2) ** 0.5


def get_remaining_monster_health(monster):
    return monster.current_health


def run_tower_attack_monster(tower, monster, damage):
    tower.attack(monster, damage)

# ------------------ Lab ---------------------


def selector_lightning(monsters):
    return None


def selector_rock(monsters):
    return None


def tower_attack(monsters, tower, tower_type):
    pass
