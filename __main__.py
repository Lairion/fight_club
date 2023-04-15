import sys
from game import Game
from windows.main_window import MainWindow


def main(game):
    game.print_main_menu()
    option = int(input("Choose option: "))
    getattr(game, game.menu_items[option])()
def main2(game):
    return MainWindow(game=game)

if __name__ == '__main__':
    app=main2(game=Game())
    app.mainloop()
