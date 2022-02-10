import json
from modules.Menus_ import Menu_
from modules.chain_ctl.Minter import Minter_
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
                index=1,
                previous_hash = bc.genesis_block.block_hash,
                nonce = 0,
                txns = [],
                signature = 'im the second unverified block :)',
                chain_data = {},
            )
    block_1 = Block_(
                index=1,
                previous_hash = block_0.block_hash,
                nonce = 0,
                txns = [],
                signature = 'im the second unverified block :)',
                chain_data = {},
            )
    block_2 = Block_(
                index=1,
                previous_hash = block_1.block_hash,
                nonce = 0,
                txns = [],
                signature = 'im the second unverified block :)',
                chain_data = {},
            )
    block_3 = Block_(
                index=1,
                previous_hash = block_2.block_hash,
                nonce = 0,
                txns = [],
                signature = 'im the second unverified block :)',
                chain_data = {},
            )
    bc.append_block_(block_0, block_1, block_2, block_3)
    print(json.dumps(bc.chain, indent=2))
    bc.get_tallest_block()
    # menu.main_menu_()

main()