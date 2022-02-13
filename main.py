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
            "[Calculate Monthly Interest Gains]",
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



def main():
    BC_ = Blockchain_(0)
    timer = Timer()
    trial = Minter_("Minter", 1250, 0, BC_)
    # trial.generator()
    # trial.check_for_uniques()
    trial.update_history_json()
    trial.history_counts()
    # BC_.validate_chain()
    # timer.start_timer()
    work = Proof_of_Work(BC_)
    work.mine_block()
    # work.mine_block(BC_)
    # work.mine_block(BC_)
    # work.mine_block(BC_)
    # i = 0
    # while i < 10:
    #     work.mine_block(BC_)
    #     i+=1


    print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(BC_.chain, indent=2))
    print("HEIGHT: ", len(BC_.chain))

    # print("TIME: " ,timer.end_timer(), "sec")

  
    # menu.main_menu_()


main()
