import json, time
from random import randint
from modules.Menus_ import Menu_
from modules.chain_ctl.Minter import Minter_
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
# from chain_ctl.Block import Block_

menu = Menu_(
        main_menu = (
            "[Chain]",
            "[Tasks]",
            "[Tools]",
            "[Projects]",
            "[Finance]",
            "[Personal]",
            "[Users]",
            "[Games]",
            ),
        finance_menu = (
            "[Calculate Monthly Interest Gains]",
        ),
        chain_menu = (
            "[Mine a Block]",
            "[Print Chain]",
            "[Print Chain]",
            "[Print Chain]",
            "[Print Chain]",
            "[Print Chain]",
            "[Print Chain]",
            "[Print Chain]",

        )        
)

'''
    Minter
    Mine One Custom
    Mine empty blocks
    Print data
    Nuke chain




'''
class Timer:
    def __init__(self) -> None:
        self.start_time = float
    def start_timer(self):
        self.start_time = time.time()
        return self.start_time
    def end_timer(self):
        return round(time.time() - self.start_time, 2)
timer = Timer()



def main():
    # BC_ = Blockchain_(0)
    # work = Proof_of_Work(BC_)
    # work.mine_block()
    
    # trial = Minter_("Minter", 250000, 0, BC_)
    # trial.generator()
    # trial.check_for_uniques()
    # trial.update_history_json()
    # trial.history_counts()

    # timer.start_timer()
    # work.mine_block(BC_)
    # work.mine_block(BC_)
    # work.mine_block(BC_)
    # i = 0
    # while i < 10:
    #     work.mine_block(BC_)
    #     i+=1
    # print("TIME: " ,timer.end_timer(), "sec")





  
    menu.main_menu_()


main()
