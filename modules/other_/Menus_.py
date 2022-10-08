from .finance_ import calculate_monthly_gains
from ..chain_ctl.Blockchain import Blockchain_, Block_
from ..chain_ctl.Minter import Minter_, Proof_of_Work
import os, json, datetime, sys

class Menu_:
    def __init__(self, main_menu:tuple, finance_menu:tuple, chain_menu:tuple):

        self.main_menu_opts = self.format_menu_(main_menu)
        self.finance_menu_opts = self.format_menu_(finance_menu)

    def format_menu_(self, _menu:tuple) -> dict:
        '''
            Take a _menu tuple containing >= 9 menu header strings so 
                it can be mapped to a dictionary in the order it was received...
                    ...where 'q' is always considered 'quit'.

        '''
        menu_opts_ = {}
        i, j = 0, len(_menu)
        
        while i < j and j <= 9:
            menu_opts_.update({i: _menu[i]})
            i+=1
        menu_opts_.update({"q": "[QUIT]"})
        return menu_opts_
        # else:
        #     print("!! _menu tuple should contain at most 9 items")
        #     raise IndexError



    def finance_menu_(self):
        '''
            Finance Tools:
                0: Calculate Monthly Gains
        '''
        menu_dict = self.finance_menu_opts
        self.print_dict(menu_dict)
        select = input("Where to? \n: ")

        match select:
            case "0":
                try:
                    print(menu_dict[0])
                    calculate_monthly_gains()
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
            case "2":
                try:
                    print(menu_dict[2])
                except KeyError:
                    pass
                finally:
                    self.finance_menu_()
            case "3":
                try:
                    print(menu_dict[3])
                except KeyError:
                    pass
                finally:
                    self.finance_menu_()                        
   
            case "q":
                print(menu_dict["q"])
                return
            case _:
                print("\n[oops...]\n")
                self.finance_menu_()

    def print_dict(self, menu_opts:dict):
        for key, value in menu_opts.items():
            print(f"{key}: {value} ")

    def main_menu_(self):
        '''
            Obnoxious menu copy/paste template to cover 10 cases with KeyError handling 
                for ease in development.
                    Remove excess cases.
        '''
        menu_dict = self.main_menu_opts
        self.print_dict(menu_dict)
        select = input("Where to? \n: ")

        match select:
            case "0":
                try:
                    print(menu_dict[0])
                    '''
                    new or existing chain and chain_id

                    '''
                    BC_ = Blockchain_(0)
                    work = Proof_of_Work(BC_)
                    work.mine_block()
                    trial = Minter_("Minter", 2500, 0, BC_)
                    trial.generator()
                    trial.check_for_uniques()
                    trial.update_history_json()
                    trial.history_counts()
                    print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(BC_.chain, indent=2))
                    print("HEIGHT: ", len(BC_.chain))
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
                    self.finance_menu_()
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







