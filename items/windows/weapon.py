from tkinter import Label, Button, Entry, OptionMenu
from items.windows.item import CreateItem, SetItem

class CreateWeapon(CreateItem):

    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Label(self, text="Power").pack()
        self.power_field = Entry(self)
        self.power_field.pack()
        Button(self, text="Create", command=self.create_weapon).pack()
        Button(self, text="Back", command=self.back).pack()
        
    def get_data(self):
        data = super().get_data()
        data.update({
            "power":int(self.power_field.get())
        })
        return data
        
    def create_weapon(self):
        data = self.get_data()
        self.controller.game.create_weapon(**data)
        self.back()
        
class SetWeapon(SetItem):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        self.options = {i.name:i for i in self.controller.game.weapons}
        keys = list(self.options.keys()) 
        self.set_str.set(keys[0])
        Label(self, text = "Set weapon").pack()
        self.dropdown = OptionMenu(self, self.set_str, *keys)
        self.dropdown.pack()

class SetWeaponHero(SetWeapon):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Button(self, text = 'Set', command = self.set_hero_weapon).pack()
        Button(self, text = 'back', command = self.back).pack()
        
    def set_hero_weapon(self):
        option_value = self.options[self.set_str.get()]
        result = self.controller.game.set_weapon(option_value)
        if not result:
            self.message.config(text = "Choose hero before!")
            return None
        self.back()
    

class SetWeaponBoss(SetWeapon):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Button(self, text = 'Set', command = self.set_boss_weapon).pack()
        Button(self, text = 'back', command = self.back).pack()
        
    def set_boss_weapon(self):
        option_value = self.options[self.set_str.get()]
        result = self.controller.game.set_boss_weapon(option_value)
        if not result:
            self.message.config(text = "Choose boss before!")
            return None
        self.back()