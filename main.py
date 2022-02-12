import json, time
from random import randint
from modules.Menus_ import Menu_
from modules.chain_ctl.Minter import Minter_, QMINTER
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
BC_ = Blockchain_(0)
class Timer:
    def __init__(self) -> None:
        self.start_time = float
    def start_timer(self):
        self.start_time = time.time()
        return self.start_time
    def end_timer(self):
        return round(time.time() - self.start_time, 2)


        
def main():
    timer = Timer()
    trial = Minter_("Minter", 50000, .0002, BC_)
    trial.generator()
    # trial.check_for_uniques()
    trial.update_history_json()
    trial.history_counts()

    # timer.start_timer()
    # work = Proof_of_Work()
    # work.mine_block(BC_)
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

    # block_1 = Block_(
    #             index= len(bc.chain.keys()),
    #             previous_hash = bc.genesis_block.block_hash,
    #             nonce = round(QMINTER.ez_rand(), 8),
    #             txns = [],
    #             signature = 'BLOCK_ONE im the first unverified block :)',
    #             chain_data = {},
    #         )
    # bc.append_block_(block_1)
    # block_2 = Block_(
    #             index=len(bc.chain.keys()),
    #             previous_hash = block_1.block_hash,
    #             nonce = round(QMINTER.ez_rand(), 8),
    #             txns = [],
    #             signature = 'BLOCK_TWO (manual)',
    #             chain_data = {},
    #         )
    # bc.append_block_(block_2)
    # block_3 = Block_(
    #             index=len(bc.chain.keys()),
    #             previous_hash = block_2.block_hash,
    #             nonce = round(QMINTER.ez_rand(), 8),
    #             txns = [],
    #             signature = 'BLOCK_THREE (manual)',
    #             chain_data = {},
    #         )
    # bc.append_block_(block_3)
    # block_4 = Block_(
    #             index=len(bc.chain.keys()),
    #             previous_hash = block_3.block_hash,
    #             nonce = round(QMINTER.ez_rand(), 8),
    #             txns = [],
    #             signature = 'BLOCK_FOUR (manual)',
    #             chain_data = {},
    #         )
    # bc.append_block_(block_4)
    # i, j = 5, 10
    # b_hash = block_4.block_hash
    # while i < j:
    #     if i < 6:
    #         block_Z = Block_(
    #                     index=i,
    #                     previous_hash = b_hash,
    #                     nonce = QMINTER.ez_rand(),
    #                     txns = [],
    #                     signature = f'BLOCK_{i}',
    #                     chain_data = {})
    #     else:
    #         k = i + randint(0, 1)
    #         block_Z = Block_(
    #                     index=k,
    #                     previous_hash = b_hash,
    #                     nonce = QMINTER.ez_rand(),
    #                     txns = [],
    #                     signature = f'BLOCK_{i}',
    #                     chain_data = {})            
    #     b_hash = block_Z.block_hash
    #     bc.append_block_(block_Z)
    #     i+=1