import json

from settings import BASE_DIR
from utils import save_data
heroes_path = BASE_DIR.joinpath("avatar/save_folder/heroes.json")
enemies_path = BASE_DIR.joinpath("avatar/save_folder/enemies.json")


class Avatar:

    body_parts = ["head", "torso", "leg", "hand"]
    attack = 0
    defence = 0
    weapon = None
    armor = None

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def __str__(self):
        return "Name:{0}, Hp:{1}, Power:{2}".format(
            self.name,
            self.hp,
            self.power
        )

    def set_armor(self, armor):
        # перевіряємо наявність  броні на персонажі
        if self.armor:
            # якщо броня є, то віднімаємо від здоров'я персонажу значення здоров'я броні
            self.hp -= self.armor.hp
        # тепер вдягаємо нову броню   
        self.armor = armor
        # додаємо здоров'я броні до здоров'я персонажа
        self.hp += self.armor.hp

    def set_weapon(self, weapon):
        if self.weapon:
            self.power -= self.weapon.power
        self.weapon = weapon
        self.power += self.weapon.power


    def __truediv__(self, other):
        # Як проходить операція ділення цього об'єкту на інший цього ж класу
        if self.attack != other.defence:
            other.hp = other.hp - self.power
        if self.defence != other.attack:
            self.hp = self.hp - other.power
        return self


    def get_data_for_save(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power
            }