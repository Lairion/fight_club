from random import randint
from tkinter import (
    Frame, Label, Button, StringVar, OptionMenu, LEFT
)
from windows.helper import Helper
from avatar.avatar import Avatar

class GameWindow(Frame, Helper):
    
    def __init__(self, parent, controller, name) -> None:
        super().__init__(parent)
        self.name = name
        self.controller = controller
        self.parts = Avatar.body_parts
        self.options = {self.parts[i]:i for i in range(len(self.parts))}
        Label(self,text="Attack").pack()
        self.attack = StringVar()
        self.attack.set(self.parts[0])
        OptionMenu(self,self.attack, *self.parts).pack()
        Label(self,text="Defence").pack()
        self.defence = StringVar()
        self.defence.set(self.parts[0])
        OptionMenu(self,self.defence, *self.parts).pack()
        Button(self, text = 'Fight', command = self.fight).pack()
        Button(self, text = 'back', command = self.back).pack()
        self.message = Label(self, width=50, height=10)
        self.message.pack(side=LEFT)
        self.message["text"] = self.get_info()
        
    def fight(self):
        hero = self.controller.game.hero
        boss = self.controller.game.boss
        if hero is None:
            self.message["text"] = "Before, you should set hero"
            return False
        if boss is None:
            self.message["text"] = "Before, you should set boss"
            return False
        if hero.hp < 0 or boss.hp < 0:
            self.back() 
        hero.attack = self.options[self.attack.get()]
        hero.defence = self.options[self.defence.get()]
        boss.attack = randint(0, len(self.parts)-1)
        boss.defence = randint(0, len(self.parts)-1)
        hero / boss
        self.message["text"] = self.get_info()

    def get_info(self):
        hero = self.controller.game.hero
        boss = self.controller.game.boss
        list_of_info = []
        if hero:
            list_of_info+=[
                f"Hero:{hero}",
                f"Attack:{self.parts[hero.attack]} "
                f"Defence:{self.parts[hero.defence]}"
            ]
        if boss:
            list_of_info+=[
                f"Boss:{boss}",
                f"Attack:{self.parts[boss.attack]} "
                f"Defence:{self.parts[boss.defence]}"
            ]
        return "\n".join(list_of_info)
        