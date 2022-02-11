import json
from random import randint
from modules.Menus_ import Menu_
from modules.chain_ctl.Minter import Minter_, QMINTER
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Block import Block_
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
def main():
    trial = Minter_("Minter", 5001, .000002)
    trial.generator()
    # trial.check_for_uniques()
    trial.update_history_json()

    bc = Blockchain_(0)
    block_1 = Block_(
                index= len(bc.chain.keys()),
                previous_hash = bc.genesis_block.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'BLOCK_ONE im the first unverified block :)',
                chain_data = {},
            )
    bc.append_block_(block_1)
    block_2 = Block_(
                index=len(bc.chain.keys()),
                previous_hash = block_1.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'BLOCK_TWO (manual)',
                chain_data = {},
            )
    bc.append_block_(block_2)
    block_3 = Block_(
                index=len(bc.chain.keys()),
                previous_hash = block_2.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'BLOCK_THREE (manual)',
                chain_data = {},
            )
    bc.append_block_(block_3)
    block_4 = Block_(
                index=len(bc.chain.keys()),
                previous_hash = block_3.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'BLOCK_FOUR (manual)',
                chain_data = {},
            )
    bc.append_block_(block_4)
    i, j = 5, 25
    b_hash = block_4.block_hash
    while i < j:
        if i < 6:
            block_Z = Block_(
                        index=i,
                        previous_hash = b_hash,
                        nonce = QMINTER.ez_rand(),
                        txns = [],
                        signature = f'BLOCK_{i}',
                        chain_data = {})
        else:
            k = i + randint(0, 1)
            block_Z = Block_(
                        index=k,
                        previous_hash = b_hash,
                        nonce = QMINTER.ez_rand(),
                        txns = [],
                        signature = f'BLOCK_{i}',
                        chain_data = {})            
        b_hash = block_Z.block_hash
        bc.append_block_(block_Z)
        i+=1
    


    print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(bc.chain, indent=2))
    print("HEIGHT: ", len(bc.chain))

    # print("qminter_check",QMINTER.generator())
    # print("qminter_check",QMINTER.generator())
    # print("qminter_check",QMINTER.generator())



    # menu.main_menu_()


main()