from functools import partial

from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
)

from modules.gui_ctl.menus.main_menu.crafting_bench import CraftingBenchMenu
from modules.gui_ctl.menus.main_menu.main_menu import MainMenu
from modules.gui_ctl.menus.main_menu.message_board import MessageBoardMenu
from modules.gui_ctl.menus.main_menu.office import OfficeMenu
from modules.gui_ctl.menus.main_menu.the_mound import MoundMenu
from modules.gui_ctl.menus.main_menu.the_pit import PitMenu
from modules.gui_ctl.menus.main_menu.throw_dirt import ThrowDirtMenu
from modules.gui_ctl.menus.main_menu.trading_post import TradingPostMenu
from modules.gui_ctl.menus.main_menu.workshop import WorkshopMenu
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
            print(key)
            match key:
                case "office":
                    button.clicked.connect(
                        partial(self.stacked_widget.setCurrentWidget, self.menus[key])
                    )
                    self.handle_office_menu()

                case "workshop":
                    pass

                case "craft":
                    pass

                case "throw":
                    pass

                case "trade":
                    pass

                case "message":
                    pass

                case "mound":
                    pass

                case "pit":
                    pass

                case "wallet":
                    button.clicked.connect(
                        lambda: self.parent.setCurrentWidget(self.parent.widget(2))
                    )

                case "goodbye":
                    button.clicked.connect(lambda: print())
                    button.clicked.connect(
                        lambda: self.parent.setCurrentWidget(self.parent.widget(2))
                    )

                case _:
                    pass

    def handle_office_menu(self):
        for key, button in self.menus["office"].buttons.items():
            match key:
                case "goodbye":
                    button.clicked.connect(
                        lambda: self.stacked_widget.setCurrentWidget(self.menus["main"])
                    )
