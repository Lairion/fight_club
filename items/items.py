import json

from settings import BASE_DIR
from utils import save_data
armors_path = BASE_DIR.joinpath("items/save_folder/armors.json")
weapons_path = BASE_DIR.joinpath("items/save_folder/weapons.json")


class Item:

    def __init__(self, name, size, durability):
        self.name = name
        # розмір
        self.size = size
        # міцність
        self.durability = durability

    def __str__(self):
        return "Name:{0}, Size:{1}, Durability:{2}".format(
            self.name,
            self.size,
            self.durability
        )

    def get_data_for_save(self):
        return {
            "name": self.name,
            "size": self.size,
            "durability": self.durability
        }


class Armor(Item):

    def __init__(self, name, size, durability, hp):
        super().__init__(name, size, durability)
        self.hp = hp

    def get_data_for_save(self):
        result = super().get_data_for_save()
        result.update({
            "hp": self.hp
        })
        return result


class Weapon(Item):

    def __init__(self, name, size, durability, power):
        super().__init__(name, size, durability)
        self.power = power

    def get_data_for_save(self):
        result = super().get_data_for_save()
        result.update({
            "power": self.power
        })
        return result


with open(armors_path) as f:
    armors_list = [Armor(**i) for i in json.load(f)]
with open(weapons_path) as f:
    weapons_list = [Weapon(**i) for i in json.load(f)]


def create_armor():
    global armors_list
    name = input("Name:")
    size = int(input("Size:"))
    durability = int(input("Durability:"))
    hp = int(input("HP:"))
    armors_list += [Armor(name, size, durability, hp)]
    save_data(armors_path, [i.get_data_for_save() for i in armors_list])


def print_parts(parts):

    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def create_weapon():
    global weapons_list
    name = input("Name:")
    size = int(input("Size:"))
    durability = int(input("Durability:"))
    power = int(input("Power:"))
    weapons_list += [Weapon(name, size, durability, power)]
    save_data(weapons_path, [i.get_data_for_save() for i in weapons_list])




def set_weapon():
    global weapons_list
    print_parts(weapons_list)
    weapon = weapons_list[int(input("Choose: "))]
    print(weapon)


def set_armor():
    global armors_list
    print_parts(armors_list)
    armor = armors_list[int(input("Choose: "))]
    print(armor)


def set_avatar():
    global avatars_list
    print_parts(avatars_list)
    avatar = avatars_list[int(input("Choose: "))]
    print(avatar)
