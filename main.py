from modules import finance_, Menu
import os, json, datetime
class Menu_:
    def __init__(self):
        main_menu = (
            "[Tasks]",
            "[Personal]",
            "[Tools]",
            "[Projects]",
            "[Finance]",
            "[Users]",
            "[Learning Tools]",
            "[Games]",
)
        main_menu_opts = {}
        i, j = 0, len(main_menu)
        while i < j:
            if i == 0:
                main_menu_opts.update({i: "[QUIT]"})
            else:
                main_menu_opts.update({i: main_menu[i]})
            i+=1

        self.main_menu_opts = main_menu_opts

    def format_menu_(self, menu_:list) -> dict:
        '''
            Take a menu_ list containing >= 9 menu header strings so 
                it can be mapped to a dictionary in the order it was received...
                    and where 'q' is always considered 'quit'.

        '''
        menu_opts_ = {}
        i, j = 0, len(menu_)
        while i < j:
            if i == 0:
                menu_opts_.update({"q": "[QUIT]"})
            else:
                menu_opts_.update({i: menu_[i]})
            i+=1
        return menu_opts_

    def print_menu_(self):
        for key, value in self.main_menu_opts.items():
            print(f"{key}: {value} ")

    def main_menu_(self):
        select = int(input("Where to? \n: "))
        match select:
            case 1:
                print(self.main_menu_opts[1])
            case 2:
                print(self.main_menu_opts[2])
            case 3:
                print(self.main_menu_opts[3])
            case 4:
                print(self.main_menu_opts[4])
            case 5:
                print(self.main_menu_opts[5])
            case 6:
                print(self.main_menu_opts[6])
            case 7:
                print(self.main_menu_opts[7])
            case 8:
                print(self.main_menu_opts[8])        
            case 9:
                print(self.main_menu_opts[9])
            case q:
                print(self.main_menu_opts[0])
                exit()

menu = Menu_







