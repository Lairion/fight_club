from tkinter import Button, Label,OptionMenu
from avatar.windows.avatar import CreateAvatar, SetAvatar

class CreateHero(CreateAvatar):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Button(self, text="Create", command=self.create_hero).pack()
        Button(self, text="Back", command=self.back).pack()

    def create_hero(self):
        data = self.get_data()
        self.controller.game.create_hero(**data)
        self.back()
        
class SetHero(SetAvatar):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        self.options = {i.name:i for i in self.controller.game.heroes}
        keys = list(self.options.keys())
        self.set_str.set(keys[0])
        Label(self, text = "Set Hero").pack()
        self.dropdown = OptionMenu(self, self.set_str, *keys)
        self.dropdown.pack()
        Button(self, text = 'Set', command = self.set_hero).pack()
        Button(self, text = 'back', command = self.back).pack()
        
        
    def set_hero(self):
        option_value = self.options[self.set_str.get()]
        result = self.controller.game.set_hero(option_value)
        self.back()