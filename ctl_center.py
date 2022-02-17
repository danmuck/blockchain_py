#!/usr/bin/env python3



import json, time
from random import randint
from modules.chain_ctl.Minter import Minter_, ez_random, No_fun
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
from modules.chain_ctl.Proof_of_Work import Proof_of_Work
# from modules.chain_ctl.No_funs import No_fun



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
    bc = Blockchain_(99)
    work = Proof_of_Work(bc)
    minter = Minter_("Minter", 120000, 0, bc)
    minter.generator()
    # minter.check_for_uniques()
    minter.update_history_json()
    minter.history_counts()
    print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(bc.chain, indent=2))
    print("HEIGHT: ", len(bc.chain))
    print(bc.hash_chain_())
    # work.mine_block(txns=["FAKER hehe :)", "8==D"], chain_data={"Im_data": "Liar, he's a my key, IM data... maybe we're both data..."})
    # print(bc.hash_chain_())
    test = ez_random().get_()
    print(test)
    # bl = Block_(0,"0xsomestringshehe", 13, [], "stresfd", {})
    # bc.append_block_(bl)
    # timer.start_timer()
    # work.mine_block(bc)
    # work.mine_block(bc)
    # work.mine_block(bc)
    # i = 0
    # while i < 10:
    #     work.mine_block(bc)
    #     i+=1
    # print("TIME: " ,timer.end_timer(), "sec")

    # menu.main_menu_()
    # ri = randint(0, 9999)
    # nf = No_fun(ri)
    # checks_ = nf.get_attrs()

    # work.mine_block(txns=["some", "testing :)"], chain_data=checks_)
    

main()
