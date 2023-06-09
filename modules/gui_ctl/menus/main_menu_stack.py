from functools import partial

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
)

from modules.gui_ctl.chain.chain_ctl import auto_miner, auto_minter
from modules.gui_ctl.menus.main_menu.crafting_bench import CraftingBenchMenu
from modules.gui_ctl.menus.main_menu.main_menu import MainMenu
from modules.gui_ctl.menus.main_menu.message_board import MessageBoardMenu
from modules.gui_ctl.menus.main_menu.office import OfficeMenu
from modules.gui_ctl.menus.main_menu.the_mound import MoundMenu
from modules.gui_ctl.menus.main_menu.the_pit import PitMenu
from modules.gui_ctl.menus.main_menu.throw_dirt import ThrowDirtMenu
from modules.gui_ctl.menus.main_menu.trading_post import TradingPostMenu
from modules.gui_ctl.menus.main_menu.workshop import WorkshopMenu
from modules.gui_ctl.menus.wallet_menu import WalletMenu
from modules.gui_ctl.tab_widget import TabWidget


class MainMenuStack(QWidget):
    def __init__(self, parent: QStackedWidget, tabs: TabWidget):
        super().__init__(parent)
        self.parent = parent
        self.tabs = tabs
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Menus
        self.menus = {
            "main": MainMenu(),
            "office": OfficeMenu(),
            "workshop": WorkshopMenu(),
            "craft": CraftingBenchMenu(),
            "throw": ThrowDirtMenu(),
            "trade": TradingPostMenu(),
            "message": MessageBoardMenu(),
            "mound": MoundMenu(),
            "pit": PitMenu(),
            "wallet": WalletMenu(),
        }

        # Add Menus and set initial
        for _, menu in self.menus.items():
            self.stacked_widget.addWidget(menu)
        self.stacked_widget.setCurrentWidget(self.menus["main"])

        # Set the layout for the widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # handle connections
        self.handle_main_menu()

    def handle_main_menu(self):
        for key, button in self.menus["main"].buttons.items():
            # print(key)
            match key:
                case "office":
                    self.open_menu(button, self.menus[key])
                    self.handle_office_menu()

                case "workshop":
                    self.open_menu(button, self.menus[key])
                    self.handle_workshop_menu()

                case "craft":
                    self.open_menu(button, self.menus[key])
                    self.handle_crafting_menu()

                case "throw":
                    self.open_menu(button, self.menus[key])
                    self.handle_throw_dirt_menu()

                case "trade":
                    self.open_menu(button, self.menus[key])
                    self.handle_trading_post_menu()

                case "message":
                    self.open_menu(button, self.menus[key])
                    self.handle_message_board_menu()

                case "mound":
                    self.open_menu(button, self.menus[key])
                    self.handle_mound_menu()

                case "pit":
                    self.open_menu(button, self.menus[key])
                    self.handle_pit_menu()

                case "wallet":
                    self.open_menu(button, self.menus[key])
                    self.handle_wallet_menu()

                    # button.clicked.connect(
                    #     lambda: self.parent.setCurrentWidget(self.parent.widget(2))
                    # )

                case "goodbye":
                    button.clicked.connect(lambda: print())
                    # self.open_menu(button, self.menus["wallet"])

                    button.clicked.connect(
                        lambda: self.parent.setCurrentWidget(self.parent.widget(2))
                    )

                case _:
                    pass

    def open_menu(self, button, menu):
        button.clicked.connect(partial(self.stacked_widget.setCurrentWidget, menu))

    def handle_office_menu(self):
        for key, button in self.menus["office"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_workshop_menu(self):
        for key, button in self.menus["workshop"].buttons.items():
            match key:
                case "start":
                    button.clicked.connect(lambda: run_auto_miner())

                    def run_auto_miner():
                        name = self.menus["workshop"].user_input["miner_name"].text()
                        iters = self.menus["workshop"].user_input["iters_entry"].value()
                        for k, v in self.menus["workshop"].suffixes.items():
                            if v.isChecked():
                                iters = iters * int(k)
                        auto_miner(name, iters)

                case "quick":
                    button.clicked.connect(auto_miner)

                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_crafting_menu(self):
        for key, button in self.menus["craft"].buttons.items():
            match key:
                case "start":
                    button.clicked.connect(lambda: run_auto_minter())

                    def run_auto_minter():
                        name = self.menus["craft"].user_input["minter_name"].text()
                        iters = self.menus["craft"].user_input["iters_entry"].value()
                        for k, v in self.menus["craft"].suffixes.items():
                            if v.isChecked():
                                iters = iters * int(k)
                        auto_minter(name, iters)

                case "quick":
                    button.clicked.connect(auto_minter)

                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_throw_dirt_menu(self):
        for key, button in self.menus["throw"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_trading_post_menu(self):
        for key, button in self.menus["trade"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_message_board_menu(self):
        for key, button in self.menus["message"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_mound_menu(self):
        for key, button in self.menus["mound"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_pit_menu(self):
        for key, button in self.menus["pit"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )

    def handle_wallet_menu(self):
        for key, button in self.menus["wallet"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )
