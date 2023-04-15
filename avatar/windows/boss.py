from tkinter import Button, Label, OptionMenu
from avatar.windows.avatar import CreateAvatar, SetAvatar


class CreateBoss(CreateAvatar):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        Button(self, text="Create", command=self.create_boss).pack()
        Button(self, text="Back", command=self.back).pack()

    def create_boss(self):
        data = self.get_data()
        self.controller.game.create_boss(**data)
        self.back()
        
class SetBoss(SetAvatar):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent, controller, name)
        self.options = {i.name:i for i in self.controller.game.enemies}
        keys = list(self.options.keys())
        self.set_str.set(keys[0])
        Label(self, text = "Set Boss").pack()
        self.dropdown = OptionMenu(self, self.set_str, *keys)
        self.dropdown.pack()
        Button(self, text = 'Set', command = self.set_boss).pack()
        Button(self, text = 'back', command = self.back).pack()
        
        
    def set_boss(self):
        option_value = self.options[self.set_str.get()]
        result = self.controller.game.set_boss(option_value)
        self.back()