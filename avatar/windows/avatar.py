from tkinter import Frame, Entry, Label, StringVar
from windows.helper import Helper

class CreateAvatar(Frame, Helper):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent)
        self.name = name
        self.controller = controller
        Label(self, text="Name").pack()
        self.name_field = Entry(self)
        self.name_field.pack()
        Label(self, text="HP").pack()
        self.hp_field = Entry(self)
        self.hp_field.pack()
        Label(self, text="Power").pack()
        self.power_field = Entry(self)
        self.power_field.pack()
        
    def get_data(self):
        return {
            "name": self.name_field.get(),
            "hp": int(self.hp_field.get()),
            "power":int(self.power_field.get())
        }
        
class SetAvatar(Frame, Helper):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent)
        self.name = name
        self.controller = controller
        self.set_str = StringVar()
        