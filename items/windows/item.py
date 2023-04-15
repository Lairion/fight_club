from tkinter import Frame, Entry, Label, StringVar
from windows.helper import Helper

class CreateItem(Frame, Helper):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent)
        self.name = name
        self.controller = controller
        Label(self, text="Name").pack()
        self.name_field = Entry(self)
        self.name_field.pack()
        Label(self, text="Size").pack()
        self.size_field = Entry(self)
        self.size_field.pack()
        Label(self, text="Durability").pack()
        self.durability_field = Entry(self)
        self.durability_field.pack()
        
    def get_data(self):
        return {
            "name":self.name_field.get(),
            "size":int(self.size_field.get()),
            "durability": int(self.durability_field.get())
        }
        
class SetItem(Frame, Helper):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent)
        self.name = name
        self.controller = controller
        self.message = Label(self)
        self.message.pack()
        self.set_str = StringVar()