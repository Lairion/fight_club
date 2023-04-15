from tkinter import (
    Label, Button, Entry, OptionMenu
)
from items.windows.item import CreateItem, SetItem


class CreateArmor(CreateItem):

    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Label(self, text="HP").pack()
        self.hp_field = Entry(self)
        self.hp_field.pack()
        Button(self, text="Create", command=self.create_armor).pack()
        Button(self, text="Back", command=self.back).pack()
        
    def get_data(self):
        data = super().get_data()
        data.update({
            "hp":int(self.hp_field.get())
        })
        return data
        
    def create_armor(self):
        data = self.get_data()
        self.controller.game.create_armor(**data)
        self.back()
        
class SetArmor(SetItem):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        self.options = {i.name:i for i in self.controller.game.armors}
        keys = list(self.options.keys())
        self.set_str.set(keys[0])
        Label(self, text = "Set armor").pack()
        self.dropdown = OptionMenu(self, self.set_str, *keys)
        self.dropdown.pack()

class SetArmorHero(SetArmor):
    
    def __init__(self, parent, controller, name ) -> None:
        super().__init__(parent, controller, name)
        Button(self, text = 'Set', command = self.set_hero_armor).pack()
        Button(self, text = 'back', command = self.back).pack()
        
    def set_hero_armor(self):
        option_value = self.options[self.set_str.get()]
        result = self.controller.game.set_armor(option_value)
        if not result:
            self.message.config(text = "Choose hero before!")
            return None
        self.back()
    

class SetArmorBoss(SetArmor):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Button(self, text = 'Set', command = self.set_boss_armor).pack()
        Button(self, text = 'back', command = self.back).pack()
        
    def set_boss_armor(self):
        option_value = self.options[self.set_str.get()]
        result = self.controller.game.set_boss_armor(option_value)
        if not result:
            self.message.config(text = "Choose boss before!")
            return None
        self.back()