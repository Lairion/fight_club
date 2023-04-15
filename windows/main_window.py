from tkinter import Tk,Frame,Button
from avatar.windows.hero import CreateHero, SetHero
from avatar.windows.boss import CreateBoss, SetBoss
from items.windows.armor import CreateArmor, SetArmorHero, SetArmorBoss
from items.windows.weapon import CreateWeapon, SetWeaponHero, SetWeaponBoss



class Main(Frame):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent)
        self.name = name
        self.controller = controller
        self.title = "Main"
        buttons = []
        for name, class_window in list(self.controller.frames.items()):
            print(name)
            buttons.append(Button(self, text=name.replace("_", " ").capitalize(), command=class_window.show_frame))
            buttons[-1].pack()

class MainWindow(Tk):
    
    windows = {
        "create_hero": CreateHero,
        "set_hero": SetHero,
        "set_hero_armor": SetArmorHero,
        "set_hero_weapon": SetWeaponHero,
        "create_boss": CreateBoss,
        "set_boss": SetBoss,
        "set_boss_armor": SetArmorBoss,
        "set_boss_weapon": SetWeaponBoss,
        "create_armor": CreateArmor,
        "create_weapon": CreateWeapon,
        "main":Main
    }
    
    def __init__(self, game=None, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        self.container = Frame(self)
        self.title("Fight club")
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.game = game
        self.frames = {}
        for menu_name, menu_class in self.windows.items():
            menu = menu_class(self.container, self, menu_name)
            self.frames.update({menu_name: menu})
            menu.grid(row=0, column=0, sticky="nsew")
        self.show_frame("main")
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()