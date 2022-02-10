from modules.Menus_ import Menu_
from chain_ctl.Minter import Minter_
from chain_ctl.Blockchain import Blockchain_
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
    trial = Minter_("Minter_Sleep", 100000, .000002)
    trial.generator()
    # trial.check_for_uniques()
    trial.update_history_json()

    bc = Blockchain_(0)
    print(bc.chain)
    # menu.main_menu_()

main()