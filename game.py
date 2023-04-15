import json
import sys
from utils import save_data
from random import randint
from items.items import Armor, Weapon, armors_path, weapons_path
from avatar.avatar import Avatar, heroes_path, enemies_path

def print_parts(parts):
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")

class Game:
    hero = None
    boss = None
    menu_items = [
        'start',
        'create_hero',
        'create_boss',
        'create_weapon',
        'create_armor',
        'set_weapon',
        'set_armor',
        'set_hero',
        'set_boss',
        'set_boss_armor',
        'set_boss_weapon',
        'view',
        'exit'
    ]

    def __init__(self):
        with open(heroes_path) as f:
            self.heroes = [Avatar(**i) for i in json.load(f)]
        with open(armors_path) as f:
            self.armors = [Armor(**i) for i in json.load(f)]
        with open(weapons_path) as f:
            self.weapons = [Weapon(**i) for i in json.load(f)]
        with open(enemies_path) as f:
            self.enemies = [Avatar(**i) for i in json.load(f)]

    def print_main_menu(self):
        print_parts(self.menu_items)

    def exit(self):
        sys.exit("EXIT")

    def create_hero(self, name, hp, power):
        self.heroes += [Avatar(name, hp, power)]
        save_data(heroes_path, [i.get_data_for_save() for i in self.heroes])

    def create_weapon(self, name, size, durability, power):
        self.weapons += [Weapon(name, size, durability, power)]
        save_data(weapons_path, [i.get_data_for_save() for i in self.weapons])

    def create_armor(self, name, size, durability, hp):
        self.armors += [Armor(name, size, durability, hp)]
        save_data(armors_path, [i.get_data_for_save() for i in self.armors])

    def set_weapon(self,weapon):
        if self.hero is None:
            return False
        self.hero.set_weapon(weapon)
        return True

    def set_armor(self, armor):
        if self.hero is None:
            return False
        self.hero.set_armor(armor)
        return True

    def set_hero(self, hero):
        self.hero = hero

    def create_boss(self, name, hp, power):
        self.enemies += [Avatar(name, hp, power)]
        save_data(enemies_path, [i.get_data_for_save() for i in self.enemies])

    def set_boss(self, boss):
        self.boss = boss

    def set_boss_weapon(self, boss_weapon):
        if self.boss is None:
            return False
        self.boss.set_weapon(boss_weapon)
        return True

    def set_boss_armor(self, boss_armor):
        if self.boss is None:
            return False
        self.boss.set_armor(boss_armor)
        return True

    def start(self):
        while self.hero.hp > 0 and self.boss.hp > 0:
            print("Choose parts for attack")
            print_parts(self.boss.body_parts)
            self.hero.attack = int(input("part number: "))
            print("Choose parts for defence")
            print_parts(self.hero.body_parts)
            self.hero.defence = int(input("part number: "))
            attack_part = randint(0, len(self.hero.body_parts)-1)
            self.boss.attack = attack_part
            print("boss attack:", self.hero.body_parts[attack_part])
            defence_part = randint(0, len(self.boss.body_parts)-1)
            self.boss.defence = defence_part
            print("boss defence:", self.hero.body_parts[defence_part])
            self.hero / self.boss
            print("hero: ", self.hero.hp)
            print("boss: ", self.boss.hp)

    def __str__(self):
        return '\n'.join([str(self.hero) , str(self.boss) ])

    def view(self):
        print(self)
        input()
