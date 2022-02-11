import json
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
    trial = Minter_("Minter", 1000, .000002)
    trial.generator()
    # trial.check_for_uniques()
    trial.update_history_json()

    bc = Blockchain_(0)
    block_0 = Block_(
                index= len(bc.chain.keys()),
                previous_hash = bc.genesis_block.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'im the first unverified block :)',
                chain_data = {},
            )
    bc.append_block_(block_0)
    block_1 = Block_(
                index=len(bc.chain.keys()),
                previous_hash = block_0.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'im the block_1 unverified block :)',
                chain_data = {},
            )
    block_2 = Block_(
                index=len(bc.chain.keys()),
                previous_hash = block_1.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'im the block_2 unverified block :)',
                chain_data = {},
            )
    block_3 = Block_(
                index=len(bc.chain.keys()),
                previous_hash = block_2.block_hash,
                nonce = QMINTER.ez_rand(),
                txns = [],
                signature = 'im the block_3 unverified block :)',
                chain_data = {},
            )
    print(block_3)
    bc.append_block_(block_1)
    bc.append_block_(block_2)
    bc.append_block_(block_3)

    print("\n\n-- [end] --\n\nCHAIN: " ,json.dumps(bc.chain, indent=2))
    bc.get_tallest_block()

    # print("qminter_check",QMINTER.generator())
    # print("qminter_check",QMINTER.generator())
    # print("qminter_check",QMINTER.generator())



    # menu.main_menu_()


main()