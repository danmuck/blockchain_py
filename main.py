from modules import finance_
import os, json, datetime


class Menu_:
    def __init__(self, main_menu, finance_menu):
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
        finance_menu = (
            "[Calculate Monthly Interest Gains]"
        )

        self.main_menu_opts = self.format_menu_(main_menu)
        self.finance_menu_opts = self.format_menu_(finance_menu)

    def format_menu_(self, menu_:list) -> dict:
        '''
            Take a menu_ list containing >= 9 menu header strings so 
                it can be mapped to a dictionary in the order it was received...
                    and where 'q' is always considered 'quit'.

        '''
        menu_opts_ = {}
        i, j = 0, len(menu_)
        while i < j:
            menu_opts_.update({i: menu_[i]})
            i+=1
        menu_opts_.update({"q": "[QUIT]"})
        return menu_opts_


    def main_menu_(self):
        '''
            Obnoxious menu copy/paste template to cover 10 cases with KeyError handling 
                for ease in development.
                    Remove excess cases for production.
        '''
        menu_dict = self.main_menu_opts
        print_dict(menu_dict)
        select = input("Where to? \n: ")

        match select:
            case "0":
                try:
                    print(menu_dict[0])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()
            case "1":
                try:
                    print(menu_dict[1])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()
            case "2":
                try:
                    print(menu_dict[2])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()
            case "3":
                try:
                    print(menu_dict[3])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "4":
                try:
                    print(menu_dict[4])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "5":
                try:
                    print(menu_dict[5])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "6":
                try:
                    print(menu_dict[6])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "7":
                try:
                    print(menu_dict[7])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "8":
                try:
                    print(menu_dict[8])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "9":
                try:
                    print(menu_dict[9])
                except KeyError:
                    pass
                finally:
                    self.main_menu_()                        
            case "q":
                print(menu_dict["q"])
                exit()
            case _:
                print("\n[oops...]\n")
                self.main_menu_()

    def finance_menu_(self):
        menu_dict = self.finance_menu_opts
        print_dict(menu_dict)
        select = int(input("Where to? \n: "))
        match select:
            case "0":
                try:
                    print(menu_dict[0])
                except KeyError:
                    pass
                finally:
                    self.finance_menu_()
            case "1":
                try:
                    print(menu_dict[1])
                except KeyError:
                    pass
                finally:
                    self.finance_menu_()
            case "q":
                print(menu_dict[0])
                exit()
        self.finance_menu_()

def print_dict(menu_opts:dict):
    for key, value in menu_opts.items():
        print(f"{key}: {value} ")

menu = Menu_(
        main_menu = (
            "[Tasks]",
            "[Personal]",
            "[Tools]",
            "[Projects]",
            "[Finance]",
            "[Users]",
            "[Learning Tools]",
            "[Games]",
            ),
        finance_menu = (
            "[Calculate Monthly Interest Gains]"
        )
)

menu.main_menu_()






